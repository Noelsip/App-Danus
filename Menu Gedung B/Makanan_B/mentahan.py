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
    700.0,
    167.0,
    anchor="nw",
    text= "DANA USAHA ITK",
    fill="#ffffff",
    font=("Open Sans",70 *-1)
)

canvas.create_text(
    900.0,
    240.0,
    anchor="nw",
    text= "STRUK",
    fill="#ffffff",
    font=("Open Sans",50 *-1)
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
    1121.0,
    256.0,
    anchor= "nw", 
    text = total,
    fill= "#000000",
    font=("Inter SemiBold", 20 * -1)
)