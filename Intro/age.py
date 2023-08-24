tutorList = ["Andrea", "Tomi", "Kelvin"]
tutor = {}

def whatAge():
	for i in tutorList:
		ageInput = input(f"Hello {i}, what is your age?\n")
		tutor[i] = ageInput
	#print(tutor)
	for i in tutor:
		print(f"{i}, you are {tutor[i]} years old!")
	
	
whatAge()
