#! /usr/bin/python

import os
import glob

# Declare all list variables

nums = ['1','3','2','0','4','7','9','6','5','8']

spec = ['!','@','#','$','+','?']

leta = ['a']
let1 = ['a','i','u']
let2 = ['ab']
let3 = ['abc']
let4 = ['abcd']
let5 = ['abcde']
let6 = ['abcdef']
let7 = ['abcdefg']
let8 = ['abcdefgh']
let9 = ['abcdefghi']
let10 = ['abcdefghij']
let11 = ['abcdefghijk']
let12 = ['aaaaaaaaaaaa']
let13 = ['aaaaaaaaaaaaa']
let14 = ['aaaaaaaaaaaaaa']
over = ['abababababababa']

# Creating And Opening all deez text filez 

pass1 = open('done/1lower8.txt', "w")

pass2 = open('done/1cap8.txt', "w")

pass3 = open('done/1lower9.txt', "w")
pass4 = open('done/2lower9.txt', "w")

pass5 = open('done/lower8plusnums.txt', "w")
pass6 = open('done/lower8plusspec.txt', "w")

pass10 = open('done/1cap9.txt', "w")
pass11 = open('done/2cap9.txt', "w")

pass14 = open('done/1lower10.txt', "w")
pass15 = open('done/2lower10.txt', "w")


output = open('done/output.txt', "w")



# Convert wordlists to list variables?? fuck
def floodvars(wls):
	numba = 0
	for each in wls.readlines():
		each = each.rstrip('\n\t\r')		
		if len(each) == 1:
	  	  let1a.append(each)
		elif len(each) == 2:
		  let2.append(each.lower())
		elif len(each) == 3:
		  let3.append(each.lower())
		elif len(each) == 4:
		  let4.append(each.lower())
		elif len(each) == 5:
		  let5.append(each.lower())
		elif len(each) == 6:
		  let6.append(each.lower())
		elif len(each) == 7:
		  let7.append(each.lower())
		elif len(each) == 8:
		  let8.append(each.lower())
		elif len(each) == 9:
		  let9.append(each.lower())
		elif len(each) == 10:
		  let10.append(each.lower())
		elif len(each) == 11:
		  let11.append(each.lower())
		elif len(each) == 12:
		  let12.append(each.lower())
		elif len(each) == 13:
		  let13.append(each.lower())
		elif len(each) == 14:
		  let14.append(each.lower())
		else:
		  over.append(each.lower())

		numba = numba + 1
	print ('Number of words: ', numba)

# Open wordlist and convert .txt to a string variable 
myfiles = []
for each_file in glob.glob("wls/*.txt"):
	numba = 0
	myfiles.append(each_file)
	wlsfile = open(each_file, "r")
	print ('Importing ',each_file)
	floodvars(wlsfile)
	
	
# Remove Duplicates of Variables imported from text files
let1 = [*set(let1)]
let2 = [*set(let2)]
let3 = [*set(let3)]
let4 = [*set(let4)]
let5 = [*set(let5)]
let6 = [*set(let6)]
let7 = [*set(let7)]
let8 = [*set(let8)]
let9 = [*set(let9)]
let10 = [*set(let10)]
let11 = [*set(let11)]
let12 = [*set(let12)]
let13 = [*set(let13)]
let14 = [*set(let14)]
over = [*set(over)]

# Sort list variables 
let1.sort()
let2.sort()
let3.sort()
let4.sort()
let5.sort()
let6.sort()
let7.sort()
let8.sort()
let9.sort()
let10.sort()
let11.sort()
let12.sort()
let13.sort()
let14.sort()
over.sort()

# Edit letters
def editLet(whatLet):
	num = 0
	total = len(whatLet)
	start = 0
	end = 30 
	while num != total:
		for each in whatLet[start:end]:
			print('Entry ',num,'- ',each)
			num = num + 1
		print ('\n')
		if end==total:
			print (' End Of List ')
		print (' (a)dd , (am)Add Multiple,  (d)elete , (dm)Delete Multiple , (n)ext , e(x)it  ')
		
		target2=input("Enter your choice : ")
		if target2=="dm":
			d1 = [int(x) for x in input("Enter numbers to delete: ").split()]
			d1.reverse()
			for every1 in d1:
				del whatLet[every1]
			num = num - 30
		elif target2=="am":
			d3 = [str(y) for y in input("Enter new variables: ").split()]
			for every2 in d3:
				whatLet.append(every2)
		elif target2=="d":
			t3=int(input("Enter number to delete: "))
			del whatLet[t3]
			num = num - 30
		elif target2=="a":
			t5=str(input("Enter new variable: "))
			whatLet.append(t5)
			editLet(whatLet)
		elif target2=="n":
			start = start + 30
			end = end + 30 
			if end > total:
				end = total
		elif target2=="x":
			print('eXit')
			return	
		else:
	                start = start + 30
	                end = end + 30
	                if end > total:
	                	end = total
	
# Edit Words 
def editWordlist():
	os.system('clear')
	print ('\n')
	print ("                                       Edit Wordlists \n\n\n\n\n")
	print ('\n')
	print ('1 Letter Words  = ',len(let1)) 
	print ('2 Letter Words  = ',len(let2))
	print ('3 Letter Words  = ',len(let3))
	print ('4 Letter Words  = ',len(let4))
	print ('5 Letter Words  = ',len(let5))
	print ('6 Letter Words  = ',len(let6))
	print ('7 Letter Words  = ',len(let7))
	print ('8 Letter Words  = ',len(let8))
	print ('9 Letter Words  = ',len(let9))
	print ('10 Letter Words = ',len(let10))
	print ('11 Letter Words = ',len(let11))
	print ('12 Letter Words = ',len(let12))
	print ('13 Letter Words = ',len(let13))
	print ('14 Letter Words = ',len(let14))
	print ('Over 14 Letters = ',len(over))
	print ('')
	print ('Total Words = ', len(let1) + len(let2) + len(let3) + len(let4) + len(let5) + len(let6) + len(let7) + len(let8) + len(let9) + len(let10) + len(let11) + len(let12) + len(let13) + len(let14) + len(over))
	print ('\n')
	print ('\n')
	print ('e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, eo, e(x)it')
	print ('\n')
	target=input("Enter your Choice : ")
	if target=="e1":
		editLet(let1)
	elif target=="e2":
		editLet(let2)
	elif target=="e3":
	        editLet(let3)
	elif target=="e4":
	        editLet(let4)
	elif target=="e5":
	        editLet(let5)
	elif target=="e6":
	        editLet(let6)
	elif target=="e7":
	        editLet(let7)
	elif target=="e8":
	        editLet(let8)
	elif target=="e9":
	        editLet(let9)
	elif target=="e10":
	        editLet(let10)
	elif target=="e11":
	        editLet(let11)
	elif target=="e12":
	        editLet(let12)
	elif target=="e13":
	        editLet(let13)	
	elif target=="e14":
		editLet(let14)	
	elif target=="eo":
		editLet(over)
	elif target=="x":
		print('Exiting')	
	else:
		print('Illegal Character----- Exiting')
		
	mainmenu()

