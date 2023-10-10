def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hello! How can I assist you?"
    elif "how are you" in user_input:
        return "I'm good, thank you! How about you?"
    elif "help" in user_input:
        return "I can help with various tasks. Just let me know what you need!"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I didn't understand. Can you please rephrase?"

def chatbot():
    print("ChatBot: Hello! How can I assist you?")

    while True:
        user_input = input("User: ")

        if user_input.lower() == "exit":
            print("ChatBot: Goodbye!")
            break

        bot_response = get_response(user_input)
        print("ChatBot:", bot_response)

# Run the chatbot
chatbot()