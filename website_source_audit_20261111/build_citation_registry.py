"""Reproduce reviewed mappings; no network, database writes, or evaluation reruns."""
import collections
import hashlib
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AUDIT = Path(__file__).resolve().parent
CANDIDATE = ROOT / 'r135_bounded_response_20261111'
sys.path.insert(0, str(CANDIDATE / 'system'))
from app.knowledge.common.public_citations import digest, text_digest
from app.knowledge.common.store import CommonStore

URL = 'https://esports.computing.psu.ac.th/'
# This list is a human content review, not lexical similarity or domain matching.
FAQ = {
 'migrated_faq_rule_smoking_alcohol': 'Rules 4.9',
 'migrated_faq_rule_en_smoking_alcohol_natural': 'Rules 4.9',
 'migrated_faq_curated_rule_food_drinks': 'Rules 4.2',
 'migrated_faq_rule_en_food_drink_natural': 'Rules 4.2',
 'migrated_policy_text_food_bring_general': 'Rules 4.2',
 'migrated_faq_curated_booking_steps': 'How to Use the Reservation System',
 'migrated_faq_rule_en_booking_steps_natural': 'How to Use the Reservation System',
 'migrated_faq_rule_moderate_damage': 'Rules 4.6 moderate damage',
 'migrated_faq_rule_checkin_advance': 'Rules 2.1',
 'migrated_faq_curated_checkin_30_minutes': 'Rules 2.1',
 'migrated_faq_rule_payment_10_minutes': 'Rules 1.3 and booking procedure',
 'migrated_faq_rule_penalty_temp_suspension': 'Rules 5.1 temporary suspension',
 'migrated_faq_rule_cancel_advance': 'Rules 3.1',
 'migrated_faq_curated_cancel_1_hour': 'Rules 3.1',
 'migrated_faq_rule_refund_policy': 'Rules 3.2 refund exception only',
 'migrated_faq_curated_refund_policy': 'Rules 3.2 refund exception only',
 'migrated_faq_rule_report_problem': 'Rules 4.12',
}


