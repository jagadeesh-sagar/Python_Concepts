'''

concurrency -> python is a single thread programme . 
soo to increase perfomance the time consuming stuff ( like d.b calls , fetching api's) is going on the python interpreter /
goes to do other stuff after the completion of 1st stuff it calls python but python waits for sometime /
in completing the 2nd stuff and goes back to main stuff ( same like in java script (event loop)) /
becoz of this interpeter doesn't wait idle 
-> it is useful of i/p bound tasks

parallelism is completely different from concurrency . 
it utilizes the multicore arch of cpu to run multi threads at a time in parallel (java)
useful for cpu bond tasks

asynchronus is like not blocking main thread /
in python async can only be achieved through concurrency /(event driven model (js same))
context switching here is more of software compared to multi threaded (os takes care -> more overheas)
'''

'''
Modern versions of Python have support for "asynchronous code" using something called "coroutines", with async and await syntax.

'''