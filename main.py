

input_number = input("write the number : ")
if input_number.isdigit() and not isspeace() :
   input_number = int(input_number)
   result_1 = input_number % 2
   if  result_1 == 0 :
    print("عدد زوجي")
   if result_1 != 0 :
      print ("عدد فردي")

else :
  print("wrong value")

#Amjad_Al_Henawi