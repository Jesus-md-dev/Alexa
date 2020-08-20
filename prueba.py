import os
import webbrowser
import time

path = "C:/Users/black/Dropbox/Amazon Alexa"

browser_path = "C:/Users/black/AppData/Local/Programs/Opera GX/launcher.exe %s"
while(True):
    files = os.listdir(path)

    nfiles = len(files)

    if(nfiles != 0):
        time.sleep(1)

        f = open(path+"/"+files[0],"r")
        strings = f.read().split(" ",1)
        f.close()
        os.remove(path+"/"+files[0])

        if(strings[0] == "bloquear"):
            os.system("rundll32.exe user32.dll, LockWorkStation")

        elif(strings[0] == "apagar"):
            os.system("shutdown /s")

        elif(strings[0] == "reiniciar"):
            os.system("shutdown /r")

        else:
            webbrowser.get(browser_path).open("http://"+strings[0]+".com")
            