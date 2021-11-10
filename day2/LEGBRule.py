'''
Created on Nov 9, 2021

@author: Krishnaiah
'''

# LGB

'''
gi = 10

def gfun():
    print(f" gfun : gi= {gi}, id(gi)= {id(gi)}")
    
print(f"main : gi= {gi}, id(gi)= {id(gi)}")
gfun()
print(f"main : gi= {gi}, id(gi)= {id(gi)}")
'''

'''
gi = 10

def gfun():
    gi = 20
    print(f" gfun : gi= {gi}, id(gi)= {id(gi)}")
    
print(f"main : gi= {gi}, id(gi)= {id(gi)}")
gfun()
print(f"main : gi= {gi}, id(gi)= {id(gi)}")
'''


#print("i = ", i)
#i = 1


# LGB
'''
gi = 10

def gfun():
    print(f" gfun : gi= {gi}, id(gi)= {id(gi)}")
    gi = 20
    print(f" gfun : gi= {gi}, id(gi)= {id(gi)}")
    
print(f"main : gi= {gi}, id(gi)= {id(gi)}")
gfun()
print(f"main : gi= {gi}, id(gi)= {id(gi)}")
'''

'''
gi = 10

def gfun():
    global gi
    
    print(f" gfun : gi= {gi}, id(gi)= {id(gi)}")
    gi = 20
    print(f" gfun : gi= {gi}, id(gi)= {id(gi)}")
    
print(f"main : gi= {gi}, id(gi)= {id(gi)}")
gfun()
print(f"main : gi= {gi}, id(gi)= {id(gi)}")
'''

'''
gi = 10
gj = 12

def gfun():
    print("= "  * 10)
    
    gi = 20
    gk = 25
    print(f" gfun : gi= {gi}, id(gi)= {id(gi)}")
    print("locals()= ", locals())
    print("globals()= ", globals())
    print("= "  * 10)
    
print(f"main : gi= {gi}, id(gi)= {id(gi)}")
gfun()
print(f"main : gi= {gi}, id(gi)= {id(gi)}")
'''



'''
gi = 10

def gfun():
#    global gi

    #gi = 20
    print("^ "*5)
    print(f" gfun : gi= {gi}, id(gi)= {id(gi)}")
    
    def nested():
        print(" - "*5)
        print(f" gfun..nested : gi= {gi}, id(gi)= {id(gi)}")
        print(" - "*5)
        
    nested()   
    print(f" gfun : gi= {gi}, id(gi)= {id(gi)}")
    print("v "*5)
    
print(f"main : gi= {gi}, id(gi)= {id(gi)}")
gfun()
print(f"main : gi= {gi}, id(gi)= {id(gi)}")
'''

'''
# LEGB
gi = 10

def gfun():
#    global gi
    gi = 20
    print("^ "*5)
    print(f" gfun : gi= {gi}, id(gi)= {id(gi)}")
    
    def nested():
        print(" - "*5)
        print(f" gfun..nested : gi= {gi}, id(gi)= {id(gi)}")
        print(" - "*5)
        
    nested()   
    print(f" gfun : gi= {gi}, id(gi)= {id(gi)}")
    print("v "*5)
    
print(f"main : gi= {gi}, id(gi)= {id(gi)}")
gfun()
print(f"main : gi= {gi}, id(gi)= {id(gi)}")
'''

'''
# LEGB
gi = 10

def gfun():
#    global gi
    gi = 20
    print("^ "*5)
    print(f" gfun : gi= {gi}, id(gi)= {id(gi)}")
    
    def nested():
        print(" - "*5)
        gi = 50
        print(f" gfun..nested : gi= {gi}, id(gi)= {id(gi)}")
        print(" - "*5)
        
    nested()   
    print(f" gfun : gi= {gi}, id(gi)= {id(gi)}")
    print("v "*5)
    
print(f"main : gi= {gi}, id(gi)= {id(gi)}")
gfun()
print(f"main : gi= {gi}, id(gi)= {id(gi)}")
'''

'''
# LEGB
gi = 10

def gfun():
#    global gi
    gi = 20
    print("^ "*5)
    print(f" gfun : gi= {gi}, id(gi)= {id(gi)}")
    
    def nested():
        global gi
        print(" - "*5)
        gi = 50
        print(f" gfun..nested : gi= {gi}, id(gi)= {id(gi)}")
        print(" - "*5)
        
    nested()   
    print(f" gfun : gi= {gi}, id(gi)= {id(gi)}")
    print("v "*5)
    
print(f"main : gi= {gi}, id(gi)= {id(gi)}")
gfun()
print(f"main : gi= {gi}, id(gi)= {id(gi)}")
'''

# LEGB
gi = 10

def gfun():
    gi = 20
    print("^ "*5)
    print(f" gfun : gi= {gi}, id(gi)= {id(gi)}")
    
    def nested():
        nonlocal gi
        print(" - "*5)
        gi = 50
        print(f" gfun..nested : gi= {gi}, id(gi)= {id(gi)}")
        print(" - "*5)
        
    nested()   
    print(f" gfun : gi= {gi}, id(gi)= {id(gi)}")
    print("v "*5)
    
print(f"main : gi= {gi}, id(gi)= {id(gi)}")
gfun()
print(f"main : gi= {gi}, id(gi)= {id(gi)}")





























    
    