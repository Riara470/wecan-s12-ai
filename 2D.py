import numpy as np

# 2D array operations
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("START:\n", arr)

# EDIT -> change 5 to 99
arr[1,1] = 99
print("\n1. EDIT [1,1] to 99:\n", arr)

# ADD ROW -> add [7,8,9]
arr = np.vstack([arr, [7, 8, 9]])
print("\n2. ADD ROW [7,8,9]:\n", arr)

# ADD COLUMN -> add [10,11,12] as new column
new_col = np.array([[10],[11],[12]])
arr = np.hstack([arr, new_col])
print("\n3. ADD COLUMN [10,11,12]:\n", arr)

# DELETE ROW -> delete row 0
arr = np.delete(arr, 0, axis=0)
print("\n4. DELETE Row 0:\n", arr)

#DELETE COLUMN -> delete column 0
arr = np.delete(arr, 0, axis=1)
print("\n5. DELETE Column 0:\n", arr)