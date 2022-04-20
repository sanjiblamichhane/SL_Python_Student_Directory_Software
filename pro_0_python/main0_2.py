from sample_p0 import *
# from sample_p0_v2 import *

if __name__ == '__main__':
    B = P0_GRADES(4, 3)
    B.P0_LIST(-1) # input error
    B.P0_LIST(5) # input error
    output_file.close() # need this line for the python file to update properly