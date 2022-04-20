#include <iostream>
#include "p0.h"
// example program: main0_2.cc
int main ()
{
        P0_GRADES B(4, 3);  // instantiate an object B which is of class
			// P0_GRADES with 4 students each with 3 exams

        B.P0_LIST(-1); // input error;
        B.P0_LIST(5); // input error;

        return 0;
}
