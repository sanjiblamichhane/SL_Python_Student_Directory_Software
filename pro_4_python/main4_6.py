from p4 import * 
from copy import deepcopy 

if __name__ == '__main__':
    G1 = P4_GRADES("G1", 4, 3)
    G2 = P4_GRADES("G2", 2, 3)
    G3 = P4_GRADES("G3", 1, 3)

    G1.P4_LIST(30)
    G2.P4_LIST(30)
    G3.P4_LIST(30)

    G1 -= 1111 
    G1 -= 3333 
    G2 -= 1111 

    G1.P4_LIST(30)
    G2.P4_LIST(30)
    G3.P4_LIST(30)

    G1 = G2 + G3 
    G1.set_name("G1")

    G1.P4_LIST(30)
    G2.P4_LIST(30)
    G3.P4_LIST(30)

    output_file.close()

    # Valid question: since you used deepcopy in main4_5.py, why isn't it here as well? 
    # We don't need deepcopy here because P4_TEMP (that is produced by G2 + G3) is just a 
    # temperary object in memory. We assign G1 to this (now they share the memory space)
    # and to P4_TEMP, it is perfectly fine. 
    # You can still use deep copy like: G1 = deepcopy(G2 + G3) but that would be a waste of
    # memory 