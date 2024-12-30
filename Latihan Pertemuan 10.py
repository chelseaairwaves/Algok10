#mencetak angka 6
for i in range(6):
    print(i)

#mencetak angka genap dari 0 hingga 10
for i in range (0, 11, 2):
    print(i)
    
#perulangan dengan step
print ("Perulangan dengan step: ")
for i in range (1, 20,3):
    print(i)

#menggunakan perulangan for untuk menggunakan total nilai dalam list
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("Total nilai:", total)
