# Python-Libraries
This is the most important feature of the NumPy library. It is the homogeneous array object. We perform all the operations on the array elements. The arrays in NumPy can be one dimensional or multidimensional. using Python NumPy and Pandas libraries (Import NumPy as np and Pandas as pd) Given the following piece of code to create a NumPy array, anIntArray: anIntArray = np.random.randint(5, 72, 48) Add Python code to convert this array into a Pandas series and then extract values stored at the positions 0, 5, 10, 15, 20 of the series. numpy.random.randint() is one of the functions for doing random sampling in numpy. it runs between the given range upto a given size. numpy.take() returns elements from an array along the mentioned indices.

import random module and generate random numbers between 1 and 3 using randint function from random module. store the random number in variable num
If num is 1 then computer_choice is "rock" , if num is 2 then computer_choice is "paper" and if num is 3 then computer_choice is "scissors"
Prompt user to enter choice using input function and store the user response in variable user_choice.
Define a loop with condition - user_choice is the same as computer_choice.
While loop will continue to run till user_choice is the same as computer_choice.
Inside while loop again generates a random number and gets computer_choice from this random number.
Print computer choice
If user_choice is equal to "rock" and computer_choice is equal to "scissors" or computer_choice is equal to "rock" and user_choice is equal to "scissors" then print - Rock smashes the scissors.Rock wins!! and store result = "rock"
If above condition is false then check if user_choice is equal to "scissors" and computer_choice is equal to "paper" or computer_choice is equal to "scissors" and user_choice is equal to "paper" then print - Scissors cuts paper.Scissors wins!! and store result = "scissors".
If both the conditions are false then  print - Paper wraps rock.Paper wins!! and store result = "paper"
Now check if the result is equal to computer_choice then print "Computer wins!!" and if the result is not equal to computer_choice then it means it is equal to user_choice so print "User wins!!"


A tuple is a container which holds a series of comma separated values (items or elements) between parentheses such as an (x, y) co-ordinate. Tuples are like lists, except they are immutable (i.e. you cannot change its content once created) and can hold mixed data types.
If there is a list, we can delete from the list and add some more elements to the list. Whereas if we take a tuple, it can't be changed.                              Tuple() is an immutable data type in python. Which means we can't modify the elements of a tuple i.e to add or delete its element. List is mutable while Tuple is immutable in python so to add "Opel" to our tuple 'Cars', we will first convert it into list using list() then we will append "Opel" to the list. Againt convert the list back to tuple using tuple() and finally print the tuple named as cars.

