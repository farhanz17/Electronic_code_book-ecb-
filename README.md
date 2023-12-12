# Electronic code book

1. Definisi: ECB adalah mode enkripsi simetris di mana setiap blok plaintext dienkripsi secara terpisah dengan kunci yang sama.
   
2. Konsep Dasar: ECB membagi plaintext menjadi blok-blok yang sama dan mengenkripsi setiap blok secara terpisah. Hal ini menyebabkan blok-blok dengan isi yang sama akan menghasilkan ciphertext yang sama.
   
3. Kelemahan: Meskipun sederhana, ECB memiliki kelemahan keamanan, yaitu kurangnya difusi. Blok-blok identik dalam plaintext akan menghasilkan blok ciphertext yang identik, sehingga pola dalam data mudah dikenali.

Konsep dasar ECB adalah menyederhanakan enkripsi dengan memperlakukan setiap blok plaintext secara independen, yang membuatnya mudah diimplementasikan tetapi memiliki kelemahan keamanan tertentu.

## Result

<img width="571" alt="Screenshot 2023-12-12 084933" src="https://github.com/farhanz17/Electronic_code_book-ecb-/assets/92637117/8f027ec5-041a-491d-960d-2d4aad78f78e">
