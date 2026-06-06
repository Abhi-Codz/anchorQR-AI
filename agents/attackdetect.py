from attacks.promptinject import detect as detect_prompt
from attacks.toolhijack import detect as detect_tool


class AttackDetectionAgent:

    @staticmethod
    def analyze(content):

        return {
            "prompt_injection":
                detect_prompt(content),

            "tool_hijacking":
                detect_tool(content)
        }