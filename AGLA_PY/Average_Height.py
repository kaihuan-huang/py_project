student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

max_height =0
for h in student_heights:
  if h > max_height:
    max_height = h
print(f'Max = {max_height}.')

total_heights = 0
for height in student_heights:
  total_heights += height
print(f"Total height is {total_heights}.")

num_of_students = 0
for student in student_heights:
  num_of_students += 1
print(f'Total student is {num_of_students}.')

average_height = round(total_heights/num_of_students)
print(f'Average height is {average_height}.')