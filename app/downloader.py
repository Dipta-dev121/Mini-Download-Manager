import requests
from urllib.parse import urlparse, unquote
import os


def download_file(url):
    # Parsing the url into parts
    parsed_url = urlparse(url)
    filename = unquote(
        parsed_url.path.split("/")[-1]
    )  # takes the last split and unquote

    if not filename:
        filename = "downloaded_file"

    # Requesting the url response
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        #Numbering duplicate filenames
        base, extension = os.path.splitext(filename)
        counter = 1
        while os.path.exists(f"../downloads/{filename}"):
            filename = f"{base}({counter}){extension}"
            counter+=1

        # writing the response content into file
        with open(f"../downloads/{filename}", "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)

        print("Download Complete!")
    except requests.exceptions.RequestException as error:
        print("Download failed:", error)
