from task_manager import TaskManager
import json
from openai import OpenAI
# Tworzymy instancję TaskManager
task_manager = TaskManager()

# Używając swojego klucza API, rozwiąż zadanie o nazwie HelloAPI
# Zadanie polega na pobraniu zmiennej cookie z powyższego taska 
# i odesłaniu jej do serwera jako odpowiedzi w polu answer (w JSON)

taskName = "blogger"

# pobranie tokena
token = task_manager.getToken(taskName)

# pobranie podpowiedzi
# hint = task_manager.getHint(taskName)
# print(hint)

task = task_manager.getTask(token)

client = OpenAI()

answer = []
for chapter in task["blog"]:
    m = [
        {
            "role": "system",
            "content": "Jesteś blogerem kuchennym. Twoim zadaniem jest opisać poszczególne etapy wykonywania pizzy",
        },
    ]
    for a in answer:
        m.append({"role": "user", "content": a[0]})
        m.append({"role": "assistant", "content": a[1]})
    m.append(
        {"role": "user", "content": chapter},
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=m,
    )
    print("# " + chapter)
    print(response.choices[0].message.content)
    answer.append(response.choices[0].message.content)

print(answer)

# wysłanie odpowiedzi
# task_manager.submitAnswer(token, answer)
