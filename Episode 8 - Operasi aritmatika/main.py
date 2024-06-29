# operasi aritmatika

a = 10
b = 3
# operasi penambahan
hasil = a + b 
print(a, ' + ', b, '=', hasil)

# operasi pengurangan
hasil = a - b 
print(a, ' - ', b, '=', hasil)

# operasi perkalian
hasil = a * b 
print(a, ' * ', b, '=', hasil)

# operasi pembagian
hasil = a / b 
print(a, ' / ', b, '=', hasil)

# operasi eksponen
hasil = a ** b 
print(a, ' ** ', b, '=', hasil)

# operasi modulus
hasil = a % b 
print(a, ' % ', b, '=', hasil)

# operasi floor devision
hasil = a // b 
print(a, "//", b, "=", hasil)

# prioritas operasi / operation precendance
'''
    1. ()
    2. eskponen **
    3. perkalian dan teman temannya * / //
    4. penambahan, pengurangan + -
'''

x = 5
y = 3
z = 8

hasil = x ** y * z / y - x + z % y // x * y
print(x,'**',y,'*',z,'/',y,"-",x,'+',z,'%',y,'//',x,'*',y, '=', hasil)

hasil = (x + y) * z
print('(',x,'+',y,') *', z, '=', hasil)
