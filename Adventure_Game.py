'''
Write a fun Python script that takes the user on a fun adventure by choosing different options for the path.
'''
name = str(input("Enter Your Name\n"))
print(f"{name} you are stuck in a forest. Your task is to get out from the forest without dieing")
print("You are walking threw forest and suddenly a wolf comes in your way. Now You have two options.")
print("1.Run 2. Climb The Nearest Tree ")
user = int(input("Choose one option 1 or 2"))
if user==1:
    print("You Died!!")
elif user==2:
    print("You Survived!!")
else:
    print("Incorrect Input")

#### Add a loop and increase the story as much as you can