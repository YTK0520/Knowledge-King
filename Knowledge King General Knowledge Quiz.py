#!/usr/bin/env python
# coding: utf-8

# Question Bank:
# 
# 1. How many blue stripes are there on the U.S. flag?
# 
#     a) 6
# 
#     b) 7
# 
#     c) 13
# 
#     d) 0
# 
# 2. Which one of these characters is not friends with Harry Potter?
# 
#     a) Ron Weasley
# 
#     b) Neville Longbottom
# 
#     c) Draco Malfoy
# 
#     d) Hermione Granger
# 
# 3. Which animal does not appear in the Chinese zodiac?
# 
#     a) Dragon
# 
#     b) Rabbit
# 
#     c) Dog
# 
#     d) Hummingbird
# 
# 4. Which country held the 2016 Summer Olympics?
# 
#     a) China
# 
#     b) Ireland
# 
#     c) Brazil
# 
#     d) Italy
# 
# 5. What does the “D” in “D-Day” stand for?
# 
#     a) Dooms
# 
#     b) Dark
# 
#     c) Day
# 
#     d) Dunkirk
# 
# 6. What is the rarest blood type?
# 
#     a) O
# 
#     b) A
# 
#     c) B
# 
#     d) AB-Negative
# 
# 7. What language is the most spoken worldwide?
# 
#     a) Chinese
# 
#     b) Spanish
# 
#     c) Arabic
# 
#     d) English
# 
# 8. Which planet in our solar system is the largest?
# 
#     a) Jupiter
# 
#     b) Saturn
# 
#     c) Neptune
# 
#     d) Earth
# 
# 9. Which ocean is the largest?
# 
#     a) Indian
# 
#     b) Pacific
# 
#     c) Atlantic
# 
#     d) Arctic
# 
# 10. Which New York City building is the tallest:
# 
#     a) Empire State Building
# 
#     b) Bank of America Tower
# 
#     c) One World Trade Center
# 
#     d) Statue of Liberty

# In[44]:


