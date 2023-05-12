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
        old_sum_Simulation = len(self.simulation)
        new_sum_Simulation = old_sum_Simulation+1
        wightOld = old_sum_Simulation / new_sum_Simulation
        wightNew = 1/new_sum_Simulation
        for key,value in self.skills.items():
            rank = (wightOld*int(self.skills[key])) + ((wightNew)*skill_array[i])
            self.skills[key] = str(int(rank)+1)
            i += 1