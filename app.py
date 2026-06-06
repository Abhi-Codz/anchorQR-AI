import streamlit as st

from agents.qrextract import QRExtractionAgent
from agents.urlvalid import URLValidationAgent
from agents.webretrieve import (
    WebpageRetrievalAgent
)

from agents.attackdetect import (
    AttackDetectionAgent
)

from agents.mitigation import (
    MitigationAgent
)

from agents.threatassessment import (
    ThreatAssessmentAgent
)

from utils.recommendation import (
    generate_recommendation
)

st.title("anchorQR - AI")

uploaded_file = st.file_uploader(
    "Upload QR Code",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    with open(
        "temp_qr.png",
        "wb"
    ) as f:

        f.write(
            uploaded_file.getbuffer()
        )

    url = QRExtractionAgent.extract(
        "temp_qr.png"
    )

    st.subheader("Extracted URL")
    st.write(url)

    if url:

        validation = (
            URLValidationAgent.validate(
                url
            )
        )

        st.subheader("Validation")
        st.write(validation)

        if validation["valid"]:

            content = (
                WebpageRetrievalAgent.retrieve(
                    url
                )
            )

            results = (
                AttackDetectionAgent.analyze(
                    content
                )
            )

            prompt_status = (
                MitigationAgent.prompt_firewall(
                    results[
                        "prompt_injection"
                    ]
                )
            )

            tool_status = (
                MitigationAgent.permission_control(
                    results[
                        "tool_hijacking"
                    ]
                )
            )

            score = (
                ThreatAssessmentAgent
                .calculate_score(
                    results
                )
            )

            risk = (
                ThreatAssessmentAgent
                .classify(score)
            )

            recommendation = (
                generate_recommendation(
                    risk
                )
            )

            st.subheader(
                "Prompt Injection Findings"
            )
            st.write(
                results[
                    "prompt_injection"
                ]
            )

            st.subheader(
                "Tool Hijacking Findings"
            )
            st.write(
                results[
                    "tool_hijacking"
                ]
            )

            st.subheader(
                "Mitigation Layer"
            )

            st.write(
                f"Prompt Firewall: {prompt_status}"
            )

            st.write(
                f"Permission Control: {tool_status}"
            )

            st.subheader(
                "Threat Assessment"
            )

            st.write(
                f"Risk Score: {score}"
            )

            st.write(
                f"Risk Level: {risk}"
            )

            st.subheader(
                "Recommendation"
            )

            st.write(
                recommendation
            )