import time
class questions:
    def __init__(self,score):
        self.score=score
    def ques(self,score):
        print("Q1: How many blue stripes are there on the U.S. flag?\n")
        print("a) 6\n\nb) 7\n\nc) 13\n\nd) 0\n")
        ans=str(input("Please input your answer(a/b/c/d):"))
        if ans=="d":
            print("Congratulations! Your answer is correct.")
            self.score+=score
        elif ans=="a" or ans=="b" or ans=="c":
            print("This is the wrong answer.\nThe correct answer is 'd'.")
        else:
            print("You input the wrong character.")
        print(f"Your current score:{self.score}\n")
        time.sleep(1)
        
        print("Q2: Which one of these characters is not friends with Harry Potter?\n")
        print("a) Ron Weasley\n\nb) Neville Longbottom\n\nc) Draco Malfoy\n\nd) Hermione Granger\n")
        ans=str(input("Please input your answer(a/b/c/d):"))
        if ans=="c":
            print("Congratulations! Your answer is correct.")
            self.score+=score
        elif ans=="a" or ans=="b" or ans=="d":
            print("This is the wrong answer.\nThe correct answer is 'c'.")
        else:
            print("You input the wrong character.")
        print(f"Your current score:{self.score}\n")
        time.sleep(1)
        
        print("Q3: Which animal does not appear in the Chinese zodiac?\n")
        print("a) Dragon\n\nb) Rabbit\n\nc) Dog\n\nd) Hummingbird\n")
        ans=str(input("Please input your answer(a/b/c/d):"))
        if ans=="d":
            print("Congratulations! Your answer is correct.")
            self.score+=score
        elif ans=="a" or ans=="b" or ans=="c":
            print("This is the wrong answer.\nThe correct answer is 'd'.")
        else:
            print("You input the wrong character.") 
        print(f"Your current score:{self.score}\n")
        time.sleep(1)
        
        print("Q4: Which country held the 2016 Summer Olympics?\n")
        print("a) China\n\nb) Ireland\n\nc) Brazil\n\nd) Italy\n")
        ans=str(input("Please input your answer(a/b/c/d):"))
        if ans=="c":
            print("Congratulations! Your answer is correct.")
            self.score+=score
        elif ans=="a" or ans=="b" or ans=="d":
            print("This is the wrong answer.\nThe correct answer is 'c'.")
        else:
            print("You input the wrong character.")
        print(f"Your current score:{self.score}\n")
        time.sleep(1)
        
        print("Q5: What does the “D” in “D-Day” stand for?\n")
        print("a) Dooms\n\nb) Dark\n\nc) Day\n\nd) Dunkirk\n")
        ans=str(input("Please input your answer(a/b/c/d):"))
        if ans=="c":
            print("Congratulations! Your answer is correct.")
            self.score+=score
        elif ans=="a" or ans=="b" or ans=="d":
            print("This is the wrong answer.\nThe correct answer is 'c'.")
        else:
            print("You input the wrong character.")
        print(f"Your current score:{self.score}\n")
        time.sleep(1)
        
        print("Q6: What is the rarest blood type?\n")
        print("a) O\n\nb) A\n\nc) B\n\nd) AB-Negative\n")
        ans=str(input("Please input your answer(a/b/c/d):"))
        if ans=="d":
            print("Congratulations! Your answer is correct.")
            self.score+=score
        elif ans=="a" or ans=="b" or ans=="c":
            print("This is the wrong answer.\nThe correct answer is 'd'.")
        else:
            print("You input the wrong character.")
        print(f"Your current score:{self.score}\n")
        time.sleep(1)
        
        print("Q7: What language is the most spoken worldwide?\n")
        print("a) Chinese\n\nb) Spanish\n\nc) Arabic\n\nd) English\n")
        ans=str(input("Please input your answer(a/b/c/d):"))
        if ans=="a":
            print("Congratulations! Your answer is correct.")
            self.score+=score
        elif ans=="b" or ans=="c" or ans=="d":
            print("This is the wrong answer.\nThe correct answer is 'a'.")
        else:
            print("You input the wrong character.")
        print(f"Your current score:{self.score}\n")
        time.sleep(1)
        
        print("Q8: Which planet in our solar system is the largest?\n")
        print("a) Jupiter\n\nb) Saturn\n\nc) Neptune\n\nd) Earth")
        ans=str(input("Please input your answer(a/b/c/d):"))
        if ans=="a":
            print("Congratulations! Your answer is correct.")
            self.score+=score
        elif ans=="b" or ans=="c" or ans=="d":
            print("This is the wrong answer.\nThe correct answer is 'a'.")
        else:
            print("You input the wrong character.")
        print(f"Your current score:{self.score}\n")
        time.sleep(1)
        
        print("Q9: Which ocean is the largest?\n")
        print("a) Indian\n\nb) Pacific\n\nc) Atlantic\n\nd) Arctic\n")
        ans=str(input("Please input your answer(a/b/c/d):"))
        if ans=="b":
            print("Congratulations! Your answer is correct.")
            self.score+=score
        elif ans=="a" or ans=="c" or ans=="d":
            print("This is the wrong answer.\nThe correct answer is 'b'.")
        else:
            print("You input the wrong character.")
        print(f"Your current score:{self.score}\n")
        time.sleep(1)
        
        print("Q10: Which New York City building is the tallest?\n")
        print("a) Empire State Building\n\nb) Bank of America Tower\n\nc) One World Trade Center\n\nd) Statue of Liberty\n")
        ans=str(input("Please input your answer(a/b/c/d):"))
        if ans=="c":
            print("Congratulations! Your answer is correct.")
            self.score+=score
        elif ans=="a" or ans=="b" or ans=="d":
            print("This is the wrong answer.\nThe correct answer is 'c'.")
        else:
            print("You input the wrong character.")
        print(f"Your total score:{self.score}\n")


# In[43]:


print("Welcome to the KNOWLEDGE KING !\nThis is a multiple choice general knowledge quiz.")
print("There will be 10 questions in this quiz.\nEach questions accounts for 10 points and the total score is 100.")
time.sleep(3)
a=questions(0)
a.ques(10)

