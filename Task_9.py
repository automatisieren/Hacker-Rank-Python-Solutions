if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = [ [j,k,l] for j in range(0,x,1) for k in range(0,y,1) for l in range(0,z,1) if j + k + l != n ]
        