import hashlib
import secrets
import time


class Simulation:

    def __init__(self, company_description, emotions, personality, call_subject):
        self.simulation_id = self.generate_id()
        self.company_description = company_description
        self.emotions = emotions
        self.call_subject = call_subject
        self.messages = []
        self.personality = personality
        self.possible_emotions = ["CALM", "ANGRY", "HAPPY", "SURPRISED", "HOPEFUL", "CONFUSED", "DISAPPOINTED",
                                  "NATURAL"]
        self.load_system()
        self.simulation_start_time = time.time()



    def load_system(self):
        content = f"""
        Welcome to the customer simulation. You will be playing the role of a customer in a phone call with a company. Here is some information to help you get started:

        - You are calling {self.company_description} for assistance or information.
        - The call subject is {self.call_subject}
        - Your initial emotions are: {self.emotions}.
        - Your personality is (Weak personality trait = 1 ... Strong personality trait = 10): {self.personality}.

        Please keep the following in mind as you respond to the company representative:

    
        - Try to be as clear and concise as possible. - If you feel like the conversation need to over say Thank you.
      
        - Make the answers short as possible.
        - Always make sure that all of your answer require the company representative to response.
        - It have to sound natural like a real person talking
        - Your responses will be converted to a voice message, so try to make them sound natural.
        - Respond based on your current emotions and personality.
        - Change your emotions based on the representative's responses.
        - In the end of your answer mention your current mood. for example   .... answer .... ְְְ*ANGRY*
        - In your answer include words that express your emotions.
        - Select the mood from the following list {str(self.possible_emotions)}
        - If you want to pause to express that something take time type (PAUSE)
        - Its important that you will answer short and natural as possible
        - Do not repeat on yourself!
        - Do not repeat on what the company representative said!
        """
        self.messages.append({"role": "system", "content": content})

    def generate_id(self):
        rand_bytes = secrets.token_bytes(16)
        hash_object = hashlib.sha256()
        hash_object.update(rand_bytes)
        hash_hex = hash_object.hexdigest()
        return hash_hex[:15]

    def extend_conversation(self, prompt, side):
        self.messages.append({"role": side, "content": prompt})

    def load_messages(self):
        return self.messages
