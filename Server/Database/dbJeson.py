agent1 = {
    "id": 2736,
    "user_name": "intSer",
    "password": "123456",
    "position": "Worker at a home internet services company that provides router extensions for homes",
    "skills": {
        "listening": 7,
        "patience": 5,
        "empathy": 6,
        "professional": 7,
        "emotional management": 6,
        "coping with stressful situations": 4,
        "expressiveness": 5
    },
    "simulation": [
        1233,
        2334,
        4375
    ]
    }
agent2 = {
    "id": 7643,
    "user_name": "marketCel",
    "password": "123456",
    "position": "sales representative who sells internet packages and calls in a cellular company",
    "skills": {
        "listening": 7,
        "patience": 9,
        "empathy": 7,
        "professional": 5,
        "emotional management": 4,
        "coping with stressful situations": 4,
        "expressiveness": 8
    },
    "simulation": [
        4763,
        2356
    ],
    }

simulation1 = {
    "id": 1233,
    "date": "2023-05-11 19:18:40",
    "company": "hot",
    "problem": "network",
    "score": "Product knowledge;7",
    "recording": "transcription",
    "owner": 2736,
    "status": "error",
    }
simulation2 = {
    "id": 2334,
    "date": "2023-01-08 10:45:40",
    "problem": "network",
    "score": "Product knowledge;7",
    "recording": "transcription",
    "owner": 2736,
    "status": "completed",
    }

simulation3 = {
    "id": 4763,
    "date": "2023-01-08 10:45:40",
    "problem": "network",
    "score": "Product knowledge;7",
    "recording": "transcription",
    "owner": 7643,
    "status": "completed",
    }

simulation4 = {
    "id": 2356,
    "date": "2023-01-08 10:45:40",
    "subject": "network",
    "score": "Product knowledge;7",
    "recording": "transcription",
    "owner": 7643,
    "status": "completed",
    }

client_skills = {
    "personal": ["empathy", "patience","fast talk","stuttering speech","loud voice","weak voice",
                 "monotonous speech","rude", "stingy", "gentle", "assertive", "manipulative"],
    "emotion": ["CALM","ANGRY","HAPPY","SURPRISED","HOPEFUL","CONFUSED","DISAPPOINTED","NATURAL"]
}
agent_skills ={
    "skills": ["listening","patience","empathy","professional","emotional management","coping with stressful situations","expressiveness"]
}

template_simulation1 = {
    "subject": "Angry client",
    "personal": {
        "empathy": 2,
        "patience": 3,
        "fast talk": 5,
        "stuttering speech": 4,
        "loud voice": 8,
        "monotonous speech": 0,
        "rude": 10,
        "stingy": 2,
        "gentle": 1,
        "assertive": 5,
        "manipulative": 2
    },
    "emotion": ["CALM","ANGRY","HAPPY","SURPRISED","HOPEFUL","CONFUSED","DISAPPOINTED","NATURAL"]
}
template_simulation2 = {
    "subject" : "Usual client",
    "personal" : {
        "empathy": 5,
        "patience": 3,
        "fast talk": 1,
        "stuttering speech": 2,
        "weak voice": 8,
        "monotonous speech": 5,
        "rude": 1,
        "stingy": 2,
        "gentle": 9,
        "assertive": 3,
        "manipulative": 0
    }
}