number = int(input("Enter the number : "))

#if statement no. 1
if(number%2==0):
    print("Even")
    #end of if statement no.1 

#if statement no. 2
if(number>=18):
    print("You are eligible to Vote ")

elif(number<0):
    print("You are entering a negative age which is not valid  ")

elif(number==0):
    print("You are entering 0 which is not a valid age  ")

else:
    print("You are not eligible to vote ")
    #end of if statement no. 2