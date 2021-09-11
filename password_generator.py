import string
import random

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
digits = string.digits
punc = string.punctuation

pass_len = int(input("Enter the length for the password: "))

lst = []

lst.extend(list(lower_case))
lst.extend(list(upper_case))
lst.extend(list(digits))
lst.extend(list(punc))

# Use this
print("".join(random.sample(lst, pass_len))) 
                                                     
# or this                     
random.shuffle(lst)                               
print("".join(lst[0:pass_len])) 
