def selectionSort(a):
    n = len(a)
    for i in range(n):
        min = i
        for j in range(i, n):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]


a = [45, 67, 89, 23, 12, 45]
selectionSort(a)
print(a)
