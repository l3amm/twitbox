import os, shutil
from subprocess import call

def install(parts):
    if len(parts) == 1:
        call(["easy_install", parts[0]])
    else:
        os.mkdir("install_path")
        os.chdir("install_path")
        call(["curl","-O",parts[1]])
        zipfile = os.path.basename(parts[1])
        call(["unzip",zipfile])
        os.chdir(zipfile[0:-4])
        call(["python", "setup.py", "install"])
        os.chdir("../..")
        shutil.rmtree("install_path")
        

if __name__=='__main__':
    f = open("Gemfile","r")
    for line in f:
        install( line.split() )