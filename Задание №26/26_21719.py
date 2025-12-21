file = open("26_21719.txt")

N = int(file.readline())
lines = [[int(x) for x in line.split()] for line in file.readlines()]

students_tasks = {}
for x in lines:
    id, task = x
    if id in students_tasks:
        students_tasks[id].add(task)
    else:
        students_tasks[id] = set()
        students_tasks[id].add(task)

for key in students_tasks:
    students_tasks[key] = sorted(students_tasks[key])

max_len = 0
student_id = -1
for key in students_tasks:
    tasks = students_tasks[key]

    current_len = 1
    for i in range(len(tasks) - 1):
        if tasks[i] == tasks[i + 1] - 2:
            current_len += 1
        else:
            if current_len > max_len or (current_len == max_len and key < student_id):
                max_len = current_len
                student_id = key
            current_len = 1
    if current_len > max_len:
        max_len = current_len
        student_id = key
    
print(student_id, max_len)
