import os
import tarfile
import subprocess

# Download and extract the dataset
def download_and_extract(url, extract_path):    
    # Get the file name from the URL
    file_name = url.split('/')[-1]

    save_path = os.path.join(extract_path, file_name)
    
    # Check if the file already exists
    if not os.path.exists(save_path):
        # Download the file
        print(f"Downloading {file_name}...")
        subprocess.run(["wget", url, "-O", save_path])

        extract_data(extract_path, file_name)
    
    else:
        print(f"{file_name} already exists.")
        extract_data(extract_path, file_name)


def extract_data(path, data_dir):
    # Check if the path exists, if not create it
    if not os.path.exists(path):
        os.makedirs(path)
    
    # Extract the data
    print(f"Extracting {data_dir}...")
    with tarfile.open(os.path.join(path, data_dir), "r:gz") as tar:
        tar.extractall(path)
