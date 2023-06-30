functions =[
    {
        "name": "get_taros_profile",
        "description": "太郎さんの情報を得る。太郎さんの情報の項目は英語で設定されている。",
        "parameters": {
            "type": "object",
            "properties": {
                "item": {
                    "type": "string",
                    "description": "太郎さんの情報の項目を指定する。英語で指定する。",
                },
            },
            "required": ["item"],
        },
    },
    {
        "name": "get_jiros_profile",
        "description": "次郎さんの情報を得る。次郎さんの情報の項目は英語で設定されている。",
        "parameters": {
            "type": "object",
            "properties": {
                "item": {
                    "type": "string",
                    "description": "次郎さんの情報の項目を指定する。英語で指定する。",
                },
            },
            "required": ["item"],
        },
    },
]

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