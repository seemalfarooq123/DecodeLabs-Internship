import string

# Knowledge Base (Dictionary of responses)
responses = {
    "hello": "Hi there! 😊",
    "hi": "Hello! 👋",
    "hey": "Hey! 😊",
    "how are you": "I'm doing great! Thanks for asking 😊",
    "what is your name": "I am your AI chatbot 🤖",
    "who are you": "I am a rule-based chatbot created by Ayeza 😎",
    "what can you do": "I can chat with you using predefined rules!",
    "bye": "Goodbye! Have a nice day 👋",
}

print("🤖 Chatbot is running! Type 'exit' to stop.\n")

# Infinite loop
while True:
    # Take input
    user_input = input("You: ")

    # Clean input (lowercase + remove spaces)
    user_input = user_input.lower().strip()

    # Remove punctuation (?, !, etc.)
    user_input = user_input.translate(str.maketrans('', '', string.punctuation))

    # Exit condition
    if user_input == "exit":
        print("Bot: Goodbye! 👋")
        break

    # Get response from dictionary
    response = responses.get(user_input)

    # If exact match found
    if response:
        print("Bot:", response)
    else:
        # Partial matching (extra improvement 🔥)
        if "name" in user_input:
            print("Bot: I am your AI chatbot 🤖")
        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hello there! 😊")
        elif "how are you" in user_input:
            print("Bot: I'm doing great! 😊")
        else:
            print("Bot: Sorry, I don't understand that 🤔")