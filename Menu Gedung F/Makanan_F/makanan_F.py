from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:/App_Danus/Menu Gedung F/Makanan_F/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("MENU MINUMAN GEDUNG F")
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
    614.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    960.0,
    528.0,
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
    subprocess.call(["python", "D:\App_Danus\Menu Gedung F\Minuman_F\minuman_F.py"])

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
    width=379.0,
    height=85.4296875
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
    59.0,
    image=image_image_3
)

canvas.create_rectangle(
    1009.0,
    703.0,
    1515.0,
    825.0,
    fill="#FAFAF5",
    outline="")

canvas.create_text(
    1197.0,
    732.0,
    anchor="nw",
    text="KeripikTempe",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1078.0,
    763.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    1292.0,
    799.0,
    image=image_image_5
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1294.0,
    799.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#DC9B99",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=1253.0,
    y=788.0,
    width=82.0,
    height=20.0
)

canvas.create_rectangle(
    1012.0,
    551.0,
    1518.0,
    673.0,
    fill="#FAFAF5",
    outline="")

canvas.create_text(
    1195.0,
    574.0,
    anchor="nw",
    text="AnekaGorengan",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    1081.0,
    612.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    1292.0,
    642.0,
    image=image_image_7
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1294.0,
    642.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#DC9B99",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=1253.0,
    y=631.0,
    width=82.0,
    height=20.0
)

canvas.create_rectangle(
    1011.0,
    390.0,
    1517.0,
    512.0,
    fill="#FAFAF5",
    outline="")

canvas.create_rectangle(
    1011.0,
    393.0,
    1517.0,
    515.0,
    fill="#FAFAF5",
    outline="")

canvas.create_text(
    1197.0,
    416.0,
    anchor="nw",
    text="Onde-onde",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    1082.0,
    453.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    1292.0,
    488.0,
    image=image_image_9
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    1294.0,
    488.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#DC9B99",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=1253.0,
    y=477.0,
    width=82.0,
    height=20.0
)

canvas.create_rectangle(
    1011.0,
    235.0,
    1519.0,
    357.0,
    fill="#FAFAF5",
    outline="")

canvas.create_text(
    1195.7275390625,
    258.0,
    anchor="nw",
    text="Bakwan",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    1082.0,
    296.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    1292.0,
    328.0,
    image=image_image_11
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    1294.0,
    328.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#DC9B99",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=1253.0,
    y=317.0,
    width=82.0,
    height=20.0
)

canvas.create_rectangle(
    402.0,
    703.0,
    908.0,
    825.0,
    fill="#FAFAF5",
    outline="")

canvas.create_text(
    588.0,
    727.0,
    anchor="nw",
    text="MacaroniPedas",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    1419.0,
    721.0,
    anchor="nw",
    text="10K/Pcs",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    471.0,
    764.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    681.0,
    795.0,
    image=image_image_13
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    683.0,
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
    x=642.0,
    y=784.0,
    width=82.0,
    height=20.0
)

canvas.create_rectangle(
    401.0,
    556.0,
    907.0,
    678.0,
    fill="#FAFAF5",
    outline="")

canvas.create_text(
    586.0,
    579.0,
    anchor="nw",
    text="RiceBowl",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    1419.0,
    576.0,
    anchor="nw",
    text="14K/Pcs",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    471.0,
    616.0,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    681.0,
    651.0,
    image=image_image_15
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    683.0,
    651.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#DC9B99",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=642.0,
    y=640.0,
    width=82.0,
    height=20.0
)

canvas.create_rectangle(
    401.0,
    398.0,
    907.0,
    520.0,
    fill="#FAFAF5",
    outline="")

canvas.create_text(
    586.0,
    417.0,
    anchor="nw",
    text="Kebab",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    1419.0,
    412.0,
    anchor="nw",
    text="11K/Pcs",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    469.0,
    458.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    681.0,
    494.0,
    image=image_image_17
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    683.0,
    494.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#DC9B99",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=642.0,
    y=483.0,
    width=82.0,
    height=20.0
)

canvas.create_rectangle(
    402.0,
    231.0,
    908.0,
    358.0,
    fill="#FAFAF5",
    outline="")

canvas.create_text(
    586.0,
    255.0,
    anchor="nw",
    text="Risol Mayo",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    1419.0,
    249.0,
    anchor="nw",
    text="3K/Pcs",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    471.0,
    294.0,
    image=image_image_18
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    681.0,
    330.0,
    image=image_image_19
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    683.0,
    330.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#DC9B99",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=642.0,
    y=319.0,
    width=82.0,
    height=20.0
)

canvas.create_text(
    816.0,
    159.0,
    anchor="nw",
    text="MAKANAN",
    fill="#000000",
    font=("SansSerifCollection", 60 * -1)
)

canvas.create_text(
    832.0,
    721.0,
    anchor="nw",
    text="6K/Pcs",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    831.0,
    563.0,
    anchor="nw",
    text="2K/Pcs",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    833.0,
    405.0,
    anchor="nw",
    text="2K/Pcs",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    832.62451171875,
    247.0,
    anchor="nw",
    text="2K/Pcs",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