# Sequence Variables lowercase 10 characters
def seqvarslower10():
	print ('\n')
	print ('Sequencing Variables Lowercase 10 Character')
	print ('\n')
	# ------- lowercase 10 ---------------------------------------------------------------
	for each in range(len(let10)):
		pass14.write(let10[each])
		pass14.write("\n")	
	# -----	lowercase 9-------------------------------------------------------------------
	for each in range(len(let1)):
		for each2 in range(len(let9)):
			pass14.write(let1[each] + let9[each2])
			pass14.write("\n")
	for each in range(len(let9)):
		for each2 in range(len(let1)):
			pass14.write(let9[each] + let1[each2])
			pass14.write("\n")
	# -----	lowercase 8-------------------------------------------------------------------
	for each in range(len(let2)):
		for each2 in range(len(let8)):
			pass14.write(let2[each] + let8[each2])
			pass14.write("\n")
	for each in range(len(let8)):
		for each2 in range(len(let2)):
			pass14.write(let8[each] + let2[each2])
			pass14.write("\n")
	for each in range(len(let8)):
		for each2 in range(len(let1)):
			for each3 in range(len(let1)):
				pass14.write(let8[each] + let1[each2] + let1[each3])
				pass14.write("\n")	
	for each in range(len(let1)):
		for each2 in range(len(let1)):
			for each3 in range(len(let8)):
				pass14.write(let1[each] + let1[each2] + let8[each3])
				pass14.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let8)):
			for each3 in range(len(let1)):
				pass14.write(let1[each] + let8[each2] + let1[each3])
				pass14.write("\n")
	# -----	lowercase 7-------------------------------------------------------------------
	for each in range(len(let3)):
		for each2 in range(len(let7)):
			pass14.write(let3[each] + let7[each2])
			pass14.write("\n")
	for each in range(len(let7)):
		for each2 in range(len(let3)):
			pass14.write(let7[each] + let3[each2])
			pass14.write("\n")
	for each in range(len(let7)):
		for each2 in range(len(let1)):
			for each3 in range(len(let2)):
				pass14.write(let7[each] + let1[each2] + let2[each3])
				pass14.write("\n")	
	for each in range(len(let2)):
		for each2 in range(len(let1)):
			for each3 in range(len(let7)):
				pass14.write(let2[each] + let1[each2] + let7[each3])
				pass14.write("\n")
	for each in range(len(let7)):
		for each2 in range(len(let2)):
			for each3 in range(len(let1)):
				pass14.write(let7[each] + let2[each2] + let1[each3])
				pass14.write("\n")	
	for each in range(len(let2)):
		for each2 in range(len(let7)):
			for each3 in range(len(let1)):
				pass14.write(let2[each] + let7[each2] + let1[each3])
				pass14.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let2)):
			for each3 in range(len(let7)):
				pass14.write(let1[each] + let2[each2] + let7[each3])
				pass14.write("\n")	
	for each in range(len(let1)):
		for each2 in range(len(let7)):
			for each3 in range(len(let2)):
				pass14.write(let1[each] + let7[each2] + let2[each3])
				pass14.write("\n")
	
					
	# -----	lowercase 6-------------------------------------------------------------------	
	
	for each in range(len(let6)):
		for each2 in range(len(let4)):
			pass14.write(let6[each] + let4[each2])
			pass14.write("\n")
	for each in range(len(let4)):
		for each2 in range(len(let6)):
			pass14.write(let4[each] + let6[each2])
			pass14.write("\n")
	for each in range(len(let6)):
		for each2 in range(len(let2)):
			for each3 in range(len(let2)):
				pass14.write(let6[each] + let2[each2] + let2[each3])
				pass14.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let6)):
			for each3 in range(len(let2)):
				pass14.write(let2[each] + let6[each2] + let2[each3])
				pass14.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let2)):
			for each3 in range(len(let6)):
				pass14.write(let2[each] + let2[each2] + let6[each3])
				pass14.write("\n")			
	for each in range(len(let6)):
		for each2 in range(len(let3)):
			for each3 in range(len(let1)):
				pass14.write(let6[each] + let3[each2] + let1[each3])
				pass14.write("\n")
	for each in range(len(let6)):
		for each2 in range(len(let1)):
			for each3 in range(len(let3)):
				pass14.write(let6[each] + let1[each2] + let3[each3])
				pass14.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let3)):
			for each3 in range(len(let6)):
				pass14.write(let1[each] + let3[each2] + let6[each3])
				pass14.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let6)):
			for each3 in range(len(let3)):
				pass14.write(let1[each] + let6[each2] + let3[each3])
				pass14.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let1)):
			for each3 in range(len(let6)):
				pass14.write(let3[each] + let1[each2] + let6[each3])
				pass14.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let6)):
			for each3 in range(len(let1)):
				pass14.write(let3[each] + let6[each2] + let1[each3])
				pass14.write("\n")					
	
	# ------- lowercase 5 ---------------------------------------------------------------
	
	for each in range(len(let5)):
		for each2 in range(len(let5)):
			pass15.write(let5[each] + let5[each2])
			pass15.write("\n")
	for each in range(len(let5)):
		for each2 in range(len(let4)):
			for each3 in range(len(let1)):
				pass15.write(let5[each] + let4[each2] + let1[each3])
				pass15.write("\n")	
	for each in range(len(let5)):
		for each2 in range(len(let1)):
			for each3 in range(len(let4)):
				pass15.write(let5[each] + let1[each2] + let4[each3])
				pass15.write("\n")
	for each in range(len(let4)):
		for each2 in range(len(let1)):
			for each3 in range(len(let5)):
				pass15.write(let4[each] + let1[each2] + let5[each3])
				pass15.write("\n")
	for each in range(len(let4)):
		for each2 in range(len(let5)):
			for each3 in range(len(let1)):
				pass15.write(let4[each] + let5[each2] + let1[each3])
				pass15.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let5)):
			for each3 in range(len(let4)):
				pass15.write(let1[each] + let5[each2] + let4[each3])
				pass15.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let4)):
			for each3 in range(len(let5)):
				pass15.write(let1[each] + let4[each2] + let5[each3])
				pass15.write("\n")
				
				
	for each in range(len(let5)):
		for each2 in range(len(let2)):
			for each3 in range(len(let3)):
				pass15.write(let5[each] + let2[each2] + let3[each3])
				pass15.write("\n")	
	for each in range(len(let5)):
		for each2 in range(len(let3)):
			for each3 in range(len(let2)):
				pass15.write(let5[each] + let3[each2] + let2[each3])
				pass15.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let2)):
			for each3 in range(len(let5)):
				pass15.write(let3[each] + let2[each2] + let5[each3])
				pass15.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let5)):
			for each3 in range(len(let2)):
				pass15.write(let3[each] + let5[each2] + let2[each3])
				pass15.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let3)):
			for each3 in range(len(let5)):
				pass15.write(let2[each] + let3[each2] + let5[each3])
				pass15.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let5)):
			for each3 in range(len(let3)):
				pass15.write(let2[each] + let5[each2] + let3[each3])
				pass15.write("\n")	
				
