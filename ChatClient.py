import json
import openai
import function_calling

class ChatClient:
    def __init__(self, api_key, model, functions):
        self.api_key = api_key
        self.past_messages = []
        self.model = model
        self.functions = functions
        openai.api_key = self.api_key

    def send_prompt(self, message):
        self.past_messages.append({"role": "user", "content": message})

        # send prompt
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.past_messages,
            functions=self.functions,
            function_call="auto",
            temperature=1
        )

        message = response["choices"][0]["message"]

        if message.get("function_call"):
            func_name = message["function_call"]["name"]
            arguments = json.loads(message["function_call"]["arguments"])
            function_response = function_calling.get_my_profile(arguments.get("item"))

            self.past_messages.append({
                "role": "function",
                "name": func_name,
                "content": function_response
                })

            second_answer = openai.ChatCompletion.create(
                model=self.model,
                messages=self.past_messages,
            )

            answer = second_answer.choices[0].message["content"]
            total_tokens = second_answer.usage["total_tokens"]

            return answer, total_tokens
        else:
            answer = response.choices[0].message["content"]
            total_tokens = response.usage["total_tokens"]

            self.past_messages.append({"role": "assistant", "content": answer})

            return answer, total_tokens

