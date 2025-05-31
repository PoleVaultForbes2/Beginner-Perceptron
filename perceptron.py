class Student:
    def __init__(self, name, prev, male, workHard, drink, firstYear):
        self.name = name
        self.prev = prev
        self.male = male
        self.workHard = workHard
        self.drink = drink
        self.firstYear = firstYear


students_list = [
    Student("Richard", True, True, False, True, False),
    Student("Alan", True, True, True, False, True),
    Student("Alison", False, False, True, False, False),
    Student("Jeff", False, True, False, True, False),
    Student("Gail", True, False, True, True, True),
    Student("Simon", False, True, True, True, False)
]

test_student_list = [
    Student("Kyle", True, True, False, False, True),
    Student("Sharon", True, False, False, False, True),
    Student("Emily", False, False, False, False, False),
    Student("Braden", True, True, False, True, True),
    Student("Bob", False, True, True, False, True),
    Student("Darron", False, True, True, True, False),
]

weights = {
    'prev': 2,
    'male': 2,
    'workHard': 2,
    'drink': 2
}

threshold = 6.0
change = 0.5


def adjust_weights(student, multiplier):
    for attr in ['prev', 'male', 'workHard', 'drink']:
        if getattr(student, attr):
            weights[attr] += multiplier * change


def check_student(student):
    total = 0
    for attr in ['prev', 'male', 'workHard', 'drink']:
        if getattr(student, attr):
            total += weights[attr]

    is_first = total >= threshold

    if is_first == student.firstYear:
        return True
    else:
        adjust_weights(student, -1 if is_first else 1)
        return False


def test(student):
    total = 0
    for attr in ['prev', 'male', 'workHard', 'drink']:
        if getattr(student, attr):
            total += weights[attr]

    is_first = total >= threshold

    if is_first == student.firstYear:
        return True
    else:
        return False


def main():
    print("Welcome to the perceptron demonstration, there are 6 students in the list so far.")
    while True:
        user_input = input("Would you like to add another student? (yes or no): ")
        if user_input.lower() == "no":
            break
        else:
            #prompts for the input
            prompts = [
                ("name", str),
                ("prev", bool),
                ("male", bool),
                ("workHard", bool),
                ("drink", bool),
                ("firstYear", bool)
            ]
            #for each prompt ask the user for input and store in student_data
            student_data = {}
            for prompt, data_type in prompts:
                user_input = input(f"What is the {prompt}: ")
                student_data[prompt] = data_type(user_input.lower() == "true")

            new_student = Student(**student_data)
            students_list.append(new_student)

    length = len(students_list)

    while True:
        num_correct = 0
        for student in students_list:
            if check_student(student):
                num_correct += 1

        print(weights)
        if num_correct == length:
            print("The perceptron found weights that work for all the students! These are the values:")
            print(weights)

            print("Let's test the other students now")
            num_pass = 0
            for student in test_student_list:
                if test(student):
                    num_pass += 1
            if num_pass == len(test_student_list):
                print("The weights worked for the test group!")
            else:
                print("The weights didn't work for the test group.")

            break


main()
