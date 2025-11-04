from main import app
from project.users.tasks import divide
task = divide.delay(1, 2)

print(task)