def build():
 store = CommonStore(CANDIDATE / 'system/data/knowledge/common.sqlite')
 with store.connect() as c:
  records = store.heads(c)
  pairs = store.sources(c)
 inventory = json.loads((AUDIT / 'EVAL200_CLAIM_INVENTORY.json').read_text(encoding='utf-8'))
 entries = []

 def add(rid, field, texts, source_fields, section, url=URL, access='live HTTP 200', page_hash=None):
  record = records[rid]
  evidence = []
  for key in source_fields:
   for ref in record['fields'][key]['evidence_refs']:
    src, raw = pairs[ref['source_id']]
    assert hashlib.sha256(raw.encode()).hexdigest() == src['sha256']
    evidence.append({'source_id': ref['source_id'], 'snapshot_sha256': src['sha256'], 'locator': ref['locator']})
  assert texts and evidence
  entries.append({'record_id': rid, 'field': field, 'record_sha256': digest(record),
                  'text_sha256': sorted({text_digest(t) for t in texts if t}), 'evidence': evidence,
                  'url': url, 'title': 'PSU Esports Studio — ' + section, 'section': section,
                  'checked_at': '2026-11-11', 'access': access,
                  'page_sha256': page_hash,
                  'approval_effect': 'none; website corroboration only'})

 page_hash = hashlib.sha256((AUDIT / 'page_00.html').read_bytes()).hexdigest()
 for rid, section in FAQ.items():
  texts = [x for x in records[rid]['fields']['answer']['value'].values() if isinstance(x, str)]
  for field in ('answer', 'owner_policy'):
   add(rid, field, texts, ['answer'], section, page_hash=page_hash)
 # Rendered periods are reviewed against the weekday table, not live availability.
 for claim in inventory:
  rid, field = claim['record_id'], claim['field']
  if rid in {'migrated_schedule_' + str(i) for i in range(5)} and field in {'service_periods','maintenance_periods'}:
   # Reviewed Thai/English period-only variants. Do not cite internal conflict
   # explanations as if the public page asserted that internal conflict.
   texts=[v for v in claim.get('values',[claim['value']]) if '\n' not in v]
   add(rid, field, texts, ['service_slots'] if field=='service_periods' else [field], 'Gaming Equipment Schedule; regular timetable only', page_hash=page_hash)
 # Exact Thai name and recorded role; cached page is not current-tenure proof.
 for field in ('display_name', 'role'):
  rid = 'member_832e24bbcd11737e'
  texts = [records[rid]['fields'][field]['value']['th']]
  add(rid, field, texts, [field], 'Members — recorded Thai profile',
      'https://esports.phuket.psu.ac.th/about-us/Members', 'search cached; crawled last month; direct fetch 502')

 target = CANDIDATE / 'system/data/knowledge/verified_web_citations.json'
 target.write_text(json.dumps({'schema_version': 1, 'entries': entries,
   'limits': ['Not a publication/currentness approval.', 'Exact reviewed outputs only; edits invalidate mappings.',
              'No price-image citation for owner-confirmed PC student zero price.',
              'Unknown or unreachable source does not mean the claim is false.']}, ensure_ascii=False, indent=2), encoding='utf-8')
 # Every observed typed claim receives a review disposition, including no-link cases.
 dispositions = []
 for claim in inventory:
  variants=claim.get('values',[claim['value']])
  approved_values=[v for v in variants if any(e['record_id']==claim['record_id'] and e['field']==claim['field'] and text_digest(v) in e['text_sha256'] for e in entries)]
  approved = len(approved_values)==len(variants)
  rid = claim['record_id']
  status, reason = 'not_verified', 'Relevant website sections checked; this exact claim has not been corroborated. No public link.'
  if approved:
   status, reason = 'corroborated', 'Reviewed exact output with record/source identity pins.'
  elif rid == 'migrated_faq_rule_booking_session_and_payment':
   status, reason = 'conflict', 'Legacy says 3 sessions; live booking page says 6. Do not cite legacy answer.'
  elif rid.startswith(('migrated_rate_', 'rate_recovered_')):
   status, reason = 'price_scope_not_verified', 'Image duration/group billing must match; PC PSU student zero is owner-confirmed, not proved by old image. No price citation.'
  elif rid.startswith('controls_'):
   status, reason = 'attachment_not_verified', 'Equipment guide entry inspected; detailed button bindings in images/attachments not verified. No link to a generic page.'
  elif rid.startswith('competition_'):
   status, reason = 'attachment_not_verified', 'Competition/download index does not establish this document clause/version. No generic index citation.'
  elif rid.startswith(('availability_', 'game_detail_', 'equipment_')):
   status, reason = 'scope_not_verified', 'Game/equipment pages and booking inventory inspected; exact claim, station relationship, edition or usage details not fully corroborated.'
  elif rid.startswith('member_'):
   status, reason = 'profile_scope_not_verified', 'Members page search cache available; exact output/person/date scope not approved by this review.'
  if approved_values and not approved:
   status,reason='partially_corroborated_variants','Only explicitly reviewed text variants may receive a link.'
  dispositions.append({**claim, 'citation_review': status, 'reason': reason, 'corroborated_values':approved_values})
 (AUDIT / 'CLAIM_CITATION_REVIEW.json').write_text(json.dumps(dispositions, ensure_ascii=False, indent=2), encoding='utf-8')
 summary={'unique_observed_record_fields':len(inventory),'registry_entries':len(entries),
          'dispositions':dict(collections.Counter(x['citation_review'] for x in dispositions)),
          'full_site_attachments_verified':False,'all_200_semantics_verified':False}
 (AUDIT / 'CITATION_REVIEW_SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps(summary))

if __name__ == '__main__':
 build()
