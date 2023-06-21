import os
from ChatClient import ChatClient
from ChatClientAzure import ChatClientAzure
import function_calling
import time

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
    while True:
        message = input("Me: ")
        # if message is empty, break
        if message == "":
            print("sys: Good bye.")
            break

        # send message
        #answer, tokens = client.chat(message)
        #answer, tokens = client.send_prompt_with_function_call(message,function_calling.functions)
        #print("AI: ", end='', flush=True)
        #print(answer)
        #print("tokens: " + str(tokens))
        print("AI: ", end='', flush=True)
        for answer, tokens in client.chat_stream(message):
            if answer == "":
                break
            print(answer, end='', flush=True)
            time.sleep(0.1)
        print('')

        # if total tokens over 4000, break
        if tokens > 4000:
            print("sys: Total token over 4000. Good bye.")
            break

if __name__ == '__main__':
    main()