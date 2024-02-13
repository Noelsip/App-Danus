
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
from time import strftime

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:/App_Danus/Login/Masuk/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("HALAMAN MASUK")

window.geometry("1920x1080")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    1070.0,
    578.0,
    anchor="nw",
    text="Nama",
    fill="#000000",
    font=("Oswald Regular", 40 * -1)
)

canvas.create_text(
    1070.0,
    757.0,
    anchor="nw",
    text="NIM",
    fill="#000000",
    font=("Oswald Regular", 40 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png")
)

def btn_clicked():
    nama= str(entry_1.get())
    nim= int(entry_2.get())
    time_string= strftime('%H:%M:%S')

    with open("D:/App_Danus/DATA BASE/DataPengguna.txt", 'w') as file:
        file.write(f"\n Nama: {nama}            Nim: {nim}             Waktu: {time_string}\n")
        
    window.destroy()
    subprocess.call(["python", "D:/App_Danus/Pilihan Gedung/build/pilihan_gedung.py"])

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= btn_clicked,
    relief="flat"
)
button_1.place(
    x=1527.0,
    y=944.0,
    width=310.0,
    height=76.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1460.5,
    681.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#900000",
    fg="#ffffff",
    font=(15),
    highlightthickness=0
)
entry_1.place(
    x=1135.0,
    y=651.0,
    width=651.0,
    height=58.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1460.5,
    854.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#900000",
    fg="#ffffff",
    font= (15),
    highlightthickness=0
)
entry_2.place(
    x=1137.0,
    y=822.0,
    width=647.0,
    height=62.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    1444.0,
    237.0,
    image=image_image_1
)

canvas.create_text(
    1190.0,
    435.0,
    anchor="nw",
    text="Silahkan Masukan Nama dan Nim Anda\nUntuk Melanjutkan Pemesanan",
    fill="#000000",
    font=("Rancho Regular", 40 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    481.0,
    403.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    480.0,
    577.0,
    image=image_image_3
)

canvas.create_rectangle(
    80.0,
    93.0,
    876.0,
    757.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    152.0,
    267.0,
    anchor="nw",
    text="SELAMAT DATANG \nDI DANA USAHA \nINSTITUT TEKNOLOGI\nKALIMANTAN",
    fill="#000000",
    font=("BoldItalic", 60 * -1)
)
window.resizable(False, False)
window.mainloop()
