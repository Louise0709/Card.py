import random
card_turple=('Spiderman','Ironman','Loki','Thor','Cap')
package=[]
while 1:	
	choice=int(input('1.draw a card\n 2.look into the bag\n 3.arrange the bag.4.leave\n Which number do you choose?'))

	if choice ==1:
		num =int(input('how many times?'))
		for i in range(0,num):
			n= random.randint(0,5)
			packge.append(card_turple[n])
			print('you got{}'.format(card_turple[n]))	
			print('put {} in in the bag already'.format(card_turple[i]))
			print('--------------------') 		
	if choice ==2:
		if  len(packge)==0:
			print('nothing here')
			print('--------------------')
			
		else:
			for i in package:
				print(i)
				print('--------------------')
	if choice==3:
		if len(package)==0:
			print('nothing here'0
		else:
	        	package.sort
			for i in package:
				print(i)
