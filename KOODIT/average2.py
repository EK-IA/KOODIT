sum = 0.0
print("This program will take several numbers than average them")
count = int(input("How many numbers would you like to average:"))
current_count = 0
while current_count < count:
    current_count = current_count + 1
    print("Number", current_count)
    number = float(input("Enter a number:"))
    sum = sum + number
print("The average was:", sum / count)