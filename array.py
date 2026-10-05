import numpy as np


students = ["John", "Alice", "Bob", "Eve"]
ages = np.array([20, 22, 19, 21])

print("Now:", ages)
print("In 2 years:", ages + 2)


for i in range(len(students)):
    print(f"{students[i]} will be {ages[i] + 2} in 2 years")