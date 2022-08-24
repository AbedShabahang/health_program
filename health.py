# compare healthy between two schools by drink milk or don't drink milk

# -------------------------------------- developer : abed shabahang
from statistics import mean

number_of_schools = 2
students_A = 0
students_B = 0
milk_in_class_A = None
milk_in_class_B = None
print("\n" + " This is a program that can examine two schools in terms of the impact of milk consumption on the physical health of students \t".strip() + "programmer : Abed Shabahang" .strip() + "\n")
for i in range(0, number_of_schools):
    name_of_class = "A" if i == 0 else "B"

    number_of_student = int(input("plz enter number of students in school " + str(name_of_class) + ":" + "\n "))
    milk_in_class = int(input("if use milk in school " + str(name_of_class) + " enter 1 else enter 0 :" + "\n "))
    list_age = list()
    list_height = list()
    list_weight = list()
    k = i
    if k == 0:
        students_A = number_of_student
        milk_in_class_A = milk_in_class

    else:
        students_B = number_of_student
        milk_in_class_B = milk_in_class

    print("now in school :", name_of_class, " ", "(number_of_students_A:", students_A, "", "milk_A:", milk_in_class_A, ") ",
          "(number_of_students_B:", students_B, "", "milk_B:", milk_in_class_B, ")")
    for j in range(0, 3):
        # --------------------------------------- list_A (age , height, weight)
        if k == 0 and j == 0:
            list_age_A = input(
                "plz enter ages of students in school " + str(name_of_class) + "\n" + "for example : 16 18 17" + "\n").split(" ")
            list_age_A = list(map(lambda x: int(x), list_age_A))
            mean_age_A = float(mean(list_age_A))
            # print("list_age_A:", list_age_A)

        elif k == 0 and j == 1:
            list_height_A = input("plz enter height of students in school " + str(name_of_class) + "\n" + "for example : 169 185 174" + "\n").split(" ")
            list_height_A = list(map(lambda x: int(x), list_height_A))
            mean_height_A = float(mean(list_height_A))
            # print("list_height_A:", list_height_A)

        elif k == 0 and j == 2:
            list_weight_A = input("plz enter weight of students in school " + str(name_of_class) + "\n" + "for example : 56 47 75" + "\n").split(" ")
            list_weight_A = list(map(lambda x: int(x), list_weight_A))
            mean_weight_A = float(mean(list_weight_A))
            # print("list_weight_A:", list_weight_A)
        # --------------------------------------- list_B (age , height, weight)
        if k == 1 and j == 0:
            list_age_B = input("plz enter ages of students in school " + str(name_of_class) + "\n" + "for example : 16 18 17" + "\n").split(" ")
            list_age_B = list(map(lambda x: int(x), list_age_B))
            mean_age_B = float(mean(list_age_B))
            # print("list_age_B:", "mean_age_B:", mean_age_B)

        elif k == 1 and j == 1:
            list_height_B = input("plz enter height of students in school " + str(name_of_class) + "\n" + "(for example : 165 182 173)" + "\n").split(" ")
            list_height_B = list(map(lambda x: int(x), list_height_B))
            mean_height_B = float(mean(list_height_B))
            # print("list_height_B :", list_height_B)

        elif k == 1 and j == 2:
            list_weight_B = input("plz enter weight of students in school " + str(name_of_class) + "\n" + "for example : 46 78 84" + "\n").split(" ")
            list_weight_B = list(map(lambda x: int(x), list_weight_B))
            mean_weight_B = float(mean(list_weight_B))
            # print("list_weight_B:", list_weight_B)


class Schools:
    count = 0

    def __init__(self, mean_age, mean_height, mean_weight, milk):
        self.mean_age = mean_age
        self.mean_height = mean_height
        self.mean_weight = mean_weight
        self.milk = milk


class School_A(Schools):

    def use_milk(self):
        if self.milk == 0:
            print("School A dont used milk for students")
            print("mean_age: %.1f" % self.mean_age)
            print("mean_height: %.1f" % self.mean_height)
            print("mean_weight: %.1f \n" % self.mean_weight)
        else:
            print("School A used milk for students")
            print("mean_age : %.1f" % self.mean_age)
            print("mean_height: %.1f" % self.mean_height)
            print("mean_weight: %.1f \n" % self.mean_weight)


class School_B(Schools):

    def use_milk(self):
        if self.milk == 0:
            print("School B dont used milk for students")
            print("mean_age: %.1f" % self.mean_age)
            print("mean_height: %.1f" % self.mean_height)
            print("mean_weight: %.1f" % self.mean_weight)
        else:
            print("School B used milk for students")
            print("mean_age : %.1f" % self.mean_age)
            print("mean_height: %.1f" % self.mean_height)
            print("mean_weight: %.1f" % self.mean_weight)


school_1 = School_A(mean_age_A, mean_height_A, mean_weight_A, milk_in_class_A)

school_2 = School_B(mean_age_B, mean_height_B, mean_weight_B, milk_in_class_B)
if mean_age_A == mean_age_B and mean_weight_A == mean_weight_B:
    print("Same")
elif mean_age_A == mean_age_B:
    if mean_weight_A > mean_weight_B:
        school_1.use_milk()
    else:
        school_1.use_milk()
else:
    school_1.use_milk()
    school_2.use_milk()

