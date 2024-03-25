def calculate_product(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

def main():
    test_date = int(input("Masukkan Tanggal Test hari ini: "))
    result = calculate_product(test_date)
    
    # Membuat string untuk menampilkan urutan angka dari 1 hingga n
    numbers = '*'.join(str(i) for i in range(1, test_date + 1))
    print(f"Hasil faktorial dari {numbers} adalah: {result}")

if __name__ == "__main__":
    main()
