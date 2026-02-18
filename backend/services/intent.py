def classify_intent(query: str) -> str:
    advisory_keywords = [
        "should I",
        "recommend",
        "best investment",
        "where should",
        "what should I invest"
    ]

    query_lower = query.lower()

    for word in advisory_keywords:
        if word in query_lower:
            return "advisory"

    return "educational"