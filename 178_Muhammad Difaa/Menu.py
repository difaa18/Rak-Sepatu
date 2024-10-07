rak_sepatu = {
    1: "Nike Air Jordan",
    2: "Nike AirMax",
    3: "Nike Kyrie 8",
    4: "Nike Paul Gourge 4",
    5: "Adidas Samba",
    6: "Dockmart",
    7: "Nike AirForce 1"
}

rak_sandal = {
    1: "Sandal Eiger",
    2: "Sandal Slop",
    3: "Sandal Jepit",
    4: "Sandal Sepatu",
    5: "Sandal Crocs"
}

beli_sepatu= int (input("Masukan Nomor Rak Sepatu Yang Ingin Anda Ingin Beli: "))
print("Rak Sepatu Ke- %d Adalah Sepatu: %s" % (beli_sepatu,rak_sepatu[beli_sepatu]))

beli_sandal= int (input("Masukan Nomor Rak Sandal Yang Anda Ingin Beli: "))
print("Rak Sandal Ke- %d Adalah Sandal: %s" % (beli_sandal,rak_sandal[beli_sandal]))