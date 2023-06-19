import openai
import os

past_messages = []

def send_prompt(message, past_messages=[]):
    # message history
    messages = past_messages + [{"role": "user", "content": message}]

    # send prompt
    responce = openai.ChatCompletion.create(
        # model (gpt-4 is not available)
        model="gpt-3.5-turbo",
        # prompt
        messages = messages,
        # temperature (0 - 2, default: 1)
        temperature=1
    )

    return responce


def main():
    # api key setting from environment variable
    openai.api_key = os.environ["OPENAI_API_KEY"]

    while True:
        message = input("Me: ")
        # if message is empty, break
        if message == "":
            print("system: Good bye.")
            break

        responce = send_prompt(message,past_messages)
        answer = responce["choices"][0]["message"]["content"]
        tokens = responce["usage"]["total_tokens"]
        print("AI: " + answer)
        print("total_tokens: " + str(responce["usage"]["total_tokens"]))
        past_messages.append({"role": "user", "content": message})
        past_messages.append({"role": "assistant", "content": answer})
        # if total tokens over 4000, break
        if tokens > 4000:
            print("system: Total token over 4000. Good bye.")
            break

if __name__ == '__main__':
    main()