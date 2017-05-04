import pyttsx
import time
engine = pyttsx.init()
# speech rate in words per minute
engine.setProperty('rate', 100)
# volume 0.0 to 1.0
engine.setProperty('volume', 0.9)
now_tuple = time.localtime()
#print(now_tuple)  # test
# slice off the year
now_str = time.asctime(now_tuple)[:-4]
print(now_str)  # test
engine.say(now_str)
engine.runAndWait()