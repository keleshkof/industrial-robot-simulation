from time import sleep

class Control:

	def __init__(self):
		self.robot_1 = [100,20,30,50]
		self.robot_2 = [50,100,20,30]
		self.robot_3 = [30,50,100,20]
		self.robot_4 = [20,30,50,100]
		self.amount = [0,0,0,0]

	def get_robot(self,n,m):
		if(n==0):
			return self.robot_1[m]
		elif(n==1):
			return self.robot_2[m]
		elif(n==2):
			return self.robot_3[m]
		elif(n==3):
			return self.robot_4[m]

	def res_amount(self):
		self.amount = [0,0,0,0]

	def get_amount(self,n):
		return self.amount[n]

	def set_amount(self,n,value):
		self.amount[n] = value

class Main:

	def __init__(self):
		self.pl_1 = list(range(4))
		self.pl_2 = list(range(4))
		self.pl_3 = list(range(4))
		self.pl_4 = list(range(4))
		self.con = Control()

	def get_pl(self,n):
		if(n == 0):
			return self.pl_1
		elif(n == 1):
			return self.pl_2
		elif(n == 2):
			return self.pl_3
		elif(n == 3):
			return self.pl_4

	def set_pl(self,n,m,value):
		if(n == 0):
			self.pl_1[m] = value
		elif(n == 1):
			self.pl_2[m] = value
		elif(n == 2):
			self.pl_3[m] = value
		elif(n == 3):
			self.pl_4[m] = value

	def read_PL(self):
		f_1 = open("PL1.txt","r")
		f_2 = open("PL2.txt","r")
		f_3 = open("PL3.txt","r")
		f_4 = open("PL4.txt","r")

		for i in range(4):
			w = f_1.readline()
			w = w.split(" ")
			self.pl_1[i] = int(w[1])

			w = f_2.readline()
			w = w.split(" ")
			self.pl_2[i] = int(w[1])

			w = f_3.readline()
			w = w.split(" ")
			self.pl_3[i] = int(w[1])

			w = f_4.readline()
			w = w.split(" ")
			self.pl_4[i] = int(w[1])

		f_1.close()
		f_2.close()
		f_3.close()
		f_4.close()

	def start(self):
		C = self.con
		countlist = [0,0,0,0]
		for i in range(4):
			inventory = [0,0,0,0]
			self.read_PL()
			flag = True
			rb1 = C.get_robot(i,0)
			rb2 = C.get_robot(i,1)
			rb3 = C.get_robot(i,2)
			rb4 = C.get_robot(i,3)
			print("------------")
			print("\nRobot",i+1)
			print("Robot Capacity:",rb1,rb2,rb3,rb4)
			while(flag):
				print("\ntime:",countlist[i])
				print("\nInventory:",inventory)
				for k in range(4):
					rb1 = C.get_robot(i,0)
					a1 = C.get_amount(0)
					rb2 = C.get_robot(i,1)
					a2 = C.get_amount(1)
					rb3 = C.get_robot(i,2)
					a3 = C.get_amount(2)
					rb4 = C.get_robot(i,3)
					a4 = C.get_amount(3)
					PL = self.get_pl(k)
					print("PL ",k+1,":",PL)
					if(rb1 > a1 or rb2 > a2 or rb3 > a3 or rb4 > a4):
						for j in range(4):
							robot = C.get_robot(i,j)
							amount = C.get_amount(j)
							pl = PL[j]
							if(amount != robot):
								if(amount < robot):
									if(robot < pl):
										amount += pl
										if(amount >= robot):
											amount = robot
										pl -= amount
										if(pl < 0):
											pl = 0
									else:
										amount += pl
										if(amount > robot):
											keeper = amount - robot
											amount = robot
										else:
											keeper = 0
										pl = keeper
								countlist[i] += 2
							else:
								countlist[i] += 1
							C.set_amount(j,amount)
							self.set_pl(k,j,pl)
					print("Capacity:","-",a1,"-",a2,"-",a3,"-",a4,"-")
					sleep(1/2)
				countlist[i] += 10
				count = 0
				for a in range(4):
					if(C.get_amount(a) == 0):
						count+=1
				if(count == 4):
					countlist[i] -= 14
					flag = False
				for b in range(4):
					inventory[b] += C.get_amount(b)
				C.res_amount()
		self.show(countlist)

	def show(self,matrix):
		min = matrix[0]
		print("------------")
		for i in range(4):
			print("Robot ",i+1," time:",matrix[i])
		id = 0
		for i in range(4):
			if(matrix[i] < min):
				min = matrix[i]
				id = i
		print("Most effective robot is Robot",(id+1))

if(__name__ == "__main__"):
	main = Main()
	main.start()

