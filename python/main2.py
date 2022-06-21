import os
import requests
from zipfile import *
from io import BytesIO
import os.path
import subprocess
from tkinter import *
from tkinter import messagebox
from shutil import *

if os.name == "nt":
    name = os.getlogin()
    pathODD = "C:/Users/" + name + "/OneDrive/Documents/TropixeelLauncher/MinecraftFolder"
    pathNM = "C:/Users/" + name + "/Documents/TropixeelLauncher/MinecraftFolder"

    pathODDD = "/Users/" + name + "/OneDrive/Documents/TropixeelLauncher/MinecraftFolder"
    pathNMM = "/Users/" + name + "/Documents/TropixeelLauncher/MinecraftFolder"


    pathOD = "C:/Users/" + name + "/OneDrive"
    pathTL1 = "C:/Users/" + name + "/OneDrive/Documents/TropixeelLauncher"
    pathTL2 = "C:/Users/" + name + "/Documents/TropixeelLauncher"
    if os.path.exists(pathTL1) | os.path.exists(pathTL2):
        if os.path.exists(pathTL1):
            if os.path.exists(pathTL1 + "/MinecraftFolder"):
                print("rien")
            else:
                createdF3 = "MinecraftFolder"
                parentF3 = "C:/Users/" + name + "/OneDrive/Documents/TropixeelLauncher"
                path3 = os.path.join(parentF3, createdF3)
                os.mkdir(path3)
                print("existe deja mais creation de mc")

        if os.path.exists(pathTL2):
            if os.path.exists(pathTL2 + "/MinecraftFolder"):
                print("rien")
            else:
                createdF4 = "MinecraftFolder"
                parentF4 = "C:/Users/" + name + "/OneDrive/Documents/TropixeelLauncher"
                path4 = os.path.join(parentF4, createdF4)
                os.mkdir(path4)
                print("existe deja mais creation de mc")


    else:
        if os.path.exists(pathOD):
            createdF1 = "TropixeelLauncher"
            parentF1 = "C:/Users/" + name + "/OneDrive/Documents"
            path1 = os.path.join(parentF1, createdF1)
            os.mkdir(path1)

            createdF3 = "MinecraftFolder"
            parentF3 = "C:/Users/" + name + "/OneDrive/Documents/TropixeelLauncher"
            path3 = os.path.join(parentF3, createdF3)
            os.mkdir(path3)
            print("full create")
        else:
            createdF2 = "TropixeelLauncher"
            parentF2 = "C:/Users/" + name + "/Documents"
            path2 = os.path.join(parentF2, createdF2)
            os.mkdir(path2)

            createdF4 = "MinecraftFolder"
            parentF4 = "C:/Users/" + name + "/Documents/TropixeelLauncher"
            path4 = os.path.join(parentF4, createdF4)
            os.mkdir(path4)
            print("full create")


def downloadAndExtractVani():
    # Defining the zip file URL
    url = 'http://pc.liltray.online/resources18.zip'

    print("Récupération de l'URL")
    filename = url.split('/')[-1]

    print("Envoi d'une requète HTTP et téléchargement")
    req = requests.get(url)

    print("Extraction")
    zipfile = ZipFile(BytesIO(req.content))
    if os.path.exists(pathODD):
        zipfile.extractall(pathODD)

    if os.path.exists(pathNM):
        zipfile.extractall(pathNM)


def downloadAndExtractMod():
    # Defining the zip file URL
    url = 'http://pc.liltray.online/resources.zip'

    print("Récupération de l'URL")
    filename = url.split('/')[-1]

    print("Envoi d'une requète HTTP et téléchargement")
    req = requests.get(url)

    print("Extraction")
    zipfile = ZipFile(BytesIO(req.content))
    if os.path.exists(pathODD):
        zipfile.extractall(pathODD)

    if os.path.exists(pathNM):
        zipfile.extractall(pathNM)


def downloadAndExtractOnlyMod():
    # Defining the zip file URL
    url = 'http:/pc.liltray.online/resourcesMod.zip'

    print("Récupération de l'URL")
    filename = url.split('/')[-1]

    print("Envoi d'une requète HTTP et téléchargement")
    req = requests.get(url)

    if os.path.exists(pathODD):
        rmtree(pathODD + "/mods")

    if os.path.exists(pathNM):
        rmtree(pathNM + "/mods")

    print("Extraction")
    zipfile = ZipFile(BytesIO(req.content))

    if os.path.exists(pathODD):
        zipfile.extractall(pathODD)

    if os.path.exists(pathNM):
        zipfile.extractall(pathNM)


def mbox():
    messagebox.showinfo("Éxécution",
                        "Téléchargement des ressources et lancement du jeu, le launcher va freeze le temps du "
                        "téléchargement puis le jeu va se lancer.")


def launchMod():

    res = T.get("1.0", "end")
    print("ok mv tu es " + res)
    if os.path.exists(pathNM):
        with open(pathNM + "/nick.txt", 'w') as f:
            f.write(T.get("1.0", "end"))
    if os.path.exists(pathODD):
        with open(pathODD + "/nick.txt", 'w') as f:
            f.write(T.get("1.0", "end"))

    if os.path.exists(pathODD):
        mbox()
        downloadAndExtractMod()
        subprocess.call([r'C:' + pathODDD + "\modded.bat"])

    if os.path.exists(pathNM):
        mbox()
        downloadAndExtractMod()
        subprocess.call([r'C:' + pathNMM + "\modded.bat"])

def launchVani():

    res = T.get("1.0", "end")
    print("ok mv tu es " + res)

    if os.path.exists(pathNM):
        with open(pathNM + "/nick.txt", 'w') as f:
            f.write(T.get("1.0", "end"))
    if os.path.exists(pathODD):
        with open(pathODD + "/nick.txt", 'w') as f:
            f.write(T.get("1.0", "end"))

    if os.path.exists(pathODD):
        mbox()
        downloadAndExtractVani()
        subprocess.call([r'C:' + pathODDD + "\vani.bat"])

    if os.path.exists(pathNM):
        mbox()
        downloadAndExtractVani()
        subprocess.call([r'C:' + pathNMM + "\vani.bat"])


print("coucou mv")
root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)
root.title("Tropixeel Launcher")
root.geometry('900x600')
p1 = PhotoImage(file='title222.png')
root.iconphoto(False, p1)

bg = PhotoImage(file="bg.png")

label1 = Label(root, image=bg)
label1.place(x=0, y=0)

root.resizable(False, False)

T = Text(root, height=2, width=40)

exit_button = Button(root, width=10, text='>Moddé 1.12!', command=lambda: launchMod())
exit_button2 = Button(root, width=10, text='>Vanilla 1.18!', command=lambda: launchVani())

T.place(rely=0.932, relx=0.59, anchor='center', height=65)
T.configure(font=("Calibri", 12, "bold"))

exit_button.place(relx=0.9, rely=0.89, height=60, )
exit_button2.place(relx=0.81, rely=0.89, height=60, )

root.mainloop()
