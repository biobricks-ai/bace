import requests
import os

url = "https://drugdesigndata.org/php/file-download.php?type=extended&id=233"
download_dir = "download"
os.makedirs(download_dir, exist_ok=True)
zip_file_path = os.path.join(download_dir, "bace_dataset.zip")

response = requests.get(url)
if response.status_code == 200:
    with open(zip_file_path, 'wb') as f:
        f.write(response.content)
    print("Download successful")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
