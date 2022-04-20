from sample_p2 import * 

class P3_GRADES(P2_GRADES):
	def __init__(self, x, y):
		'''create an object B with x students each with y grades;
		read the names from studentNames.txt file
		'''
		# call the base class constructor:
		super().__init__(x,y)

		self.lastNames = []
		self.firstNames = []
		# replace pass with your code below:
		pass

	def P3_LIST(self, x):
		'''if x is 1, list grades and names;
		if x is 0, use inheritance self.P1_LIST(1);
		otherwise, input error;
		'''

		# replace pass with your code below:
		pass

	def P3_SORT(self, x):
		'''if x == 0, sort based on ids with inheritance;
		if x == 1, alphabetize based on last names;
		returns no values;
		'''

		# replace pass with your code below:
		pass

	def P3_VERIFY(self, F, L):
		'''if there is such a student and return index;
		if there is no such a student and return -1;
		if first/last name > 14 characters, error and return -2;
		'''

		# replace pass with your code below:
		pass

	def P3_REPORT(self, w, x, y, z):
		'''example usage: B.REPORT(w, x, y, z);
		if w == 0, use inheritance P2_REPOrt(x, y, z); return -1;
		if w == 1, id x, pin y, and exam z, and names; return index;
		if input error: return -2;
		'''

		# replace pass with your code below:
		pass









