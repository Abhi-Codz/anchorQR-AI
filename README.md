# <p align="center">anchorQR - AI</p>
A storage repository about a basic system, demonstrating phishing based cyber issues, particularly in regards to QR Scanning. This assignment does well to furnish a simulation of analyzing, and mitigating the cyber threats that may reside within a QR Code, using a Multi Agentic Architecture - Based on the papers: "Gone Quishing" and "AgentDojo". Assigned midst University's Summer-School Workshop, titled <b> Applied Cyber Security with Multi-Agentic AI </b>. 

Proposal Paper: https://docs.google.com/document/d/1pmQvw8RusE966cHGzmYOmGEdIzaWZ4hsaxT9htblQC0/edit?usp=sharing
<br>
<p align = "center">(Refer to the paper above for academic insight) </p>

![](https://github.com/Abhi-Codz/anchorQR-AI/blob/ff03a0c61e7abb1a20571b9c5a473de617aa581f/screenshots/Screenshot%202026-06-07%20010430.png)
![](https://github.com/Abhi-Codz/anchorQR-AI/blob/ff03a0c61e7abb1a20571b9c5a473de617aa581f/screenshots/Screenshot%202026-06-07%20010446.png)
![](https://github.com/Abhi-Codz/anchorQR-AI/blob/ff03a0c61e7abb1a20571b9c5a473de617aa581f/screenshots/Screenshot%202026-06-07%20010518.png)

## How to install, you may ask?
### I. Clone the Repository 
```git clone https://github.com/YOUR_USERNAME/AnchorQR-AI.git```

### II. Create a Virtual Envionment within the system
```python -m venv .venv``` -  For Windows, not certain of Mac or Linux, do query that to the Search Engine.
### III. Install the List Dependencies
```pip install -r requirements.txt```

## How to Run now?
### Activate the Streamlit Application:
```streamlit run app.py```
### The application will automatically launch onto your browser
eg. http://localhost:8501

## How does the demonstration function, perhaps?
<b> I. Create or you may obtain a QR Code that points to a certain webpage, be it local, or public. <br>
<b> II. Upload the QR onto the Streamlit interface, wherein it asks to upload. <br>
<b> III. Now the sytem with, </b>
- Extract the embedded URL
- Validate the URL
- Retrieve webpage content
- Analyze for Prompt Injection attacks
- Analyze for Tool Hijacking attacks
- Apply mitigation strategies
- Generate a risk assessment
<br>
<b> IV. Enjoy the report furnished.

# Disclaimer

This project is intended solely for educational, and research purposes, probably.
The implemented attack demonstrations are controlled simulations designed to evaluate Multi-Agentic security mechanisms, and should rather not be used for malicious activities, not that it's advanced enough to be used with such an intent.
