import streamlit as st
import PyPDF2
from textblob import TextBlob

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ''
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to translate text
def translate_text(input_text, source_language, target_language):
    blob = TextBlob(input_text)
    translated_text = blob.translate(from_lang=source_language, to=target_language)
    return str(translated_text)

def main():
    st.title("PDF Text Translator")

    # Sidebar
    st.sidebar.title("Tool Options")
    selected_tool = st.sidebar.radio("Select Tool", ["Text Translation"])

    if selected_tool == "Text Translation":
        st.sidebar.header("Translation Settings")
        pdf_file = st.sidebar.file_uploader("Upload PDF file")

        if pdf_file:
            source_language = st.sidebar.selectbox("Source Language", ["en", "ar"])
            target_language = st.sidebar.selectbox("Target Language", ["en", "ar"])
            translate_button = st.sidebar.button("Translate")

            if translate_button:
                try:
                    input_text = extract_text_from_pdf(pdf_file)
                    translated_text = translate_text(input_text, source_language, target_language)
                    st.subheader("Translated Text")
                    st.write(translated_text)
                except Exception as e:
                    st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