######	-------------------------- 4 char -------------------	

	for each in range(len(let4)):
		for each2 in range(len(let4)):
			for each3 in range(len(let2)):
				pass15.write(let4[each] + let4[each2] + let2[each3])
				pass15.write("\n")
	for each in range(len(let4)):
		for each2 in range(len(let2)):
			for each3 in range(len(let4)):
				pass15.write(let4[each] + let2[each2] + let4[each3])
				pass15.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let4)):
			for each3 in range(len(let3)):
				pass15.write(let3[each] + let4[each2] + let3[each3])
				pass15.write("\n")
	for each in range(len(let4)):
		for each2 in range(len(let3)):
			for each3 in range(len(let3)):
				pass15.write(let4[each] + let3[each2] + let3[each3])
				pass15.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let3)):
			for each3 in range(len(let4)):
				pass15.write(let3[each] + let3[each2] + let4[each3])
				pass15.write("\n")						
							
	
														
	print ('\n')
	print ('Sequence Variables Lowercase 10 Character Complete')
	print ('\n')
		
# Sequence Variables lowercase 9 characters
def seqvarslower9():
	
	print ('\n')
	print ('Sequencing Variables Lowercase 9 Character')
	print ('\n')
	# ------- lowercase 9 ---------------------------------------------------------------
	for each in range(len(let9)):
		pass3.write(let9[each])
		pass3.write("\n")

	# -----	lowercase 8-------------------------------------------------------------------
	for each in range(len(let1)):
		for each2 in range(len(let8)):
			pass3.write(let1[each] + let8[each2])
			pass3.write("\n")
	for each in range(len(let8)):
		for each2 in range(len(let1)):
			pass3.write(let8[each] + let1[each2])
			pass3.write("\n")
	# -----	lowercase 7 ----------------------------------------------------------------------
	for each in range(len(let2)):
		for each2 in range(len(let7)):
			pass3.write(let2[each] + let7[each2])
			pass3.write("\n")
	for each in range(len(let7)):
		for each2 in range(len(let2)):
			pass3.write(let7[each] + let2[each2])
			pass3.write("\n")
	for each in range(len(let7)):
		for each2 in range(len(let1)):
			for each3 in range(len(let1)):
				pass3.write(let7[each] + let1[each2] + let1[each3])
				pass3.write("\n")	
	for each in range(len(let1)):
		for each2 in range(len(let1)):
			for each3 in range(len(let7)):
				pass3.write(let1[each] + let1[each2] + let7[each3])
				pass3.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let7)):
			for each3 in range(len(let1)):
				pass3.write(let1[each] + let7[each2] + let1[each3])
				pass3.write("\n")

       # ------ lowercase 6 ----------------------------------------------------------------------
	for each in range(len(let6)):
		for each2 in range(len(let1)):
			for each3 in range(len(let2)):
				pass3.write(let6[each] + let1[each2] + let2[each3])
				pass3.write("\n")	
	for each in range(len(let6)):
		for each2 in range(len(let2)):
			for each3 in range(len(let1)):
				pass3.write(let6[each] + let2[each2] + let1[each3])
				pass3.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let6)):
			for each3 in range(len(let2)):
				pass3.write(let1[each] + let6[each2] + let2[each3])
				pass3.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let6)):
			for each3 in range(len(let1)):
				pass3.write(let2[each] + let6[each2] + let1[each3])
				pass3.write("\n")	
	for each in range(len(let1)):
		for each2 in range(len(let2)):
			for each3 in range(len(let6)):
				pass3.write(let1[each] + let2[each2] + let6[each3])
				pass3.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let1)):
			for each3 in range(len(let6)):
				pass3.write(let2[each] + let1[each2] + let6[each3])
				pass3.write("\n")
	for each in range(len(let6)):
		for each2 in range(len(let3)):
				pass3.write(let6[each] + let3[each2])
				pass3.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let6)):
				pass3.write(let3[each] + let6[each2])
				pass3.write("\n")
	
	# ---------- lowercase 5 --------------------------------------------------------------------------

	for each in range(len(let5)):
		for each2 in range(len(let2)):
			for each3 in range(len(let2)):
				pass3.write(let5[each] + let2[each2] + let2[each3])
				pass3.write("\n")	
	for each in range(len(let2)):
		for each2 in range(len(let5)):
			for each3 in range(len(let2)):
				pass3.write(let2[each] + let5[each2] + let2[each3])
				pass3.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let2)):
			for each3 in range(len(let5)):
				pass3.write(let2[each] + let2[each2] + let5[each3])
				pass3.write("\n")
	for each in range(len(let5)):
		for each2 in range(len(let3)):
			for each3 in range(len(let1)):
				pass3.write(let5[each] + let3[each2] + let1[each3])
				pass3.write("\n")	
	for each in range(len(let5)):
		for each2 in range(len(let1)):
			for each3 in range(len(let3)):
				pass3.write(let5[each] + let1[each2] + let3[each3])
				pass3.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let5)):
			for each3 in range(len(let3)):
				pass3.write(let1[each] + let5[each2] + let3[each3])
				pass3.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let5)):
			for each3 in range(len(let1)):
				pass4.write(let3[each] + let5[each2] + let1[each3])
				pass4.write("\n")	
	for each in range(len(let1)):
		for each2 in range(len(let3)):
			for each3 in range(len(let5)):
				pass4.write(let1[each] + let3[each2] + let5[each3])
				pass4.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let1)):
			for each3 in range(len(let5)):
				pass4.write(let3[each] + let1[each2] + let5[each3])
				pass4.write("\n")
	
	# ------------lowercase 4 ----------------------------------------------------------------
	for each in range(len(let5)):
		for each2 in range(len(let4)):
				pass4.write(let5[each] + let4[each2])
				pass4.write("\n")
	for each in range(len(let4)):
		for each2 in range(len(let5)):
				pass4.write(let4[each] + let5[each2])
				pass4.write("\n")
	for each in range(len(let4)):
		for each2 in range(len(let4)):
			for each3 in range(len(let1)):
				pass4.write(let4[each] + let4[each2] + let1[each3])
				pass4.write("\n")
	for each in range(len(let4)):
		for each2 in range(len(let1)):
			for each3 in range(len(let4)):
				pass4.write(let4[each] + let1[each2] + let4[each3])
				pass4.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let4)):
			for each3 in range(len(let4)):
				pass4.write(let1[each] + let4[each2] + let4[each3])
				pass4.write("\n")
	

	

	print ('\n')
	print ('Sequence Variables Lowercase 9 Character Complete')
	print ('\n')

