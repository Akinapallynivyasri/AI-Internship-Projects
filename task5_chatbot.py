print("🤖 Chatbot: Hello! Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if "hello" in user or "hi" in user:
        print("Bot: Hello! How can I help you?\n")

    elif "how are you" in user:
        print("Bot: I am doing great! 😊\n")

    elif "your name" in user:
        print("Bot: I am your AI chatbot.\n")

    elif "ai" in user:
        print("Bot: AI stands for Artificial Intelligence.\n")

    elif "time" in user:
        import datetime
        print("Bot: Current time is", datetime.datetime.now().strftime("%H:%M"), "\n")

    elif "college" in user:
        print("Bot: Hope you are enjoying your college life!\n")

    elif "thank" in user:
        print("Bot: You're welcome! 😊\n")

    elif "bye" in user:
        print("Bot: Goodbye! Have a great day 👋")
        break

    else:
        print("Bot: Sorry, I didn't understand that.\n")