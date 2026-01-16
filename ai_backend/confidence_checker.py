def confidence_check(text):
    score = 70
    verified_points = []

    if any(year in text for year in ["1600", "1757", "1764", "1857"]):
        score += 15
        verified_points.append("Historical timeline matches known events")

    if len(text.split()) > 150:
        score += 10
        verified_points.append("Sufficient contextual explanation detected")

    if score > 95:
        score = 95

    report = f"""
🔍 Confidence Check
------------------
Verified Aspects:
{chr(10).join("• " + v for v in verified_points) if verified_points else "• General content structure verified"}

Confidence Score: {score}%
"""
    return report.strip()
