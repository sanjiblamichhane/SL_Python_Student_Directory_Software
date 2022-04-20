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

		with open("studentNames.txt", "r") as i_f_2:
			for i in range(self.n):
				line = i_f_2.readline().split()
				self.firstNames.append(line[0])
				self.lastNames.append(line[1])

		output_file.write('<><><>P3<><><> P3_GRADES CREATES OBJECT WITH NAMES.\n')

	def P3_LIST(self, x):
		'''if x is 1, list grades and names;
		if x is 0, use inheritance self.P1_LIST(1);
		otherwise, input error;
		'''
		output_file.write("<><><>P3<><><> START P3_LIST\n")
		if x == 0:
			output_file.write("<><><>P3<><><> SINCE CALLED BY 0, INHERIT FROM P1_LIST(1):\n")
			self.P1_LIST(1)
		elif x == 1:
			output_file.write("<><><>P3<><><> SINCE CALLED BY 1, LISTING  NAMES AND GRADES:\n")
			for i in range(self.n):
				output_file.write(f"<><><>P3<><><> {self.firstNames[i]}\t{self.lastNames[i]}\t{self.id[i]}")
				for j in range(self.e):
					output_file.write(f"\t{self.grades[i][j]}")
				output_file.write("\n")
		else:
			output_file.write("<><><>P3<><><> SINCE NOT CALLED WITH 0 OR 1, INPUT ERROR.\n")

		output_file.write("<><><>P3<><><> END P3_LIST\n")

	def P3_SORT(self, x):
		'''if x == 0, sort based on ids with inheritance;
		if x == 1, alphabetize based on last names;
		returns no values;
		'''
		output_file.write("<><><>P3<><><> START P3_SORT\n")
		if x == 0:
			output_file.write("<><><>P3<><><> SINCE CALLED WITH 0, INHERIT FROM P2_SORT(1):\n")
			self.P2_SORT(1)
		elif x == 1:
			# sort last names using selection sort
			output_file.write("<><><>P3<><><> SINCE CALLED WITH 1, SORT STUDENTS IN ALPHABETICAL ORDER BASED ON LAST NAMES\n")
			for i in range(self.n):
				min_name = self.lastNames[i]
				min_pos = i 
				for j in range(i, self.n):
					if min_name > self.lastNames[j]:
						min_name = self.lastNames[j]
						min_pos = j

				# swap two variables without a temp variable - just to show that it can be done in python
				self.lastNames[min_pos], self.lastNames[i] = self.lastNames[i], self.lastNames[min_pos]
				self.firstNames[min_pos], self.firstNames[i] = self.firstNames[i], self.firstNames[min_pos]
				self.id[min_pos],self.id[i] = self.id[i], self.id[min_pos]
				self.pin[min_pos],self.pin[i] = self.pin[i], self.pin[min_pos]

				for k in range(self.e):
					self.grades[i][k], self.grades[min_pos][k] = self.grades[min_pos][k], self.grades[i][k]
		else:
			output_file.write("<><><>P3<><><> SINCE NOT CALLED WITH 0 OR 1, INPUT ERROR.\n")

		output_file.write("<><><>P3<><><> END P3_SORT\n")
	def P3_VERIFY(self, F, L):
		'''if there is such a student and return index;
		if there is no such a student and return -1;
		if first/last name > 14 characters, error and return -2;
		'''
		output_file.write("<><><>P3<><><> START P3_VERIFY\n")
		if (len(F) <= 14 and len(L) <= 14):
			found = 0
			found_pos = -1

			for i in range(self.n):
				if F == self.firstNames[i] and L == self.lastNames[i]:
					found = 1
					found_pos = i 
					break

			if found == 1:
				output_file.write(f"<><><>P3<><><> THERE IS A STUDENT AS {F} {L}.\n")
				output_file.write("<><><>P3<><><> END P3_VERIFY\n")
				return found_pos
			else:
				output_file.write(f"<><><>P3<><><> THERE IS NO STUDENT AS {F} {L}.\n")
				output_file.write("<><><>P3<><><> END P3_VERIFY\n")
				return -1
		else:
			output_file.write("<><><>P3<><><> INPUT ERROR\n")
			output_file.write("<><><>P3<><><> END P3_VERIFY\n")
			return -2

	def P3_REPORT(self, w, x, y, z):
		'''example usage: B.REPORT(w, x, y, z);
		if w == 0, use inheritance P2_REPOrt(x, y, z); return -1;
		if w == 1, id x, pin y, and exam z, and names; return index;
		if input error: return -2;
		'''
		output_file.write("<><><>P3<><><> START P3_REPORT\n")
		if w == 0:
			output_file.write("<><><>P3<><><> SINCE CALLED WITH 0, INHERIT FROM P2_REPORT:\n")
			self.P2_REPORT(x,y,z)
			output_file.write("<><><>P3<><><> END P3_REPORT\n")
			return -1
		elif w == 1:
			output_file.write("<><><>P3<><><> SINCE CALLED WITH 1, FIRST INHERIT FROM P2_REPORT:\n")
			ret_value = self.P2_REPORT(x,y,z)
			if ret_value != -1 and ret_value != -2:
				output_file.write(f"<><><>P3<><><> STUDENT NAME IS: {self.firstNames[ret_value]} {self.lastNames[ret_value]}\n")
				output_file.write("<><><>P3<><><> END P3_REPORT\n")
				return ret_value
			else:
				output_file.write("<><><>P3<><><> INPUT ERROR RETURNED BY P2_REPORT\n")
				output_file.write("<><><>P3<><><> END P3_REPORT\n")
				return -2
		else:
			output_file.write("<><><>P3<><><> SINCE NOT CALLED WITH 0 OR 1, INPUT ERROR\n")
			output_file.write("<><><>P3<><><> END P3_REPORT\n")









