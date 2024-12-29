import sys
import shutil

if len(sys.argv) > 1:
    original_file = sys.argv[1]
    backup_file = f"{original_file}.bak"
    try:
        shutil.copy(original_file, backup_file)
        print(f"Backup of {original_file} created as {backup_file}")
    except FileNotFoundError:
        print(f"Error: The file {original_file} does not exist.")
else:
    print("Please provide a file name.")
