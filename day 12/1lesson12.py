Grade1 = int(input("Enter your grade 1/100: "))

if Grade1 > 90 and Grade1 < 100:
    print("თქვენ დაგიფინანსდებათ სწავლა.")

if Grade1 > 70 and Grade1 < 80:
    print("თქვენ დაგიფინანსდებათ სწავლა 1500 ლარით.")

if Grade1 > 40 and Grade1 < 70:
    print("თქვენ დაგიფინანსდებათ სწავლა 500 ლარით.")

if Grade1 < 40:
    print("თქვენ არ დაგიფინანსდებათ სწავლის პროცესი.")