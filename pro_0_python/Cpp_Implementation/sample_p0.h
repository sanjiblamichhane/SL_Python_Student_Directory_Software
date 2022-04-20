#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

// declare a pointer to an input file:
ifstream i_f; 
// declare a pointer to the output file called output.txt:
ofstream o_f("output.txt", ios::out);  


  class P0_GRADES{

   public:      // public interfaces for this class

        P0_GRADES(int, int); // constructor;
		// example usage: B.P0_GRADES(x, y);
		// B is an object with x students each with y exams;
		// it populates the protected data members using
		// values read from an input file called studentGrades.txt;
		// returns no values;

        int P0_LIST(int); // a method; 
		// example usage: B.P0_LIST(x);
		// B is object, x is an integer;
		// if x == 1, list all ids and return 1;
		// otherwise, report input error and return -1;

        int P0_MIN(int, int); // a method; 
		// example: B.P0_MIN(x,  y);
		// B is object, x and y are integers;
		// if x == 1 and 0<= y <e, find min in exam y return min;
		// otherwise, report input error and return -1;

        int P0_MAX(int, int); // a method; 
		// example: B.P0_MAX(x, y);
		// B is object, x and y are integers;
		// if x == 1 and 0<= y <e, find max in exam y return max;
		// otherwise, report input error and return -1;

   protected: // protected var to be used by this class (not from main)
		// and classes that inherit from this class;

        int n;  // no of students
        int e;  // no of exams
        int id[20]; // integer array for student ids: max 20 students
        int pin[20]; // integer array for pin numbers: max 20 students
        int grades[20][10]; // integer array for grades: max 20 students max 10 exams
   };

P0_GRADES::P0_GRADES(int x, int y)
{
        int i, j;

	i_f.open("studentGrades.txt", ios::in); // open input file;

	n = x; // assign number of students;
	e = y; // assign number of exams;

        for(i=0; i<n; i++)
        {
		i_f >> id[i] >> pin[i];
		for(j = 0; j < e; j++)
		{
			i_f>> grades[i][j];
		}
        }
	i_f.close(); // close input file;
	i_f.clear(); // rewind file pointer to the top of the file;

        o_f << "+ CONTSTRUCTOR SUCCESSFULLY INSTANTIATED AN OBJECT." << endl;
        o_f << "+ THERE ARE "
                << n << " STUDENTS IN THIS P0_GRADES OBJECT." << endl;
} // end of constructor

int
P0_GRADES::P0_LIST(int x)
{
        int i, j;
cout << "\nin P0_LIST method: x: " << x << endl;
       	o_f << "+ START OUTPUT FROM P0_LIST METHOD: " << endl;
	if(x == 1)
	{
cout << "in P0_LIST method: since x is 1, list ids" << endl <<endl;
        	o_f << "+ THERE ARE "
                	<< n << " STUDENTS IN THIS P0_GRADES OBJECT:" << endl;
	
        	for(i=0; i<n; i++)
        	{
                	o_f << id[i] << endl;
        	}
        	o_f << "+ END OUTPUT FROM P0_LIST METHOD: " << endl;
		return 1;
	}
	else
	{
cout << "in P0_LIST method: report input error since x is not 1\n" << endl;
		o_f << "+ INPUT ERROR" << endl;
        	o_f << "+ END OUTPUT FROM P0_LIST METHOD: " << endl;
		return -1;
	}
} // end of P0_LIST

int
P0_GRADES::P0_MIN(int x, int y)
{
	int i, min;
cout << "\nin P0_MIN method: x: " << x << " y: " << y << endl;
       	o_f << "+ START OUTPUT FROM P0_MIN METHOD: " << endl;
	if(x == 1 && y >=0 && y <e)
	{
cout << "in P0_MIN method: since x is 1, find minimum grade for exam " << y 
	<< endl << endl;
		min = grades[0][y];

		for(i=0; i<n; i++)
		{
			if (min > grades[i][y])
			{
				min = grades[i][y];
			}
			else {}
		}
		o_f << "+ THE LOWEST GRADE IS " << min << "." << endl;
        	o_f << "+ END OUTPUT FROM P0_MIN METHOD: " << endl;
		return min;
	}
	else
	{
cout << "in P0_MIN method: report input error since: either x is not 1,"
	<< " or y is out of bounds\n" << endl;
		o_f << "+ INPUT ERROR" << endl;
        	o_f << "+ END OUTPUT FROM P0_MIN METHOD: " << endl;
		return -1;
	}
}// end of P0_MIN

int
P0_GRADES::P0_MAX(int x, int y)
{
	int i, max;
cout << "\nin P0_MAX method: x: " << x << " y: " << y << endl;
       	o_f << "+ START OUTPUT FROM P0_MAX METHOD: " << endl;
	if(x == 1 && y >=0 && y <e)
	{
cout << "in P0_MAX method: since x is 1, find maximum grade for exam " << y 
	<< endl << endl;
		max = grades[0][y];

		for(i=0; i<n; i++)
		{
			if (max < grades[i][y])
			{
				max = grades[i][y];
			}
			else {}
		}
		o_f << "+ THE HIGHEST GRADE IS " << max << "." << endl;
        	o_f << "+ END OUTPUT FROM P0_MAX METHOD: " << endl;
		return max;
	}
	else
	{
cout << "in P0_MAX method: report input error since: either x is not 1,"
	<< " or y is out of bounds\n" << endl;
		o_f << "+ INPUT ERROR" << endl;
        	o_f << "+ END OUTPUT FROM P0_MAX METHOD: " << endl;
		return -1;
	}
}// end of P0_MAX
