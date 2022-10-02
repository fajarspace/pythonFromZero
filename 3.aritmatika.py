a = 10
b = 3

# penjumlahan
x = a + b
print(a,"+",b,'=',x)

# perkalian
x = a * b
print(a,"*",b,'=',x)

# pembagian
x = a / b
print(a,"/",b,'=',x)

# eksponen / pangkat
x = a ** b
print(a,"**",b,'=',x)

# modulus / sisa bagi
x = a % b
print(a,"%",b,'=',x)

# floor division / mengubah float ke int
x = a // b
print(a,"//",b,'=',x)

# operational precedence / prioritas
x = 3
y = 2
z = 4
hasil = x + y * z # perkalian dahulu yang dieksekusi
print(x,'+',y,'*',z,'=',hasil)

hasil = (x + y) * z # () merupakan prioritas yg harus didahulukan
print('(',x,'+',y,')','*',z,'=',hasil)