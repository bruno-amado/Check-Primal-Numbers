def prime(number):
   a = range(1, number)
   for i in a: 
      if number == 2:
         return("That's the only even primal number!")
      elif number % i  == 0:
         return("This number is not a Prime!")         
      elif number % i != 0: 
         return("This number is a Prime Number!")         
      else:
         return("That's not a number")
         
print (prime(int(input("Enter a number: "))))


