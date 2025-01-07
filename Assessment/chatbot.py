import random

def generate_agent_name():
    agent_names = ["PoppletonBot", "PoppyBot", "Poppleton Assistant", "Poppleton Help"]
    return random.choice(agent_names)

def generate_random_response():
    responses = [
        "I can't answer that. Check the University portal, perhaps that will help.",
        "I don't understand.",
        "Sorry, you're not making sense to me.",
        "Hmm, let me think about that.",
    ]
    return random.choice(responses)

def main():
    greetings = ["Please state your name.", "What's your name?", "Hello there! What's your name?"]
    print(random.choice(greetings))
    user_name = input().strip()
    print(f"Nice to meet you, {user_name}! I'm {generate_agent_name()}, how can I help you?")

    while True:
        user_input = input().strip().lower()

        if user_input in ["bye", "quit", "exit"]:
            print("Goodbye!")
            break

        if any(word in user_input for word in ["hungry", "starving", "meal", "bite"]):
            responses = [
                "The campus cafe does nice pizza's. You should try it out.",
                "How about a burger or a pizza?",
                f"{user_name}, if you're hungry go eat something.",
                "There's plenty of food choices next to the University.",
                "The campus cafe sells tasty sandwiches. You should give it a try!",
                "You can join the cooking club.",
                "The campus cafe is open Mon-Fri from 8AM-5PM and on weekends it's open from 9AM-2PM"
            ]
            response = random.choice(responses)
        elif any(word in user_input for word in ["thirsty", "drink", "water", "coffee", "tea"]):
            responses = [
                "If you're thirsty, grab yourself a glass of water.",
                "How about going to the campus cafe? They do nice drinks",
                f"Staying hydrated is important {user_name}, Keep sipping water throughout the day.",
                "You could try a smoothie or a fresh juice.",
                "There's water fountains around the campus.",
                "The campus cafe is open Mon-Fri from 8AM-5PM and on weekends it's open from 9AM-2PM"
            ]
            response = random.choice(responses)
        elif any(word in user_input for word in ["gym", "health", "healthy", "fitness"]):
            responses = [
                "The gym is the best place to stay fit and healthy.",
                "You should go outdoors on a nice bike ride with Duncan. I've heard he's an excellent cyclist!",
                "The campus gym offers free fitness classes for students throughout the week. Check online for more info.",
                "Make sure to stay fit. It's important and your future self will thank you.",
                "The campus gym is available to all students and it's open on Mon-Fri from 8AM-4PM",
                "Make sure you stretch before working out."
            ]
            response = random.choice(responses)
        elif any(word in user_input for word in ["sports", "sport"]):
            responses = [
                "What's your favourite sport?",
                "Our university has teams for football, boxing, cricket, and more. Check online for more info",
                "Do you like sports?",
                "So what sports are you in to?"
            ]
            response = random.choice(responses)
        elif any(word in user_input for word in ["mma", "ufc", "mixed martial arts"]):
            responses = [
                "MMA is a very interesting sport",
                "Glad to hear you like MMA. It's my favourite sport",
                "Did you know the first UFC event was held with no weight classes or time limits?",
                "Our university doesn't have an MMA team, but we do have a boxing team that you can join."
            ]
            response = random.choice(responses)
        elif any(word in user_input for word in ["boxing"]):
            responses = [
                f"Our university has a great boxing team {user_name}! You should definitely join.",
                "The gym offers free boxing classes on Mondays and Tuesdays. You should try a session",
                "Boxing is an amazing sport",
                "If you want to join the boxing team then you must train at the campus boxing gym."
            ]
            response = random.choice(responses)
        elif any(word in user_input for word in ["football", "footy", "soccer"]):
            responses = [
                f"Well great news for you {user_name}, our university has a solid football team that you should definitely check out",
                "Loads of students from our university enjoy football and play it regularly. You should play a game next time.",
                f"Poppleton FC could definitely use you {user_name}. Make sure to check our team out and join.",
                "The trials for the football team are on the second Wednesday of every month at 9AM."
            ]
            response = random.choice(responses)
        elif any(word in user_input for word in ["basketball"]):
            responses = [
                f"Unfortunately {user_name}, the university doesn't have a basketball team due to the lack of interest.",
                "We don't have a basketball team, perhaps you could try to start and organise one.",
                "Basketball is fun!"
            ]
            response = random.choice(responses)
        elif any(word in user_input for word in ["cricket"]):
            responses = [
                "Our university has a cricket team. The trials are on the first Wednesday of every month at 9AM.",
                f"We have Poppleton Cricket Club, and we could definitely use you {user_name}."
            ]
            response = random.choice(responses)
        elif any(word in user_input for word in ["where", "lost"]):
            responses = [
                "Lost? Around the campus there's maps that'll help you locate yourself.",
                "If you're struggling to find your way around campus check the map online or the maps around campus."
            ]
            response = random.choice(responses)
        elif any(word in user_input for word in
                 ["study room", "quiet room", "study rooms", "quiet rooms", "group work"]):
            responses = [
                "Our university has study rooms for group work or focused study sessions. You can book one online or from the library.",
                "If you need a space to work with classmates or on your own, the study rooms are a great option.",
            ]
            response = random.choice(responses)
        elif any(word in user_input for word in ["book", "books", "reading time", "library"]):
            responses = [
                "The library has a wide selection of books on every subject. You can find textbooks, novels, and even research papers.",
                "Don’t forget to borrow books for your assignments. The library has all the required books for your courses.",
                "The university library also has a great collection of fiction books. You should check them out when you need a break.",
                "The library is a great place for studying and finding all the resources you need for your courses.",
                "You can find a quiet space in the library to focus on your work.",
                "Don't forget that the library also offers online resources for your research if you can't find what you're looking for.",
                "The library is open Mon-Fri from 8AM-5PM and on the weekend its open from 9AM-2PM."
            ]
            response = random.choice(responses)
        elif any(word in user_input for word in ["career", "careers", "job", "jobs"]):
            responses = [
                "Our campus has career fairs every December and February where you can meet potential employers and learn about job opportunities.",
                "If you're looking for work experience or for a job, check the university portal for job postings.",
                "If you need help writing a CV the university has a template and guide online that you can use to help you!",
                "If money is a concern then you can apply for the student finance. Speak to the library desk or check online for more info"
            ]
            response = random.choice(responses)
        elif any(word in user_input for word in ["dorm", "dorms", "accommodation"]):
            responses = [
                "If you're interested in our accommodation then check the accommodation page on the University website.",
                "Our university offers accommodation on the campus with both shared and private rooms available.",
                "If you'd prefer to live off campus, there are plenty of nearby options.",
                "If you live far away from campus, you can find accommodation close to, or on the campus to make travelling easier."
            ]
            response = random.choice(responses)
        elif any(word in user_input for word in
                 ["clubs", "societies", "extracurricular activities", "hobbies", "socialise"]):
            responses = [
                "We have clubs for everything from photography to debating to video gaming.",
                "Joining a club or a society is a good way to make friends and explore your interests."
            ]
            response = random.choice(responses)
        else:
            response = generate_random_response()

        print(response)

if __name__ == "__main__":
    main()
