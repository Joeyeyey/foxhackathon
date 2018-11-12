import calendar
import datetime

class EventDay():
	def __init__(self, day, weekday):
		self.day = day
		self.weekday = weekday
	events = []

class FoxCalendar():
	def __init__(self, month = datetime.datetime.now().month, year = datetime.datetime.now().year):
		self.calendar = calendar.Calendar(6)
		self.year = year
		self.month = month
		self.days = []
		self.numdays = (datetime.date(self.year, self.month + 1, 1) - datetime.date(self.year, self.month, 1)).days
		for i in range(1, self.numdays+1):
			self.days.append(EventDay(i, datetime.date(self.year, self.month, i).weekday()))
	
	def printCalendar(self):
		for i in range(self.numdays):
			print ("%s - %s" %(self.days[i].day,calendar.day_name[self.days[i].weekday]))
	
	def calendarFormat(self):
		print("%s %s" %(self.year, calendar.month_name[self.month]))
		for i in range(0,self.days[0].weekday + 1):
			print ("[  ]", end="")
		for i in self.days:
			if i.weekday == 6:
				print()
			print ("[{:02d}]".format(i.day), end="")
		for i in range(5 - self.days[-1].weekday):
			print ("[  ]", end="")
		if self.days[-1].weekday == 6:
			for i in range(0,6):
				print ("[  ]", end="")
		print()

today = FoxCalendar()
for i in range(1,12):
	nextmonth = FoxCalendar(month = i)
	nextmonth.calendarFormat()
	print()
