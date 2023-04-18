import pywhatkit
import time

pywhatkit.sendwhatmsg_instantly("+584248470352", "Hola")

# pywhatkit.sendwhatmsg("+584248470352", "Hola", 13, 58)

for x in range(0,10):
    time.sleep(1)
    pywhatkit.sendwhatmsg_instantly("+584248470352", "Hola")