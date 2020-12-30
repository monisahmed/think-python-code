# think python example 5 exercise do_n 

def call():
	print("calling")


def do_n(f,n):
	for i in range(n):
		f()



do_n(call,10)


