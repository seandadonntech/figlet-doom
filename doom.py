import pyfiglet
direction = input("what options of text do you to print? don't know type help for list of commands \n")
#----------------------------------------------
#slant mode
#------------------------------------------------------------------------------------------------------------------------
if direction == "doom": # this is an argument/ IM ADDING MORE OPTIONS FOR THIS PROGRAM
  input = input("what text to you what to print out in slant mode? press q to quit\n")
result = pyfiglet.figlet_format(f"{input}", font = "doom" )
print(result)

if direction == "q":
 quit()

else :
 print("invaild command program closed ")
