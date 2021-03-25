#!/usr/bin/env python
# coding: utf-8

# In[12]:


import random


# In[13]:


word_list = ["tree", "flower", "car", "hobbies", "football", "palm", "picture", 
             "picture", "python", "data", "bootcamp", "ironhack", "computer", "berlin", "london"]


# In[14]:


random_word = random.choice(word_list)
word_len = len(random_word)    
underscore = ['_ '] * len(random_word)
guessed_correct_letters = []
guessed_letters = []
random_word_set = set(random_word)
set_guessed_letters = set()
life = 5


# In[15]:


print("Let's play Hangman: \n\n")

print("You have 5 lives. The word is", word_len, "letters long:", "_ "*len(random_word))


def print_underscore():
    print("")
    print(''.join([x+" " for x in underscore]))
    print("")

win = False
    
while life > 0 and win == False :
    print("")
    user_input_pre = input("What letter do you want to guess? ")
    
    if  user_input_pre.isdigit():
        print("\n{} is not a letter!".format(user_input_pre))
        continue
        
    user_input = user_input_pre.lower() #turn input into lower in case it's a capital letter
    
    if user_input in guessed_letters: #not only correct guessed letters, otherwise it doesnt recognize wrong duplicates
        print("\nYou've already tried the letter {}!".format(user_input))
        continue
    
    guessed_letters.append(user_input) #keep track of letters guessed    
        
    if user_input in random_word:
      
        for i, x in enumerate(random_word):
            if x == user_input:
                underscore[i] = user_input       
      
        print("\nWell Done! {} is in the word".format(user_input))
        print_underscore()
        guessed_correct_letters.append(user_input)
        set_guessed_letters = set(guessed_letters)
        if len(random_word_set.difference(set_guessed_letters)) == 0:
            print("Yay! You won. The word was {}".format(random_word))
            win = True
                        
    else: 
        
        life -= 1
        
        print("")
        print(user_input,"is not in this word... you have", life, "lives left")
        
        if life == 0:
            print("")
            print("You are out of lives...Game over :'(")

