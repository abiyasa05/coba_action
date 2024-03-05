# main.py

def fungsi_pertama():
    print("Menjalankan Fungsi Pertama")
    hasil_pertama = 5
    return hasil_pertama

def fungsi_kedua(input_fungsi_pertama):
    print("Menjalankan Fungsi Kedua dengan input:", input_fungsi_pertama)
    hasil_kedua = input_fungsi_pertama * 2
    return hasil_kedua

def main():
    # Langkah 1: Jalankan Fungsi Pertama
    output_fungsi_pertama = fungsi_pertama()

    # Langkah 2: Jalankan Fungsi Kedua dengan hasil Fungsi Pertama sebagai input
    output_final = fungsi_kedua(output_fungsi_pertama)

    # Tampilkan hasil akhir
    print("Hasil Akhir:", output_final)

if __name__ == "__main__":
    main()
