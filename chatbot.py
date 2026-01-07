
def chatbot():


    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi":
            print(" Hi! Nice to meet you ")

        elif user_input == "how are you":
            print(" I'm fine, thanks! How about you?")

        elif user_input == "bye":
            print(" Goodbye! Have a great day ")
            break

        else:
            print(" Sorry, I don't understand that.")


chatbot()
