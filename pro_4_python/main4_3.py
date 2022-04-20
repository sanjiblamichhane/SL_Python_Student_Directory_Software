from p4 import * 

if __name__ == '__main__':
    G1 = P4_GRADES("G1", 4, 3)
    G2 = P4_GRADES("G2", 2, 3)
    G3 = P4_GRADES("G3", 4, 3)

    if G1 == G3:
        G1.P4_LIST(30)
        G3.P4_LIST(30)
    
    if not (G1 == G2):
        G1.P4_LIST(10)
        G2.P4_LIST(10)

    output_file.close()