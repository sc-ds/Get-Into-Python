def yo(n):

    if n>1:

        yo(n//2)

    print(n%2,end='')

n=int(input("Enter the decimal number: "))

yo(n)
