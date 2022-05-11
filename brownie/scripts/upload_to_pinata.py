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
metadata_filepath_template = "metadata/{}/{}.json"
headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"), 
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}

def main():
    print(network.show_active())
    for piece in art_piece_metadata.values():
        print(piece)
        if (piece["name"] == None):
            continue 

        filename = piece["filename"]
        filepath = image_filepath_template.format(filename)
        print(f"The current file path is: {filepath}")
        pinata_response = pin_file_to_pinata(filepath)
        ipfs_hash = pinata_response["IpfsHash"]
        image_uri = image_uri_template.format(ipfs_hash, filename)
        pin_json_to_pinata(image_uri, piece)

def pin_json_to_pinata(image_uri, art_piece_metadata):
    metadata = public_metadata_template
    metadata["name"] = art_piece_metadata["name"]
    metadata["description"] = art_piece_metadata["description"]
    metadata["image"] = image_uri
    filepath = metadata_filepath_template.format(network.show_active(), 
        art_piece_metadata["name"])
    if Path(filepath).exists():
        print(f"{filepath} already exists.")
    else: 
        print(os.getcwd())
        with open(filepath, "w") as file:
            json.dump(metadata, file)
            response = pin_file_to_pinata_2(filepath)

def pin_file_to_pinata(filepath):
    filename = filepath.split("/")[-1]
    with Path(filepath).open("rb") as fp: 
        file_binary = fp.read()
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (filename, file_binary)},
            headers=headers
        )
        print(response.json())
        return response.json()
           
def pin_file_to_pinata_2(filepath):
    print('---pin_file_to_pinata_2---')
    print(filepath)
    filename = filepath.split("/")[-1]
    print(filename)
    with Path(filepath).open("r") as fp: 
        # file_binary = json.load(fp.read())
        file_binary = '{"name": "covid", "description": "desc", "image": "https://ipfs.io/ipfs/QmfGRphZSS2avjtZFPa7FvfDL4h2sXPDbtk1c5f6eZHkup?filename=covid.gif"}'
        print(file_binary)
        print(fp)
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (filename, file_binary)},
            headers=headers
        )
        print(response.json())
        return response.json()
