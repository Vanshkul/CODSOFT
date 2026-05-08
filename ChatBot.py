def chatbot():
    while True:
        ui=input("YOU: ").lower().strip()
        if ui=="exit":
            print("ChatBot:GoodBye!")
            return
        elif "hello" in ui or "hi" in ui:
            print("ChatBot: Hi There! how can i help you today?")
        elif "who are you" in ui:
            print("ChatBot: I  am simple chat bot.following predefined rule")
        elif "what can you do" in ui:
            print("ChatBot: I can respond to spacific keywords using if-else logic!")
        elif "how are you" in ui:
            print("ChatBot: I'm fine! how are you?")
        elif "i am fine" in ui:
            print("ChatBot: Sounds good how may i help you?")
        elif "thank you" in ui:
            print("ChatBot:Its completely my plasure!!")
        elif "codsoft" in ui:
            print("CodSoft is a compony. It conduct online internship program if you want to know more about it plz visit https://www.codsoft.in/")
        else:
            print("Chatbot:I am sorry,I don't have rule defined for the querry yet.");
print("Chatbot:Hello! im rule based bot.(Type'quite' to stop)")
chatbot()
