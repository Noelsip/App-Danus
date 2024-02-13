import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import ImageTk, Image
from matplotlib import image

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:/App_Danus/Menu Gedung B/Minuman_B/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("MENU MINUMAN GEDUNG B")

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

class button_next ():
    def btn_clicked_next(self):
        Golda_Coffee     = entry_2.get().strip()
        Teh_Kotak       = entry_3.get().strip()
        Floridina       = entry_4.get().strip()
        Minuman_Jelly   = entry_6.get().strip()
        Le_Minerale     = entry_7.get().strip()
        Teh_Pucuk       = entry_8.get().strip()

        Nama_Minuman = [
        ("Golda Coffee  ", Golda_Coffee,8000), #harga),
        ("Teh Kotak     ", Teh_Kotak,2500),
        ("Floidina      ", Floridina,12000),
        ("Minuman Jelly ", Minuman_Jelly,3000),
        ("Le Minerale   ", Le_Minerale,3000),
        ("Teh Pucuk     ", Teh_Pucuk, 4000)
        ]

        hargaPesanan = []
        TotalPembelian = 0
        for item in Nama_Minuman:
            nama_item, jumlah, harga= item
            jumlah = int(jumlah) if jumlah else 0
            TotalPembelian += jumlah*harga

        # with open("D:/App_Danus/DATA BASE/Header.txt","w") as f:
        #     f.write("NAMA ITEM      \tJUMLAH          \tHARGA\n")

        with open('D:/App_Danus/DATA BASE/total_makanan.txt','r') as f:
            total_makanan= f.read()
            total = int(total_makanan)
            TotalPembelian += total

        with open('D:/App_Danus/DATA BASE/makanan.txt','r') as f:
            makanan = f.read()

        with open("D:/App_Danus/DATA BASE/struk.txt", "w") as f:
            for nama, pesan,harga in Nama_Minuman:
                if pesan:
                    f.write(f"{nama}    \t\t\t{pesan}\n")
            f.write(f"{makanan}\n")
        with open("D:/App_Danus/DATA BASE/pesanan_makanan.txt","w") as f:
            for nama_item, pesan,harga in Nama_Minuman:
                if pesan:
                    pesan = int(pesan)
                    hargaPesanan.append(pesan*harga)
                else:
                    continue
            print(hargaPesanan)
            for i in hargaPesanan:
                if i== 0:
                    continue
                else:
                    f.write(f"Rp{i}\n")        
        with open("D:/App_Danus/DATA BASE/harga_makanan.txt","r") as f:
            harga_makanan= f.read()


        
        with open("D:/App_Danus/DATA BASE/Total_harga.txt","w") as f:
            # f.write('__________________________________________\n')
            f.write(f"TOTAL     Rp. {TotalPembelian}")
            
        window.destroy()
        subprocess.call(["python", "D:/App_Danus/STRUK/build/struk.py"])
    def enter():
            canvas.config(cursor="hand2")
    def leave():
            canvas.config(cursor="")

tagname = 'event'
img2= ImageTk.PhotoImage(Image.open("Button.png"))
button_next1 = canvas.create_image(1550,965, image=img2, tag=tagname)

canvas.tag_bind(tagname, "<Enter>", lambda event: button_next.enter())
canvas.tag_bind(tagname, "<Leave>", lambda event: button_next.leave())
canvas.tag_bind(button_next1, "<Button-1>", button_next.btn_clicked_next)


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
    64.0,
    image=image_image_3
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
    text="Le Minerale\n",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_23 = PhotoImage(
    file=relative_to_assets("image_17.png"))
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
    text="3K/Pcs",
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
    text="Teh Pucuk",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_26 = PhotoImage(
    file=relative_to_assets("image_5.png"))
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
window.resizable(True, True)
window.mainloop()
