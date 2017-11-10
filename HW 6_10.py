# Home Work 09.11.17

print("Домашнее задание 2 09.11.17")

print()
print("--------------------------------------------------------------------------------------------------------------")

print("7. Преобразовать строку с американским форматом даты в европейский")
current_date = "11.09.2017"
print()
print(current_date)
lst = current_date.split(".")
mounth = lst[0]
day = lst[1]
year = lst[2]
new_format = day + "." + mounth + "." + year
print(new_format)
print("--------------------------------------------------------------------------------------------------------------")
print()

print("8. Написать программу, которая преобразует имя студента, ставя фамилию на первое место, а имя на второе.")
print()
student_old = "Oleksandr Makeiev"
print(student_old)
lst = student_old.split(" ")
name = lst[0]
surname = lst[1]
student_new = surname + " " + name
print(student_new)
print("--------------------------------------------------------------------------------------------------------------")
print()

print("9. Написать программу, которая преобразует имя переменной в формате snake_style в формат CamelizedStyle.\n Для простоты считаем, что имя переменной всегда состоит из 3-х слов.\n Например: ‘employee_first_name’ -> ‘EmployeeFirstName’")
print()
string = "employee_first_name"
print(string)
lst = string.split("_")
employee = lst[0]
first = lst[1]
name = lst[2]
result = employee.title() + first.title() + name.title()
print(result)
print("--------------------------------------------------------------------------------------------------------------")
print()

#---------------------------------------------------------------------------------------------------------------

#print("10. Дана строка Leonid Listyev*1956-05-10*1995-03-01.\n""Требуется написать программу, которая по переданной строке определит возраст писателя и вернет его имя и возраст.")
#print()
#text1 = 'Leonid Listyev*1956-05-10*1995-03-01'
#print(text1)
#name = str(text1[:14])
#print(name)
#year_of_birth = int(text1[15:19])
#print(year_of_birth)
#year_of_death = int(text1[26:30])
#print(year_of_death)
#age = year_of_death - year_of_birth
#age_print = str(age)
#print(age_print)
#result = name + " " + age_print
#print(result)

#----------------------------------------------------------------------------
print("Задание 10")
text = 'Leo Tolstoy*1828-08-28*1910-11-20'
print(text)
name = str(text[:11])
#print(name)
year_of_birth = int(text[12:16])
#print(year_of_birth)
year_of_death = int(text[23:27])
#print(year_of_death)
age = year_of_death - year_of_birth
age_print = str(age)
#print(age_print)
result = name + "," + " " + age_print
print(result)