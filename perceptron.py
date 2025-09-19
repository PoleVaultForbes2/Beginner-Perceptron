import math
import random

# Class of students with 4 attributes to determine Honors
class Student:
    def __init__(self, name, prev, male, workHard, drink, firstYear):
        self.name = name
        self.prev = prev
        self.male = male
        self.workHard = workHard
        self.drink = drink
        self.firstYear = int(firstYear)  # ensure it's 0 or 1


# Training set
students_list = [
    Student("Richard", True, True, False, True, False),
    Student("Alan", True, True, True, False, True),
    Student("Alison", False, False, True, False, False),
    Student("Jeff", False, True, False, True, False),
    Student("Gail", True, False, True, True, True),
    Student("Simon", False, True, True, True, False)
]

# Testing Set (Custom so not really any relevance)
test_student_list = [
    Student("Kyle", True, True, False, False, True),
    Student("Sharon", True, True, False, False, True),
    Student("Emily", False, False, False, False, False),
    Student("Braden", True, True, False, True, False),
    Student("Bob", False, True, True, False, True),
    Student("Darron", False, True, True, True, False),
]

# Initialize weights randomly
weights = {
    'prev': random.uniform(-1, 1),
    'male': random.uniform(-1, 1),
    'workHard': random.uniform(-1, 1),
    'drink': random.uniform(-1, 1)
}
bias = random.uniform(-1, 1)

learning_rate = 0.1
epochs = 5000   # number of training passes


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# Testing the weights to aquire t/f for honors
def forward(student):
    """Forward pass: weighted sum -> sigmoid activation"""
    z = bias
    for attr in weights:
        z += weights[attr] * int(getattr(student, attr))
    return sigmoid(z)


def train():
    global bias
    for epoch in range(epochs):
        total_loss = 0
        for student in students_list:
            # Forward pass
            y_hat = forward(student)
            y_true = student.firstYear

            # Loss (binary cross entropy)
            loss = -(y_true * math.log(y_hat + 1e-8) + (1 - y_true) * math.log(1 - y_hat + 1e-8))
            total_loss += loss

            # Backpropagation (gradient descent update)
            error = y_hat - y_true
            for attr in weights:
                weights[attr] -= learning_rate * error * int(getattr(student, attr))
            bias -= learning_rate * error

        # Print progress every 500 epochs
        if epoch % 500 == 0:
            print(f"Epoch {epoch}, Loss = {total_loss:.4f}")


# Testing 
def test_group(group):
    correct = 0
    for student in group:
        prob = forward(student)
        prediction = 1 if prob >= 0.5 else 0
        if prediction == student.firstYear:
            correct += 1
    return correct, len(group)


def main():
    print("Training with backpropagation...")
    train()

    print("\nFinal weights:")
    print(weights)
    print("Bias:", bias)

    print("\nTesting on training data:")
    correct, total = test_group(students_list)
    print(f"Accuracy: {correct}/{total}")

    print("\nTesting on test data:")
    correct, total = test_group(test_student_list)
    print(f"Accuracy: {correct}/{total}")


if __name__ == "__main__":
    main()
