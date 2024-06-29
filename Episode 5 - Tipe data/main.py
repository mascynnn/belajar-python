# tipe data adalah macam macam data yang bisa dimasukkan pada variabel

# integer (bilangan tanpa koma)
data_integer = 10
print(data_integer, " adalah ", type(data_integer))

# float (bilangan dengan koma)
data_float = 20.5
print(data_float, " adalah ", type(data_float))

# string (kumpulan karakter huruf/kata)
data_string = "makhasin"
print(data_string, " adalah ", type(data_string))

# boolean (data true/false)
data_bool = True
print(data_bool, " adalah ", type(data_bool))

# tipe data complex
# bilangan complex
data_complex = complex(5,3)
print(data_complex, " adalah ", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double, c_char
data_c_double = c_double(4.5)
print(data_c_double, " adalah ", type(data_c_double))
