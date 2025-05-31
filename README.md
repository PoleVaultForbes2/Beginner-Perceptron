# Perceptron Simulation: Student Classifier
This project demonstrates a basic perceptron algorithm by simulating how it might classify students based on a few binary traits. It is designed as an educational tool to help understand the core mechanics of perceptron learning.

🧑‍💻 **Author**

Josh Forbes

📘 **Project Overview**
The goal of the perceptron is to predict whether a student is a first-year student based on certain attributes like:
* Whether they have previous experience
* Their gender
* Whether they work hard
* Whether they drink

The model uses a simple linear combination of weighted inputs and a threshold to make predictions, then adjusts the weights when a misclassification occurs.

🧠 **How It Works**

1.)  Each student is represented by a set of boolean features.

2.)  A weight is assigned to each feature.

3.)  The perceptron calculates the weighted sum of features.

4.)  If the sum is above a threshold, it predicts "first-year student".

5.)  If the prediction is incorrect, weights are updated using the perceptron learning rule.

🧪 **Dataset**

Training Students
~~~~~~~~~~~~~~~~~~~~~~~~~~~
students_list = [
    Student("Richard", True, True, False, True, False),
    Student("Alan", True, True, True, False, True),
    Student("Alison", False, False, True, False, False),
    Student("Jeff", False, True, False, True, False),
    Student("Gail", True, False, True, True, True),
    Student("Simon", False, True, True, True, False)
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Test Students
~~~~~~~~~~~~~~~~~~~~~~~~~~~
test_student_list = [
    Student("Kyle", True, True, False, False, True),
    Student("Sharon", True, False, False, False, True),
    Student("Emily", False, False, False, False, False),
    Student("Braden", True, True, False, True, True),
    Student("Bob", False, True, True, False, True),
    Student("Darron", False, True, True, True, False)
]
~~~~~~~~~~~~~~~~~~~~~~~~~~~

⚙️ **Features & Parameters**
* Initial Weights: {'prev': 2, 'male': 2, 'workHard': 2, 'drink': 2}
* Threshold: 6.0
* Learning Rate (change): 0.5

🏃‍♂️ **Running the Program**

Run the program with:
~~~~~~~~~~~~~~~~~~~~~~~~~~~
python3 perceptron_sim.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~
You will be prompted to add more students with boolean inputs (true or false) for each trait.

The perceptron will:
* Learn weights based on the provided student data.
* Stop when all training data is correctly classified.
* Test the learned weights on a separate test set.

💡 **Learning Highlights**
This project illustrates:
* The fundamentals of binary classification
* How weight adjustment helps correct model errors
* The importance of thresholding in activation
* The learning loop of perceptrons
