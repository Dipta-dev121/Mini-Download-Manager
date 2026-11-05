import requests
from urllib.parse import urlparse, unquote
import os
import time


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
        total_size = int(response.headers.get("content-length", 0))

        # Numbering duplicate filenames
        base, extension = os.path.splitext(filename)
        counter = 1
        while os.path.exists(f"../downloads/{filename}"):
            filename = f"{base}({counter}){extension}"
            counter += 1

        # writing the response content into file
        downloaded_size = 0
        start_time = time.perf_counter()
        with open(f"../downloads/{filename}", "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)

                    downloaded_size += len(chunk)

                    elapsed_time = time.perf_counter() - start_time
                    speed = downloaded_size / elapsed_time / (1024 * 1024)

                    #shows progress
                    if total_size > 0:
                        progress = (downloaded_size / total_size) * 100
                        print(f"\rProgress: {progress:.2f}% | "f"Speed: {speed:.2f} MB/s",end="")

        print("Download Complete!")
    except requests.exceptions.RequestException as error:
        print("Download failed:", error)
