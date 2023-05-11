from uuid import UUID


class Agent:

    def __init__(self,user_name,password,id=None,position=None,skills=None,simulation=None):
        self.id = id
        self.user_name = user_name
        self.password = password
        self.position = position
        self.skills = skills
        self.simulation = simulation

    def add_simulation(self,sim_id):
        self.simulation.append(sim_id)

    def update_skills(self, skill_array):
        i = 0
        for key,value in self.skills.items():
            self.skills[key] = str(skill_array[i])
            i += 1