#  Sequence Variables First Cap 9 characters
def seqvarsCap9():
	
	print ('\n')
	print ('Sequencing Variables First Cap 9 Character')
	print ('\n')
	# ------- lowercase 9 ---------------------------------------------------------------
	for each in range(len(let9)):
		pass10.write(let9[each].capitalize())
		pass10.write("\n")

	# -----	lowercase 8-------------------------------------------------------------------
	for each in range(len(let1)):
		for each2 in range(len(let8)):
			pass10.write(let1[each].capitalize() + let8[each2])
			pass10.write("\n")
	for each in range(len(let8)):
		for each2 in range(len(let1)):
			pass10.write(let8[each].capitalize() + let1[each2])
			pass10.write("\n")
	# -----	lowercase 7 ----------------------------------------------------------------------
	for each in range(len(let2)):
		for each2 in range(len(let7)):
			pass10.write(let2[each].capitalize() + let7[each2])
			pass10.write("\n")
	for each in range(len(let7)):
		for each2 in range(len(let2)):
			pass10.write(let7[each].capitalize() + let2[each2])
			pass10.write("\n")
	for each in range(len(let7)):
		for each2 in range(len(let1)):
			for each3 in range(len(let1)):
				pass10.write(let7[each].capitalize() + let1[each2] + let1[each3])
				pass10.write("\n")	
	for each in range(len(let1)):
		for each2 in range(len(let1)):
			for each3 in range(len(let7)):
				pass10.write(let1[each].capitalize() + let1[each2] + let7[each3])
				pass10.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let7)):
			for each3 in range(len(let1)):
				pass10.write(let1[each].capitalize() + let7[each2] + let1[each3])
				pass10.write("\n")

       # ------ lowercase 6 ----------------------------------------------------------------------
	for each in range(len(let6)):
		for each2 in range(len(let1)):
			for each3 in range(len(let2)):
				pass10.write(let6[each].capitalize() + let1[each2] + let2[each3])
				pass10.write("\n")	
	for each in range(len(let6)):
		for each2 in range(len(let2)):
			for each3 in range(len(let1)):
				pass10.write(let6[each].capitalize() + let2[each2] + let1[each3])
				pass10.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let6)):
			for each3 in range(len(let2)):
				pass10.write(let1[each].capitalize() + let6[each2] + let2[each3])
				pass10.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let6)):
			for each3 in range(len(let1)):
				pass10.write(let2[each].capitalize() + let6[each2] + let1[each3])
				pass10.write("\n")	
	for each in range(len(let1)):
		for each2 in range(len(let2)):
			for each3 in range(len(let6)):
				pass10.write(let1[each].capitalize() + let2[each2] + let6[each3])
				pass10.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let1)):
			for each3 in range(len(let6)):
				pass10.write(let2[each].capitalize() + let1[each2] + let6[each3])
				pass10.write("\n")
	for each in range(len(let6)):
		for each2 in range(len(let3)):
				pass10.write(let6[each].capitalize() + let3[each2])
				pass10.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let6)):
				pass10.write(let3[each].capitalize() + let6[each2])
				pass10.write("\n")
	
	# ---------- lowercase 5 --------------------------------------------------------------------------

	for each in range(len(let5)):
		for each2 in range(len(let2)):
			for each3 in range(len(let2)):
				pass10.write(let5[each].capitalize() + let2[each2] + let2[each3])
				pass10.write("\n")	
	for each in range(len(let2)):
		for each2 in range(len(let5)):
			for each3 in range(len(let2)):
				pass10.write(let2[each].capitalize() + let5[each2] + let2[each3])
				pass10.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let2)):
			for each3 in range(len(let5)):
				pass10.write(let2[each].capitalize() + let2[each2] + let5[each3])
				pass10.write("\n")
	for each in range(len(let5)):
		for each2 in range(len(let3)):
			for each3 in range(len(let1)):
				pass10.write(let5[each].capitalize() + let3[each2] + let1[each3])
				pass10.write("\n")	
	for each in range(len(let5)):
		for each2 in range(len(let1)):
			for each3 in range(len(let3)):
				pass10.write(let5[each].capitalize() + let1[each2] + let3[each3])
				pass10.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let5)):
			for each3 in range(len(let3)):
				pass10.write(let1[each].capitalize() + let5[each2] + let3[each3])
				pass10.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let5)):
			for each3 in range(len(let1)):
				pass11.write(let3[each].capitalize() + let5[each2] + let1[each3])
				pass11.write("\n")	
	for each in range(len(let1)):
		for each2 in range(len(let3)):
			for each3 in range(len(let5)):
				pass11.write(let1[each].capitalize() + let3[each2] + let5[each3])
				pass11.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let1)):
			for each3 in range(len(let5)):
				pass11.write(let3[each].capitalize() + let1[each2] + let5[each3])
				pass11.write("\n")
				
