def minNumber_of_coin(arr, amount):

    count = 0
    j = len(arr) - 1

    while j >= 0:
        while amount >= arr[j]:
            amount -= arr[j]
            count += 1
        j -= 1

    return count


arr = [1, 2, 5, 10, 20, 50, 100, 500]
amount = int(input("enter the amount value: "))
print(minNumber_of_coin(arr, amount))
