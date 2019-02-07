import csv ,os

x_mean = y_mean =0
x_sum = y_sum =0
x_diff_sq = y_diff_sq=0
x_diff_m_y_diff =0


with open ('abc.csv','r+',newline='') as f:
	r= csv.reader(f)
	data = list(r)
	
	x= int(input('Enter value of X:'))	
	
	n= len(data)
	if len(data)<4:
		print('Training data is too less to predict Y!!!')
		y=int(input("Enter value for Y:"))
		w=csv.writer(f)
		w.writerow([x,y])
	else:
		f.seek(5)
		r= csv.reader(f)
		data1= list(r)

		for line in data1:
			x_sum += float(line[0])
			y_sum += float(line[1])
		x_mean = x_sum/(n-1)
		y_mean = y_sum/(n-1)


		for line in data1:
			x1= float(line[0]) - x_mean
			y1= float(line[1]) - y_mean
			x_diff_sq	+= (x1 **2)
			y_diff_sq	+= (y1 **2)
			x_diff_m_y_diff += (x1*y1)		

		r = x_diff_m_y_diff	/(x_diff_sq	* y_diff_sq)**(1/2)
		sy =(y_diff_sq/(n-1))**(1/2)
		sx =(x_diff_sq/(n-1))**(1/2)


		B =(sy/sx)*r
		A = y_mean -(B*x_mean)

		y_ass = A +B*x
		print('The Predcted value of Y for X = {} is: {}'.format(x,y_ass))
		print()
		ind = True	
		while ind == True:
			ind = False
			opt = input('Do You want to Update the predicted value in file or Ignore(Y|N|I):').upper()
			if opt == 'Y':
				w = csv.writer(f)
				w.writerow([x,y_ass])
			elif opt == 'N':
				y=float(input("Enter value for Y:"))
				w=csv.writer(f)
				w.writerow([x,y])
			elif opt == 'I':
				os._exit(0)
			else:
				print('invalid input.... Try again!!!')
				print()
				ind = True
