from main_system import MainSystem


# Instance created
main_system = MainSystem()

print("Welcome to Attendance Record System.\nPlease enter you below credentials to proceed\n")
user_identification = input("Are you a admin or employee? ")
username = input("Enter your username: ")
password = input("Enter your password: ")
main_system.authenticate(designation=user_identification, username=username, password=password)

