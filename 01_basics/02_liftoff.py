# Loop: For
# List Or Range

#RANGE AND FOR LOOP
def countdown1():
    for i in range(10, 0, -1):
        print(i, end =" ")

    print("Lift off")

countdown1()

#METHOD 2nd

# LIST AND FOR LOOP
number_list: list[int] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
def countdown2():
    for i in number_list:
        print(i, end=" ")

    print("Lift off")

countdown2()