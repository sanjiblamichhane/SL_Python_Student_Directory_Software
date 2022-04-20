from p4 import * 
from copy import deepcopy 

if __name__ == '__main__':
    G1 = P4_GRADES("G1", 4, 3)
    G2 = P4_GRADES("G2", 2, 3)

    G1.P4_LIST(30)
    G2.P4_LIST(30)

    G2 = deepcopy(G1) 
    G2.set_name("G2") # set the objName to G2
    # Note: we can't overload the = operator, G2 will take G1's objName as well
    # print(type(G2)) # check if this worked - it should 
    
    G1.P4_LIST(30)
    G2.P4_LIST(30) 
    

    output_file.close()

    # short explanation of deepcopy:
    # when using the assignment operator with lists, tuples, and custom objects
    # the assignment operator makes a copy. The original and the copy share the
    # same memory space. That means, any modification made to the original can be
    # observed on the copy as well. To unlink the objects, i.e. make sure they don't
    # share the same memory space, we need to use a deepcopy. A deepcopy is a copy
    # of an object that does NOT share the same memory space, making them independent of
    # each other. 
