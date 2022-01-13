import random

def ans(ask):
    """It receive the question and gives the answer if condition match."""
    extra = ["Hmmm","Oh","yes","I see","Tell me more","Like"]
    # it checks the condition and prints the answer
    if "library" in ask:
        print("The library is closed today.")
    elif "wifi" in ask:
        print("WiFi is excellent across the campus.")
    elif "deadline" in ask:
        print("Your deadline has been extended by two working days.")
    elif "coffee" in ask:
        print("Teekee is open until 9pm this evening.")
    elif "fee" in ask:
        print("Contact to the Administration.")
    elif "hoilday" in ask:
        print("You can ask to the SSD department.")
    else:
        print(random.choice(extra))

def chat(name):
    """It receive name and run the entire function."""
    name_rand= ["July","Anny","Harry","John","Maya","Jenifer"]
    network = [True,True,True,True,True,True,False]
    print(f"\nHi, {name}! Thank you, and Welcome to PopChat!")
    print(f"My name is {random.choice(name_rand)}, and it will be my pleasure to help you.")
    if random.choice(network) == False: #it checks the network connection
        print("*****NETWORK ERROR*****\n")
        exit()
    else:
        while True: # it will loop the program
            ask = input("--->")
            if ask == "bye" or ask == "exit" or ask == "help": # it exit the program if the condition match
                break
            else:
                ans(ask)
    print(f"Thanks, {name}, for using PopChat. See you again soon!\n")

def check_email(email,domain):
    """It receive the email and domain and check the email."""
    a = email.index("@")
    if email.count("@") >= 2: # it check the @ in email
        print("Invalid email")
    elif a < 3 : # it check the position of @ in email
        print("Invalid email")
    elif domain not in email: # it check the domain in email
        print("Domain doesn't match.")
    else:
        name = email[:a] # it extract the name from the email
        chat(name)

domain = "pop.ac.uk"
print("\nWelcome to Pop Chat")
print("One of our operators will be pleased to help you today.\n")
email = input("Please enter your Poppleton email address: ")
if email == "": 
    print("\nNo E-mail entered. Nothing to do.\n")
else:
    check_email(email,domain)  # it pass to check the email

