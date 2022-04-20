#include <iostream>
#include "p0.h"
// example program: main0_4.cc
int main ()
{
        P0_GRADES B(4, 3);  // instantiate an object B which is of class
			// P0_GRADES with 4 students each with 3 exams

        B.P0_MAX(1, 2); // find max grade for exam 2;
        B.P0_MAX(-1, 2); // input error;

        return 0;
}
