Grade1 = int(input("Enter your grade 1/10: "))

if Grade1 == 10:
    print("Good job! The teacher will tell your mother that you did well.")

if Grade1 == 9 or Grade1 == 8:
    print("Teacher will talk to mother about your grade.")

if Grade1 == 5 or Grade1 == 6 or Grade1 == 7:
    print("The teacher will tell your mother that you did not do so well.")

if Grade1 < 5:
    print("Bad job. The teacher is kicking you out of the school.")
