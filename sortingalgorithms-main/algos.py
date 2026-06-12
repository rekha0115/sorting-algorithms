
# --BUBBLE SORT
def bubble_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (arr[j] > arr[j + 1] and not reverse) or \
               (arr[j] < arr[j + 1] and reverse):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
# --SELECTION SORT
def selection_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if (arr[j] < arr[idx] and not reverse) or \
               (arr[j] > arr[idx] and reverse):
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
    return arr
# --INSERTION SORT
def insertion_sort(arr, reverse=False):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and (
            (arr[j] > key and not reverse) or
            (arr[j] < key and reverse)
        ):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
# -- MERGE SORT
def merge_sort(arr, reverse=False):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], reverse)
    right = merge_sort(arr[mid:], reverse)
    return merge(left, right, reverse)
def merge(left, right, reverse):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if (left[i] <= right[j] and not reverse) or \
           (left[i] >= right[j] and reverse):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --QUICK SORT 
def quick_sort(arr, reverse=False):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    if not reverse:
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
    else:
        left = [x for x in arr if x > pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x < pivot]
    return quick_sort(left, reverse) + middle + quick_sort(right, reverse)

def main():
    print("===== SORTING ALGORITHMS PROJECT =====")
    arr = list(map(int, input("Enter numbers (space-separated): ").split()))
    while True:
        print("\n----- MENU -----")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 6:
            print("Exiting program...")
            break
        order = input("Sort order (a = ascending / d = descending): ")
        reverse = True if order.lower() == 'd' else False
        temp_arr = arr.copy()
        if choice == 1:
            print("Sorted:", bubble_sort(temp_arr, reverse))
        elif choice == 2:
            print("Sorted:", selection_sort(temp_arr, reverse))
        elif choice == 3:
            print("Sorted:", insertion_sort(temp_arr, reverse))
        elif choice == 4:
            print("Sorted:", merge_sort(temp_arr, reverse))
        elif choice == 5:
            print("Sorted:", quick_sort(temp_arr, reverse))
        else:
            print("Invalid choice!")

        print("Original Array remains:", arr)
if __name__ == "__main__":
    main()
