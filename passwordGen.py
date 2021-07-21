import string
import random
def password_gen():
    lo_wer = random.sample(string.ascii_lowercase,2)
    up_per = random.sample(string.ascii_uppercase,2)
    num  = random.sample(string.digits,2)
    punc = random.sample(string.punctuation,2)
    all = lo_wer + up_per + num + punc
    temp = random.sample(all,8)
    password = "".join(temp)
    print(password)
password_gen()    
