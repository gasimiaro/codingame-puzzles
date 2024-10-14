#https://www.codingame.com/ide/puzzle/swatch-internet-time

time, utc = input().split()
time_h = int(time[0:2])  
time_m = int(time[3:5])  
time_s = int(time[6:])    

time_in_seconds = time_h * 3600 + time_m * 60 + time_s

utc_sign = utc[3]
utc_h = int(utc[4:6])  
utc_min = int(utc[7:])  

utc_offset_seconds = utc_h * 3600 + utc_min * 60

if utc_sign == "+":
    time_in_seconds -= (utc_offset_seconds - 3600) 
else:
    time_in_seconds += (utc_offset_seconds + 3600)  

time_in_seconds %= 86400

beats = (time_in_seconds / 86.4)

if str(int(beats * 1000)/1000)[-1] == "5":
      beats += 0.01 


rounded_beats = round(beats, 3)

print(f"@{rounded_beats:.2f}")