# ------------lowercase 4 ----------------------------------------------------------------
	for each in range(len(let5)):
		for each2 in range(len(let4)):
				pass11.write(let5[each].capitalize() + let4[each2])
				pass11.write("\n")
	for each in range(len(let4)):
		for each2 in range(len(let5)):
				pass11.write(let4[each].capitalize() + let5[each2])
				pass11.write("\n")
	for each in range(len(let4)):
		for each2 in range(len(let4)):
			for each3 in range(len(let1)):
				pass11.write(let4[each].capitalize() + let4[each2] + let1[each3])
				pass11.write("\n")
	for each in range(len(let4)):
		for each2 in range(len(let1)):
			for each3 in range(len(let4)):
				pass11.write(let4[each].capitalize() + let1[each2] + let4[each3])
				pass11.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let4)):
			for each3 in range(len(let4)):
				pass11.write(let1[each].capitalize() + let4[each2] + let4[each3])
				pass11.write("\n")
	
	for each in range(len(let2)):
		for each2 in range(len(let3)):
			for each3 in range(len(let4)):
				pass11.write(let2[each].capitalize() + let3[each2] + let4[each3])
				pass11.write("\n")
	for each in range(len(let4)):
		for each2 in range(len(let3)):
			for each3 in range(len(let2)):
				pass11.write(let4[each].capitalize() + let3[each2] + let2[each3])
				pass11.write("\n")	
	for each in range(len(let4)):
		for each2 in range(len(let2)):
			for each3 in range(len(let3)):
				pass11.write(let4[each].capitalize() + let2[each2] + let3[each3])
				pass11.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let2)):
			for each3 in range(len(let4)):
				pass11.write(let3[each].capitalize() + let2[each2] + let4[each3])
				pass11.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let4)):
			for each3 in range(len(let2)):
				pass11.write(let3[each].capitalize() + let4[each2] + let2[each3])
				pass11.write("\n")	
	for each in range(len(let2)):
		for each2 in range(len(let3)):
			for each3 in range(len(let4)):
				pass11.write(let2[each].capitalize() + let3[each2] + let4[each3])
				pass11.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let4)):
			for each3 in range(len(let3)):
				pass11.write(let2[each].capitalize() + let4[each2] + let3[each3])
				pass11.write("\n")

	print ('\n')
	print ('Sequence Variables First Cap 9 Character Complete')
	print ('\n')


# Sequence Variables lowercase 8 character
def seqvarslower8():
	
	print ('\n')
	print ('Sequencing Variables Lowercase 8 Character')
	print ('\n')
	# -------------	lowercase 8 --------------------------------------------------------
	for each in range(len(let8)):
		pass1.write(let8[each])
		pass1.write("\n")

	# -----	lowercase 7-------------------------------------------------------------------
	for each in range(len(let1)):
		for each2 in range(len(let7)):
			pass1.write(let1[each] + let7[each2])
			pass1.write("\n")
	for each in range(len(let7)):
		for each2 in range(len(let1)):
			pass1.write(let7[each] + let1[each2])
			pass1.write("\n")
	# -----	lowercase 6 ----------------------------------------------------------------------
	for each in range(len(let2)):
		for each2 in range(len(let6)):
			pass1.write(let2[each] + let6[each2])
			pass1.write("\n")
	for each in range(len(let6)):
		for each2 in range(len(let2)):
			pass1.write(let6[each] + let2[each2])
			pass1.write("\n")
	for each in range(len(let6)):
		for each2 in range(len(let1)):
			for each3 in range(len(let1)):
				pass1.write(let6[each] + let1[each2] + let1[each3])
				pass1.write("\n")	
	for each in range(len(let1)):
		for each2 in range(len(let1)):
			for each3 in range(len(let6)):
				pass1.write(let1[each] + let1[each2] + let6[each3])
				pass1.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let6)):
			for each3 in range(len(let1)):
				pass1.write(let1[each] + let6[each2] + let1[each3])
				pass1.write("\n")

	# -----	lowercase 5 ------------------------------------------------------------------------------------------
	for each in range(len(let5)):
		for each2 in range(len(let3)):
			pass1.write(let5[each] + let3[each2])
			pass1.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let5)):
			pass1.write(let3[each] + let5[each2])
			pass1.write("\n")
	for each in range(len(let5)):
		for each2 in range(len(let1)):
			for each3 in range(len(let2)):
				pass1.write(let5[each] + let1[each2] + let2[each3])
				pass1.write("\n")
	for each in range(len(let5)):
		for each2 in range(len(let2)):
			for each3 in range(len(let1)):
				pass1.write(let5[each] + let2[each2] + let1[each3])
				pass1.write("\n")
	
	for each in range(len(let2)):
		for each2 in range(len(let1)):
			for each3 in range(len(let5)):
				pass1.write(let2[each] + let1[each2] + let5[each3])
				pass1.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let5)):
			for each3 in range(len(let2)):
				pass1.write(let1[each] + let5[each2] + let2[each3])
				pass1.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let2)):
			for each3 in range(len(let5)):
				pass1.write(let1[each] + let2[each2] + let5[each3])
				pass1.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let5)):
			for each3 in range(len(let1)):
				pass1.write(let2[each] + let5[each2] + let1[each3])
				pass1.write("\n")

	# --------- lowercase 4 ----------------------------------------------------------------------------------

	for each in range(len(let4)):
		for each2 in range(len(let2)):
			for each3 in range(len(let2)):
				pass1.write(let4[each] + let2[each2] + let2[each3])
				pass1.write("\n")
	for each in range(len(let4)):
		for each2 in range(len(let1)):
			for each3 in range(len(let3)):
				pass1.write(let4[each] + let1[each2] + let3[each3])
				pass1.write("\n")	
	for each in range(len(let4)):
		for each2 in range(len(let3)):
			for each3 in range(len(let1)):
				pass1.write(let4[each] + let3[each2] + let1[each3])	
				pass1.write("\n")

	for each in range(len(let1)):
		for each2 in range(len(let4)):
			for each3 in range(len(let3)):
				pass1.write(let1[each] + let4[each2] + let3[each3])
				pass1.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let3)):
			for each3 in range(len(let4)):
				pass1.write(let1[each] + let3[each2] + let4[each3])
				pass1.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let1)):
			for each3 in range(len(let4)):
				pass1.write(let3[each] + let1[each2] + let4[each3])
				pass1.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let4)):
			for each3 in range(len(let1)):
				pass1.write(let3[each] + let4[each2] + let1[each3])
				pass1.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let4)):
			for each3 in range(len(let2)):
				pass1.write(let2[each] + let4[each2] + let2[each3])
				pass1.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let2)):
			for each3 in range(len(let4)):
				pass1.write(let2[each] + let2[each2] + let4[each3])
				pass1.write("\n")

	# --------lowercase 3----------------------------------------------------------------------------------------------
	for each in range(len(let2)):
		for each2 in range(len(let3)):
			for each3 in range(len(let3)):
				pass1.write(let2[each] + let3[each2] + let3[each3])
				pass1.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let2)):
			for each3 in range(len(let3)):
				pass1.write(let3[each] + let2[each2] + let3[each3])
				pass1.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let3)):
			for each3 in range(len(let2)):
				pass1.write(let3[each] + let3[each2] + let2[each3])
				pass1.write("\n")


	print ('\n')
	print ('Sequence Variables Lowercase 8 Character Complete')
	print ('\n')
	#--------------------------------------------------------------------------------------------------------
	
	
	
