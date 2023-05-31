from dotenv import load_dotenv
import streamlit as st
from file_handler import load_pdf_text
from text_processing import split_text_into_chunks
from embeddings import create_embeddings
from question_answering import ask_question


def main():
    load_dotenv()
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF 💬")

    # Upload file
    pdf_file = st.file_uploader("Upload your PDF", type="pdf")

    # Extract the text
    if pdf_file is not None:
        text = load_pdf_text(pdf_file)
        chunks = split_text_into_chunks(text)
        knowledge_base = create_embeddings(chunks)

        # Show user input
        user_question = st.text_input("Ask a question about your PDF:")
        if user_question:
            response = ask_question(knowledge_base, user_question)
            st.write(response)


if __name__ == '__main__':
    main()
