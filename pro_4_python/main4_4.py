from p4 import * 

if __name__ == '__main__':
    G1 = P4_GRADES("G1", 4, 3)
    G2 = P4_GRADES("G2", 2, 3)

    G1.P4_LIST(10)
    G2.P4_LIST(10)

    if G1 == G2:
        pass 
    else:
        pass 

    G1 -= 2222 
    G1 -= 4444 

    if G1 == G2:
        G1.P4_LIST(30)
        G2.P4_LIST(30)
    
    G1 -= 1234 
    G1 -= -1 

    output_file.close()