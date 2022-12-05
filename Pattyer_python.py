# --------- Tutorial Link-https://www.youtube.com/watch?v=fX64q6sYom0 ----------------


# ************ Square ********************
"""
n =5
for i in range(n):   #n rows
    for j in range(n):   # n columns
        print("*", end=' ')
    print('')
"""


# ************ Increasing triangle ********************
"""
n = 5
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print('')
"""

# ************ Decreasing triangle ********************

"""
n = 5
for i in range(n):   #0-4
    for j in range(i,n):
        print("*", end=" ")
    print("")
"""


# ************ Right Side Increasing triangle ********************
"""
n = 5
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ") 
    print("")
"""

# ************ Right Side Decreasing triangle ********************
# """
n = 5
for i in range(n):
    for j in range(i+1):
        print(" ", end = " ")
    for j in range(i, n):
        print("*", end=" ")
    print("")
# """


# ************ Hill Pattern ******************** 
"""
n = 5
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print("")
    """

# ************ Reverse Hill Pattern ******************** 
"""
n = 5 
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n-1):
        print("*", end=" ")
    for j in range(i,n):
        print("*", end=" ")
    print("")
# """

# ************ Diamond Pattern ********************
"""
n = 5
for i in range(n-1):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print("")

for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n-1):
        print("*", end=" ")
    for j in range(i,n):
        print("*", end=" ")
    print("")
"""

# ************ Butterfly Pattern ********************
# """
n=5

# Upper Butterfly
for i in range(n-1):
    for j in range(i+1):
        print("*", end=" ")
    for j in range(i, n-1):
        print(" ", end=" ")
    for j in range(i, n-1):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print("")

#lower butterfly
for i in range(n):
    for j in range(i, n):
        print("*", end=" ")
    for j in range(i):
        print(" ", end=" ")
    for j in range(i):
        print(" ", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print("")

# """


