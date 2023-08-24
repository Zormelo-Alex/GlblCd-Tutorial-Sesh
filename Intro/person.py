def get_age():
	age = int(input("please enter your age \n"))
	return age

def get_name():
	name = input("please enter your name \n")
	return name

username = get_name()
user_age = get_age()

print("Hello", username, "you are", user_age, "years old")
