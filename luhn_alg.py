card_num = raw_input("Jumlah Kartu > ")
card_num = int(card_num)
for x in range(0, card_num):
    credit_card = raw_input("Kartu %d> " % (x+1))
    credit_card = credit_card.replace("-", "")
    y = 0
    wildcard = 0
    odd_add = 0
    even_add = 0
    count = 0
    """ 
    - Double value in even position and add it to even_add
    - If doubled value > 9 do doubled value mod 10 + 1
    - Add value in odd position to odd_add
	"""
    while (y < len(credit_card)):
    	if(credit_card[y] == '?'):
    		wildcard += 1
    	else:
    		if(y % 2 == 0):
    			temp = int(credit_card[y]) * 2
    			if(temp > 9):
    				temp = (temp % 10) + 1
    			even_add += temp
    		else:
    			odd_add += int(credit_card[y])
    	y+=1
    """ 
    - Add odd position and even position as total
    - Add total with generated number from the loop
    - if valid count add by 1
	"""
    if (wildcard>0):
    	if(wildcard == 1):
    		for a in range(0,10):
    			valid = (odd_add + even_add + a) % 10 == 0
    			if(valid) :
    				count += 1
    	elif(wildcard == 2):
    		for a in range(0,10):
    			for b in range(0,10):
    				valid = (odd_add + even_add + a + b) % 10 == 0
    				if(valid) :
    					count += 1
    	elif(wildcard == 3):
    		for a in range(0,10):
    			for b in range(0,10):
	    			for c in range(0,10):
	    				valid = (odd_add + even_add + a + b + c) % 10 == 0
	    				if(valid) :
    						count += 1
    	elif(wildcard == 4):
    		for a in range(0,10):
    			for b in range(0,10):
	    			for c in range(0,10):
	    				for d in range(0,10):
		    				valid = (odd_add + even_add + a + b + c + d) % 10 == 0
		    				if(valid) :
    							count += 1
    else:
    	valid = (odd_add + even_add) % 10 == 0
    	if(valid):
    		count += 1
    print("Output Kartu %d> %d" % (x+1, int(count)))
