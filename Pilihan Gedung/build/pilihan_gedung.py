from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:/App_Danus/Pilihan Gedung/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Pilihan Gedung")

window.geometry("1920x1080")
window.configure(bg = "#D9D8D8")


canvas = Canvas(
    window,
    bg = "#D9D8D8",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    1920.0,
    136.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    259.0,
    54.0,
    anchor="nw",
    text="Danus-ITK",
    fill="#525252",
    font=("KronaOne Regular", 30 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    171.0,
    73.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

#profil
def btn_clicked():
    window.destroy()
    subprocess.call(["python", "#"])

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= btn_clicked,
    relief="flat"
)
button_1.place(
    x=1541.0,
    y=58.0,
    width=130.0,
    height=53.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))

#beranda
def btn_clicked():
    window.destroy()
    subprocess.call(["python", "D:/App_Danus/Pilihan Gedung/build/pilihan_gedung.py"])

button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command= btn_clicked,
    relief="flat"
)
button_2.place(
    x=1375.0,
    y=58.0,
    width=130.0,
    height=53.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))

#Logout
class button_pilihan_gedung():    
    def btn_clicked_logout():
        window.destroy()
        subprocess.call(["python", "D:/App_Danus/Login/Masuk/Masuk.py"])
    def enter():
            canvas.config(cursor="hand2")
    def leave():
            canvas.config(cursor="")
    def on_closing ():
        if messagebox.showinfo("PESANAN DISIMPAN, Lanjutkan opsi berikutnya?"):
            window.destroy()
tagname = 'event'
img1= ImageTk.PhotoImage(Image.open("Button.png"))
button_next1 = canvas.create_image(1550,965, image=img1, tag=tagname)

canvas.tag_bind(tagname, "<Enter>", lambda event: button_next.enter())
canvas.tag_bind(tagname, "<Leave>", lambda event: button_next.leave())
canvas.tag_bind(button_next1, "<Button-1>", button_next.btn_clicked_next)


button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
#Gedung B
def btn_clicked():
    window.destroy()
    subprocess.call(["python", "D:\App_Danus\Menu Gedung B\Makanan_B\makanan_b.py"])

button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command= btn_clicked,
    relief="flat"
)
button_4.place(
    x=181.0,
    y=804.0,
    width=291.0,
    height=111.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))

#Gedung E
def btn_clicked():
    window.destroy()
    subprocess.call(["python", "D:\App_Danus\Menu Gedung E\Makanan_E\makanan_E.py"])

button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command= btn_clicked,
    relief="flat"
)
button_5.place(
    x=630.0,
    y=804.0,
    width=291.0,
    height=111.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))

#Gedung F
def btn_clicked():
    window.destroy()
    subprocess.call(["python", "D:\App_Danus\Menu Gedung F\Makanan_F\makanan_F.py"])

button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command= btn_clicked,
    relief="flat"
)
button_6.place(
    x=1079.0,
    y=804.0,
    width=291.0,
    height=111.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))

#Gedung G
def btn_clicked():
    window.destroy()
    subprocess.call(["python", "D:\App_Danus\Menu Gedung G\Makanan_G\makanan_G.py"])

button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command= btn_clicked,
    relief="flat"
)
button_7.place(
    x=1525.0,
    y=804.0,
    width=291.0,
    height=111.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    946.0,
    484.0,
    image=image_image_2
)

canvas.create_text(
    299.0,
    388.0,
    anchor="nw",
    text="SELAMAT DATANG DI DANA USAHA \nINSTITUT TEKNOLOGI KALIMANTAN",
    fill="#000000",
    font=("NunitoSans BoldItalic", 64 * -1)
)
window.resizable(True, True)
window.mainloop()
