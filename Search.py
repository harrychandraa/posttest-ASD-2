var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
print("var",var)

def find_data(data):
    for i in range(len(var)):
        if isinstance(var[i], str) and var[i] == data:
            return i
        elif isinstance(var[i], list) and data in var[i]:
            return (i, var[i].index(data))
    return None

while True:
    data_to_find = input("Masukkan nama (ketik 'selesai' untuk keluar): ")
    if data_to_find == "selesai":
        break
    result = find_data(data_to_find)
    if result is None:
        print(f"Data {data_to_find} tidak ditemukan dalam list.")
    elif isinstance(result, int):
        print(f"Data {data_to_find} ditemukan pada indeks ke-{result} pada list.")
    else:
        print(f"Data {data_to_find} ditemukan pada indeks ke-{result[0]} pada list, dan pada kolom ke-{result[1]}.")