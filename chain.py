import os
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import (
    HumanMessage,
)
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def chat():
    chat = AzureChatOpenAI(
        model_name='gpt-35-turbo',
        openai_api_key = os.environ["AZURE_OPENAI_API_KEY"] ,
        openai_api_base = os.environ["AZURE_OPENAI_API_BASE"],
        openai_api_version = "2023-06-01-preview",
        deployment_name = os.environ["AZURE_OPENAI_MODEL"],
        )
    template = PromptTemplate.from_template("{keyword}を解説するQiita記事のタイトル案は?")

    chain = LLMChain(llm=chat, prompt=template)
    output = chain.run("Azure")

    print(output)