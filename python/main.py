import os
import requests
from zipfile import *
from io import BytesIO
import os.path
import subprocess
from tkinter import *
from tkinter import messagebox
from shutil import *


def createBaseFolder():
    directory9 = "TropixeelLauncher"
    parent_dir9 = "C:/"
    path268 = os.path.join(parent_dir9, directory9)
    os.mkdir(path268)


def downloadAndExtractVani():
    # Defining the zip file URL
    url = 'http://filetropixeel.duckdns.org/resources18.zip'

    print("Récupération de l'URL")
    filename = url.split('/')[-1]

    print("Envoi d'une requète HTTP et téléchargement")
    req = requests.get(url)


    print("Extraction")
    zipfile = ZipFile(BytesIO(req.content))
    zipfile.extractall('C:/TropixeelLauncher/Minecraft1-18')


def downloadAndExtractMod():
    # Defining the zip file URL
    url = 'http://filetropixeel.duckdns.org/resources.zip'

    print("Récupération de l'URL")
    filename = url.split('/')[-1]

    print("Envoi d'une requète HTTP et téléchargement")
    req = requests.get(url)
    rmtree("C:/TropixeelLauncher/Minecraft/")

    print("Extraction")
    zipfile = ZipFile(BytesIO(req.content))
    zipfile.extractall('C:/TropixeelLauncher/Minecraft')


def downloadAndExtractOnlyMod():
    # Defining the zip file URL
    url = 'http://filetropixeel.duckdns.org/resourcesMod.zip'

    print("Récupération de l'URL")
    filename = url.split('/')[-1]

    print("Envoi d'une requète HTTP et téléchargement")
    req = requests.get(url)

    rmtree("C:/TropixeelLauncher/Minecraft/mods")

    print("Extraction")
    zipfile = ZipFile(BytesIO(req.content))

    zipfile.extractall('C:/TropixeelLauncher/Minecraft')


def launchMod():
    path96 = "C:/TropixeelLauncher/Minecraft/assets"
    path987 = "C:/TropixeelLauncher/Minecraft/libraries"
    path885 = "C:/TropixeelLauncher/Minecraft/versions"
    path835 = "C:/TropixeelLauncher/Minecraft/runtime"
    res = T.get("1.0", "end")
    print("ok mv tu es " + res)
    with open('C:/TropixeelLauncher/Minecraft/nick.txt', 'w') as f:
        f.write(T.get("1.0", "end"))

    if os.path.exists(path96) & os.path.exists(path987) & os.path.exists(path885) & os.path.exists(path835):
        messagebox.showinfo("Éxécution",
                            "Vérification des mods et lancement du jeu")
        downloadAndExtractOnlyMod()
        subprocess.call([r'C:\TropixeelLauncher\Minecraft\gs.bat'])
        exit(0)
    else:
        mbox()
        downloadAndExtractMod()
        subprocess.call([r'C:\TropixeelLauncher\Minecraft\gs.bat'])
        exit(0)


def launchVani():
    path96 = "C:/TropixeelLauncher/Minecraft1-18/assets"
    path987 = "C:/TropixeelLauncher/Minecraft1-18/libraries"
    path885 = "C:/TropixeelLauncher/Minecraft1-18/versions"
    path835 = "C:/TropixeelLauncher/Minecraft1-18/runtime"

    res = T.get("1.0", "end")
    print("ok mv tu es " + res)
    with open('C:/TropixeelLauncher/Minecraft1-18/nick.txt', 'w') as f:
        f.write(T.get("1.0", "end"))

    if os.path.exists(path96) & os.path.exists(path987) & os.path.exists(path885) & os.path.exists(path835):
        subprocess.call([r'C:\TropixeelLauncher\Minecraft1-18\gs18.bat'])
        messagebox.showinfo("Éxécution",
                            "Fichiers déjà téléchargés, lancement du jeu.")
        exit(0)
    else:
        mbox()
        downloadAndExtractVani()

        subprocess.call([r'C:\TropixeelLauncher\Minecraft1-18\gs18.bat'])
        exit(0)


def mbox():
    messagebox.showinfo("Éxécution",
                        "Téléchargement des ressources et lancement du jeu, le launcher va freeze le temps du "
                        "téléchargement puis le jeu va se lancer.")


path = "C:/TropixeelLauncher"
path9 = "C:/TropixeelLauncher/Minecraft"
path5 = "C:/TropixeelLauncher/Minecraft1-18"

if os.path.exists(path9) & os.path.exists(path5):
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

    # Create label

    # exit button.

    exit_button = Button(
        root,
        width=10,
        text='>Moddé 1.12!',

        command=lambda: launchMod()
    )
    exit_button2 = Button(
        root,
        width=10,
        text='>Vanilla 1.18!',

        command=lambda: launchVani()
    )

    T.place(rely=0.932, relx=0.59, anchor='center', height=65)
    T.configure(font=("Calibri", 12, "bold"))

    exit_button.place(
        relx=0.9,
        rely=0.89,
        height=60,

    )
    exit_button2.place(
        relx=0.81,
        rely=0.89,
        height=60,

    )

    root.mainloop()

elif os.path.exists(path):
    directory1 = "Minecraft"
    parent_dir1 = "C:/TropixeelLauncher"
    path3 = os.path.join(parent_dir1, directory1)
    os.mkdir(path3)
    directory6 = "Minecraft1-18"
    parent_dir6 = "C:/TropixeelLauncher"
    path4 = os.path.join(parent_dir6, directory6)
    os.mkdir(path4)
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

    # Create label

    # exit button.

    exit_button = Button(
        root,
        width=10,
        text='>Moddé 1.12!',

        command=lambda: launchMod()
    )
    exit_button2 = Button(
        root,
        width=10,
        text='>Vanilla 1.18!',

        command=lambda: launchVani()
    )

    T.place(rely=0.932, relx=0.59, anchor='center', height=65)
    T.configure(font=("Calibri", 12, "bold"))

    exit_button.place(
        relx=0.9,
        rely=0.89,
        height=60,

    )
    exit_button2.place(
        relx=0.81,
        rely=0.89,
        height=60,

    )

    root.mainloop()
else:
    directory = "TropixeelLauncher"
    parent_dir = "C:/"
    path2 = os.path.join(parent_dir, directory)
    os.mkdir(path2)
    directory1 = "Minecraft"
    parent_dir1 = "C:/TropixeelLauncher"
    path3 = os.path.join(parent_dir1, directory1)
    os.mkdir(path3)
    directory6 = "Minecraft1-18"
    parent_dir6 = "C:/TropixeelLauncher"
    path4 = os.path.join(parent_dir6, directory6)
    os.mkdir(path4)
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

    # Create label

    # exit button.

    exit_button = Button(
        root,
        width=10,
        text='>Moddé 1.12!',

        command=lambda: launchMod()
    )
    exit_button2 = Button(
        root,
        width=10,
        text='>Vanilla 1.18!',

        command=lambda: launchVani()
    )

    T.place(rely=0.932, relx=0.59, anchor='center', height=65)
    T.configure(font=("Calibri", 12, "bold"))

    exit_button.place(
        relx=0.9,
        rely=0.89,
        height=60,

    )
    exit_button2.place(
        relx=0.81,
        rely=0.89,
        height=60,

    )

    root.mainloop()
