import random
card_turple=('Spiderman','Ironman','Loki','Thor','Cap')
package=[]
while 1:	
	choice=int(input('1.draw a card\n 2.look into the bag\n 3.arrange the bag\n 4.leave.\n Which number do you choose?'))

	if choice ==1:
		num =int(input('how many times?'))
		for i in range(0,num):
			n= random.randint(0,5)
			print('you got{}'.format(card_turple[n]))
			package.append(card_turple[n])
			print('put {} in in the bag already'.format(card_turple[n]))		
	if choice ==2:
		if len(package)==0:
			print('nothing here')
		else:
			print(package)
	if choice ==3:
		if len(package)==0:
			print('nothing here')
		else:
			package.sort()
			for i in package:
				print(i)
	if choice==4:
		break	
