from datetime import datetime

print("================================")
print("        BASIC CHATBOT")
print("================================")
print("Hello! I am a simple Python chatbot.")
print("You can chat with me or type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hello", "hi", "hey", "hii", "helo"]:
        print("Bot: Hello! How are you?")

    elif user_input in [
        "how are you",
        "how are you doing",
        "how r u",
        "how are u"
    ]:
        print("Bot: I'm doing good! Thanks for asking. How are you?")

    elif user_input in [
        "i am good",
        "iam good",
        "i'm good",
        "i am doing good",
        "iam doing good",
        "i'm doing good",
        "good",
        "fine",
        "i am fine",
        "iam fine",
        "i'm fine",
        "great",
        "i am great",
        "i'm great"
    ]:
        print("Bot: That's great to hear!")

    elif user_input in [
        "i am bad",
        "iam bad",
        "i'm bad",
        "not good",
        "i am not good",
        "i'm not good",
        "sad",
        "i am sad",
        "i'm sad"
    ]:
        print("Bot: I'm sorry to hear that. I hope your day gets better!")

    elif user_input in [
        "what is your name",
        "what's your name",
        "your name",
        "who are you"
    ]:
        print("Bot: I'm a simple Python chatbot.")

    elif user_input in [
        "what can you do",
        "what do you do",
        "help",
        "what are your features"
    ]:
        print("Bot: I can have a simple conversation, tell you the current time, and respond to common questions.")

    elif user_input in [
        "what time is it",
        "what is the time",
        "tell me the time",
        "current time"
    ]:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: The current time is", current_time)

    elif user_input in [
        "thank you",
        "thanks",
        "thank u",
        "thx"
    ]:
        print("Bot: You're welcome!")

    elif user_input in [
        "good morning",
        "morning"
    ]:
        print("Bot: Good morning! Have a great day!")

    elif user_input in [
        "good afternoon",
        "afternoon"
    ]:
        print("Bot: Good afternoon! How is your day going?")

    elif user_input in [
        "good evening",
        "evening"
    ]:
        print("Bot: Good evening! Hope you're having a nice day.")

    elif user_input in [
        "good night",
        "night"
    ]:
        print("Bot: Good night! Sleep well.")

    elif user_input in [
        "what are you doing",
        "what r u doing",
        "what are u doing"
    ]:
        print("Bot: I'm here chatting with you!")

    elif user_input in [
        "who made you",
        "who created you",
        "who developed you"
    ]:
        print("Bot: I was created as a basic Python chatbot project.")

    elif user_input in [
        "nice to meet you",
        "nice meeting you"
    ]:
        print("Bot: Nice to meet you too!")

    elif user_input in [
        "bye",
        "goodbye",
        "see you",
        "see you later",
        "exit",
        "quit"
    ]:
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: I'm not sure how to respond to that yet.")