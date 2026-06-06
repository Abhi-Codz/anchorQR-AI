def generate_recommendation(risk):

    if risk == "HIGH":

        return (
            "Do not trust this webpage. "
            "Potential malicious behavior detected."
        )

    if risk == "MEDIUM":

        return (
            "Proceed carefully. "
            "Suspicious indicators detected."
        )

    return (
        "No significant threats detected."
    )