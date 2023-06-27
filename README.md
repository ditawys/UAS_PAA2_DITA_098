### Analysis algorithm untuk mengevaluasi:
a. Worst case

b. Best case

c. Average case

Menganalisis algoritma pengurutan yaitu bubble sort dan insertion sort berikut:

1. Bubble Sort:
   
   a. Worst case: O(n^2)
      Pada worst case, jika elemen dalam array terurut secara terbalik, Bubble Sort akan melakukan iterasi maksimal (n-1) pada setiap fase pengurutan dan membandingkan setiap pasangan elemen, sehingga menghasilkan kompleksitas waktu O(n^2).

   b. Best case: O(n)
      Pada best case, jika elemen dalam array sudah terurut secara menaik, Bubble Sort akan melakukan satu iterasi untuk memeriksa apakah ada pertukaran elemen. Jika tidak ada pertukaran yang dilakukan pada iterasi pertama, algoritma akan berhenti. Sehingga kompleksitas waktu pada kasus terbaik adalah O(n).

   c. Average case: O(n^2)
      Pada rata-rata kasus, Bubble Sort akan melakukan iterasi sebanyak (n-1) pada setiap fase pengurutan, dan pada setiap iterasi, membandingkan setiap pasangan elemen. Jadi, kompleksitas waktu rata-rata adalah O(n^2).

3. Insertion Sort:
   
   a. Worst case: O(n^2)
      Pada worst case, jika elemen dalam array terurut secara terbalik, setiap elemen akan harus digeser ke posisi yang benar secara berulang kali selama iterasi. Sehingga kompleksitas waktu pada kasus terburuk adalah O(n^2).

   b. Best case: O(n)
      Pada best case, jika elemen dalam array sudah terurut secara menaik, Insertion Sort hanya perlu membandingkan setiap elemen dengan elemen sebelumnya dan tidak perlu melakukan pergeseran. Sehingga kompleksitas waktu pada kasus terbaik adalah O(n).

   c. Average case: O(n^2)
      Pada rata-rata kasus, jika elemen dalam array diacak secara acak, Insertion Sort akan melakukan pergeseran elemen sejumlah (n^2)/4 kali, yang menghasilkan kompleksitas waktu rata-rata O(n^2).

Dengan demikian, berdasarkan analisis di atas, kompleksitas waktu algoritma Bubble Sort dan Insertion Sort adalah sama untuk worst case dan average case, yaitu O(n^2), sedangkan pada best case, Insertion Sort memiliki kompleksitas waktu yang lebih baik yaitu O(n) dibandingkan dengan Bubble Sort yang tetap O(n^2).


Menganalisis algoritma menghitung shortest path menggunakan algoritma TSP dan Djikstra berikut:
1. Traveling Salesman Problem (TSP):
   
   a. Worst case: O(n!)
      Dalam TSP, kompleksitas waktu terburuk terjadi ketika setiap simpul harus dikunjungi sekali dan kemudian kembali ke simpul awal. Dalam kasus ini, jumlah permutasi yang mungkin adalah (n-1)! dan diperlukan waktu yang cukup lama untuk mencari solusi optimalnya.

   b. Best case: O(n^2)
      Pada kasus terbaik, jika graf tidak memiliki siklus dan semua simpul terhubung langsung dengan simpul awal, algoritma TSP hanya perlu memeriksa setiap simpul tepat satu kali. Dalam kasus ini, kompleksitas waktu adalah O(n^2).

   c. Average case: Tidak ada jawaban pasti
      Kompleksitas waktu rata-rata dalam TSP tergantung pada karakteristik spesifik dari graf yang diberikan dan urutan kunjungan yang dihasilkan oleh algoritma. Tidak ada jawaban pasti untuk kompleksitas waktu rata-rata dalam TSP.

2. Dijkstra:
   
   a. Worst case: O((V + E)logV)
      Dalam Dijkstra, V adalah jumlah simpul (vertices) dan E adalah jumlah tepi (edges). Dalam kasus terburuk, algoritma Dijkstra harus memeriksa semua simpul dan tepi di dalam graf yang diberikan, sehingga kompleksitas waktu adalah O((V + E)logV).

   b. Best case: O(V + E)
      Pada kasus terbaik, jika simpul awal adalah simpul tujuan atau terhubung langsung dengan simpul tujuan, algoritma Dijkstra hanya perlu memeriksa simpul dan tepi sekali. Dalam kasus ini, kompleksitas waktu adalah O(V + E).

   c. Average case: O((V + E)logV)
      Kompleksitas waktu rata-rata dalam algoritma Dijkstra juga bergantung pada struktur graf yang diberikan. Namun, secara umum, kompleksitas waktu rata-rata adalah O((V + E)logV).

Dengan demikian, berdasarkan analisis di atas, kompleksitas waktu algoritma TSP adalah O(n!) dalam worst case, O(n^2) dalam best case, dan kompleksitas waktu rata-rata yang tidak dapat ditentukan dengan pasti. Sedangkan, kompleksitas waktu algoritma Dijkstra adalah O((V + E)logV) dalam worst case dan average case, dan O(V + E) dalam best case.
