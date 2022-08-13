import time
import os
import shutil

from filePicker import pickFile
from progressBar import progressBar


def deleteFromReact(path: str):
    l1 = [i.name for i in os.scandir(path)]
    if "node_modules" in l1:
        shutil.rmtree(path + "/node_modules")


def checkIfReactProject(path: str):
    l1 = [i.name for i in os.scandir(path)]
    if "node_modules" not in l1:
        return 0
    if "package.json" not in l1:
        return 0
    if "yarn.lock" not in l1:
        return 0
    return 1


os.system('clear')

print("Please select the folder or directory")
pickedFileDir = pickFile()
time.sleep(0.5)
print("Please wait while the data is being fetched...")
l2 = [i[0] for i in os.walk(pickedFileDir + "/")]
print("Data fetched successfully!")
time.sleep(1)
print("Now filtering the data...")
l2 = list(filter(checkIfReactProject, l2))
print("Hold tight while we clear the useless data ;)")
for item in progressBar(l2, prefix='Progress:', suffix='Complete', length=50):
    deleteFromReact(item)
    time.sleep(0.1)
print("Successfully cleaned all the react js's junk!")
