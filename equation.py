def evaluate_equation(a):
    for x in range(1,a+1):
        #a^2x - ax + 1
        value = ( pow(a,(2*x))-(pow(a,x)) + 1 )
        print(value)

if  __name__ == '__main__':
    a= int(input('Enter Value of a : '))
    evaluate_equation(a)