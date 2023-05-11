from abc import ABC, abstractmethod


class Simulator(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def start_simulation(self, company_description, emotions, personality, call_subject):
        pass

    @abstractmethod
    def generate_answer(self, simulation_id, question):
        pass

