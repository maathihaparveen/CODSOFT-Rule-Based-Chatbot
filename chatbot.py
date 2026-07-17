print("====================================")
print(" Welcome to Rule-Based Chatbot ")
print(" Type 'bye' to exit")
print("====================================")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am doing great. Thank you!")

    elif user == "what is your name":
        print("Bot: My name is Rule-Based Chatbot.")

    elif user == "who created you":
        print("Bot: I was created using Python.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "what is python":
        print("Bot: Python is a popular programming language.")

    elif user == "what is machine learning":
        print("Bot: Machine Learning helps computers learn from data.")

    elif user == "what is chatbot":
        print("Bot: A chatbot is a computer program that talks with users.")

    elif user == "good morning":
        print("Bot: Good Morning! Have a wonderful day.")

    elif user == "good afternoon":
        print("Bot: Good Afternoon!")

    elif user == "good evening":
        print("Bot: Good Evening!")

    elif user == "good night":
        print("Bot: Good Night! Sweet dreams.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "thanks":
        print("Bot: Happy to help!")

    elif user == "what can you do":
        print("Bot: I can answer simple predefined questions.")

    elif user == "where are you from":
        print("Bot: I live inside your Python program!")

    elif user == "what is today's date":
        print("Bot: Sorry, I cannot tell the current date.")

    elif user == "tell me a joke":
        print("Bot: Why do programmers prefer Python? Because it's easy to read!")

    elif user == "who is your favourite teacher":
        print("Bot: Every teacher who shares knowledge is my favourite!")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand. Please ask another question.")