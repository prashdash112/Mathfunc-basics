def eigenvalue_calc(a,v,val):
    import numpy as np
    '''
    Eigen value is the factor (denoted by lambda) by which the eigen vector is scaled
    a is primary matrix. 
    v is a vector that's multiplied to a. 
    val is the estimate value user need to enter under which the eigen value will probably lie. 
    '''
    a=np.array(a)
    v=np.array(v)
    try:
        a.shape[1]==v.shape[0]
        prod=np.dot(a,v)
        for i in range(val):
            if np.all(prod==i*v):
                print('Eigen value \u03BB is:',i)
                break;
        else:
            print("Either eigenvalue doesn't exist or try increasing the val value")
        
    except: 
        print('DIMENSION ERROR: Multiplication of A & V is impossible because LEN(c(A))!=LEN(r(V))')
        
if __name__=='__main__':
    eigenvalue_calc([[-6,3],[4,5]],[[1],[4]],7)
    
    
