# Electronic code book

## Profil
| #               | Biodata                      |
| --------------- | ---------------------------- |
| **Nama**        | Muhammad Farhan              |
| **NIM**         | 312110128                    |
| **Kelas**       | TI.21.A1                     |
| **Mata Kuliah** | Kriptografi                  |

1. Definisi: ECB adalah mode enkripsi simetris di mana setiap blok plaintext dienkripsi secara terpisah dengan kunci yang sama.
   
2. Konsep Dasar: ECB membagi plaintext menjadi blok-blok yang sama dan mengenkripsi setiap blok secara terpisah. Hal ini menyebabkan blok-blok dengan isi yang sama akan menghasilkan ciphertext yang sama.
   
3. Kelemahan: Meskipun sederhana, ECB memiliki kelemahan keamanan, yaitu kurangnya difusi. Blok-blok identik dalam plaintext akan menghasilkan blok ciphertext yang identik, sehingga pola dalam data mudah dikenali.

Konsep dasar ECB adalah menyederhanakan enkripsi dengan memperlakukan setiap blok plaintext secara independen, yang membuatnya mudah diimplementasikan tetapi memiliki kelemahan keamanan tertentu.

## Fungsi-fungsi:
- `hex_to_bin`: Mengonversi string heksadesimal ke biner.
- `bin_to_hex`: Mengonversi string biner ke heksadesimal.
- `encrypt_ecb`: Fungsi enkripsi ECB.

## Langkah-langkah:
1. **Input dari Pengguna:**
   - Menerima plaintext dalam bentuk heksadesimal dan kunci dalam bentuk biner.

2. **Proses Enkripsi:**
   - Mengonversi plaintext ke biner, melakukan padding jika diperlukan.
   - Membagi plaintext menjadi blok-blok 4 bit.
   - Menginisialisasi list untuk hasil enkripsi.
   - Enkripsi setiap blok:
     - XOR blok dengan kunci.
     - Geser setiap bit ke liri.
     - Konversi hasil ke heksadesimal dan tambahkan ke list.
   - Mengembalikan list hasil enkripsi.

3. **Menampilkan Hasil:**
   - Menampilkan plaintext, kunci, dan hasil enkripsi ECB dalam format list.

## Penggunaan:
1. Masukkan plaintext dalam bentuk heksadesimal.
2. Masukkan kunci dalam bentuk biner.
3. Lihat hasil enkripsi.

## Result

<img width="571" alt="Screenshot 2023-12-12 084933" src="https://github.com/farhanz17/Electronic_code_book-ecb-/assets/92637117/8f027ec5-041a-491d-960d-2d4aad78f78e">
