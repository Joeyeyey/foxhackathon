import calendar
import datetime

class EventDay():
	def __init__(self, day):
		self.day = day
	events = []


class FoxCalendar():
	def __init__(self, month = datetime.datetime.now().month, year = datetime.datetime.now().year):
		self.calendar = calendar.Calendar(6)
		self.year = year
		self.month = month
		self.days = []
		self.numdays = (datetime.date(self.year, self.month + 1, 1) - datetime.date(self.year, self.month, 1)).days
		for i in range(1, self.numdays+1):
			self.days.append(EventDay(i))
		
	def getWeek(numweek):
		
	def printCalendar(self):
		for i in range(self.numdays):
			print (self.days[i].day)


today = FoxCalendar()
	
today.printCalendar()
today
