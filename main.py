from random_user import RandomUser

# Create a new instance of the RandomUser class
user = RandomUser()
# Print the first name of the user
# print(user.get_first_name())

# Print the last name of the user
# print(user.get_last_name())

# # Print the full name of the user
# print(user.get_full_name())

# # Print the email name of the user
# print(user.get_email_name())

# # Print the email name of the user
# print(user.get_phone_name())

# # Print the location name of the user
# print(user.get_location_name())

# # Print the picture name of the user
# print(user.get_picture_name())
def static_metod():
    answer={
        "frist_name":user.get_first_name(),
        "last_name":user.get_last_name(),
        "full_name":user.get_full_name(),
        "email":user.get_email_name(),
        "phone":user.get_phone_name(),
        "picture":user.get_picture_name()
    }
    m=0
    list=[]
    user_name=5
    s=0
    while m<user_name:
        list.append(answer)
        m+=1
        s+=1
        print(s)
    return list
print(static_metod())