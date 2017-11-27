# 22
string = input("Введите имена и фамилии студентов через запятую на английском языке (пример: John White, Gregory House, Jack Smith, Jay Z): ")
list_of_enrollees = string.split(",")

def group_by_surname(list_of_enrollees):

    enrollees_AtoI = 0
    enrollees_JtoP = 0
    enrollees_QtoT = 0
    enrollees_UtoZ = 0

    for enrollees in list_of_enrollees:
        surname = enrollees.split()[1][0]

        if 'A' <= surname.upper() <= 'I':
            enrollees_AtoI += 1
        elif 'J' <= surname.upper() <= 'P':
            enrollees_JtoP += 1
        elif 'Q' <= surname.upper() <= 'T':
            enrollees_QtoT += 1
        else:
            enrollees_UtoZ += 1

    return enrollees_AtoI, enrollees_JtoP, enrollees_QtoT, enrollees_UtoZ

group_by_surname(list_of_enrollees)
print("Количество абитуриентов в группе: \nA-I: %d\nJ-P: %d\nQ-T: %d\nU-Z: %d" % (group_by_surname(list_of_enrollees)))
