import os
import requests
from zipfile import *
from io import BytesIO
import os.path
import subprocess
from tkinter import *
from tkinter import messagebox


def createBaseFolder():
    directory = "TropixeelLauncher"
    parent_dir = "C:/"
    path2 = os.path.join(parent_dir, directory)
    os.mkdir(path2)


def downloadAndExtract():
    # Defining the zip file URL
    url = 'http://85.169.118.199/resources.zip'

    # Split URL to get the file name
    filename = url.split('/')[-1]

    # Downloading the file by sending the request to the URL
    req = requests.get(url)

    # extracting the zip file contents
    zipfile = ZipFile(BytesIO(req.content))
    zipfile.extractall('C:/TropixeelLauncher/Minecraft')


def launch():
    res = T.get("1.0", "end")
    print(res)
    with open('C:/TropixeelLauncher/Minecraft/nick.txt', 'w') as f:
        f.write(T.get("1.0", "end"))
    mbox()
    downloadAndExtract()

    subprocess.call([r'C:\TropixeelLauncher\Minecraft\gs.bat'])


def mbox():
    messagebox.showinfo("Éxécution", "Téléchargement des ressources et lancement du jeu, le launcher va dfreeze le temps du téléchargement puis le jeu va ce lancer.")


path = "C:/TropixeelLauncher"

if os.path.exists(path):
    root = Tk()
    frame1 = Frame(root)
    frame2 = Frame(root)
    root.title("Tropixeel Launcher")
    root.geometry('300x150')
    root.resizable(False, False)
    root.configure(bg='lightgray')

    T = Text(root, height=1, width=52)

    # Create label
    l = Label(root, text="Pseudo :")

    l.config(font=("Calibri", 14))
    # exit button
    exit_button = Button(
        root,
        text='lancer',
        command=lambda: launch()
    )

    l.pack()
    T.pack()
    exit_button.pack(
        ipadx=3,
        ipady=6,
        expand=True
    )

    root.mainloop()


else:
    createBaseFolder()
    downloadAndExtract()
