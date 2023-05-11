import openai
from Server.Simulator.Simulation import Simulation
from Server.Simulator.Simulator import Simulator


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
        """
        completion = openai.ChatCompletion.create(
            model=self.model_engine,
            messages=[{"role": "system", "content": request + f'\nHere is the full simulation: {conversation}'}]
        )
        response = completion['choices'][0]['message']['content']
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
        return response, "NATURAL"
