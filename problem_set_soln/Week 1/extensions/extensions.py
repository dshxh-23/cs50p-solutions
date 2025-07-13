ls = ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]

name = input("File name: ").lower().strip()
if "." in name:
    ext = name.split(".")[-1]
    if ext == "gif" or ext == "png":
        print(f"image/{ext}")
    elif ext == "jpeg" or ext == "jpg":
        print("image/jpeg")
    elif ext == "pdf" or ext == "zip":
        print(f"application/{ext}")
    elif ext == "txt":
        print("text/plain")
    else:
        print('application/octet-stream')
else:
    print('application/octet-stream')

