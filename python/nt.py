import os
import requests
from zipfile import *
from io import BytesIO
import os.path
import subprocess
from tkinter import *
from tkinter import messagebox

def createBaseFolder():
    directory9 = "TropixeelLauncher"
    parent_dir9 = "C:/"
    path268 = os.path.join(parent_dir9, directory9)
    os.mkdir(path268)


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
    exit(0)


def mbox():
    messagebox.showinfo("Éxécution",
                        "Téléchargement des ressources et lancement du jeu, le launcher va freeze le temps du "
                        "téléchargement puis le jeu va ce lancer.")


path = "C:/TropixeelLauncher"
path9 = "C:/TropixeelLauncher/Minecraft"

if os.path.exists(path9):
    print("coucou mv")
    root = Tk()
    frame1 = Frame(root)
    frame2 = Frame(root)
    root.title("Tropixeel Launcher")
    root.geometry('900x600')

    bg = PhotoImage(file="bg.png")

    label1 = Label(root, image=bg)
    label1.place(x=0, y=0)

    root.resizable(False, False)

    T = Text(root, height=2, width=40)


    # Create label

    # exit button.

    exit_button = Button(
        root,
        width=20,
        text='Lancer!',

        command=lambda: launch()
    )

    T.place(rely=0.932, relx=0.59, anchor='center', height=65)
    T.configure(font=("Calibri", 12, "bold"))


    exit_button.place(
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
    print("coucou mv")
    root = Tk()
    frame1 = Frame(root)
    frame2 = Frame(root)
    root.title("Tropixeel Launcher")
    root.geometry('900x600')

    bg = PhotoImage(file="bg.png")

    label1 = Label(root, image=bg)
    label1.place(x=0, y=0)

    root.resizable(False, False)

    T = Text(root, height=2, width=40)

    # Create label

    # exit button.

    exit_button = Button(
        root,
        width=20,
        text='Lancer!',

        command=lambda: launch()
    )

    T.place(rely=0.932, relx=0.59, anchor='center', height=65)
    T.configure(font=("Calibri", 12, "bold"))

    exit_button.place(
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
    print("coucou mv")
    root = Tk()
    frame1 = Frame(root)
    frame2 = Frame(root)
    root.title("Tropixeel Launcher")
    root.geometry('900x600')

    bg = PhotoImage(file="bg.png")

    label1 = Label(root, image=bg)
    label1.place(x=0, y=0)

    root.resizable(False, False)

    T = Text(root, height=2, width=40)

    # Create label

    # exit button.

    exit_button = Button(
        root,
        width=20,
        text='Lancer!',

        command=lambda: launch()
    )

    T.place(rely=0.932, relx=0.59, anchor='center', height=65)
    T.configure(font=("Calibri", 12, "bold"))

    exit_button.place(
        relx=0.81,
        rely=0.89,
        height=60,

    )

    root.mainloop()

