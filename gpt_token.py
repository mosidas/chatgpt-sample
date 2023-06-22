import tiktoken
from tiktoken.core import Encoding

def count_characters(text):
    """
    文字数をカウントする
    """
    return len(text)

def count_tokens_gpt35(text):
    """
    gpt-3.5におけるトークン数をカウントする
    """
    encoding: Encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    tokens = encoding.encode(text)
    return len(tokens)