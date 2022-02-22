def average(mylist):
    total = sum(mylist)
    average = total / len(mylist)
    return average

points = [2, 3, 4]
average_score = average(points)
print(f"The average is: {average_score}")

