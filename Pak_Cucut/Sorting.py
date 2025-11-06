def insertion_sort_asc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


numbers = [2, 10, 3, 1, 17, 25, 16, 9, 18]

asc = insertion_sort_asc(numbers.copy())
print("Ascending order:", asc)

desc = insertion_sort_desc(numbers.copy())
print("Descending order:", desc)