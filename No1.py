#Dita Widayanti Setiawan_F55121098_C TI

import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    end_time = time.time()
    return arr, end_time - start_time

def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    end_time = time.time()
    return arr, end_time - start_time

def print_iterations(arr, iterations):
    print("Iterasi Pertama:")
    for i in range(iterations):
        print(arr[i], end=" ")
    print("\n")
    print("Iterasi Terakhir:")
    for i in range(len(arr)-iterations, len(arr)):
        print(arr[i], end=" ")
    print("\n")

def print_computation_time(time):
    print("Waktu Komputasi Pengurutan:", time, "detik\n")

def print_before_after(arr, sorted_arr):
    print("Sebelum Pengurutan:", arr)
    print("Setelah Pengurutan:", sorted_arr, "\n")

def bubble_sort_analysis():
    print("Analisis Bubble Sort:")
    print("Worst case: O(n^2)")
    print("Best case: O(n)")
    print("Average case: O(n^2)\n")

def insertion_sort_analysis():
    print("Analisis Insertion Sort:")
    print("Worst case: O(n^2)")
    print("Best case: O(n)")
    print("Average case: O(n^2)\n")

def main():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
           26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
           17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
           40, 7, 41, 81]

    print("Pilih metode pengurutan:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    choice = int(input("Masukkan pilihan (1/2): "))

    if choice == 1:
        sorted_arr, time_taken = bubble_sort(arr.copy())
        print_iterations(sorted_arr, 5)
        print_computation_time(time_taken)
        print_before_after(arr, sorted_arr)
        bubble_sort_analysis()
    elif choice == 2:
        sorted_arr, time_taken = insertion_sort(arr.copy())
        print_iterations(sorted_arr, 5)
        print_computation_time(time_taken)
        print_before_after(arr, sorted_arr)
        insertion_sort_analysis()
    else:
        print("Pilihan tidak valid!")

if __name__ == '__main__':
    main()
