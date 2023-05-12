import time

import openai
from Server.Simulator.Simulation import Simulation
from Server.Simulator.Simulator import Simulator
from Server.Models.simulation import Simulation as save_sim


class OpenAISimulator(Simulator):

    def __init__(self):
        super().__init__()
        self.model_engine = "gpt-3.5-turbo"
        self.openai_api_key = "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"
        self.connect()
        self.simulations = {}

    def connect(self):
        openai.api_key = self.openai_api_key

    def start_simulation(self, company_description, emotions, personality, call_subject):
        simulation = Simulation(company_description, emotions, personality, call_subject)
        training_skills = simulation.personality + simulation.emotions
        save_simulation = Simulation(simulation.simulation_id,company_description, company_description,training_skills, owner)

        self.simulations[str(simulation.simulation_id)] = simulation
        return str(simulation.simulation_id)

    def review_simulation(self, simulation_id):
        simulation = self.simulations[simulation_id]
        conversation = simulation.messages
        request = """
        I have simulation that finished, In the simulation there is an AI which called (assistant) and Agent which called (user)
        The mission for the AI described in the simulation.
        Your mission is to give the Agent review how did he acted during the phone call.
        Start which giving a general review. after that rank the agent in all of the following categories from 1 to 10 ["listening","patience","empathy","professional","emotional management","coping with stressful situations","expressiveness"]
        Here is 
        __________ format example _______________
        Overall, the Agent provided good customer service during the phone call. They were able to listen to the customer's issue and suggest some solutions. The agent also remained calm and professional throughout the call
        
        Rankings:
        - Listening: 8
        - Patience: 7
        - Empathy: 7
        - Professional: 9
        - Emotional management: 8
        - Coping with stressful situations: 8
        - Expressiveness: 7
        __________________________________________
        
        Follow those Rules:
        - Do not mention the words user and assistant in the response
        """
        completion = openai.ChatCompletion.create(
            model=self.model_engine,
            messages=[{"role": "system", "content": request + f'\nHere is the full simulation: {conversation}'}]
        )
        response = f"- Initial mood: {simulation.emotions}\n- Simulation Time: {time.time() - self.simulations[simulation_id].simulation_start_time}\n- Review:\n" + \
                   completion['choices'][0]['message']['content']
        return response

    def generate_answer(self, simulation_id, question):
        simulation = self.simulations[simulation_id]
        simulation.extend_conversation(question, 'user')
        current_situation = simulation.load_messages()
        completion = openai.ChatCompletion.create(
            model=self.model_engine,
            messages=current_situation
        )
        response = completion['choices'][0]['message']['content']
        simulation.extend_conversation(response, 'assistant')
        try:
            emotion = response.split("*")[-2]
            answer = response.split("*")[0]
            if emotion not in simulation.possible_emotions:
                emotion = 'NATURAL'

            return answer, emotion
        except Exception as ex:
            for emo in simulation.possible_emotions:
                if emo in response:
                    answer = response.replace(emo, " ")
                    emotion = emo
                    return answer, emotion
            return response, 'NATURAL'
