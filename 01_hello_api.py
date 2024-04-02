from task_manager import TaskManager
# Tworzymy instancję TaskManager
task_manager = TaskManager()

# Używając swojego klucza API, rozwiąż zadanie o nazwie HelloAPI
# Zadanie polega na pobraniu zmiennej cookie z powyższego taska 
# i odesłaniu jej do serwera jako odpowiedzi w polu answer (w JSON)

taskName = "helloapi"

# pobranie tokena
token = task_manager.getToken(taskName)

# pobranie podpowiedzi
task_manager.getHint(taskName)

# przygotowanie odpowiedzi
answer = task_manager.getTask(token).get('cookie')

# wysłanie odpowiedzi
task_manager.submitAnswer(token, answer)