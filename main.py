# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import Counter

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Sonarqube')

arr = [5, 7, 3, 0, 9, 4, 3, 2];
temp = 0;

print("Elements of original array: ");

for i in range(0, len(arr)):
    print(arr[i], end=" ");

for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if (arr[i] > arr[j]):
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
print();

print("Elements of array sorted in ascending order");
for i in range(0, len(arr)):
    print(arr[i], end=" ");

my_dict = {i:arr.count(i) for i in arr}
print("\nCount of repeated each elements in list ")
print (my_dict) ;

