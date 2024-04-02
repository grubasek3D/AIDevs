from task_manager import TaskManager
import json
from openai import OpenAI

task_manager = TaskManager()
client = OpenAI()

taskName = "liar"

# pobranie tokena
token = task_manager.getToken(taskName)
task = task_manager.getTask(token)

### Rozwiązanie zadania:
question = "What is love?"
response = task_manager.sendData(token, {"question": question})
response_answer = response["answer"]

model = "gpt-3.5-turbo"
message = [
        {"role": "system",
        "content": f"""You are working as a censor system. 
                    Please check if this sentence is answer to question:
                    {question}
                    ### Answer only YES or NO."""},
        
        {"role": "user",
        "content": f"{response_answer}"}
        ]

answer = client.chat.completions.create(
    model = model,
    messages = message
).model_dump()

task_manager.submitAnswer(token, answer["choices"][0]["message"]["content"])
