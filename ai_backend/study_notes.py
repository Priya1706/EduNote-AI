import re

def generate_study_notes(text):
    years = re.findall(r"\b(1[6-9]\d{2}|20\d{2})\b", text)

    lines = [l.strip() for l in text.split("\n") if len(l.strip()) > 30]

    definitions = []
    key_points = []

    for line in lines:
        if "is" in line.lower() or "was" in line.lower():
            definitions.append("• " + line)
        else:
            key_points.append("• " + line)

    notes = f"""
📘 READY-TO-STUDY NOTES
======================

📌 Definitions:
{chr(10).join(definitions[:3]) if definitions else "• Not explicitly found"}

📅 Important Years:
{', '.join(sorted(set(years))) if years else "Not mentioned"}

📝 Key Points:
{chr(10).join(key_points[:5])}

📖 Conclusion:
• The topic explains key concepts discussed in the lecture and their significance.
"""
    return notes.strip()
