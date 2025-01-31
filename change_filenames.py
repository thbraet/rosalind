import os
import re

def sanitize_filename(filename):
    """Convert filename to lowercase with underscores instead of camelCase and spaces."""
    # Replace spaces with underscores
    filename = filename.replace(" ", "_")
    
    # Convert camelCase to snake_case
    filename = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', filename)

    # Ensure everything is lowercase
    return filename.lower()

def rename_files_and_folders(root_dir):
    """Recursively rename all files and folders in root_dir."""
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):  # Bottom-up to rename files first
        for filename in filenames:
            old_path = os.path.join(dirpath, filename)
            new_filename = sanitize_filename(filename)
            new_path = os.path.join(dirpath, new_filename)
            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f"Renamed file: {old_path} -> {new_path}")

        for dirname in dirnames:
            old_path = os.path.join(dirpath, dirname)
            new_dirname = sanitize_filename(dirname)
            new_path = os.path.join(dirpath, new_dirname)
            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f"Renamed folder: {old_path} -> {new_path}")

# Usage
root_folder = "/home/thbraet/thbraet.github.io/bioinformatics/rosalind"  # Change this to your target directory
rename_files_and_folders(root_folder)
