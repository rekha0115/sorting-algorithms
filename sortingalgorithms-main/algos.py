
# --BUBBLE SORT
def bubble_sort(arr, reverse=False):
   n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# --SELECTION SORT
def selection_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
# --INSERTION SORT
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
    
# -- MERGE SORT
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right

# --QUICK SORT 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)
    
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
