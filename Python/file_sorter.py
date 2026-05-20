import os

files = os.listdir()

for file in files:
    print(file)

    if file.endswith('.txt'):
        print("这是文本文件")

    if file.endswith('.jpg'):
        print("这是图片文件")

    if file.endswith('.rar'):
        print("这是压缩文件")

    if file.endswith('.pdf'):
        print("这是PDF文件")