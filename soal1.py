def hitung_nilai_akhir(tugas, uts, uas):
    """Fungsi untuk menghitung nilai akhir mahasiswa."""
    return (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)


def tentukan_huruf(nilai):
    """Fungsi untuk menentukan nilai huruf dari nilai akhir."""
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 55:
        return "C"
    elif nilai >= 40:
        return "D"
    else:
        return "E"


def cek_status(huruf):
    """Fungsi untuk menentukan lulus atau tidak lulus."""
    if huruf == "A" or huruf == "B" or huruf == "C":
        return "Lulus"
    else:
        return "Tidak Lulus"


def cetak_tabel(daftar_mhs):
    """Fungsi void untuk mencetak tabel rekap dan statistik."""
    print("Nama       | Nilai Akhir | Huruf | Status")
    print("------------------------------------------")
    
    total_nilai = 0
    jumlah_lulus = 0
    jumlah_mhs = 0 
    
    for mhs in daftar_mhs:
        jumlah_mhs = jumlah_mhs + 1  
        
        nama = mhs[0]
        tugas = mhs[1]
        uts = mhs[2]
        uas = mhs[3]
        
        na = hitung_nilai_akhir(tugas, uts, uas)
        huruf = tentukan_huruf(na)
        status = cek_status(huruf)
        
        total_nilai = total_nilai + na
        if status == "Lulus":
            jumlah_lulus = jumlah_lulus + 1
            
        print(f"{nama:10} | {na:11.2f} | {huruf:5} | {status:10}")
        
    print("------------------------------------------")
    # Menghitung rata-rata menggunakan variabel jumlah_mhs
    rata_rata = total_nilai / jumlah_mhs
    print(f"Rata-rata Nilai Akhir Kelas: {rata_rata:.2f}")
    print(f"Banyaknya Mahasiswa Lulus  : {jumlah_lulus}")


def main():
    """Fungsi utama jalannya program."""
    # Format data: [nama, tugas, uts, uas]
    data = [
        ["Andi", 80, 70, 90],
        ["Bunga", 90, 85, 88],
        ["Citra", 60, 45, 50],
        ["Dimas", 75, 80, 65],
        ["Eka", 30, 40, 35]
    ]
    cetak_tabel(data)


if __name__ == "__main__":
    main()