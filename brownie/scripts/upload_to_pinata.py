from pathlib import Path 
from metadata.art_metadata import art_pieces
import requests
import os

PINATA_BASE_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"
filepath_base = "./img/{}"
headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"), 
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}

# filenames = [ 
#     "covid.gif",
#     "essay.jpg",
#     "hand.jpg",
#     "high.gif",
#     "tornado.gif"
# ]

def main():
    for piece in art_pieces.items():
        print(piece)
        # filepath = filepath_base.format(filename)
        # print(f"The current file path is: {filepath}")
        # with Path(filepath).open("rb") as fp: 
        #     image_binary = fp.read()
        #     response = requests.post(
        #         PINATA_BASE_URL + endpoint,
        #         files={"file": (filename, image_binary)},
        #         headers=headers
        #     )
        #     print(response.json())

