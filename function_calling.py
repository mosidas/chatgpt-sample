import requests
import urllib.parse
import json

# functions =[
#     {
#         "name": "get_taros_profile",
#         "description": "太郎さんの情報を得る。太郎さんの情報の項目は英語で設定されている。",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "item": {
#                     "type": "string",
#                     "description": "太郎さんの情報の項目を指定する。英語で指定する。",
#                 },
#             },
#             "required": ["item"],
#         },
#     },
#     {
#         "name": "get_jiros_profile",
#         "description": "次郎さんの情報を得る。次郎さんの情報の項目は英語で設定されている。",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "item": {
#                     "type": "string",
#                     "description": "次郎さんの情報の項目を指定する。英語で指定する。",
#                 },
#             },
#             "required": ["item"],
#         },
#     },
# ]

functions =[
    {
        "name": "get_profiles",
        "description": "人物の情報リストを得る。",
        "parameters": {
            "type": "object",
            "properties": {
                "item": {
                    "type": "string",
                    "description": "人物の情報を検索するためのキーを指定する。複数ある場合はスペース区切りで指定する。",
                },
                "skip": {
                    "type": "integer",
                    "description": "同じitemで別の検索結果を要求されているとき、この値を5ずつふやす。初期値は0。",
                },
            },
            "required": ["item"],
        },
    },
]


def get_profiles(item, skip=0, top=5):
    encoded_item = urllib.parse.quote(item)
    url = "https:/xxx"
    headers = {
        "api-key":"xxx",
        "Content-Type":"application/json;charset=utf-8"}

    body = {
        "search": item,
        "searchFields": "name",
        "searchMode": "all",
        "queryType": "simple",
        "select": "name, kana, age, date, sex, blood, mail, tel, tel2, code, address, corp, credit, expiry, mynumber",
        "count": "true",
        "skip": skip,
        "top": 5
    }
    res = requests.post(url, headers=headers,json=body)
    res_json = res.json()
    values = res_json['value']
    return str(values)


def get_taros_profile(item):
    # define my profile
    my_profile = {
        "name": "太郎",
        "age": 20,
        "height": 170,
        "weight": 60,
        "hobby": "野球",
    }

    # if item is not in my profile, return error
    if item not in my_profile:
        return "no infomation."
    else:
        return str(my_profile[item])

def get_jiros_profile(item):
    # define my profile
    my_profile = {
        "name": "次郎",
        "age": 35,
        "height": 197,
        "weight": 99,
        "hobby": "サッカー",
    }

    # if item is not in my profile, return error
    if item not in my_profile:
        return "no infomation."
    else:
        return str(my_profile[item])