from p4 import * 

if __name__ == '__main__':
    G1 = P4_GRADES("G1", 4, 3)
    G2 = P4_GRADES("G2", 2, 3)

    if (G1 == 4): # if ( G1.__eq__(4) )
        G1.P4_LIST(30) # list;

    if not (G1 == 5):
        G1.P4_LIST(10) # list;

    output_file.close()