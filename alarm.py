from time import sleep
import webbrowser as wb

h, m, s = map(int, input("H M S\n").split())
time_left = 60*60*h + 60*m + s

while time_left > 0:
	print("Time left: ", time_left)
	sleep(1)
	time_left -= 1

wb.open("alarm.mp3")
