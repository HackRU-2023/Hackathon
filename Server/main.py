from Server.FlaskServer import load_config_file
from Server.Utils.Voice import Voice
from Simulator.OpenAISimulator import OpenAISimulator
import time


simulator = OpenAISimulator()
simulation_id = simulator.start_simulation('A company that provide internet', "Angry",
                                           "{Cheap:10, Friendly : 4}",
                                           "He paying for 100mb internet but only get 5mb after internet check")


answer = simulator.generate_answer(simulation_id, "Hello, how can i help")
print(answer)

config = load_config_file(r"C:\Hackaton\Server\configuration.json")
voice = Voice(config)
bt = 0
sum = 0

while True:
    question = input("> ")
    if question == "review":
        review = simulator.review_simulation(simulation_id)
        break

    start = time.time()
    answer, mood = simulator.generate_answer(simulation_id, question)
    print(f"Mood: {mood}\n"+answer)
    #voice.generate_emotional_speech(answer, 'en-US-AIGenerate1Neural', "test.wav")
    sum += time.time() - start
    bt += 1
    time.sleep(1)



print('current average: ' + str(sum / bt))
print(review)

