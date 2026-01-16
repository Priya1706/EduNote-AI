def summarize_text(text):
    lines = text.split("\n")
    important_points = []

    for line in lines:
        line = line.strip()
        if (
            len(line) > 40
            and ("year" in line.lower()
                 or "because" in line.lower()
                 or "rights" in line.lower()
                 or "battle" in line.lower())
        ):
            important_points.append("• " + line)

    # limit output size
    return "\n".join(important_points[:6])
