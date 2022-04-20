output_file = open("python_Output.txt",'w')

class P0_GRADES:
    # start implementation of constructor:
    def __init__(self, x, y):
        ''' 
        this is the constructor
            Example usage: B = P0_GRADES(x,y)
            B is an object with x students and y exams;
            it populates the data members using values read
            from an input file called studentGrades.txt
            returns no values 
        '''
        self.n = x # number of students
        self.e = y # number of exam
        self.id = []
        self.pin = []
        self.grades = []
        
        # In Python, this is the conventional way to read in a text file; 
        # the "with" statement closes the file at the end of the with clause;
        # typically the file is read line by line and parsed; 
        with open('studentGrades.txt','r') as i_f:
            for line in i_f: 
                self.id.append(int(line.split()[0])) # first element of each line is the id
                self.pin.append(int(line.split()[1])) # second element of each line is pin
                self.grades.append([int(x) for x in line.split()[2:]]) # the rest of the line is grades 
        # end with

        output_file.write("+ CONTSTRUCTOR SUCCESSFULLY INSTANTIATED AN OBJECT.\n")
        output_file.write(f"+ THERE ARE {self.n} STUDENTS IN THIS P0_GRADES OBJECT.\n")
    # end implementation of constructor

    # start implementation of method P0_LIST:
    def P0_LIST(self, x):
        '''
        A method
        Example usage: B.P0_LIST(x) where B is an object and x is an integer
        if x == 1, list all ids and return 1;
        otherwise, report input error and return -1;
        '''
        output_file.write("+ START OUTPUT FROM P0_LIST METHOD: \n")
        if x == 1:
            output_file.write(f"+ THERE ARE {self.n} STUDENTS IN THIS P0_GRADES OBJECT:\n")
            for i in range(self.n):
                output_file.write(f"{self.id[i]}\n")

            output_file.write("+ END OUTPUT FROM P0_LIST METHOD\n")
            return 1
        else:
            output_file.write("+ INPUT ERROR\n")
            output_file.write("+ END OUTPUT FROM P0_LIST METHOD\n")
            return -1
    # end implementation of method P0_LIST

    # start implementation of method P0_MIN:
    def P0_MIN(self, x, y):
        ''' A method
        example usage: B.P0_MIN(x,y) where B is an object, x and y are integers
        if x == 1 and 0 <= y < e, find the min in exam y and return min
        otherwise, report input error and return -1
        '''
        if (x == 1) and (y >= 0) and (y < self.e):
            min_grade = self.grades[0][y]
            for i in range(self.n):
                if min_grade > self.grades[i][y]:
                    min_grade = self.grades[i][y]
            
            output_file.write(f"+ THE LOWEST GRADE IS {min_grade}.\n")
            output_file.write("+ END OUTPUT FROM P0_MIN METHOD\n")
            return min_grade
        else:
            output_file.write("+ INPUT ERROR\n")
            output_file.write("+ END OUTPUT FROM P0_MIN METHOD\n")
            return -1
    # end implementation of method P0_MIN

    # start implementation of method P0_MAX:
    def P0_MAX(self, x, y):
        ''' A method
        example usage: B.P0_MIN(x,y) where B is an object, x and y are integers
        if x == 1 and 0 <= y < e, find the max in exam y and return max
        otherwise, report input error and return -1
        '''
        if (x == 1) and (y >= 0) and (y < self.e):
            max_grade = self.grades[0][y]
            for i in range(self.n):
                if max_grade < self.grades[i][y]:
                    max_grade = self.grades[i][y]
            
            output_file.write(f"+ THE LOWEST GRADE IS {max_grade}.\n")
            output_file.write("+ END OUTPUT FROM P0_MIN METHOD\n")
            return max_grade
        else:
            output_file.write("+ INPUT ERROR\n")
            output_file.write("+ END OUTPUT FROM P0_MIN METHOD\n")
            return -1
    # end implementation of method P0_MIN

if __name__ == '__main__':
    output_file.close()
