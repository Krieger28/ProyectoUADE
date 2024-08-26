testestest = 0
import os
clear = lambda: os.system('cls')
from threading import Timer
booolean = False
def testtt():
    print("holaaa")
    global booolean 
    booolean = True
i=0

while i < 2234556:
    r = Timer(2.0, testtt)
    if booolean == False:
        r.start()
    
    
    clear()