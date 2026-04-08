import shutil
import os

backup_file = "sample_backup.txt"
shutil.copy("/Users/timchik/Desktop/pp2/Practice-06/sample.txt", backup_file)
print(f"Backup created: {backup_file}\n")

print("Reading backup file contents:")
with open(backup_file, "r") as f:
    print(f.read())

def safe_delete(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    else:
        print(f"File not found: {file_path}")

safe_delete(backup_file)