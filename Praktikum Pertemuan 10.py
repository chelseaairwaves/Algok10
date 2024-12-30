#membuat perulangan for dengan list
for i in [1, 2, 3, 4, 5]:
    print ("inipengulangan ke - ",i)

#membuat perulangan for dengan list dengan isi string
#perulangan sebanyak 8 kali
print ("Perulangan for dengan list dengan isi string: ")
for i in ["Rawon", "Nasi Kuning", "Soto Madura", "Kupat Tahu", "Kerak Telor", "Rendang Batoko", "Pempek Selam", "Ayam Betutu"]:
    print (i, "adalah masakan khas nusantara....")

#membuat perulangan for dengan string
print ("Perulangan for dengan string: ")
for i in ("abcde"):
    print (i, "adalah alfabet")

#membuat perulangan while
i = 1
while i <=5:
    print(i)
    i=i+1

print("program selesai")

#membuat program fibonacci:
n = int(input ("Masukkan jumlah angka fibonacci: "))
a, b = 0, 1

for _ in range (n):
    print (a, end=" ")
    a, b = b,a + b


#menentukan bilangan prima
print (" menentukan bilangan Prima")
number = int(input("Masukkan angka: "))
is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

if is_prime and number > 1:
    print(number, "adalah bilangan prima.")
else:
    print(number, "bukan bilangan prima.")
