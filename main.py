import os
from ChatClient import ChatClient
from ChatClientAzure import ChatClientAzure
import function_calling
import time
import gpt_token

def main():
    # api key setting from environment variable
    api_key = os.environ["OPENAI_API_KEY"]
    # create chat client
    client = ChatClient(api_key,"gpt-3.5-turbo-0613",function_calling.functions)
    # # setting from environment variable
    # api_key = os.environ["AZURE_OPENAI_API_KEY"]
    # api_base = os.environ["AZURE_OPENAI_API_BASE"]
    # model = os.environ["AZURE_OPENAI_MODEL"]
    # # create chat client
    # client = ChatClientAzure(api_key, api_base, model)
    estimated_message_tokens = []
    estimated_answer_tokens = []
    while True:
        # get message
        message = input("Me: ")
        estimated_message_tokens.append(gpt_token.count_tokens_gpt35(message))
        # if message is empty, break
        if message == "":
            print("sys: Good bye.")
            break

        # send message
        # answer, tokens = client.chat(message)
        # send message with function calling
        # answer, tokens = client.send_prompt_with_function_call(message,function_calling.functions)
        # estimated_answer_tokens.append(gpt_token.count_tokens_gpt35(answer))
        # print("AI: " + answer)
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

        print('---')
        print("sys: Estimated message tokens: " + str(estimated_message_tokens[-1]))
        print("sys: Estimated answer tokens : " + str(estimated_answer_tokens[-1]))
        print("sys: Estimated total tokens  : " + str(sum(estimated_answer_tokens) + sum(estimated_message_tokens)))
        print("sys: Actually total tokens   : " + str(tokens))
        print('---')

        # if total tokens over 4000, break
        if tokens > 4000:
            print("sys: Total token over 4000. Good bye.")
            break

if __name__ == '__main__':
    main()