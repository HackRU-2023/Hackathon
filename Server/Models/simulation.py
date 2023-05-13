import uuid
from datetime import datetime


class Simulation:
    summary = ""
    recording = ""

    def __init__(self, id, description, problem,training_skills, owner="123", status="error"):
        self.id = id
        datenow = datetime.datetime.now()
        self.date = datenow.strftime("%Y-%m-%d %H:%M:%S")
        self.description = description
        self.problem = problem
        self.training_skills = training_skills
        self.owner = owner
        self.status = status

    def template_json(self):
        str = {
            "id": self.id,
            "date": self.date,
            "company": self.description,
            "problem": self.problem,
            "training_skills": self.score,
            "summary": "",
            "recording": "",
            "owner": self.owner,
            "status": "error"
        }
        return str

    def update_sim_finish(self,summary,recording):
        self.summary = summary
        self.recording = recording
        self.status = "completed"

