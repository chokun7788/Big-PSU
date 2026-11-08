"""Render known row facts, preserving unspecified gestures and untranslated notes."""
from .query_scope import control_projection
def render_bindings(rows,question,lang):
    def local(v):
        if not isinstance(v,dict):return str(v or '')
        if v.get(lang):return v[lang]
        other=v.get('th' if lang=='en' else 'en') or ''
        return ('[Translation pending; Thai source] ' if lang=='en' and other else '')+other
    lines=[]
    for row in rows:
        parts=[local(row.get('button_label')) or ', '.join(row['buttons']),local(row['action']),local(row.get('notes')),local(row.get('section'))]
        extra=local(row.get('context'))
        if extra and extra!=parts[-1]:parts.append(extra)
        if row['gesture']!='unknown':parts.append(row['gesture'])
        lines.append(' | '.join(parts).rstrip(' |'))
    display={lang:'\n'.join(lines)}
    return control_projection(display,question,lang) or display[lang]
