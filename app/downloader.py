import requests

def download_file(url):
    try:
        response=requests.get(url)
        response.raise_for_status()
        
        with open("../downloads/file.zip", "wb") as file:
            file.write(response.content)

        print("Download Complete!")
    except requests.exceptions.RequestException as error:
        print("Download failed:", error)