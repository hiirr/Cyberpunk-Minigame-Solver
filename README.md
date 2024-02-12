# Cyperbunk 2077 Breach Protocol Minigame Solver


> Tugas Kecil 1 IF2211 Strategi Algoritma

Tugas kecil ini dibuat dengan menggunakan strategi algoritma brute force yang terinspirasi untuk menyelesaikan sebuah permainan kecil pada permainan Cyberpunk 2077 Breach Protocol


## Instalasi
Instalasi program dilakukan dengan melakukan clone repository ini dengan mengetik pada terminal

```shell
git clone https://github.com/hiirr/Cyberpunk-Minigame-Solver.git
```

ketergantungan: python 3.x

## Kompilasi

Apabila repository sudah di-clone, kompilasi program dengan mengetik

```shell
python main.py
```
catatan: program dapat digunakan pada windows dan linux

## Penggunaan

1. **Pilih di antara dua pilihan metode pada program ini,**
- Metode 1: File TXT
  Berikan masukan melalui file `.txt`.
- Metode 2:** CLI: Masukkan langsung dari baris perintah.

2. **Ikuti petunjuk untuk memasukkan data berdasarkan metode yang dipilih.**

3. **Program akan mencari solusi dan menampilkannya di CLI.**
4. **Secara opsional, Anda dapat memilih untuk menyimpan solusi ke file TXT.**

#### Format File txt
```shell
Ukuran buffer
Ukuran matriks (kolom baris)
Matriks
Jumlah sekuens
sekuens ke-1
bobot untuk sekuens ke-1
sekuens ke-2
bobot untuk sekuens ke-2
...
sekuens ke-n
bobot untuk sekuens ke-n
```
contoh,
```shell
7
6 6
7A 55 E9 E9 1C 55
55 7A 1C 7A E9 55
55 1C 1C 55 E9 BD
BD 1C 7A 1C 55 BD
BD 55 BD 7A 1C 1C
1C 55 55 7A 55 7A
3
BD E9 1C
15
BD 7A BD
20
BD 1C BD 55
30
```
### Kontributor

Zahira Dina Amalia,
NIM 13522085