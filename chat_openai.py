import os
from ChatClient import ChatClient
import function_calling
import time
import gpt_token

api_key = os.environ["OPENAI_API_KEY"]

estimated_message_tokens = []
estimated_answer_tokens = []
system_prompt = "あなたはAIアシスタントです。"

def print_estimated_tokens():
    print('---')
    print("sys: Estimated message tokens: " + str(estimated_message_tokens[-1]))
    print("sys: Estimated answer tokens : " + str(estimated_answer_tokens[-1]))
    print("sys: Estimated total tokens  : " + str(sum(estimated_answer_tokens) + sum(estimated_message_tokens)))
    print('---')

def chat():
    while True:
        client = ChatClient(api_key, "gpt-3.5-turbo-0613", function_calling.functions, system_prompt)
        # get message
        message = input("Me: ")
        estimated_message_tokens.append(gpt_token.count_tokens_gpt35(message))
        # if message is empty, break
        if message == "":
            print("sys: Good bye.")
            break

        try:
            # send message
            answer, tokens = client.chat(message)
            estimated_answer_tokens.append(gpt_token.count_tokens_gpt35(answer))
            print("AI: " + answer)
        except Exception as e:
            err_code, err_message = e.args
            client.remove_last_message()
            print("sys: " + err_message + " (" + err_code + ")")

        print_estimated_tokens()

        # if total tokens over 4000, break
        if tokens > 4000:
            print("sys: Total token over 4000. Good bye.")
            break

def chat_function_calling():
    while True:
        client = ChatClient(api_key, "gpt-3.5-turbo-0613", function_calling.functions, system_prompt)
        # get message
        message = input("Me: ")
        estimated_message_tokens.append(gpt_token.count_tokens_gpt35(message))
        # if message is empty, break
        if message == "":
            print("sys: Good bye.")
            break

        try:
            # send message
            answer, tokens = client.chat_with_function_call(message)
            estimated_answer_tokens.append(gpt_token.count_tokens_gpt35(answer))
            print("AI: " + answer)
            print_estimated_tokens()
            # if total tokens over 4000, break
            if tokens > 4000:
                print("sys: Total token over 4000. Good bye.")
                break
        except Exception as e:
                print("sys: " + str(e))


def chat_stream():
    while True:
        client = ChatClient(api_key, "gpt-3.5-turbo-0613", function_calling.functions, system_prompt)
        # get message
        message = input("Me: ")
        estimated_message_tokens.append(gpt_token.count_tokens_gpt35(message))
        # if message is empty, break
        if message == "":
            print("sys: Good bye.")
            break

        try:
            # send message with stream
            print("AI: ", end='', flush=True)
            answers = []
            for answer, tokens in client.chat_stream(message):
                print(answer, end='', flush=True)
                answers.append(answer)
                time.sleep(0.05)
            print('')
            estimated_answer_tokens.append(gpt_token.count_tokens_gpt35("".join(answers)))
        except Exception as e:
            if len(e.args) == 2:
                err_code, err_message = e.args
                client.remove_last_message()
                print("sys: " + err_message + " (" + err_code + ")")
            else:
                print("sys: " + e)

        print_estimated_tokens()

        # if total tokens over 4000, break
        if tokens > 4000:
            print("sys: Total token over 4000. Good bye.")
            break