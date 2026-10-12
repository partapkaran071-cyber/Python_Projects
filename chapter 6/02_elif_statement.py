number = int(input("Enter the number : "))

if(number>=18):
    print("You are eligible to Vote ")

elif(number<0):
    print("You are entering a negative age which is not valid  ")

elif(number==0):
    print("You are entering 0 which is not a valid age  ")


else:
    print("You are not eligible to vote ")