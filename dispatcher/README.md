## Task Dispatcher

Dispatches (triggers) functions at specifed regular intervals as specifed by the user.  
The user creates a simple task with **create()** and using **run()** will check what tasks shall be triggered.
**Tasks will be run using soft time requirements (tasks may run with a small delay)**
This allows for a clean non blocking control flow between tasks.

### Disclaimer
This is not a RTOS, this only serves as a module to trigger functions. There is no handling of irregular events within tasks.  
No threading support, assumes only 1 CPU core exists.  
Due to the CPU spinning while idle, not ideal for energy saving programs and programs that do not have many tasks scheduled.
Especially for programs that are time sensitive a proper RTOS will be crucial to use.

