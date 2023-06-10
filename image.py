import openai
import settings
import requests
import datetime

prompt = """
頭が赤い魚を食べた猫
"""

def create_image_from_text(text):
    # api key setting
    openai.api_key = settings.api_key

    # send prompt
    response = openai.Image.create(
        # prompt
        prompt = text,
        # images number (1-10)
        n = 1,
        # image size 256x256、512x512、1024x1024
        size = '512x512',
        # url b64_json
        response_format = 'url'
        )

    # get image url
    image_url = response['data'][0]['url']

    # save image to current directory
    dt_now = datetime.datetime.now()
    image_data = requests.get(image_url).content
    with open(f"chatgpt_image_{dt_now.strftime('%Y-%m-%d-%H-%M-%S')}.jpg", "wb") as f:
        f.write(image_data)

    return image_url

if __name__ == '__main__':
    print(create_image_from_text(prompt))