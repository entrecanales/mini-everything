import os
import os.path

print("Hello! What kind of file are you looking for?")
print("Give me the FULL name of the file (with extension)")
print("Or . + the extension to find all files with that extension! (For instance, .py will look for all files with the py extension)")
print("Whatever the case I'll look into this directory and every child directory! So... what are you looking for? 👀")
file = input()

files = []

for dirpath, dirnames, filenames in os.walk("."):
    if (file.startswith('.')):
        for name in [f for f in filenames if f.endswith(file)]:
            files.append(f"{dirpath}/{name}")
    else:
        for name in [f for f in filenames if f == file]:
            files.append(f"{dirpath}/{name}")

if (len(files) == 0):
    print("We found nothing!")

else:
    for file in files:
        print(file)
