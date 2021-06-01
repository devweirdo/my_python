from calculator_class import calculator
from clock import runtime
import threading
import time

calc=calculator()
clock = runtime()
t1=threading.Thread(target=calc.run)
t2=threading.Thread(target=clock.run)
t1.start()
t2.start()

calc.root.mainloop()
