'''
Task starts
    ↓
Runs until:
    await
or
    return
    ↓
Event loop gets control


The event loop repeatedly takes tasks from the Ready Queue.


An event loop is a scheduler that continuously executes ready tasks, 
suspends tasks that reach an await, and resumes them when the awaited operation completes,or any return 
allowing a single thread to handle many concurrent I/O operations efficiently.


aync functions are called as coroutines 

Steps:

    1.Registration: You submit asynchronous functions (coroutines) to the loop as Tasks.
    2.Monitoring: The event loop continuously monitors this task queue.
    3.Execution: It runs the top task until it hits a breakpoint—usually an await keyword.
    4.Delegation: When a task awaits on an I/O operation (like a network request or database query), the loop pauses that task and hands the waiting over to the Operating System.
    5.Context Switching: While the OS handles the I/O, the loop moves to the next ready task in the queue.
'''