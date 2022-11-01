from sys import platform
linkFile = "/home/truyen/FsosAPI/file.mp3"
port = "COM3"
if platform == "linux" or platform == "linux2":
    linkFile = "/home/truyen/FsosAPI/file.mp3"
    port = "tty/USB0"
    print(linkFile)
    print(port)
    print(platform)
else:
    print(linkFile)
    print(port)
    print(platform)