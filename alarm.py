from time import sleep
import webbrowser as wb

# Rings alarm every hour 
while True:
	time_left = 60 * 60
	while time_left > 0:
		print("Time left: ", time_left, end='\r')
		sleep(1)
		time_left -= 1

	wb.open("alarm.mp3") # Ring the alarm.