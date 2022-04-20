# using sample_p0 import *, we already imported the output file
# we don't have to open the file again, since running this line will
# open the file. We can just use the file object now 
from sample_p0 import * 

# inheriting P0_GRADES
class P1_GRADES(P0_GRADES): 
    def __init__(self, w, z):
        super().__init__(w, z) # calling the base class constructor

        output_file.write("__P1__ P1_GRADES CONSTRUCTOR CREATED A NEW OBJECT.\n")
        
    def P1_LIST(self, q):
        ''' a method
        list the grades for a given exam
        if q is 0, list the ids (use inheritance)
        if q is 1, list the ids and grades for all exams
        returns no values
        '''
        output_file.write("__P1__ START P1_LIST\n")
        if (q == 0):
            output_file.write("__P1__ SINCE CALLED WITH 0, INHERIT FROM P0_LIST:\n")
            self.P0_LIST(1) # call from base class
        elif (q == 1):
            output_file.write("__P1__ SINCE CALLED WITH 1, LIST IDS AND GRADES:\n")
            output_file.write("__P1__ ====\t======\n")
            output_file.write("__P1__  ID \tGRADES\n")
            output_file.write("__P1__ ====\t======\n")

            for i in range(self.n):
                output_file.write(f"__P1__ {self.id[i]}\t")
                for j in range(self.e):
                    output_file.write(f"{self.grades[i][j]}\t")
                output_file.write("\n")
        else:
            output_file.write("__P1__ SINCE NOT CALLED WITH 0 OR 1, INPUT ERROR\n")
        
        output_file.write("__P1__ END P1_LIST\n")

    def P1_FIND(self, r, s):
        ''' another method
        example usage B.P1_FIND(r, s)
        list the grades of student with id r and pin s
        if student exsts, return its index
        if no such student, give list of all students; return -1
        if r and/or s are illegal, return -2
        reults: 0 < r< 10000 and 0 < s < 1000
        '''

        output_file.write("__P1__ START P1_FIND\n")
        if (r > 0) and (r < 10000) and (s > 0) and (s < 1000):
            found = False
            for i in range(self.n):
                if self.id[i] == r and self.pin[i] == s:
                    found = True 
                    found_pos = i 
            
            if found:
                output_file.write(f"__P1__ GRADES OF STUDENT WITH ID {r}:\n__P1__ ")
                for j in range(self.e):
                    output_file.write(f"{self.grades[found_pos][j]}\t")
                output_file.write("\n")
                output_file.write("__P1__ END P1_FIND\n")
                return found_pos 
            else:
                output_file.write(f"__P1__ NO SUCH STUDENT WITH ID {r}\n")
                output_file.write("__P1__ ALL STUDENT IDS ARE:\n")
                self.P0_LIST(1)
                output_file.write("__P1__ END P1_FIND\n")
                return -1
        else:
            output_file.write("__P1__ INPUT ERROR\n")
            output_file.write("__P1__ END P1_FIND\n" )
            return -2



