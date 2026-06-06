PROMPT_PATTERNS = [
    "ignore previous instructions",
    "ignore all instructions",
    "override system prompt",
    "forget your instructions",
    "disregard all rules",
    "you are now",
    "act as"
]


def detect(content: str):

    findings = []

    content = content.lower()

    for pattern in PROMPT_PATTERNS:
        if pattern in content:
            findings.append(pattern)

    return findings