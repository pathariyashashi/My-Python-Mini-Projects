import time 
alarm_time=input("Set Alarm Time(HH:MM:SS):")
print("Alarm set for",alarm_time)
while True:
    current_time = time.strftime("%H:%M:S%")
    print(current_time)
    if current_time==alarm_time:
        print("WAKE UP!")
        break
    time.sleep(1)