#include <iostream>
#include "p0.h"
// example program: main0_3.cc
int main ()
{
        P0_GRADES B(4, 3);  // instantiate an object B which is of class
			// P0_GRADES with 4 students each with 3 exams

        B.P0_MIN(1, 0); // find min grade for exam 0;
        B.P0_MIN(-1, 0); // input error;

        return 0;
}
