import os
from ChatClient import ChatClient
import function_calling

def main():
    # api key setting from environment variable
    api_key = os.environ["OPENAI_API_KEY"]
    # create chat client
    client = ChatClient(
        api_key,
        "gpt-3.5-turbo-0613",
        function_calling.functions)
    while True:
        message = input("Me: ")
        # if message is empty, break
        if message == "":
            print("sys: Good bye.")
            break

        # answer, total_tokens
        answer, total_tokens = client.send_prompt(message)
        print("AI: " + answer)
        print("total_tokens: " + str(total_tokens))

        # if total tokens over 4000, break
        if total_tokens > 4000:
            print("sys: Total token over 4000. Good bye.")
            break

if __name__ == '__main__':
    main()