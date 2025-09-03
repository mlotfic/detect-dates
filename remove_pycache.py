import os
import shutil

def remove_pycache(root_folder):
    for root, dirs, files in os.walk(root_folder):
        for d in dirs:
            if d == "__pycache__":
                cache_path = os.path.join(root, d)
                try:
                    shutil.rmtree(cache_path)
                    print(f"[REMOVED] {cache_path}")
                except Exception as e:
                    print(f"[ERROR]   {cache_path} -> {e}")

if __name__ == "__main__":
    folder_to_clean = "."   # current folder, change if needed
    remove_pycache(folder_to_clean)
