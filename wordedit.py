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
