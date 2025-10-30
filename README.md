# IF3070-Tubes-1-G50 - Bin Packing Optimization

Implementasi berbagai algoritma optimasi untuk menyelesaikan masalah **Bin Packing** menggunakan Python. Proyek ini mencakup algoritma Hill Climbing (berbagai varian), Simulated Annealing, dan Genetic Algorithm.

## Deskripsi Proyek
Bin Packing adalah masalah optimasi kombinatorial yang bertujuan untuk menempatkan sejumlah barang dengan ukuran berbeda ke dalam kontainer dengan kapasitas terbatas, dengan tujuan meminimalkan jumlah kontainer yang digunakan.

## Tech Stack
[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://python.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-orange?logo=matplotlib)](https://matplotlib.org/)

## Algoritma yang Diimplementasikan
### 1. Hill Climbing Variants
- **Steepest Ascent Hill Climbing** 
- **Hill Climbing with Sideways Move** 
- **Random Restart Hill Climbing** 
- **Stochastic Hill Climbing** 
### 2. Simulated Annealing
### 3. Genetic Algorithm

## Cara Menjalankan
### Prerequisites
- Python 3.13+
- Matplotlib library

### Instalasi Dependencies
```bash
pip install matplotlib
```

### Menjalankan Aplikasi
```bash
cd src
python main.py
```

## Format File Input
File input menggunakan format JSON dengan struktur berikut:

```json
{
  "kapasitas_kontainer": 100,
  "barang": [
    {"id": "A", "ukuran": 40},
    {"id": "B", "ukuran": 60},
    {"id": "C", "ukuran": 70},
    {"id": "D", "ukuran": 30},
    {"id": "E", "ukuran": 20}
  ]
}
```

## Output Program
Setiap algoritma menampilkan:
- State awal dan akhir
- Nilai objective function
- Jumlah kontainer yang digunakan
- Waktu eksekusi
- Grafik perkembangan (jika ada perbaikan)

## Contributors

Berikut adalah daftar kontributor beserta pembagian tugasnya masing-masing:

| **Nama** | **NIM**  | **Pembagian Tugas** |
| ---------------------- | ------------- | ----------- |
| Fadil Rifqi R P     | 18223107     | Stochastic, Sideway Move, Random-Restart, Simulated Annealing |
| Anggita Najmi Layali| 18223122      | Steepest Ascent, Stochastic, Genetic Algorithm, setup program |