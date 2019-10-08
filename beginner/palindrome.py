//Program in python to check a given number is a Palindrome or not.

n1= int(input(“Enter the number: ”))
temp=n1 //storing the number in temporary variable
rev=0
while(n1>0):
digit=n1%10
rev=rev*10+digit //reversing the digit and storing it in a variable
n1=n1//10
if (temp==rev) : //comparing temp variable and rev variable
print(“It is a palindrome ”)
else:
print(“It is not a palindrome ”)
