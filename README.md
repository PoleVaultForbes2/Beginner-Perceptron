# Student Classifier with Backpropagation
This project demonstrates how a perceptron can evolve into a **logistic regression–style classifier** using **sigmoid activation** and **backpropagation**.  
It simulates how a model might classify students as first-year or not based on a few binary traits. The project is designed as an educational tool to help understand the transition from the simple perceptron learning rule to modern neural network training with gradient descent.

🧑‍💻 **Author**  
Josh Forbes  

📘 **Project Overview**  
The goal of this project is to predict whether a student is a first-year student based on certain attributes like:  
* Whether they have previous experience  
* Their gender  
* Whether they work hard  
* Whether they drink  

The model uses:  
* A linear combination of weighted inputs  
* A sigmoid activation function to output probabilities  
* A binary cross-entropy loss function  
* Backpropagation with gradient descent to update weights  

🧠 **How It Works**  

1.)  Each student is represented by a set of boolean features.  

2.)  A weight is assigned to each feature and adjusted during training.  

3.)  The perceptron calculates the weighted sum of features.  

4.)  The weighted sum is passed through the **sigmoid function**:  
~~~~~~~~~~~~~~~~~~~~~~~~~~~
σ(x) = 1 / (1 + e^(-x))
~~~~~~~~~~~~~~~~~~~~~~~~~~~  

This converts the sum into a probability between 0 and 1.  

5.)  Binary cross-entropy loss measures prediction error:  
~~~~~~~~~~~~~~~~~~~~~~~~~~~
L = -(y log(ŷ) + (1 - y) log(1 - ŷ))
~~~~~~~~~~~~~~~~~~~~~~~~~~~  

6.)  Backpropagation computes gradients of the loss with respect to each weight and updates them using gradient descent:  
~~~~~~~~~~~~~~~~~~~~~~~~~~~
w ← w - η * (ŷ - y) * x
~~~~~~~~~~~~~~~~~~~~~~~~~~~  

7.)  Over many epochs, the model refines its weights to minimize loss and improve classification accuracy.  

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
* Activation Function: Sigmoid  
* Loss Function: Binary Cross-Entropy  
* Initial Weights: Random small values  
* Bias: Random small value  
* Learning Rate: 0.1  
* Epochs: 5000 (configurable)  

🏃‍♂️ **Running the Program**  

Run the program with:  
~~~~~~~~~~~~~~~~~~~~~~~~~~~
python3 student_classifier.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The model will:  
* Train on the provided student dataset using backpropagation  
* Print training loss at intervals to show learning progress  
* Display final learned weights and bias  
* Test performance on both training and test groups  

💡 **Learning Highlights**  
This project illustrates:  
* The evolution from a simple perceptron rule to gradient-based learning  
* How the sigmoid function allows outputs to be interpreted as probabilities  
* The role of loss functions in guiding learning  
* The mechanics of backpropagation and gradient descent  
* Practical binary classification with a toy dataset  
