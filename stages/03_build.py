import pandas as pd
import shutil
from pathlib import Path

raw_dir = Path("raw")
brick_dir = Path("brick")
pdb_dir = brick_dir / "pdb"

brick_dir.mkdir(parents=True, exist_ok=True)
pdb_dir.mkdir(parents=True, exist_ok=True)

# Convert CSV files to Parquet
for csv_file in raw_dir.glob('**/*.csv'):
    df = pd.read_csv(csv_file, encoding='ISO-8859-1')  # Assuming the files are encoded in ISO-8859-1
    if not df.empty:
        parquet_file_path = brick_dir / f"{csv_file.stem}.parquet"
        df.to_parquet(parquet_file_path, engine='pyarrow')
        print(f"Parquet file created for {csv_file.name}")

# Copy PDB files
for pdb_file in raw_dir.glob('**/*.pdb'):
    shutil.copy(pdb_file, pdb_dir)
    print(f"Copied PDB file {pdb_file.name} to {pdb_dir}")

