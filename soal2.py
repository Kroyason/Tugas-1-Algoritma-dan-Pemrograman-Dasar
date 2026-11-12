def hitung_biaya_berat(berat):
    """Fungsi untuk menghitung biaya pengiriman berdasarkan berat paket."""
    if berat <= 2:
        return 10000
    else:
        kelebihan = berat - 2
        return 10000 + (kelebihan * 4000)


def hitung_biaya_jarak(jarak):
    """Fungsi untuk menghitung biaya tambahan berdasarkan jarak pengiriman."""
    if jarak <= 20:
        return 0
    else:
        return 5000


def hitung_potongan(ongkos_kotor, status_anggota):
    """Fungsi untuk menghitung potongan diskon 10 persen bagi anggota."""
    if status_anggota == "Ya":
        return 0.10 * ongkos_kotor
    else:
        return 0


def cetak_struk(daftar_pesanan):
    """Fungsi void untuk mencetak rekap struk dan total pendapatan."""
    print("Pelanggan  | Biaya Berat | Biaya Jarak | Potongan | Ongkir Akhir")
    print("----------------------------------------------------------------")
    
    total_pendapatan = 0
    
    for pesanan in daftar_pesanan:
        nama = pesanan[0]
        berat = pesanan[1]
        jarak = pesanan[2]
        status_anggota = pesanan[3]
        
        biaya_berat = hitung_biaya_berat(berat)
        biaya_jarak = hitung_biaya_jarak(jarak)
        ongkir_kotor = biaya_berat + biaya_jarak
        potongan = hitung_potongan(ongkir_kotor, status_anggota)
        ongkir_akhir = ongkir_kotor - potongan
        
        total_pendapatan = total_pendapatan + ongkir_akhir
        
        print(f"{nama:10} | Rp {biaya_berat:8} | Rp {biaya_jarak:8} | Rp {potongan:5.0f} | Rp {ongkir_akhir:9.0f}")
        
    print("----------------------------------------------------------------")
    print(f"Total Pendapatan Ongkos Kirim Hari Ini: Rp {total_pendapatan:.0f}")


def main():
    """Fungsi utama jalannya program."""
    # Format data: [nama, berat, jarak, anggota]
    data_pesanan = [
        ["Rina", 1, 10, "Bukan"],
        ["Sari", 5, 25, "Bukan"],
        ["Tono", 5, 25, "Ya"],
        ["Umar", 2, 30, "Ya"],
        ["Vina", 8, 15, "Bukan"]
    ]
    cetak_struk(data_pesanan)


if __name__ == "__main__":
    main()