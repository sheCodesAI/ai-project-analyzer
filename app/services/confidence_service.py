
def calculate_confidence(project_text: str, missing_information: list[str]) -> int:
    """
    Calculate confidence score using simple rule-based logic.
    """

    score = 100

    score -= len(missing_information) * 10

    vague_words = [
        "approximately",
        "approx",
        "later",
        "not confirmed",
        "may",
        "expected",
    ]

    text = project_text.lower()

    for word in vague_words:
        if word in text:
            score -= 5

    return max(score, 0)