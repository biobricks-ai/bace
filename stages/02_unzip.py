import zipfile
import os

download_dir = "download"
raw_dir = "raw"
os.makedirs(raw_dir, exist_ok=True)

with zipfile.ZipFile(os.path.join(download_dir, "bace_dataset.zip"), 'r') as zip_ref:
    zip_ref.extractall(raw_dir)
print("Extraction successful")
