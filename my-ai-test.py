from datetime import datetime

def greet_user():
    name = input("What's your name? ")
    now = datetime.now()
    print(f"\n👋 Hello {name}!")
    print("✅ This msage as printed from a Python script uploaded via VS Code to GitHub.")
    print("🕒 Current dt and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

greet_user()
