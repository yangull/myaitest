from datetime import datetime

def greet_user():
    name = input("What's your name? ")
    now = datetime.now()
    print(f"\n👋 Hello {name}!")
    print("✅ This message was printed from a Python script uploaded via VS Code to GitHub.")
    print("🕒 Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

greet_user()
