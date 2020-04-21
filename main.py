import json
import sys
import glob

from vulns.fixedSeed import *

# Load json data
jsonFile = open("extensions.json", "r").read()
parsedJson = json.loads(jsonFile)

# Getting target directory
target = '.'
files = glob.glob(target+'/**', recursive=True)

for file in files :
    filename = file.split('/')[-1]

    if '.' in filename :
        ext = file.split(".")[-1]

        try:
            functions = parsedJson[ext]

            for function in functions :
                getattr(main, function)(file)

        except KeyError :
            continue

