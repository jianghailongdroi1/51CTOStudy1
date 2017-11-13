import threading
import time
def run(n):
    time.sleep(1)
    print("run... ", n )

for i in range(10):
    #run(i)
    t = threading.Thread(target=run,
                         args=(i,))
    t.start()


