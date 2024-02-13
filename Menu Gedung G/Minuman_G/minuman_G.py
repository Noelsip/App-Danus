from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:/App_Danus/Menu Gedung G/Minuman_G/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("MENU MINUMAN GEDUNG G")
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

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

def btn_clicked():
    nama_makanan_1 = entry_1
    nama_makanan_2 = entry_2
    nama_makanan_3 = entry_3
    nama_makanan_4 = entry_4
    nama_makanan_5 = entry_5
    nama_makanan_6 = entry_6
    nama_makanan_7 = entry_7
    nama_makanan_8 = entry_8

    with open("Data Pengguna/Data MASUK", "a") as f:
        f.write(f"\n Jumlah makanan: {nama_makanan_1}, {nama_makanan_2}, {nama_makanan_3}, {nama_makanan_4}, {nama_makanan_5}, {nama_makanan_6}, {nama_makanan_7}, {nama_makanan_8}")
    
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
    x=1550.0,
    y=965.0,
    width=373.44677734375,
    height=100.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))

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
    x=23.0,
    y=12.0,
    width=100.0,
    height=100.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    320.0,
    78.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1284.0,
    768.0,
    image=image_image_4
)

canvas.create_text(
    1217.0,
    725.0,
    anchor="nw",
    text="TehPucuk",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    1100.0,
    768.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    1351.0,
    802.0,
    image=image_image_6
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1353.0,
    801.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#DC9B99",
    fg="#000716",
    highlightthickness=0,

)
entry_1.place(
    x=1312.0,
    y=790.0,
    width=82.0,
    height=20.0
)

canvas.create_text(
    1459.0,
    713.0,
    anchor="nw",
    text="4K/Pcs",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    1285.0,
    603.0,
    image=image_image_7
)

canvas.create_text(
    1215.0,
    572.0,
    anchor="nw",
    text="Golda Coffee",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    1100.0,
    603.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    1351.0,
    634.0,
    image=image_image_9
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1353.0,
    640.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#DC9B99",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=1312.0,
    y=629.0,
    width=82.0,
    height=20.0
)

canvas.create_text(
    1459.0,
    553.0,
    anchor="nw",
    text="8K/Pcs",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    1284.0,
    452.0,
    image=image_image_10
)

canvas.create_text(
    1217.0,
    414.0,
    anchor="nw",
    text="TehKotak",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    1099.0,
    453.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    1351.0,
    485.0,
    image=image_image_12
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    1353.0,
    485.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#DC9B99",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=1312.0,
    y=474.0,
    width=82.0,
    height=20.0
)

canvas.create_text(
    1442.0,
    402.0,
    anchor="nw",
    text="2,5K/Pcs",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    1285.0,
    294.0,
    image=image_image_13
)

canvas.create_text(
    1216.0,
    256.0,
    anchor="nw",
    text="Floridina",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    1099.0,
    294.0,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    1351.0,
    326.0,
    image=image_image_15
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    1353.0,
    326.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#DC9B99",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=1312.0,
    y=315.0,
    width=82.0,
    height=20.0
)

canvas.create_text(
    1451.0,
    244.0,
    anchor="nw",
    text="12K/Pcs",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    830.0,
    146.0,
    anchor="nw",
    text="MINUMAN",
    fill="#000000",
    font=("SansSerifCollection", 60 * -1)
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    677.0,
    764.0,
    image=image_image_16
)

canvas.create_text(
    610.0,
    726.0,
    anchor="nw",
    text="LeMinerale",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    492.0,
    766.0,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    742.0,
    795.0,
    image=image_image_18
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    744.0,
    795.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#DC9B99",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=703.0,
    y=784.0,
    width=82.0,
    height=20.0
)

canvas.create_text(
    847.0,
    719.0,
    anchor="nw",
    text="3K/Pcs",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    676.0,
    614.0,
    image=image_image_19
)

canvas.create_text(
    608.0,
    583.0,
    anchor="nw",
    text="MinumanJelly",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_20 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(
    490.0,
    614.0,
    image=image_image_20
)

image_image_21 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(
    742.0,
    649.0,
    image=image_image_21
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    744.0,
    649.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#DC9B99",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=703.0,
    y=638.0,
    width=82.0,
    height=20.0
)

canvas.create_text(
    845.0,
    558.0,
    anchor="nw",
    text="3K/Pcs",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_22 = PhotoImage(
    file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(
    676.0,
    463.0,
    image=image_image_22
)

canvas.create_text(
    608.0,
    421.0,
    anchor="nw",
    text="Better\n",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_23 = PhotoImage(
    file=relative_to_assets("image_23.png"))
image_23 = canvas.create_image(
    491.0,
    464.0,
    image=image_image_23
)

image_image_24 = PhotoImage(
    file=relative_to_assets("image_24.png"))
image_24 = canvas.create_image(
    742.0,
    498.0,
    image=image_image_24
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    744.0,
    498.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#DC9B99",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=703.0,
    y=487.0,
    width=82.0,
    height=20.0
)

canvas.create_text(
    815.0,
    408.0,
    anchor="nw",
    text="5K/Pcs",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_25 = PhotoImage(
    file=relative_to_assets("image_25.png"))
image_25 = canvas.create_image(
    676.0,
    296.0,
    image=image_image_25
)

canvas.create_text(
    608.0,
    259.0,
    anchor="nw",
    text="Sosis",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_26 = PhotoImage(
    file=relative_to_assets("image_26.png"))
image_26 = canvas.create_image(
    489.0,
    296.0,
    image=image_image_26
)

image_image_27 = PhotoImage(
    file=relative_to_assets("image_27.png"))
image_27 = canvas.create_image(
    742.0,
    334.0,
    image=image_image_27
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    744.0,
    334.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#DC9B99",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=703.0,
    y=323.0,
    width=82.0,
    height=20.0
)

canvas.create_text(
    807.0,
    250.0,
    anchor="nw",
    text="4K/Pcs",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
