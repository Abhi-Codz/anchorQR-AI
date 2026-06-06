TOOL_PATTERNS = [
    "send_email",
    "delete_file",
    "execute_command",
    "run_shell",
    "download_and_run",
    "export_user_data",
    "access_database"
]


def detect(content: str):

    findings = []

    content = content.lower()

    for pattern in TOOL_PATTERNS:
        if pattern in content:
            findings.append(pattern)

    return findings