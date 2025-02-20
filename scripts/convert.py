# File: scripts/convert.py

import csv
import json
import os


def csv_to_json(csv_file_path, json_file_path):
    """
    Converts a CSV file to a JSON file in a meaningful way.
    """
    data = {}

    with open(csv_file_path, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)  # Extract headers from the first row

        for row in csv_reader:
            key = row[0]  # Use the first column as the key
            values = row[1:]  # Remaining columns as values
            data[key] = {headers[i + 1]: float(values[i]) for i in range(len(values))}

    with open(json_file_path, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)


def ensure_directories():
    """
    Ensures that the required directories (res/csv and res/json) exist.
    """
    base_res_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../res"))
    csv_folder_path = os.path.join(base_res_path, "csv")
    json_folder_path = os.path.join(base_res_path, "json")

    # Create directories if they don't exist
    os.makedirs(csv_folder_path, exist_ok=True)
    os.makedirs(json_folder_path, exist_ok=True)

    return csv_folder_path, json_folder_path


def convert_all_csv_to_json():
    """
    Converts all CSV files in the res/csv directory to JSON files in the res/json directory.
    """
    # Ensure necessary directories exist and get their paths
    csv_folder_path, json_folder_path = ensure_directories()

    # Process all .csv files in the res/csv folder
    for file_name in os.listdir(csv_folder_path):
        if file_name.endswith(".csv"):
            csv_file_path = os.path.join(csv_folder_path, file_name)
            json_file_path = os.path.join(
                json_folder_path, f"{os.path.splitext(file_name)[0]}.json"
            )

            print(f"Converting {csv_file_path} to {json_file_path}...")
            csv_to_json(csv_file_path, json_file_path)
            print(f"Conversion complete: {json_file_path}")


if __name__ == "__main__":
    convert_all_csv_to_json()
