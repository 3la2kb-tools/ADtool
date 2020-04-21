import re
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def py_fixed_seed(filename):

    content = open(filename, "r").read()
    scan = 0
    if "import random" in content :
        moduleName = "random"
        if "import random as" in content :
            moduleSearch = re.search('import\s+random\s+as\s+(\w+)', content, re.IGNORECASE)
            if moduleSearch :
                moduleName = moduleSearch.group(1)

        if moduleName+".seed(" in content :
            print(bcolors.OKGREEN+"[+] Found usage of a fixed seed in :"+bcolors.ENDC+bcolors.OKBLUE+filename+bcolors.ENDC+"\n"+os.popen("grep -n '"+moduleName+".seed(' "+filename).read())

