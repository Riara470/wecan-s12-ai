import numpy as np

# 3D: 2 pages, 2 rows, 3 cols -> shape (2,2,3)
arr = np.array([
    [[1, 2, 3],      # Page 0
     [4, 5, 6]],
    
    [[7, 8, 9],      # Page 1
     [10, 11, 12]]
])

print("START shape", arr.shape)
print(arr)

# EDIT -> Page 0, Row 1, Col 1 = 5 -> change to 99
arr[0, 1, 1] = 99
print("\n1. EDIT [0,1,1] to 99:\n", arr)

# ADD -> Add new page [[13,14,15],[16,17,18]]
new_page = np.array([[[13, 14, 15],
                      [16, 17, 18]]])

arr = np.concatenate((arr, new_page), axis=0)
print("\n2. ADD new PAGE (now 3 pages) shape", arr.shape)
print(arr)

# DELETE -> Delete Page 1
arr = np.delete(arr, 1, axis=0)
print("\n3. DELETE Page 1 (axis=0) shape", arr.shape)
print(arr)

# DELETE ROW -> Delete row 0 from ALL pages
arr = np.delete(arr, 0, axis=1)
print("\n4. DELETE Row 0 from all pages shape", arr.shape)
print(arr)

# DELETE COLUMN -> Delete col 0 from ALL
arr = np.delete(arr, 0, axis=2)
print("\n5. DELETE Col 0 from all shape", arr.shape)
print(arr)