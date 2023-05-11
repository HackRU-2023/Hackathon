import hashlib
import secrets


class Simulation:

    def __init__(self, company_description, emotions, personality, call_subject):
        self.simulation_id = self.generate_id()
        self.company_description = company_description
        self.emotions = emotions
        self.call_subject = call_subject
        self.messages = []
        self.personality = personality
        self.load_system()

    def load_system(self):
        content = f"""
        Welcome to the customer simulation. You will be playing the role of a customer in a phone call with a company. Here is some information to help you get started:

        - You are calling {self.company_description} for assistance or information.
        - The call subject is {self.call_subject}
        - Your initial emotions are: {self.emotions}.
        - Your personality is: {self.personality}.

        Please keep the following in mind as you respond to the company representative:

    
        - Try to be as clear and concise as possible. - If you feel like the conversation need to over say Thank you.
      
        - Make the answers short as possible.
        - Always make sure that all of your answer require the company representative to response.
        - It have to sound natural like a real person talking
        - Your responses will be converted to a voice message, so try to make them sound natural.
        - Respond based on your current emotions and personality.
        - Change your emotions based on the representative's responses.
        - In the end of your answer mention your current mood. for example   .... answer .... (ANGRY)
        - If you want to pause to express that something take time type (PAUSE)
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
