import os
from fit_to_csv import process_fit_to_csv

if __name__ == "__main__":
    source_dir = r"/home/emac/Documents/perso/fit_to_csv/data/fit"
    target_dir = r"/home/emac/Documents/perso/fit_to_csv/data/csv"

    # Check directory
    os.makedirs(target_dir, exist_ok=True)

    for file_name in os.listdir(source_dir):
        if file_name.endswith(".fit"):
            source_file = os.path.join(source_dir, file_name)
            # print(f"Processing {source_file}...")
            process_fit_to_csv(source_file, target_dir)

    print("Processing complete for all FIT files !")