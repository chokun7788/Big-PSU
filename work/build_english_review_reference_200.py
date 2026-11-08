"""Create a paired English answer reference from the user's frozen Thai review."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


PROJECT = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
WORKSPACE = Path(__file__).resolve().parents[1]
SOURCE = PROJECT / "reports/master_ground_truth_eval/master_gt_eval_20260924_195543_intent_trap_manual_review_v2.jsonl"
REVIEW = Path(r"C:\Users\Chokhun\Downloads\intent_trap_review_2026-09-24T13-54-43-758Z.json")
PRIOR_PROJECTION = PROJECT / "reports/master_ground_truth_eval/intent_trap_review_bilingual_assisted_20260924.json"
OUT = WORKSPACE / "outputs/intent_trap_english_reference_200_20260926.jsonl"
MANIFEST = WORKSPACE / "outputs/intent_trap_english_reference_200_20260926_manifest.json"
SITE = "https://esports.computing.psu.ac.th/"


# One carefully written reference per scenario. Each scenario has five
# paraphrases whose target and requested facet are the same.
# The wording is derived from the user's Thai review and the existing
# bilingual policy registry. It is a translated evaluation reference, not an
# assertion that the owner has approved public access/food policy wording.
SCENARIOS: dict[int, tuple[str, str]] = {
    101: ("public_access", "Yes. Members of the public can book and use the studio. A service fee may apply according to the service and user group."),
    106: ("public_access", "Yes. Someone who is not a PSU student can book and use the studio. Fees may depend on the service and user group."),
    111: ("booking_eligibility", "Yes. A visitor from another university can book through the online reservation system. The applicable fee depends on the service and user group."),
    116: ("membership", "No separate studio membership or PSU student status is required for a public visitor to book. The visitor must follow the reservation and check-in steps; a service fee may apply."),
    121: ("equipment_access", "Yes. A parent can book and use the studio equipment offered for reservation. Fees may depend on the service and user group."),
    126: ("booking_without_psu_id", "Yes. A PSU student ID is not required for a public visitor to reserve a station. Use the National ID field when booking and present a national ID card at check-in; the applicable fee may vary."),
    131: ("pc_public_access", "Yes. The PC Zone can be booked by public visitors as well as PSU users. Follow the reservation rules; fees may depend on the user group and service."),
    136: ("alumni_access", "Yes. An alumnus without a current student card may book as a public visitor and present a national ID card at check-in. The applicable fee may vary."),
    141: ("visitor_booking", "Yes. A visitor from outside Phuket can book a station through the online system. Fees may depend on the service and user group."),
    146: ("checkin_document", "An external visitor should enter a National ID when booking and present a national ID card at check-in. Booking and payment do not replace the check-in ID requirement."),
    201: ("bring_food", "Yes, you may bring food and drinks into the studio. Eating and drinking are allowed only in designated areas."),
    206: ("carry_water", "Yes, you may carry a water bottle inside. If you drink from it, use a designated area."),
    211: ("carry_snack", "Yes, you may carry a snack in your bag into the studio. Eating is restricted to designated areas."),
    216: ("bring_coffee", "Yes, you may bring coffee into the studio. Drink it only in a designated area."),
    221: ("outside_food", "Yes, you may bring outside food in without eating in the gaming area. Eat only in a designated area."),
    226: ("carry_drink", "Yes, you may carry a drink through the studio entrance. Drinking is restricted to designated areas."),
    231: ("carry_takeaway", "Yes, you may carry takeaway food through the studio. Eating it is restricted to designated areas."),
    236: ("water_bottle_rule", "You may bring a water bottle inside. The food and drink rule restricts consumption to designated areas."),
    241: ("carry_snack_without_eating", "No. Carrying a snack without eating it is not the prohibited activity described by the food rule. Eat only in a designated area."),
    246: ("personal_beverage", "Yes, you may bring your own beverage into the studio. Drink it only in a designated area."),
    401: ("equipment_access", "Yes. Public visitors can book and use the studio's available equipment. Fees may depend on the service and user group."),
    406: ("pc_access", "Yes. Public visitors can book and use the studio PCs. Fees may depend on the service and user group."),
    411: ("ps5_without_psu_id", "Yes. Someone without a PSU ID can book the PlayStation 5 service as a public visitor. Present a national ID card at check-in; the applicable fee may vary."),
    416: ("vr_access", "Yes. An external visitor can book and use the VR service. Fees may depend on the service and user group."),
    421: ("cockpit_access", "Yes. A non-student can book and use the Cockpit service. Fees may depend on the service and user group."),
    426: ("nintendo_access", "Yes. A parent can book and use the Nintendo service. Fees may depend on the service and user group."),
    431: ("pc_public_or_student", "The studio PCs are available to public visitors as well as students through the reservation system. Fees may depend on the user group."),
    436: ("tourist_access", "Yes. A tourist can book and use the studio equipment offered for reservation. Fees may depend on the service and user group."),
    441: ("station_and_seating", "Yes. A public visitor can use a booked gaming station and its seating under the studio's service rules. Fees may depend on the service and user group."),
    446: ("eligible_groups", "PSU students, staff, and public visitors can book studio stations. They must follow the reservation and check-in rules; fees may vary by service and user group."),
    451: ("outside_scope", "I can help with verified PSU Esports Studio questions such as bookings, equipment, games, opening hours, and rules. I cannot answer the chicken-and-egg question from studio information."),
    456: ("clarify_garbled", "I cannot tell which studio topic you meant from that text. Please rephrase the question or name the game, equipment, booking detail, or rule you need."),
    461: ("outside_scope_weather", "I do not have verified weather information in this studio assistant. I can help with PSU Esports Studio bookings, equipment, hours, games, and rules."),
    466: ("outside_scope_stock", "I cannot recommend a stock in this studio assistant. I can help with PSU Esports Studio bookings, equipment, hours, games, and rules."),
    471: ("scope_boundary", "I can answer questions about PSU Esports Studio, including bookings, equipment, hours, games, prices, and rules. Please ask a studio-related question."),
    476: ("greeting", "Hello! Ask me about PSU Esports Studio bookings, equipment, games, opening hours, prices, or rules."),
    481: ("refuse_fabrication", "I cannot make up facts about the studio. Ask a specific question and I will use the available verified studio information."),
    486: ("clarify_station", "Which station or equipment type do you mean, and what would you like to know about it?"),
    491: ("suggest_topics", "You can ask about booking a slot, whether a station is available, equipment, games, opening hours, prices, or studio rules."),
    496: ("clarify_game", "Which game or equipment zone do you mean? Please name it so I can give a relevant studio answer."),
}


def main() -> None:
    raw = SOURCE.read_bytes()
    reviewed = json.loads(REVIEW.read_text(encoding="utf-8"))
    previous = json.loads(PRIOR_PROJECTION.read_text(encoding="utf-8"))
    source_hash = hashlib.sha256(raw).hexdigest()
    if reviewed["source_sha256"] != source_hash or previous["source_sha256"] != source_hash:
        raise ValueError("Frozen review and prior projection do not match source corpus")
    corpus = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
    by_id = {row["id"]: row for row in corpus}
    manual = {row["id"]: row for row in reviewed["decisions"]}
    projected = {row["id"]: row for row in previous["decisions"]}
    if len(corpus) != 400 or len(by_id) != 400 or len(manual) != 200 or len(SCENARIOS) != 40:
        raise ValueError("Unexpected source counts")

    output: list[dict] = []
    issue_counts: Counter[str] = Counter()
    for number in list(range(101, 151)) + list(range(201, 251)) + list(range(401, 501)):
        scenario_start = number - (number - 1) % 5
        facet, reference = SCENARIOS[scenario_start]
        english_id = f"INTENT-TRAP-EN-{number:04d}"
        thai_id = f"INTENT-TRAP-TH-{number:04d}"
        english = by_id[english_id]
        thai = by_id[thai_id]
        old_projection = projected[english_id]
        thai_feedback = manual.get(thai_id) or projected.get(thai_id)
        if thai_feedback is None:
            raise ValueError(f"Missing Thai feedback for {thai_id}")

        issues: list[str] = []
        if thai_id not in manual:
            issues.append("thai_decision_inferred_from_four_siblings")
        if english_id not in manual:
            issues.append("english_not_manually_reviewed")
        if (english["actual_route"], english["actual_status"]) != (thai["actual_route"], thai["actual_status"]):
            issues.append("old_answers_differed_in_route_or_status")
        if scenario_start == 201 and number in (201, 202):
            issues.append("thai_note_about_booking_is_off_facet_for_food")
        if scenario_start == 146:
            issues.append("thai_note_did_not_answer_requested_id")
        if scenario_start in (451, 471):
            issues.append("old_english_answer_less_helpful_than_thai")
        for issue in issues:
            issue_counts[issue] += 1

        policy_basis = (
            "reviewer_interpretation_with_site_context"
            if english["domain"] in {"outsider_eligibility", "food_bring_scope", "equipment_access_trap"}
            else "scope_response_guidance"
        )
        output.append({
            "id": english_id,
            "paired_thai_id": thai_id,
            "scenario_start": scenario_start,
            "domain": english["domain"],
            "facet": facet,
            "question_en": english["question"],
            "question_th": thai["question"],
            "reference_answer_en": reference,
            "reference_kind": "english_answer_candidate_from_user_thai_review",
            "reference_status": "pending_owner_policy_confirmation" if policy_basis.startswith("reviewer_") else "ready_for_human_semantic_review",
            "source_basis": policy_basis,
            "source_url": SITE if policy_basis.startswith("reviewer_") else "",
            "thai_review": {
                "origin": "user_manual" if thai_id in manual else "sibling_projection",
                "decision_on_old_answer": thai_feedback["decision"],
                "note_th": thai_feedback.get("note", ""),
                "note_en_literal": old_projection.get("translated_source_note_en", old_projection.get("reference_note_en", "")),
            },
            "english_existing_manual_decision_on_old_answer": manual[english_id]["decision"] if english_id in manual else None,
            "translation_analysis": {
                "paired_question_same_intent": True,
                "issues": issues,
                "old_english_route": english["actual_route"],
                "old_english_status": english["actual_status"],
            },
        })

    if len(output) != 200 or len({row["id"] for row in output}) != 200:
        raise ValueError("English reference must have 200 unique paired rows")
    if any(not row["reference_answer_en"].strip() for row in output):
        raise ValueError("Empty reference answer")
    if issue_counts["old_answers_differed_in_route_or_status"] != 31:
        raise ValueError(f"Unexpected route difference count: {issue_counts}")
    if issue_counts["thai_note_about_booking_is_off_facet_for_food"] != 2:
        raise ValueError("Food note exceptions changed")
    if issue_counts["thai_note_did_not_answer_requested_id"] != 5:
        raise ValueError("Document note exceptions changed")

    with OUT.open("x", encoding="utf-8") as handle:
        for row in output:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    manifest = {
        "schema_version": 1,
        "source_corpus": str(SOURCE),
        "source_corpus_sha256": source_hash,
        "source_review": str(REVIEW),
        "source_review_sha256": hashlib.sha256(REVIEW.read_bytes()).hexdigest(),
        "prior_projection": str(PRIOR_PROJECTION),
        "rows": len(output),
        "scenario_templates": len(SCENARIOS),
        "paired_question_alignment_checked": True,
        "thai_manual_decisions": sum(row["thai_review"]["origin"] == "user_manual" for row in output),
        "thai_sibling_projections": sum(row["thai_review"]["origin"] == "sibling_projection" for row in output),
        "english_manual_decisions_on_old_answers": sum(row["english_existing_manual_decision_on_old_answer"] is not None for row in output),
        "reference_status_counts": dict(Counter(row["reference_status"] for row in output)),
        "issue_counts": dict(issue_counts),
        "reference_file_sha256": hashlib.sha256(OUT.read_bytes()).hexdigest(),
        "interpretation": "English candidate answers for evaluation, derived from Thai reviewer feedback and published site context; not 200 English human-reviewed answers or owner-approved policy",
    }
    with MANIFEST.open("x", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(json.dumps({"rows": len(output), "status": manifest["reference_status_counts"], "issues": dict(issue_counts)}, ensure_ascii=False))
    print(OUT)
    print(MANIFEST)


if __name__ == "__main__":
    main()
