class MitigationAgent:

    @staticmethod
    def prompt_firewall(prompt_hits):

        if len(prompt_hits) > 0:
            return "BLOCKED"

        return "SAFE"

    @staticmethod
    def permission_control(tool_hits):

        if len(tool_hits) > 0:
            return "DENIED"

        return "ALLOWED"