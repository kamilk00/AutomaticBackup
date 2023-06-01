import os
import shutil
from datetime import datetime

def create_backup():

    current_date = datetime.now().strftime("%d_%m_%Y")
    backup_folder = f"backup_{current_date}"
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    #read file paths from the given txt file
    with open("files_to_backup.txt", "r") as file:
        file_paths = file.read().splitlines()

    #create files backup
    for file_path in file_paths:
        if os.path.exists(file_path):
            file_name = os.path.basename(file_path) + f'_{current_date}'
            backup_path = os.path.join(backup_folder, file_name)
            shutil.copy2(file_path, backup_path)

    #read folder paths from the given txt file
    with open("folders_to_backup.txt", "r") as file:
        folder_paths = file.read().splitlines()
    
    #create backup of folders
    for folder_path in folder_paths:
        if os.path.exists(folder_path):
            folder_name = os.path.basename(folder_path) + f'_{current_date}'
            backup_path = os.path.join(backup_folder, folder_name)
            shutil.copytree(folder_path, backup_path)


if __name__ == '__main__':
    create_backup()