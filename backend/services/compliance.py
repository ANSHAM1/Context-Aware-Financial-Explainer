def compliance_check(text: str) -> tuple[bool, str]:
    blocked_phrases = [
        "you should invest",
        "i recommend",
        "best option is",
        "guaranteed return"
    ]

    for phrase in blocked_phrases:
        if phrase in text.lower():
            return True, "Response blocked due to advisory content."

    return False, text