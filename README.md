📘 StudyFlow — PDF Question Answering Agent

StudyFlow is a simple AI-powered PDF Question Answering tool built using Streamlit, Google Gemini API, and PyPDF2.
It allows users to upload a PDF and ask questions based only on the extracted text.

.✨ Features

📄 Upload a PDF

🔍 Extracts text from the PDF

❓ Ask questions strictly using the document’s content

⚡ Uses Google Gemini 2.5 Flash for fast and affordable inference

🔐 No API key input required in UI (handled securely through Streamlit Secrets)

🎨 Clean and minimal UI built with Streamlit

🛠 Tech Stack

Python 3

Streamlit

PyPDF2

Google Gemini API (google-generativeai)
 
📦 Installation (Run Locally)

Clone the repository:

```
git clone https://github.com/tpgx404/StudyFlow-agent.git
cd StudyFlow-agent
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the app:

```
streamlit run app.py
```

View in browser at:

https://studyflow-agent-cxpgnkzshstacmkvbzgcuz.streamlit.app/

🔐 Setting Up Secrets (For Deployment)

In Streamlit Cloud → App settings → Secrets, add:

```
GEMINI_API_KEY = "your_api_key_here"
```

The app will automatically read this key using:

```
import os
api_key = os.getenv("GEMINI_API_KEY")
```

No need to expose the key in UI.

🌐 Deployment

This app is deployed using Streamlit Cloud.

Steps:

Push code to GitHub

Open https://share.streamlit.io

Deploy → Select repo

Set Main file path = app.py

Add API Key in Secrets

Deploy 🎉

📁 Project Structure

```
StudyFlow-agent/
│── app.py
│── requirements.txt
│── README.md
```

🖼 Screenshots

[Home Page] <img width="1742" height="776" alt="image" src="https://github.com/user-attachments/assets/181b9ae1-6032-46d3-9714-c03f325304ba" />

[PDF Upload] <img width="1186" height="811" alt="image" src="https://github.com/user-attachments/assets/e33c617e-5b01-4ced-aba2-1520d0dbc5de" />

[Answer Output] <img width="1120" height="749" alt="image" src="https://github.com/user-attachments/assets/dfac7b53-7f34-4e0b-9636-697bc6bffa34" />


⚙ Limitations

Only the first ~15,000 characters of a PDF are processed (due to API limits).

Works best with text-based PDFs, not scanned images.

Long PDFs should be split into smaller segments for accurate results.

📚 Acknowledgments

Google Gemini API

Streamlit

PyPDF2

VTU Internship Program , Google X kaggle AI intensive course

👩‍💻 Author

Thanmayi Prakash






