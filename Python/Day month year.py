import calendar
print("Enter the day, month, and year separated by a space on a single line.")
data = input("{}: ".format("Date")).split(' ')

day = int(data[0]); month = int(data[1]); year = int(data[2])

if day//10 == 1:
    suffix = 'th'
elif day % 10 == 2:
    suffix = 'nd'
elif day%10 == 1:
    suffix = 'st'
elif day % 10 == 3:
    suffix = 'rd'
else:
    suffix = 'th'

day = str(day)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month = months[month-1]

print(day + suffix,  month, year)
