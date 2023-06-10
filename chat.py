import openai
import settings

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
    # api key setting
    openai.api_key = settings.api_key

    while True:
        message = input("message: ")
        responce = send_prompt(message,past_messages)
        answer = responce["choices"][0]["message"]["content"]
        tokens = responce["usage"]["total_tokens"]
        print("answer: " + answer)
        print("total_tokens: " + str(responce["usage"]["total_tokens"]))
        past_messages.append({"role": "user", "content": message})
        past_messages.append({"role": "assistant", "content": answer})
        if tokens > 4000:
            print("total token over 4000.")
            break

if __name__ == '__main__':
    main()