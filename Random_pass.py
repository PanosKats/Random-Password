import string
import random

# Lower and upercase letters ,numbers and punctuation for the password
Letters = string.ascii_letters
Numbers = string.digits
Puncuation = string.punctuation

def get_password_length() :
    '''
    So we will get the password  length from the  user but it can easily
    change if we want a certain length for sugested password lets say in 
    sign up page.
    The input always comes in string so we typecast in numeric 
    '''
    length = input("How long u want the password to be?")
    return int(length)

def pass_gen(length=8) :
    '''
    So we want to make the paassword.We must get letters, numbers,puncuation 
    get the code and shuffle it.I will also turn it to list cause i dont really like errors

    '''
      # create alphanumerical from string constants
    saveit = f'{Letters}{Numbers}{Puncuation}'

    # convert saveit from string to list and shuffle
    saveit = list(saveit)
    random.shuffle(saveit)

    # generate random password and convert to string
    random_password = random.choices(saveit, k=length)
    random_password = ''.join(random_password)
    return random_password



# testing password generator with it's default length of 8
password_one = pass_gen()

# testing password generator using user's input as length
password_length = get_password_length()
password_two = pass_gen(password_length)

print("Deafault password length (" + str(len(password_one)) + "):\t\t" + password_one )
print("password 2 (" + str(len(password_two)) + "):\t\t" + password_two )




    
