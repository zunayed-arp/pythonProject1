courses = ['History','Math','Physics','CompSci']
courses_2 = ['Computer','Education']
print(courses[:])

courses.append("Art")
print(courses)
courses.insert(0,'Art')
print(courses)
print(courses)
courses.extend(courses_2)
print(courses)
courses.remove("History")
print(courses)
popped = courses.pop()

print(popped)
nums = [1, 5, 2, 4, 3]
sorted_courses = sorted(courses)
print(courses)
print(help(courses))

