# luhn-algorithm
Implementation of Luhn Algorithm in credit card

# Specification
* The maximum number of cards to be checked is 10
* Every credit card number has formed XXXX-XXXX-XXXX-XXXX
* You can use wildcard characters '?' in credit card number and it can spawn everywhere
* Wildcard characters means you can change '?' with numbers from 0 to 9
* The maximum number of wildcard characters is 4

# How To Use
* Open luhn_alg.py using python

	```sh
	$ python luhn_alg.py
	```
* Input number of cards to be checked (i.e. 2) and press Enter
	
	```python
	Jumlah Kartu > 2
	```
* Input credit card number to be checked and press Enter
	
	```python
	Kartu 1> 4111-1111-1111-1111
	Kartu 2> 4111-1111-1111-11?2
	```
* After that the program will show you the numbers of the valid credit card number from the input
	
	```python
	Output Kartu 1> 1
	Output Kartu 2> 1
	```

# How It Works
* Suppose the credit card number is 4111-1111-1111-1111
* For every number in even position double it
* If the number bigger than 9 do the number modulo with 10 and add it by 1
    
    | Position             | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
  	|----------------------|---|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|
    | Credit Card Number   | 4 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1  | 1  | 1  | 1  | 1  | 1  |
    | Double even position | 8 | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 2  | 1  | 2  | 1  | 2  | 1  |
* Add all the numbers in the position 0 to 15

    8 + 1 + 2 + 1 + 2 + 1 + 2 + 1 + 2 + 1 + 2 + 1 + 2 + 1 + 2 + 1 = 30
* If the addition modulo with 10 resulting 0 then credit card number is valid, else credit card number is invalid

    30 mod 10 = 0 (Valid)

# How Wildcard Works
* Count the number of wildcard appeared in credit card number
* Add the numbers in odd position and even position as total
* Do iteration numbers of wildcard times and add it with total
* If the addition modulo with 10 resulting 0 then credit card number is valid and counter add by 1
* Repeat iteration if in range 0 to 9

# Source
* [Wikipedia](https://en.wikipedia.org/wiki/Luhn_algorithm)
* [Rosseta](http://rosettacode.org/wiki/Luhn_test_of_credit_card_numbers)