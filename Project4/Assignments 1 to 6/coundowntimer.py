import time

def Countdown_timer(t):
    while t > 0:
        mins , secs = divmod(t,60)
        format_time = '{:02d}:{:02d}'.format(mins,secs)
        print(format_time,end='\r')
        time.sleep(1)
        t -= 1
    print("Your time is up, soldier! 🎖️")
        
t = int(input("How many seconds should the countdown be? ⏳: "))
Countdown_timer(t)
    