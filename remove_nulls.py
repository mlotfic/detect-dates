import os

def clean_null_bytes_in_file(file_path):
    with open(file_path, "rb") as f:
        data = f.read()

    if b"\x00" in data:
        cleaned = data.replace(b"\x00", b"")
        with open(file_path, "wb") as f:
            f.write(cleaned)
        print(f"[CLEANED] {file_path}")
    else:
        print(f"[OK]      {file_path}")

def clean_folder(root_folder):
    for root, _, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                clean_null_bytes_in_file(file_path)

if __name__ == "__main__":
    folder_to_clean = "src"   # change if needed
    clean_folder(folder_to_clean)
    print("Cleaning completed.")