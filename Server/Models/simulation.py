import uuid
from datetime import datetime


class Simulation:
    score = ""
    recording = ""

    def __init__(self,description, problem, owner, status="error"):
        self.id = int(uuid.uuid4().int) % (10 ** 4)
        datenow = datetime.datetime.now()
        self.date = datenow.strftime("%Y-%m-%d %H:%M:%S")
        self.description = description
        self.problem = problem
        self.owner = owner
        self.status = status

    def template_json(self):
        str = {
            "id": self.id,
            "date": self.date,
            "company": self.description,
            "problem": self.problem,
            "score": "",
            "recording": "",
            "owner": self.owner,
            "status": "error"
        }
        return str

