import os

src = [
    {
        "type": "AzureCognitiveSearch",
        "parameters": {
                "endpoint": os.environ["AZURE_SEARCH_API_URL"],
                "key": os.environ["AZURE_SEARCH_API_KEY"],
                "indexName": os.environ["AZURE_SEARCH_API_INDEX"],
        }
    }
]
