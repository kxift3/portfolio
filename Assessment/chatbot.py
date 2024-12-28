import random

def chatbot():
    greetings = ["What’s your name?", "Hello there, who are you?", "Who speaks?"]
    user_name = input(random.choice(greetings))
    print(f"Hi {user_name}, nice to meet you!")

    agent_names = ["Kaif", "Farhan", "Rayyan", "Saahil", "Mateen", "Samyan", "Nouman", "Ifzaan"]
    agent_name = random.choice(agent_names)

    print(f"My name is {agent_name}. How can I help you?")
    print("You can ask me anything. Type 'exit', 'bye', 'goodbye', 'safe', or 'do one' to end this conversation.")

    while True:
        user_input = input(f"{user_name}: ").lower()

        if user_input in ["quit", "exit", "bye", "goodbye", "safe", "do one"]:
            print(f"{agent_name}: Goodbye, {user_name}!")
            break
        elif "coffee" in user_input or "thirsty" in user_input or "drink" in user_input:
            print(f"{agent_name}: The coffee bar is open from 8 AM to 6 PM.")
            print(f"{agent_name}: I recommend the Vanilla Latte from the coffee bar.")
        elif "food" in user_input or "hungry" in user_input:
            food_response = random.choice([
                "I recommend Jollibee in Leeds City Centre.",
                "You can try Mahmoods. It's next to Leeds City University."
            ])
            print(f"{agent_name}: {food_response}")
        elif "library" in user_input:
            print(f"{agent_name}: The library is open from 8 AM to 6 PM.")
            print(f"{agent_name}: If you're struggling to find a book, check the online library, it's available 24/7.")
        elif "sports" in user_input or "gym" in user_input or "health" in user_input:
            sports_response = random.choice([
                "The sports centre is open from 6 AM to 10 PM.",
                "Why don't you go on a bike ride with Duncan? He's an amazing cyclist."
            ])
            print(f"{agent_name}: {sports_response}")
        else:
            print(f"{agent_name}: I’m not sure about that, {user_name}. Can you ask something else?")

chatbot()
