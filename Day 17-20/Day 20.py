from threading import Timer
import time

def countdown():
  timestring = input("Enter time period with an h, m or s suffix to signify the unit. \nExample: 5s, 6m, 1h: ")
  try:
    timestring, unit = (int(timestring[:-1]), timestring[len(timestring)-1:])
    
    if unit =='m':
      timestring = timestring * 60
    elif unit =='h':
      timestring = timestring * 3600
    def bell():
      while True:
        # print('bell')
        print("\a")
    ring_bell = Timer(timestring, bell)
    ring_bell.start()
    
    while True and (unit =='s' or unit =='m' or unit =='h'):
      if timestring:
        if unit=='h':
          min, secs = divmod(timestring, 60)
          hr, mins = divmod(min, 60)
          t = "{:02d}h:{:02d}m:{:02d}s".format(hr, mins, secs)
        else:
          min, secs = divmod(timestring, 60)
          t = "{:02d}m:{:02d}s".format(min, secs)
    
        print(f"You have {t} left")
        time.sleep(1)
        timestring -= 1

  except:
    print("Your input is invalid!")
  return

countdown()
