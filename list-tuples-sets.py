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
