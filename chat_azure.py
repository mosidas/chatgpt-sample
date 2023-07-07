from ChatClientAzure import ChatClientAzure
import os
import time
import gpt_token
import data_sources

api_key = os.environ["AZURE_OPENAI_API_KEY"]
api_base = os.environ["AZURE_OPENAI_API_BASE"]
model = os.environ["AZURE_OPENAI_MODEL"]

estimated_message_tokens = []
estimated_answer_tokens = []
# system_prompt = "あなたはAIアシスタントです。"
system_prompt = None

def print_estimated_tokens():
    print('---')
    print("sys: Estimated message tokens: " + str(estimated_message_tokens[-1]))
    print("sys: Estimated answer tokens : " + str(estimated_answer_tokens[-1]))
    print("sys: Estimated total tokens  : " + str(sum(estimated_answer_tokens) + sum(estimated_message_tokens)))
    print('---')

def chat():
    while True:
        client = ChatClientAzure(api_key, api_base, model, "2023-06-01-preview", system_prompt)
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

def chat_on_your_data():
    while True:
        client = ChatClientAzure(api_key, api_base, model, "2023-06-01-preview", system_prompt)
        # get message
        message = input("Me: ")
        estimated_message_tokens.append(gpt_token.count_tokens_gpt35(message))
        # if message is empty, break
        if message == "":
            print("sys: Good bye.")
            break

        try:
            # send message
            answer, tokens = client.chat_on_your_data(message, data_sources.src)
            estimated_answer_tokens.append(gpt_token.count_tokens_gpt35(answer))
            print("AI: " + answer)
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

def chat_stream():
    while True:
        client = ChatClientAzure(api_key, api_base, model, "2023-06-01-preview", system_prompt)
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
                if answer == "":
                    break
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