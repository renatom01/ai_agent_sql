#importing functions 
from llm_function import answer_question


def main():
    
    """
    The main function serves a s the entry point and central execution unit for the SQL Agent Chatbot script. 
    The chatbot leverages the answer_question function to interpret user 
    queries and generate appropriate responses.

    Args:
        user_input (str): user input of the chatbot as string.

    Returns:
        string: answer of the chatbot.
    """
    
    
    print("SQL Agent Chatbot - Type 'exit' to end the conversation")

    while True:
        user_input = input("User: ")

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        chatbot_response = answer_question(user_input)
        print(f"Chatbot: {chatbot_response}")

if __name__ == "__main__":
    main()