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

print("Задание 10")
s = 'Leo Tolstoy*1828-08-28*1910-11-20'
lst = s.split('*')
print(lst)
name = s.split( "*")[0]
date1 = lst[1]
date2 = lst[2]
year1 = date1.split('-')[0]
year2 = date2.split('-')[0]
age = int(year2) - int(year1)
age_print = str(age)
result = name + "," + " " + age_print
print(result)