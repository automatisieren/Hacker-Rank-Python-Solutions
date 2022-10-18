from cmath import polar
if __name__ == "__main__":
    complex = complex(input().strip())
    (r, angle) = polar(complex)    
    print(f"{r}\n{angle}")