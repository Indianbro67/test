import os
import shutil

def create_folders():
    num_folders = int(input("How many folders do you want to create? "))
    
    for i in range(1, num_folders + 1):
        folder_name = str(i)
        os.makedirs(folder_name)

        shutil.copy("send.py", folder_name)
        shutil.copy("messages.txt", folder_name)
        
        print(f"Folder '{folder_name}' devil done'.")

if __name__ == "__main__":
    create_folders()

