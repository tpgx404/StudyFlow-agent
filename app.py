import os
import streamlit as st
import google.generativeai as genai
import PyPDF2

st.set_page_config(page_title="StudyFlow — PDF Question Answering Agent", layout="centered")
st.title("StudyFlow — PDF Question Answering Agent")

# --- API KEY HANDLING (Secrets + fallback) ---
# 1. Try to read from Streamlit Secret (os.environ)
api_key = os.getenv("GEMINI_API_KEY")

# 2. If no secret found, show input box (for local testing)
if not api_key:
    api_key = st.text_input("Enter your Gemini API Key", type="password")

# 3. Stop if still no key
if not api_key:
    st.info("Enter your Gemini API key above to enable the agent.")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)

# --- Model selection ---
model_id = st.selectbox(
    "Choose a Gemini model:",
    [
        "gemini-2.5-flash",
        "gemini-2.5-pro",
        "gemini-2.0-flash",
        "gemini-2.0-flash-001"
    ],
)

model = genai.GenerativeModel(model_id)

# --- PDF Upload ---
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    pdf_text = ""
    reader = PyPDF2.PdfReader(uploaded_file)

    for page in reader.pages:
        text = page.extract_text()
        if text:
            pdf_text += text + "\n"

    # Limit text to avoid token overload
    if len(pdf_text) > 15000:
        pdf_text = pdf_text[:15000]
        st.warning("PDF too large. Only first 15000 characters used.")

    st.success("PDF loaded successfully.")

    question = st.text_input("Ask a question based on the PDF:")

    # --- Generate Answer ---
    if question:
        with st.spinner("Thinking..."):
            prompt = f"""
Use ONLY the text below to answer the question. 
If the answer is not in the document, reply exactly:
"I cannot find that information in the document."

DOCUMENT:
{pdf_text}

QUESTION:
{question}
"""

            try:
                response = model.generate_content(prompt)
                st.write("### Answer:")
                st.write(response.text)

            except Exception as e:
                st.error("Model failed to respond.")
                st.error(str(e))

