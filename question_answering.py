from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback


def ask_question(knowledge_base, user_question):
    """
    Answer user's question based on the knowledge base.
    """
    docs = knowledge_base.similarity_search(user_question)

    llm = OpenAI()
    chain = load_qa_chain(llm, chain_type="stuff")
    with get_openai_callback() as cb:
        response = chain.run(input_documents=docs, question=user_question)

    return response
