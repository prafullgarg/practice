import time
def func():
	start=time.time()
	s=0
	for i in range(30):
		s+=i
	end=time.time()
	print(s,end-start) 
func()    