# Sequence Variables lowercase 8 plus nums character
def seqvarslower8plusnums():
	
	print ('\n')
	print ('Sequencing Variables Lowercase 8 plus nums Character')
	print ('\n')


	# -----	lowercase 7-------------------------------------------------------------------
	for each in range(len(nums)):
		for each2 in range(len(let7)):
			pass5.write(nums[each] + let7[each2])
			pass5.write("\n")
	for each in range(len(let7)):
		for each2 in range(len(nums)):
			pass5.write(let7[each] + nums[each2])
			pass5.write("\n")
	# -----	lowercase 6 ----------------------------------------------------------------------
	for each in range(len(let6)):
		for each2 in range(len(nums)):
			for each3 in range(len(nums)):
				pass5.write(let6[each] + nums[each2] + nums[each3])
				pass5.write("\n")	
	for each in range(len(nums)):
		for each2 in range(len(nums)):
			for each3 in range(len(let6)):
				pass5.write(nums[each] + nums[each2] + let6[each3])
				pass5.write("\n")
	for each in range(len(nums)):
		for each2 in range(len(let6)):
			for each3 in range(len(nums)):
				pass5.write(nums[each] + let6[each2] + nums[each3])
				pass5.write("\n")

	# -----	lowercase 5 ------------------------------------------------------------------------------------------
	
	for each in range(len(let5)):
		for each2 in range(len(nums)):
			for each3 in range(len(let2)):
				pass5.write(let5[each] + nums[each2] + let2[each3])
				pass5.write("\n")
	for each in range(len(let5)):
		for each2 in range(len(let2)):
			for each3 in range(len(nums)):
				pass5.write(let5[each] + let2[each2] + nums[each3])
				pass5.write("\n")
	
	for each in range(len(let2)):
		for each2 in range(len(nums)):
			for each3 in range(len(let5)):
				pass5.write(let2[each] + nums[each2] + let5[each3])
				pass5.write("\n")
	for each in range(len(nums)):
		for each2 in range(len(let5)):
			for each3 in range(len(let2)):
				pass5.write(nums[each] + let5[each2] + let2[each3])
				pass5.write("\n")
	for each in range(len(nums)):
		for each2 in range(len(let2)):
			for each3 in range(len(let5)):
				pass5.write(nums[each] + let2[each2] + let5[each3])
				pass5.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let5)):
			for each3 in range(len(nums)):
				pass5.write(let2[each] + let5[each2] + nums[each3])
				pass5.write("\n")

	# --------- lowercase 4 ----------------------------------------------------------------------------------

	for each in range(len(let4)):
		for each2 in range(len(nums)):
			for each3 in range(len(let3)):
				pass5.write(let4[each] + nums[each2] + let3[each3])
				pass5.write("\n")	
	for each in range(len(let4)):
		for each2 in range(len(let3)):
			for each3 in range(len(nums)):
				pass5.write(let4[each] + let3[each2] + nums[each3])	
				pass5.write("\n")

	for each in range(len(nums)):
		for each2 in range(len(let4)):
			for each3 in range(len(let3)):
				pass5.write(nums[each] + let4[each2] + let3[each3])
				pass5.write("\n")
	for each in range(len(nums)):
		for each2 in range(len(let3)):
			for each3 in range(len(let4)):
				pass5.write(nums[each] + let3[each2] + let4[each3])
				pass5.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(nums)):
			for each3 in range(len(let4)):
				pass5.write(let3[each] + nums[each2] + let4[each3])
				pass5.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let4)):
			for each3 in range(len(nums)):
				pass5.write(let3[each] + let4[each2] + nums[each3])
				pass5.write("\n")



	print ('\n')
	print ('Sequence Variables Lowercase 8 plus nums Character Complete')
	print ('\n')
	#--------------------------------------------------------------------------------------------------------	
	
