input_bilangan = int(input("Masukan bilangan bulat: "))
bilangan_dalam_baris = int(input_bilangan)
baris = 0
while baris < input_bilangan:
   kolom = 0
   while kolom < bilangan_dalam_baris:
       print(bilangan_dalam_baris, end=" ")
       kolom += 1
   print()
   bilangan_dalam_baris -= 1
   baris += 1
