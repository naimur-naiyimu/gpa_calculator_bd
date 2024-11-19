from gpa_calculator_bd import calculate_gpa, calculate_cgpa, calculate_average

# Calculate GPA
gpa = calculate_gpa([4.0, 3.5], [3, 4])

# Calculate CGPA
cgpa = calculate_cgpa([3.5, 3.7], [15, 18])

# Calculate Average Marks
average = calculate_average([85, 90, 78])
gpa = round(gpa, 2)

print(gpa, cgpa, average)