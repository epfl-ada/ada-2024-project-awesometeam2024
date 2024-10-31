import os
import tarfile
import urllib.request

def download_and_extract(url, extract_path):    
    file_name = url.split('/')[-1]
    
    if not os.path.exists(file_name):
        print(f"Downloading {file_name}...")
        urllib.request.urlretrieve(url, file_name)
        print("Download complete.")
    else:
        print(f"{file_name} already exists.")
    
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)
    
    with tarfile.open(file_name, "r:gz") as tar:
        tar.extractall(path=extract_path)
        print(f"Extracted to {extract_path}")

    # Remove file we don't need ???
