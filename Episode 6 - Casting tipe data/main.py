# casting = merubah tipe data satu ke tipe data yang lain
# tipe data = int, float, str, bool

#  INTEGER
print("\nINI DARI INTEGER")
data_int = 10
print("data = ", data_int, type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # data bool hanya akan false ketika int = 0

print("data = ", data_float, type(data_float))
print("data = ", data_str, type(data_str))
print("data = ", data_bool, type(data_bool))

#  BOOLEAN
print("\nINI DARI BOOLEAN")
data_bool = True
print("data = ", data_bool, type(data_bool))

data_int = int(data_bool) # bilangan bool bernilai 1 jika true dan 0 jika false
data_str = str(data_bool)
data_float = float(data_bool) 

print("data = ", data_int, type(data_bool))
print("data = ", data_str, type(data_bool))
print("data = ", data_float, type(data_bool))

#  STRING
print("\nINI DARI STRING")
data_str = "10"
print("data = ", data_str, type(data_str))

data_int = int(data_str) 
data_bool = bool(data_str)
data_float = float(data_str) 

print("data = ", data_int, type(data_str)) # akan error jika string bukan angka
print("data = ", data_bool, type(data_str)) # akan error jika string bukan angka
print("data = ", data_float, type(data_str)) # nilai dari str jika diubah menjadi bool hanya akan bernilai false ketika data str tersebut kosong
