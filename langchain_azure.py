import os
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import (
    HumanMessage,
)
from langchain.prompts import PromptTemplate

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def chat():
    """
    Chat with OpenAI API.
    """
    chat = AzureChatOpenAI(
        model_name="gpt-35-turbo",
        openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
        openai_api_base=os.environ["AZURE_OPENAI_API_BASE"],
        openai_api_version="2023-06-01-preview",
        deployment_name=os.environ["AZURE_OPENAI_MODEL"],
    )

    message = input("Me: ")
    print("AI: " + chat([HumanMessage(content=message)]).content)


def chat_template():
    """
    Chat with OpenAI API.
    """
    chat = AzureChatOpenAI(
        model_name="gpt-35-turbo",
        openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
        openai_api_base=os.environ["AZURE_OPENAI_API_BASE"],
        openai_api_version="2023-06-01-preview",
        deployment_name=os.environ["AZURE_OPENAI_MODEL"],
    )

    template = PromptTemplate.from_template("{keyword}を解説するQiita記事のタイトル案は?")
    prompt = template.format(keyword="Python")

    print("AI: " + chat([HumanMessage(content=prompt)]).content)


def chat_chain():
    """
    chat chain
    """
    chat = AzureChatOpenAI(
        model_name="gpt-35-turbo",
        openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
        openai_api_base=os.environ["AZURE_OPENAI_API_BASE"],
        openai_api_version="2023-06-01-preview",
        deployment_name=os.environ["AZURE_OPENAI_MODEL"],
    )
