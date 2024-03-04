import requests

def download_files(url):
    local_filename = url.split("/")[-1]
    with requests.get(url, stream=True) as r:
        print("Downloading...")