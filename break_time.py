import time
import webbrowser

total_breaks = 3
break_count = 0

print ("This program started on "+time.ctime())
while (break_count < total_breaks ):
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/embed/4hpEnLtqUDg?hd=1&autoplay=1")
	break_count = break_count + 1
exit(0)
