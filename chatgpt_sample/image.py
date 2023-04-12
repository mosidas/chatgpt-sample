import openai
import settings
import requests
import datetime

prompt = """
頭が赤い魚を食べた猫
"""

def create_image_from_text(text):
    # api key の設定
    openai.api_key = settings.api_key

    # 応答設定
    response = openai.Image.create(
        # プロンプト
        prompt = text,
        # 何枚の画像を生成するか  1〜10
        n = 1,
        # 画像サイズ 256x256、512x512、1024x1024
        size = '512x512',
        # API応答のフォーマット url b64_json
        response_format = 'url'
        )

    # API応答から画像URLを指定
    image_url = response['data'][0]['url']

    # 画像をローカルに保存
    dt_now = datetime.datetime.now()
    image_data = requests.get(image_url).content
    with open(f"chatgpt_image_{dt_now.strftime('%Y-%m-%d-%H-%M-%S')}.jpg", "wb") as f:
        f.write(image_data)

    return image_url

if __name__ == '__main__':
    print(create_image_from_text(prompt))