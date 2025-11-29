📘 StudyFlow — PDF Question Answering Agent

StudyFlow is a simple AI-powered PDF Question Answering tool built using Streamlit, Google Gemini API, and PyPDF2.
It allows users to upload a PDF and ask questions based only on the extracted text.

This project was created as part of the VTU internship requirement.

✨ Features

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

http://localhost:8501

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

(Add after uploading images to GitHub)

![Home Page](images/home.png)
![PDF Upload](images/upload.png)
![Answer Output](images/output.png)

⚙ Limitations

Only the first ~15,000 characters of a PDF are processed (due to API limits).

Works best with text-based PDFs, not scanned images.

Long PDFs should be split into smaller segments for accurate results.

📚 Acknowledgments

Google Gemini API

Streamlit

PyPDF2

VTU Internship Program

👩‍💻 Author

Thanmayi Prakash
