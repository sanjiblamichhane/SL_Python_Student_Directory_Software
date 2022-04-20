output_file = open("python_Output.txt",'w')

class P0_GRADES:
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

        # creating a Python array of a specific length and initializing all elements to 0 
        # Note that these arrays are not static, we can append to or pop from these lists
        self.id = [0 for _ in range(x)]     # same as int id[x] = {0, 0, 0, 0, 0, ... etc.} in C++
        self.pin = [0 for _ in range(x)]    # same as int pin[x] = {0, 0, 0, 0, 0, ... etc.} in C++
        self.grades = [[0 for _ in range(y)] for _ in range(x)] # same as grades[x][y] = {{0,0,0...},{0,0,0}}
        

        # not as conventional way in Python but closer to the original sample_p0.h 
        i = 0 
        with open('studentGrades.txt','r') as i_f:
            for line in i_f: 
                self.id[i] = line.split()[0] # read first word from the line and put it into id array
                self.pin[i] = line.split()[1] # read second word from the line and put it in pin array
                for j in range(self.e):
                    self.grades[i][j] = line.split()[j+2] # fille in the grades array 
                i += 1

        output_file.write("+ CONTSTRUCTOR SUCCESSFULLY INSTANTIATED AN OBJECT.\n")
        output_file.write(f"+ THERE ARE {self.n} STUDENTS IN THIS P0_GRADES OBJECT.\n")
    
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
            output_file.write("+ END OUTPUT FROM P0_MIN METHOD: \n")
            return min_grade
        else:
            output_file.write("+ INPUT ERROR\n")
            output_file.write("+ END OUTPUT FROM P0_MIN METHOD: \n")
            return -1

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
            output_file.write("+ END OUTPUT FROM P0_MIN METHOD: \n")
            return max_grade
        else:
            output_file.write("+ INPUT ERROR\n")
            output_file.write("+ END OUTPUT FROM P0_MIN METHOD: \n")
            return -1

if __name__ == '__main__':
    B = P0_GRADES(4,3)
    output_file.close()