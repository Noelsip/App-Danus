from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:/App_Danus/STRUK/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    960.0,
    543.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    981.0,
    539.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1380.0,
    867.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    980.0,
    318.0,
    image=image_image_4
)
with open("D:/App_Danus/DATA BASE/pesanan_makanan.txt","r") as f:
    harga = f.read() #done

# with open("D:/App_Danus/DATA BASE/Header.txt","r") as f:
#     header = f.read()

with open("D:/App_Danus/DATA BASE/Total_harga.txt","r") as f:
    total = f.read() #blm

with open("D:/App_Danus/DATA BASE/struk.txt","r") as f:
    struk = f.read()


canvas.create_text(
    1350.0,
    360.0,
    anchor= "nw", 
    text = harga,
    fill= "#000000",
    font=("Consolas", 20 * -1)
)
canvas.create_text(
    464.0,
    360.0,
    anchor= "nw", 
    text = struk,
    fill= "#000000",
    font=("Consolas", 20 * -1)
)

canvas.create_text(
    750.0,
    167.0,
    anchor="nw",
    text="DANA USAHA ITK",
    fill="#FFFFFF",
    font=("OpenSansRoman Bold", 70 * -1)
)

canvas.create_text(
    950.0,
    240.0,
    anchor="nw",
    text="STRUK",
    fill="#FFFFFF",
    font=("OpenSansRoman Bold", 48 * -1)
)

canvas.create_text(
    464.0,
    330.0,
    anchor="nw",
    text= "NAMA ITEM",
    fill= "#ffffff",
    font= ("Inter SemiBold", 22 * -1)
)

canvas.create_text(
    850.0,
    330.0,
    anchor="nw",
    text= "JUMLAH ITEM",
    fill= "#ffffff",
    font= ("Inter SemiBold", 22 * -1)
)

canvas.create_text(
    1350.0,
    330.0,
    anchor="nw",
    text= "HARGA",
    fill= "#ffffff",
    font= ("Inter SemiBold", 22 * -1)
)
canvas.create_text(
    1150.0,
    850.0,
    anchor= "nw", 
    text = total,
    fill= "#000000",
    font=("OpenSansRoman Bold", 30 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

def btn_clicked_home():
    window.destroy()
    subprocess.call(["python","D:/App_Danus/Pilihan Gedung/build/pilihan_gedung.py"])

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked_home,
    relief="flat"
)
button_1.place(
    x=0.0,
    y=0.0,
    width=100.0,
    height=100.0
)
window.resizable(False, False)
window.mainloop()
