from sample_p1 import *

class P2_GRADES(P1_GRADES):
	def __init__(self, x, y):
		super().__init__(x, y) # call base class constructor
		output_file.write("====P2==== P2_GRADES CONSTRUCTOR.\n")

	def P2_SORT(self, x):
		output_file.write("====P2==== START P2_SORT\n")

		if(x == 1):
			# range(0, self.n) is the same as range(self.n)
			for i in range(self.n):
				min = self.id[i]
				min_pos = i

				for j in range(i, self.n):
					if min > self.id[j]:
						min = self.id[j]
						min_pos = j

				# swap the ids
				temp = self.id[min_pos]
				self.id[min_pos] = self.id[i]
				self.id[i] = temp

				# swam the pins
				temp = self.pin[min_pos]
				self.pin[min_pos] = self.pin[i]
				self.pin[i] = temp

				for k in range(self.e):
					temp = self.grades[min_pos][k]
					self.grades[min_pos][k] = self.grades[i][k]
					self.grades[i][k] = temp
			output_file.write("====P2==== STUDENTS ARE SORTED BASED ON IDS:\n")
			self.P0_LIST(1)
		else:
			output_file.write("====P2==== INPUT ERROR\n")

		output_file.write("====P2==== END P2_SORT\n")

	def P2_REPORT(self, x, y, z):
		output_file.write("====P2==== START P2_REPORT\n")

		if (x < 0 or x > 9999 or y < 0 or y > 999 or z < 0 or z >= self.e):
			output_file.write("====P2==== INPUT ERROR.\n")
			output_file.write("====P2==== END P2_REPORT\n")
			print(f"x = {x} y = {y} z ={z}")
			return -2
		else:
			return_value = self.P1_FIND(x, y)
			print(f"x = {x} y = {y} z ={z} ret = {return_value}")
			if (return_value == -1):
				output_file.write(f"====P2==== NO SUCH STUDENT WITH ID {x}.\n")
				output_file.write("====P2==== END P2_REPORT\n")
				return -1
			elif (return_value == -2):
				output_file.write("====P2==== INPUT ERROR.\n")
				output_file.write("====P2==== END P2_REPORT\n")
				return -2
			else:
				GRADE = self.grades[return_value][z]

				if (GRADE > 75):
					output_file.write(f"====P2==== STUDENT {x} HAS A PASSING GRADE FOR EXAM {z}.\n")
				else:
					output_file.write(f"====P2==== STUDENT {x} HAS A FALILING GRADE FOR EXAM {z}.\n")
					
				output_file.write("====P2==== END P2_REPORT\n")
				return return_value
			


