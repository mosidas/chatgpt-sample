import openai
import settings

def main():
    # api key の設定
    openai.api_key = settings.api_key

    # プロンプトの設定
    responce = openai.ChatCompletion.create(
        # モデル
        model="gpt-3.5-turbo",
        # プロンプト
        messages=[
            {"role": "system", "content": "関西弁で話してください。"},     # 役割設定（省略可）
            {"role": "user", "content": "人生で大切なことは何ですか？"},   # 最初の質問
        ],
        #temperature=1  # 温度（0-2, デフォルト1）
    )

    answer = responce["choices"][0]["message"]["content"]
    print(answer)

if __name__ == '__main__':
    main()