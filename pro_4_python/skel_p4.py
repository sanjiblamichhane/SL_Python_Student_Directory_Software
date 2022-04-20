from sample_p3 import * 

# overloaded operators in python are __[name of operation]__ 
# where name of operation is the operator you want to overload
# https://docs.python.org/3/reference/datamodel.html for a full list of overloadable operators
class P4_GRADES(P3_GRADES):
    def __init__(self, O_N, x, y):
        '''constructor;
		example usage: G.P4_GRADES("G1", x, y);
		create an object G with x students each with y grades;
        '''
        super().__init__(x, y) # call the base class constructor 

        self.objName = O_N # set self.objName
        
        # replace pass with your code:
        pass 

    def set_name(self, object_name):
        self.objName = object_name

    def P4_LIST(self, x):
        '''a method;
		example usage: G.P4_LIST(x);
		if x == 10, use inheritance from P1_LISt(1);
		if x == 30, use inheritance from P3_LISt(1);
		otherwise input error;
		returns no values;
        '''

        # replace pass with your code:
        pass 

    def __eq__(self, input_var):
        ''' an overloaded operator;
        example usage: if (G == 4)
        if n is 4, return True;
        otherwise return False;

        example usage: if (G1 == G2)
        return 1 if n in G1 is equal to n in G2;
        return 0 otherwise;
        '''

        # if input_var is a integer (i.e. if G == 4)
        if isinstance(input_var,int):
            # replace pass with your code
            pass

        # if input_var is a P4_GRADES (i.e. if G1 == G2)
        elif isinstance(input_var, type(self)):
            # replace pass with your code
            pass
        else:
            TypeError(f"INPUT MUST BE OF TYPE P4_GRADES OR INT")
    
    # -= operator. You must return self to return the object 
    def __isub__(self, x):
        '''an overloaded operator;
        example usage: G -= 1234;
        remove student id 1234 from class if exists;
        
        IMPORTANT: This method always returns self 
        '''
        # replace pass with your code
        pass

    def __add__(self, obj2):
        '''// an overloaded operator;
        example usage: G1+G2;
        step 1: create a temporary P4_GRADES object (call it P4_TEMP);
        step 2: copy elements of G1 into P4_TEMP; don't forget to update n and e;
        step 3: append elements of G2 into P4_TEMP; don't forget to update n and e;
        step 4: return P4_TEMP object;

        OR 

        In Python, simply add the members of both classes together, e.g. P4_TEMP.id = self.id + obj2.id

        '''

        P4_TEMP = P4_GRADES("P4_TEMP", 0, 0)

        # replace pass with your code
        pass








        