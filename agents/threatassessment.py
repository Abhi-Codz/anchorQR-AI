class ThreatAssessmentAgent:

    @staticmethod
    def calculate_score(results):

        score = 0

        score += (
            len(results["prompt_injection"])
            * 25
        )

        score += (
            len(results["tool_hijacking"])
            * 25
        )

        return min(score, 100)

    @staticmethod
    def classify(score):

        if score >= 70:
            return "HIGH"

        if score >= 40:
            return "MEDIUM"

        return "LOW"