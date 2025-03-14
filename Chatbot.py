responses = {
    "hello": "Hi there! How can I assist you today?",
    "tell me about": "Could you specify what you'd like to know about?",
    "bye": "Goodbye! Have a great day!",
}

def get_bot_response(user_message):
    user_message = user_message.lower()  # Convert input to lowercase
    return responses.get(user_message, "I'm sorry, I don't understand that.")  # Default response

def main():
    print("Welcome to the chatbot! I am here for queries and assistance.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Chatbot:", get_bot_response("bye"))
            break  # Exit the loop
        else:
            print("Chatbot:", get_bot_response(user_input))

# Step 5: Exit the Program
if __name__ == "__main__":
    main()
                