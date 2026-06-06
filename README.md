# anchorQR-AI
A storage repository about a basic system, demonstrating phishing based cyber issues, particularly in regards to QR Scanning. This assignment does well to furnish a simulation of analyzing, and mitigating the cyber threats that may reside within a QR Code, using a Multi Agentic Architecture - Based on the papers: "Gone Quishing" and "AgentDojo".

Proposal Paper: https://docs.google.com/document/d/1pmQvw8RusE966cHGzmYOmGEdIzaWZ4hsaxT9htblQC0/edit?usp=sharing
(Refer to the paper above for academic insight)

# How to install, you may ask?
## I. Clone the Repository 
>> git clone https://github.com/YOUR_USERNAME/AnchorQR-AI.git

## II. Create a Virtual Envionment within the system
>> python -m venv .venv -  For Windows, not certain of Mac or Linux, do query that to the Search Engine.
## III. Install the List Dependencies
>> pip install -r requirements.txt

# How to Run now?
## Activate the Streamlit Application:
>> streamlit run app.py
## The application will automatically launch onto your browser
eg. http://localhost:8501
# How does the demonstration function, perhaps?
## I.
- Create or you may obtain a QR Code that points to a certain webpage, be it local, or public.
## II.
- Upload the QR onto the Streamlit interface, wherein it asks to upload.
## III.
Now the sytem with,
- Extract the embedded URL
- Validate the URL
- Retrieve webpage content
- Analyze for Prompt Injection attacks
- Analyze for Tool Hijacking attacks
- Apply mitigation strategies
- Generate a risk assessment
## IV.
- Enjoy the report furnished.

# Disclaimer

This project is intended solely for educational, and research purposes, probably.
The implemented attack demonstrations are controlled simulations designed to evaluate Multi-Agentic security mechanisms, and should rather not be used for malicious activities, not that it's advanced enough to be used with such an intent.
