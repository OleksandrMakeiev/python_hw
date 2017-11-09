# Home Work 09.11.17

print("1.	Преобразовать строку с американским форматом даты в европейский")
current_date= "11.09.2017"
print()
print(current_date)
lst = current_date.split(".")
mounth = lst[0]
day = lst[1]
year = lst[2]
new_format = lst[1]+ "." +lst[0]+ "."+lst[2]
print (new_format)
print("--------------------------------------------------------------------------------------------------------------")
print()


print("2.	Написать программу, которая преобразует имя студента, ставя фамилию на первое место, а имя на второе.")
print()
student_old = "Oleksandr Makeiev"
print(student_old)
lst = student_old.split(" ")
name = lst[0]
surname = lst[1]
student_new = lst[1]+ " "+lst[0]
print(student_new)
print("--------------------------------------------------------------------------------------------------------------")
print()


print("3.	Написать программу, которая преобразует имя переменной в формате snake_style в формат CamelizedStyle.\n Для простоты считаем, что имя переменной всегда состоит из 3-х слов.\n Например: ‘employee_first_name’ -> ‘EmployeeFirstName’")
print()
string1 = "employee_first_name"
print(string1)
lst = string1.split("_")
word1 = lst[0]
word2 = lst[1]
word3 = lst[2]
string2 =  lst[0].title() + lst[1].title() + lst[2].title()
print(string2)
print("--------------------------------------------------------------------------------------------------------------")
print()


print("4. Дана строка Leonid Listyev*1956-05-10*1995-03-01.\n""Требуется написать программу, которая по переданной строке определит возраст писателя и вернет его имя и возраст.")
print()
text1 = "Leonid Listyev*1956-05-10*1995-03-01"
print(text1)
name = str(text1[:14])
#print(name)
year_of_birth = int(text1[15:19])
#print(year_of_birth)
year_of_death = int(text1[26:30])
#print(year_of_death)
life = year_of_death - year_of_birth
life1 =str(life)
#print(life)
text2 = (name)+ " " +(life1)
print(text2)