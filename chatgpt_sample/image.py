import openai
import settings
import requests
import json

prompt = """
頭が赤い魚を食べた猫
"""

def create_image_from_text(text):
     # api key の設定
    openai.api_key = settings.api_key

    # 応答設定
    response = openai.Image.create(
                  prompt = text,             # 画像生成に用いる説明文章
                  n = 1,                     # 何枚の画像を生成するか
                  size = '512x512',          # 画像サイズ
                  response_format = "url"    # API応答のフォーマット
                )

    # API応答から画像URLを指定
    image_url = response['data'][0]['url']
    
    # 画像をローカルに保存
    image_data = requests.get(image_url).content
    with open("chat-gpt-generated-image.jpg", "wb") as f:
        f.write(image_data)
        
    return image_url

if __name__ == '__main__':
    create_image_from_text(prompt)