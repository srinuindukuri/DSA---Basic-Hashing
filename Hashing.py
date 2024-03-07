# Print Repeating elements in an array...
def first_repeating_element(arr, n):
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                return i
    return -1

arr = [10, 5, 3, 4, 7, 2, 4]
n = len(arr)

index = first_repeating_element(arr, n)

if index == -1:
    print("Repeating element not found..")
else:
    print("Repeating element is", arr[index])

## -------------------------------------------------------------
# Print the duplicates elements in an array...
arr1 = [10, 5, 3, 4, 7, 2, 5]
print("Duplicates elements in an array: ")
for i in range(len(arr1)):
    for j in range(i+1, len(arr1)):
        if arr1[i] == arr1[j]:
            print(arr1[j])

