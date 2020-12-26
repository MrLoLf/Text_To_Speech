import gtts
from gtts import gTTS
from playsound import playsound
import tkinter as tk
import os
from pathlib import Path


def main():
    def txt_to_speech():
        try:
            try:
                message = msg.get()
                check.set("")
                lab.config(bg="white")
                speech = gTTS(text=message, lang=lang.get())
                speech.save("Text.mp3")
                __dirpath__ = Path(globals().get("__file__", "./_")).absolute().parent
                path = str(__dirpath__) + "\\Text.mp3"
                playsound(path)
                os.remove(path)
            except ValueError:
                check.set("The langauge is not supported!")
                lab.config(bg="red")
        except AssertionError:
            pass

    def kill():
        root.destroy()

    def reset():
        check.set("")
        lab.config(bg="white")
        msg.set("")

    def ar():
        lang.set("ar")

    def bn():
        lang.set("bn")

    def zh_CN():
        lang.set("zh-CN")

    def cs():
        lang.set("cs")

    def da():
        lang.set("da")

    def nl():
        lang.set("nl")

    def en():
        lang.set("en")

    def fil():
        lang.set("fil")

    def fi():
        lang.set("fi")

    def fr():
        lang.set("fr")

    def de():
        lang.set("de")

    def el():
        lang.set("el")

    def hi():
        lang.set("hi")

    def hu():
        lang.set("hu")

    def id():
        lang.set("id")

    def it():
        lang.set("it")

    def ja():
        lang.set("ja")

    def ko():
        lang.set("ko")

    def no():
        lang.set("no")

    def pl():
        lang.set("pl")

    def pt():
        lang.set("pt")

    def ru():
        lang.set("ru")

    def sk():
        lang.set("sk")

    def es():
        lang.set("es")

    def sv():
        lang.set("sv")

    def th():
        lang.set("th")

    def tr():
        lang.set("tr")

    def uk():
        lang.set("uk")

    def vi():
        lang.set("vi")

    root = tk.Tk()
    root.title("Text To Speech")
    root.geometry("285x150")
    lang = tk.StringVar()
    lang.set("en")

    menu = tk.Menu(root)
    root.config(menu=menu)
    langmenu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Language", menu=langmenu)
    langmenu.add_command(label="Arabic", command=ar)
    langmenu.add_command(label="Bengali", command=bn)
    langmenu.add_command(label="Chinese", command=zh_CN)
    langmenu.add_command(label="Czech", command=cs)
    langmenu.add_command(label="Danish", command=da)
    langmenu.add_command(label="Dutch", command=nl)
    langmenu.add_command(label="English", command=en)
    langmenu.add_command(label="Filipino", command=fil)
    langmenu.add_command(label="Finnish", command=fi)
    langmenu.add_command(label="French", command=fr)
    langmenu.add_command(label="German", command=de)
    langmenu.add_command(label="Greek", command=el)
    langmenu.add_command(label="Hindi", command=hi)
    langmenu.add_command(label="Hungarian", command=hu)
    langmenu.add_command(label="Indonesian", command=id)
    langmenu.add_command(label="Italian", command=it)
    langmenu.add_command(label="Japanese", command=ja)
    langmenu.add_command(label="Korean", command=ko)
    langmenu.add_command(label="Norwegian", command=no)
    langmenu.add_command(label="Polish", command=pl)
    langmenu.add_command(label="Portuguese", command=pt)
    langmenu.add_command(label="Russian", command=ru)
    langmenu.add_command(label="Slovak", command=sk)
    langmenu.add_command(label="Spanish", command=es)
    langmenu.add_command(label="Swedish", command=sv)
    langmenu.add_command(label="Thai", command=th)
    langmenu.add_command(label="Turkish", command=tr)
    langmenu.add_command(label="Ukrainisch ", command=uk)
    langmenu.add_command(label="Vietnamese ", command=vi)

    root.configure(bg="white")
    tk.Label(root, text="Text To Speech", font="arial 15 bold").grid(row=0, column=1)
    tk.Label(root, text="Enter your Text:", font="arial 12").grid(row=1, column=1)
    msg = tk.StringVar()
    tk.Entry(root, textvariable=msg).grid(row=2, column=1)
    tk.Button(root, text="Play", font="arial 13", bg="lightgreen", command=txt_to_speech).grid(row=3, column=0)
    tk.Button(root, text="Exit", font="arial 13", bg="red", command=kill).grid(row=3, column=1)
    tk.Button(root, text="Reset", font="arial 13", bg="yellow", command=reset).grid(row=3, column=2)
    check = tk.StringVar()
    lab = tk.Label(root, textvariable=check)
    lab.grid(row=4, column=1)
    root.mainloop()


if __name__ == "__main__":
    main()
