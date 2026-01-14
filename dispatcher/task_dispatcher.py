# Task Dispatcher for simple execution of tasks
# Dispatcher allows CPU to spin when no tasks ready (not useful for energy saving programs)
# *** Not a RTOS ***
from time import ticks_ms,ticks_diff

# Task queues
task_queue = []
run_queue = []

# Task to perform
# function: What function to trigger
# interval: Trigger function at regular specified intervals in ms
# A internal variable next_run will be registered which tells run() when the task should be triggered

class Task:
    def __init__(self,function,interval):
        self.function = function
        self.interval = interval
        self.timestamp = ticks_ms() + self.interval

# Create a task and add to queue
def create(function,interval):
    task = Task(function,interval)
    task_queue.append(task)

# Main Loop
def run():
    while True:
        now = ticks_ms()
        for task in task_queue:
            if ticks_diff(now, task.timestamp) >= task.interval:
                task.timestamp += task.interval
                run_queue.append(task)

      # Run due tasks
        for task in run_queue:
            task.function()
            
        run_queue.clear()
           
