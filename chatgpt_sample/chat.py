import openai
import settings

prompt = """
- じゃんけんをプレイできるアプリケーション
- pythonで作成する
"""
def main():
    # api key の設定
    openai.api_key = settings.api_key

    # プロンプトの設定
    responce = openai.ChatCompletion.create(
        # モデル
        model="gpt-3.5-turbo",
        # プロンプト
        messages=[
            # 役割設定（省略可）
            {"role": "system", "content": "あなたはプログラム開発者です。指定された条件でプログラムコードを出力してください。"},
            # 最初の質問
            {"role": "user", "content": prompt},
        ],
        # 温度（0-2, デフォルト1）
        #temperature=1
    )

    answer = responce["choices"][0]["message"]["content"]
    print("answer: " + answer)
    print("total_tokens: " + str(responce["usage"]["total_tokens"]))

if __name__ == '__main__':
    main()