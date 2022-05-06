from pathlib import Path 
from metadata.art_metadata import public_metadata_template, art_piece_metadata
from brownie import network
import requests
import json
import os

PINATA_BASE_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"
image_filepath_template = "./img/{}"
image_uri_template = "https://ipfs.io/ipfs/{}?filename={}"
metadata_filepath_template = "./metadata/{}/{}"
headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"), 
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}

def main():
    # print(network.show_active())
    for piece in art_piece_metadata.values():
        # print(piece)
        if (piece["name"] == None):
             continue 

        filename = piece["filename"]
        filepath = image_filepath_template.format(filename)
        print(f"The current file path is: {filepath}")
        response_json = pin_file_to_pinata(filepath)
        ipfs_hash = response_json["IpfsHash"]
        image_uri = image_uri_template.format(ipfs_hash, filename)
        upload_json(image_uri, piece)

def upload_json(image_uri, art_piece_metadata):
    metadata = public_metadata_template
    metadata["name"] = art_piece_metadata["name"]
    metadata["description"] = art_piece_metadata["description"]
    metadata["image_uri"] = image_uri
    filepath = metadata_filepath_template.format(network.show_active(), 
        art_piece_metadata["name"])
    if Path(filepath).exists():
        print(f"{filepath} already exists.")
    else: 
        with open(filepath, "w") as file:
            json.dump(metadata, file)
            pin_file_to_pinata(file)


def pin_file_to_pinata(filepath):
    filename = filepath.split("/")[-1:][0]
    with Path(filepath).open("rb") as fp: 
        file_binary = fp.read()
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (filename, file_binary)},
            headers=headers
        )
        print(response.json())
        return response.json()
           
