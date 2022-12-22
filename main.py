from random_user import RandomUser
import pprint

# Create a new instance of the RandomUser class
user = RandomUser()
def static_method(num_users):
    answer={
        "first_name":user.get_first_name(),
        "last_name":user.get_last_name(),
        "full_name":user.get_full_name(),
        "email":user.get_email(),
        "phone":user.get_phone(),
        "picture":user.get_picture()
        
    }


    s=0
    m=0
    n=[]
    while m!=num_users:
        m+=1
        n.append(answer)
        s+=1
        print(s)
    return n

pprint.pprint(static_method(5))