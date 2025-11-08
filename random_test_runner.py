from main import app
from project.users.tasks import divide

# enqueue task to the default queue
# t1 = divide.apply_async(args=[1, 5])
# print(t1)
# 
# # enqueue task to the high_priority queue
# t2 = divide.apply_async(args=[1, 5], queue='high_priority')
# print(t2)
# 
# # enqueue task to the low_priority queue
# t3 = divide.apply_async(args=[1, 5], queue='low_priority')
# print(t3)


# enqueue task to the default queue
divide.delay(1, 2)

from project.users.tasks import dynamic_example_one, dynamic_example_two, dynamic_example_three

# enqueue task to the default queue
dynamic_example_one.delay()

# enqueue task to the high_priority queue
dynamic_example_three.delay()

# enqueue task to the low_priority queue
dynamic_example_two.delay()