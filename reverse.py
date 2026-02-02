'''write a program to find the reverse of the number'''

def reverse(num):
     rev = 0
     while num>0:
         rev = rev*10+num%10
         num//=10
     return rev

def isPalindrome(num):
    return num==reverse(num)
print(reverse(1236))
print(ispalindrome(1236))

print(reverse(123))
<<<<<<< Updated upstream
print(ispalindrome(1239))

=======
print(isPalindrome(123))
>>>>>>> Stashed changes

print(reverse(121))
print(isPalindrome(121))

def getPalindromes(start,end):
    res=" "
    for i in range(1,end+1):
        if isPalindrome(i):
            res=res+str(i)+","
    return res
print(getPalindromes(1,10000))        



            
