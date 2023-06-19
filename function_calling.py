functions =[
    {
        "name": "get_taros_profile",
        "description": "太郎さんの情報を得る",
        "parameters": {
            "type": "object",
            "properties": {
                "item": {
                    "type": "string",
                    "description": "taro's profile item",
                },
            },
            "required": ["item"],
        },
    }
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
        return "error: item is not in my profile"
    else:
        return str(my_profile[item])