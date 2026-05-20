import os
import shutil

rules = {
   '.txt':'Documents',
   '.jpg':'Images',
   '.jpeg':'Images',
   '.png':'Images',
   '.gif':'Images',
   '.rar':'Archives',
   '.zip':'Archives',
   '.7z':'Archives',
   '.mp3':'Music',
   '.wav':'Music',
   '.flac':'Music',
   '.mp4':'Videos',
   '.avi':'Videos',
   '.mkv':'Videos',
   '.py':'Python'
}

files = os.listdir()

for file in files:
    
    if os.path.isdir(file):
        continue

    for entensuin, folder in rules.items():
        if file.endswith(entensuin):
           os.makedirs(folder, exist_ok=True)
           shutil.move(file, folder)
           print(file,"已移动到", folder)
           break
    