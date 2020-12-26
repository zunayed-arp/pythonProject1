courses = ['History','Math','Physics','CompSci']

courses.insert(0,"Chemistry")
print(courses[2:])
print(courses)

print(courses.index('CompSci'))

for index,course in enumerate(courses):
    print(index, course)