# Sequence Variables lowercase 8 plus special character
def seqvarslower8plusspec():
	
	print ('\n')
	print ('Sequencing Variables Lowercase 8 plus special Character')
	print ('\n')


	# -----	lowercase 7-------------------------------------------------------------------
	for each in range(len(spec)):
		for each2 in range(len(let7)):
			pass6.write(spec[each] + let7[each2])
			pass6.write("\n")
	for each in range(len(let7)):
		for each2 in range(len(spec)):
			pass6.write(let7[each] + spec[each2])
			pass6.write("\n")
	# -----	lowercase 6 ----------------------------------------------------------------------
	for each in range(len(let6)):
		for each2 in range(len(spec)):
			for each3 in range(len(spec)):
				pass6.write(let6[each] + spec[each2] + spec[each3])
				pass6.write("\n")	
	for each in range(len(spec)):
		for each2 in range(len(spec)):
			for each3 in range(len(let6)):
				pass6.write(spec[each] + spec[each2] + let6[each3])
				pass6.write("\n")
	for each in range(len(spec)):
		for each2 in range(len(let6)):
			for each3 in range(len(spec)):
				pass6.write(spec[each] + let6[each2] + spec[each3])
				pass6.write("\n")

	# -----	lowercase 5 ------------------------------------------------------------------------------------------
	
	for each in range(len(let5)):
		for each2 in range(len(spec)):
			for each3 in range(len(let2)):
				pass6.write(let5[each] + spec[each2] + let2[each3])
				pass6.write("\n")
	for each in range(len(let5)):
		for each2 in range(len(let2)):
			for each3 in range(len(spec)):
				pass6.write(let5[each] + let2[each2] + spec[each3])
				pass6.write("\n")
	
	for each in range(len(let2)):
		for each2 in range(len(spec)):
			for each3 in range(len(let5)):
				pass6.write(let2[each] + spec[each2] + let5[each3])
				pass6.write("\n")
	for each in range(len(spec)):
		for each2 in range(len(let5)):
			for each3 in range(len(let2)):
				pass6.write(spec[each] + let5[each2] + let2[each3])
				pass6.write("\n")
	for each in range(len(spec)):
		for each2 in range(len(let2)):
			for each3 in range(len(let5)):
				pass6.write(spec[each] + let2[each2] + let5[each3])
				pass6.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let5)):
			for each3 in range(len(spec)):
				pass6.write(let2[each] + let5[each2] + spec[each3])
				pass6.write("\n")

	# --------- lowercase 4 ----------------------------------------------------------------------------------

	for each in range(len(let4)):
		for each2 in range(len(spec)):
			for each3 in range(len(let3)):
				pass6.write(let4[each] + spec[each2] + let3[each3])
				pass6.write("\n")	
	for each in range(len(let4)):
		for each2 in range(len(let3)):
			for each3 in range(len(spec)):
				pass6.write(let4[each] + let3[each2] + spec[each3])	
				pass6.write("\n")

	for each in range(len(spec)):
		for each2 in range(len(let4)):
			for each3 in range(len(let3)):
				pass6.write(spec[each] + let4[each2] + let3[each3])
				pass6.write("\n")
	for each in range(len(spec)):
		for each2 in range(len(let3)):
			for each3 in range(len(let4)):
				pass6.write(spec[each] + let3[each2] + let4[each3])
				pass6.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(spec)):
			for each3 in range(len(let4)):
				pass6.write(let3[each] + spec[each2] + let4[each3])
				pass6.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let4)):
			for each3 in range(len(spec)):
				pass6.write(let3[each] + let4[each2] + spec[each3])
				pass6.write("\n")



	print ('\n')
	print ('Sequence Variables Lowercase 8 plus spec Character Complete')
	print ('\n')
	#--------------------------------------------------------------------------------------------------------
	
	
	
