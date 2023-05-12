import openai

from Server.FlaskServer import get_client_agent_strongs


class InitUtil:
    @staticmethod
    def matching_customer(model_engine, db):
        agent_skills, client_personals, client_emotions = get_client_agent_strongs(db)
        request = f"""
I have a list of employee characteristics, in addition to that, I have a list of customer characteristics and a list of customer emotions.
given the characteristics of the employee, look for which characteristics he should improve on (the scale is from 1-10) and thus "match" a number to each of the client's characteristics so that the client will have characteristics that will "challenge" the agent, given the agent's list of characteristics. (For example with an agent he is intolerant, so match him with a tolerant client to challenge him).
agent_skills = {agent_skills}
possible client personals = {client_personals}
possible client emotions = {client_emotions}

Generate me the list of the wanted client personals and initial emotion

"""
        completion = openai.ChatCompletion.create(
            model=model_engine,
            messages=[{"role": "system", "content": request}]
        )
        response = completion['choices'][0]['message']['content']
        return response
