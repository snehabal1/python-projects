#
# Take a break
#
import webbrowser
import time

print("This timer started at "+time.ctime())
total_breaks=2
count_breaks =0

while count_breaks < total_breaks:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=-qlJiGGvPUI")
    count_breaks = count_breaks +1
