# nilai dari komparasi ini adalah True or False

# > < >= <= == != is isnot

a = 4
b = 2

# lebih besar dari >
print('==========Lebih besar dari >')
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = a > b
print(a,'>',b,'=',hasil)

# lebih kurang dari >
print('==========Lebih kurang dari <')
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = a < b
print(a,'<',b,'=',hasil)

# Lebih besar sama dengan >=
print('==========Lebih besar sama dengan >=')
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = a >= b
print(a,'>=',b,'=',hasil)

# Lebih kecil sama dengan >=
print('==========Lebih kecil sama dengan <=')
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = a <= b
print(a,'<=',b,'=',hasil)

# sama dengan =
print('==========sama dengan =')
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == a
print(b,'==',a,'=',hasil)

# tidak sama dengan !=
print('==========tidak sama dengan !=')
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != a
print(b,'!=',a,'=',hasil)

# is sebagai komparasi object identity
print('==========is sebagai komparasi object identity')
x = 5
y = 5
print('nilai x =',x,'id','=',hex(id(x)))
print('nilai y =',y,'id','=',hex(id(y)))
hasil = x is y # nilai 'y' tidak bisa menggunakan literal (5)
print('x is y =', hasil)

# is not sebagai komparasi object identity
print('==========is not sebagai komparasi object identity')
x = 5
y = 6
print('nilai x =',x,'id','=',hex(id(x)))
print('nilai y =',y,'id','=',hex(id(y)))
hasil = x is not y # nilai 'y' tidak bisa menggunakan literal (5)
print('x is y =', hasil)