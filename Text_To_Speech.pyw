# author: Fabian Roscher
# date: 26.11.2020
# description: Text to speech in GUI
from gtts import gTTS
from playsound import playsound
import os
import winsound
try:
    from pathlib import Path
    import tkinter as tk
except ImportError:
    from pathlib2 import Path
    import Tkinter as tk


def main():
    def txt_to_speech(event=None):
        try:
            try:
                check.set("")
                lab.config(bg="white")
                speech = gTTS(text=ent.get(), lang=lang.get())
                speech.save("Text.mp3")
                __dirpath__ = Path(globals().get("__file__", "./_")).absolute().parent
                path = str(__dirpath__) + "\\Text.mp3"
                try:
                    playsound(path)
                except Exception:
                    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
                    check.set("Wasn't able to load the characters!")
                    lab.config(bg="red")
                os.remove(path)
            except ValueError:
                winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
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
        language.set("Language: Arabic")

    def bn():
        lang.set("bn")
        language.set("Language: Bengali")

    def zh_cn():
        lang.set("zh-CN")
        language.set("Language: Chinese")

    def cs():
        lang.set("cs")
        language.set("Language: Czech")

    def da():
        lang.set("da")
        language.set("Language: Danish")

    def nl():
        lang.set("nl")
        language.set("Language: Dutch")

    def en():
        lang.set("en")
        language.set("Language: English")

    def fil():
        lang.set("fil")
        language.set("Language: Filipino")

    def fi():
        lang.set("fi")
        language.set("Language: Finnish")

    def fr():
        lang.set("fr")
        language.set("Language: French")

    def de():
        lang.set("de")
        language.set("Language: German")

    def el():
        lang.set("el")
        language.set("Language: Greek")

    def hi():
        lang.set("hi")
        language.set("Language: Hindi")

    def hu():
        lang.set("hu")
        language.set("Language: Hungarian")

    def ind():
        lang.set("id")
        language.set("Language: Indonesian")

    def it():
        lang.set("it")
        language.set("Language: Italian")

    def ja():
        lang.set("ja")
        language.set("Language: Japanese")

    def ko():
        lang.set("ko")
        language.set("Language: Korean")

    def no():
        lang.set("no")
        language.set("Language: Norwegian")

    def pl():
        lang.set("pl")
        language.set("Language: Polish")

    def pt():
        lang.set("pt")
        language.set("Language: Portuguese")

    def ru():
        lang.set("ru")
        language.set("Language: Russian")

    def sk():
        lang.set("sk")
        language.set("Language: Slovak")

    def es():
        lang.set("es")
        language.set("Language: Spanish")

    def sv():
        lang.set("sv")
        language.set("Language: Swedish")

    def th():
        lang.set("th")
        language.set("Language: Thai")

    def tr():
        lang.set("tr")
        language.set("Language: Turkish")

    def uk():
        lang.set("uk")
        language.set("Language: Ukrainisch")

    def vi():
        lang.set("vi")
        language.set("Language: Vietnamese")

    root = tk.Tk()
    root.title("Text To Speech")
    root.geometry("300x160")
    lang = tk.StringVar()
    lang.set("en")

    menu = tk.Menu(root)
    root.config(menu=menu)
    langmenu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Language", menu=langmenu)
    langmenu.add_command(label="Arabic", command=ar)
    langmenu.add_command(label="Bengali", command=bn)
    langmenu.add_command(label="Chinese", command=zh_cn)
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
    langmenu.add_command(label="Indonesian", command=ind)
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
    ent = tk.Entry(root, textvariable=msg)
    ent.bind('<Return>', txt_to_speech)
    ent.grid(row=2, column=1)
    tk.Button(root, text="Play", font="arial 13", bg="lightgreen", command=txt_to_speech).grid(row=3, column=0)
    tk.Button(root, text="Exit", font="arial 13", bg="red", command=kill).grid(row=3, column=1)
    tk.Button(root, text="Reset", font="arial 13", bg="yellow", command=reset).grid(row=3, column=2)
    language = tk.StringVar()
    language.set("Language: English")
    langlab = tk.Label(root, textvariable=language, font="arial 13")
    langlab.grid(row=4, column=1)
    check = tk.StringVar()
    lab = tk.Label(root, textvariable=check)
    lab.grid(row=5, column=1)
    root.mainloop()


if __name__ == "__main__":
    main()
