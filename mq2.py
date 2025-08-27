# Data awal
datalkan = [
    ["Ikan Lele", "Clarias batrachus", "Clariidae"],
    ["Ikan Gurame", "Osphronemus goramy", "Osphronemidae"],
    ["Ikan Cupang", "Betta splendens", "Osphronemidae"]
]


#Ubah menjadi kolom
nama_ikan, nama_ilmiah, nama_family = zip(*datalkan)


#Buat list nama_genus dari data nama_ilmiah yang sudah dipisah
nama_genus = [i.split()[0] for i in nama_ilmiah]


# Setiap variabel (nama_ikan, dll) kini berisi 3 elemen yang bisa diakses via indeks
print(f"{'Nama Ikan':<12} | {nama_ikan[0]:<18} | {nama_ikan[1]:<18} | {nama_ikan[2]}")
print(f"{'Nama Ilmiah':<12} | {nama_ilmiah[0]:<18} | {nama_ilmiah[1]:<18} | {nama_ilmiah[2]}")
print(f"{'Nama Genus':<12} | {nama_genus[0]:<18} | {nama_genus[1]:<18} | {nama_genus[2]}")
print(f"{'Nama Family':<12} | {nama_family[0]:<18} | {nama_family[1]:<18} | {nama_family[2]}")