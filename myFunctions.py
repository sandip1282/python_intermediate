'''
Created on Nov 8, 2021

@author: Krishnaiah
'''

# GB
def add(x=0, y=0):
    print("... add called ...")
    return x+y



print("__name__= ", __name__) 

if '__main__' == __name__:
    print(" Stmt 1")
    print("__doc__= ", __doc__)
    # default= '__main__' 
    # default= 'myFunctions'

    gi = 10
    print(f"gi= {gi}, id(gi)={id(gi)}")
else:
    print(" Stmt 2")