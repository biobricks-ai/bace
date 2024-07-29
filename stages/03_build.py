import pandas as pd
import os
import shutil

raw_dir = "raw"
brick_dir = "brick"
pdb_dir = os.path.join(brick_dir, "pdb")
os.makedirs(brick_dir, exist_ok=True)
os.makedirs(pdb_dir, exist_ok=True)

for root, dirs, files in os.walk(raw_dir):
    for file in files:
        # Skip files in the __MACOSX folder
        if '__MACOSX' in root:
            continue

        if file.endswith('.csv'):
            csv_file_path = os.path.join(root, file)
            parquet_file_path = os.path.join(brick_dir, f"{os.path.splitext(file)[0]}.parquet")

            # Try reading the CSV file with different encodings
            df = None
            for encoding in ['utf-8', 'ISO-8859-1', 'cp1252']:
                try:
                    df = pd.read_csv(csv_file_path, encoding=encoding)
                    break  # Exit the loop if read successfully
                except UnicodeDecodeError:
                    continue

            if df is not None and not df.empty:
                # Write to Parquet file
                df.to_parquet(parquet_file_path, engine='pyarrow')
                print(f"Parquet file created for {file}")
            else:
                print(f"Skipping {file} as it contains no data.")
        elif file.endswith('.pdb'):
            pdb_file_path = os.path.join(root, file)
            shutil.copy(pdb_file_path, pdb_dir)
            print(f"Copied PDB file {file} to {pdb_dir}")
