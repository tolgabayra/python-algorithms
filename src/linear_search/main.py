from numpy import random

""" 
Doğrusal aramayı en temel ve basit yöntem olarak gösterebiliriz. 
Eşleşme bulana dek, listedeki bütün elemanları birer birer kontrol etmek üzerine kurulu bir algoritma
"""


def LinearSearch(array, n, k):
    for j in range(0, n):
        print("Runned.")
        if array[j] == k:
            return j

    return -1


array = random.randint(100, size=(1000))

k = 7
n = len(array)

result = LinearSearch(array, n, k)

if result == -1:
    print("Element not found")

else:
    print("Element found at index:", result)