# Sequence Variables lowercase 8 character First Cap
def seqvarsCap8():

	print ('\n')
	print ('Sequencing Variables First Cap 8 Character')
	print ('\n')
	
	# -------------	lowercase 8 --------------------------------------------------------
	for each in range(len(let8)):
		pass2.write(let8[each].capitalize())
		pass2.write("\n")	

	# -----	lowercase 7-------------------------------------------------------------------
	for each in range(len(let1)):
		for each2 in range(len(let7)):
			pass2.write(let1[each].capitalize() + let7[each2])
			pass2.write("\n")

	for each in range(len(let7)):
		for each2 in range(len(let1)):
			pass2.write(let7[each].capitalize() + let1[each2])
			pass2.write("\n")
	
	# -----	lowercase 6 ----------------------------------------------------------------------
	for each in range(len(let2)):
		for each2 in range(len(let6)):
			pass2.write(let2[each].capitalize() + let6[each2])
			pass2.write("\n")
	for each in range(len(let6)):
		for each2 in range(len(let2)):
			pass2.write(let6[each].capitalize() + let2[each2])
			pass2.write("\n")
	for each in range(len(let6)):
		for each2 in range(len(let1)):
			for each3 in range(len(let1)):
				pass2.write(let6[each].capitalize() + let1[each2] + let1[each3])	
				pass2.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let1)):
			for each3 in range(len(let6)):
				pass2.write(let1[each].capitalize() + let1[each2] + let6[each3])
				pass2.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let6)):
			for each3 in range(len(let1)):
				pass2.write(let1[each].capitalize() + let6[each2] + let1[each3])
				pass2.write("\n")

	# -----	lowercase 5 ------------------------------------------------------------------------------------------
	for each in range(len(let5)):
		for each2 in range(len(let3)):
			pass2.write(let5[each].capitalize() + let3[each2])
			pass2.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let5)):
			pass2.write(let3[each].capitalize() + let5[each2])
			pass2.write("\n")
	for each in range(len(let5)):
		for each2 in range(len(let1)):
			for each3 in range(len(let2)):
				pass2.write(let5[each].capitalize() + let1[each2] + let2[each3])
				pass2.write("\n")
	for each in range(len(let5)):
		for each2 in range(len(let2)):
			for each3 in range(len(let1)):
				pass2.write(let5[each].capitalize() + let2[each2] + let1[each3])
				pass2.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let1)):
			for each3 in range(len(let5)):
				pass2.write(let2[each].capitalize() + let1[each2] + let5[each3])
				pass2.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let5)):
			for each3 in range(len(let2)):
				pass2.write(let1[each].capitalize() + let5[each2] + let2[each3])
				pass2.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let2)):
			for each3 in range(len(let5)):
				pass2.write(let1[each].capitalize() + let2[each2] + let5[each3])
				pass2.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let5)):
			for each3 in range(len(let1)):
				pass2.write(let2[each].capitalize() + let5[each2] + let1[each3])
				pass2.write("\n")

	# --------- lowercase 4 ----------------------------------------------------------------------------------
	
	for each in range(len(let4)):
		for each2 in range(len(let2)):
			for each3 in range(len(let2)):
				pass2.write(let4[each].capitalize() + let2[each2] + let2[each3])
				pass2.write("\n")
	for each in range(len(let4)):
		for each2 in range(len(let1)):
			for each3 in range(len(let3)):
				pass2.write(let4[each].capitalize() + let1[each2] + let3[each3])	
				pass2.write("\n")
	for each in range(len(let4)):
		for each2 in range(len(let3)):
			for each3 in range(len(let1)):
				pass2.write(let4[each].capitalize() + let3[each2] + let1[each3])
				pass2.write("\n")		
	for each in range(len(let1)):
		for each2 in range(len(let4)):
			for each3 in range(len(let3)):
				pass2.write(let1[each].capitalize() + let4[each2] + let3[each3])
				pass2.write("\n")
	for each in range(len(let1)):
		for each2 in range(len(let3)):
			for each3 in range(len(let4)):
				pass2.write(let1[each].capitalize() + let3[each2] + let4[each3])
				pass2.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let1)):
			for each3 in range(len(let4)):
				pass2.write(let3[each].capitalize() + let1[each2] + let4[each3])
				pass2.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let4)):
			for each3 in range(len(let1)):
				pass2.write(let3[each].capitalize() + let4[each2] + let1[each3])
				pass2.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let4)):
			for each3 in range(len(let2)):
				pass2.write(let2[each].capitalize() + let4[each2] + let2[each3])
				pass2.write("\n")
	for each in range(len(let2)):
		for each2 in range(len(let2)):
			for each3 in range(len(let4)):
				pass2.write(let2[each].capitalize() + let2[each2] + let4[each3])
				pass2.write("\n")
	for each in range(len(let4)):
		for each2 in range(len(let4)):
			pass2.write(let4[each].capitalize() + let4[each2])
			pass2.write("\n")

	# --------lowercase 3----------------------------------------------------------------------------------------------
	for each in range(len(let2)):
		for each2 in range(len(let3)):
			for each3 in range(len(let3)):
				pass2.write(let2[each].capitalize() + let3[each2] + let3[each3])
				pass2.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let2)):
			for each3 in range(len(let3)):
				pass2.write(let3[each].capitalize() + let2[each2] + let3[each3])
				pass2.write("\n")
	for each in range(len(let3)):
		for each2 in range(len(let3)):
			for each3 in range(len(let2)):
				pass2.write(let3[each].capitalize() + let3[each2] + let2[each3])
				pass2.write("\n")


	print ('\n')
	print ('Sequence Variables First Cap 8 Character Complete')
	print ('\n')

	#--------------------------------------------------------------------------------------------------------
		

# Writing to the output.txt
def writeOutput():
	for each in range(len(let1)):
		output.write(let1[each])
		output.write("\n")
	for each in range(len(let2)):
		output.write(let2[each])
		output.write("\n")		
	for each in range(len(let3)):
		output.write(let3[each])
		output.write("\n")		
	for each in range(len(let4)):
		output.write(let4[each])
		output.write("\n")
	for each in range(len(let5)):
		output.write(let5[each])
		output.write("\n")		
	for each in range(len(let6)):
		output.write(let6[each])		
		output.write("\n")
	for each in range(len(let7)):
		output.write(let7[each])
		output.write("\n")		
	for each in range(len(let8)):
		output.write(let8[each])
		output.write("\n")		
	for each in range(len(let9)):
		output.write(let9[each])
		output.write("\n")		
	for each in range(len(let10)):
		output.write(let10[each])
		output.write("\n")		
	for each in range(len(let11)):
		output.write(let11[each])
		output.write("\n")		
	for each in range(len(let12)):
		output.write(let12[each])
		output.write("\n")		
	for each in range(len(let13)):
		output.write(let13[each])
		output.write("\n")		
	for each in range(len(let14)):
		output.write(let14[each])
		output.write("\n")		
	for each in range(len(over)):
		output.write(over[each])
		output.write("\n")	
	print (' OUTPUT DONE ')
					

# What ppl see when they start the program :)
def mainmenu():

	
	os.system('clear')
	print ('\n')
	print ("                                          PWD HAX               January 7th,2025\n\n\n\n\n")
	print ('\n')
	print ('1 Letter Words  = ',len(let1)) 
	print ('2 Letter Words  = ',len(let2))
	print ('3 Letter Words  = ',len(let3))
	print ('4 Letter Words  = ',len(let4))
	print ('5 Letter Words  = ',len(let5))
	print ('6 Letter Words  = ',len(let6))
	print ('7 Letter Words  = ',len(let7))
	print ('8 Letter Words  = ',len(let8))
	print ('9 Letter Words  = ',len(let9))
	print ('10 Letter Words = ',len(let10))
	print ('11 Letter Words = ',len(let11))
	print ('12 Letter Words = ',len(let12))
	print ('13 Letter Words = ',len(let13))
	print ('14 Letter Words = ',len(let14))
	print ('Over 14 Letters = ',len(over))
	print ('')
	print ('Total Words = ', len(let1) + len(let2) + len(let3) + len(let4) + len(let5) + len(let6) + len(let7) + len(let8) + len(let9) + len(let10) + len(let11) + len(let12) + len(let13) + len(let14) + len(over))
	print ('\n')
	print ('\n')
	print ('(c)ompile Wordlists, (e)dit Wordlists, (f)insh, e(x)it ')
	print ('\n')
	target=input("Enter your Choice : ")
	if target=="c":
		writeOutput()
		seqvarslower8()
		seqvarslower8plusnums()
		seqvarslower8plusspec()
		seqvarsCap8()
		seqvarslower9()
		seqvarsCap9()
		seqvarslower10()
	elif target=="e":
		os.system('clear')
		editWordlist()
	elif target=="f":
		writeOutput()
		mainmenu()
	elif target=="x":
		print()
		print()
		print('Goodbye')
		exit()
	else:
		mainmenu()		   

#Start Program
mainmenu()




