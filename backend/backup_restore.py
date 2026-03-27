import shutil
import os
from datetime import datetime

def backup(source, destination):
    """Creates a backup of the specified source directory or file."""
    if os.path.exists(source):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_name = f"{os.path.basename(source)}_backup_{timestamp}"
        backup_path = os.path.join(destination, backup_name)
        
        if os.path.isdir(source):
            shutil.make_archive(backup_path, 'zip', source)
        else:
            shutil.copy2(source, backup_path)
        print(f"Backup created at: {backup_path}")
    else:
        print(f"Source {source} does not exist.")

def restore(backup_file, destination):
    """Restores from a backup zip file to the specified destination."""
    if os.path.exists(backup_file):
        shutil.unpack_archive(backup_file, destination)
        print(f"Restored backup from: {backup_file} to {destination}")
    else:
        print(f"Backup file {backup_file} does not exist.")
