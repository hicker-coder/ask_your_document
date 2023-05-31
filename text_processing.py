from langchain.text_splitter import CharacterTextSplitter


def split_text_into_chunks(text):
    """
    Split the text into chunks using a character-based text splitter.
    """
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks
