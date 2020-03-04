def sagslash(adet):
	for i in range(int(adet)):
		print("/",end="")

def solslash(adet):
	for i in range(int(adet)):
		print("\\",end="")

def satiratla(adet):
	for i in range(int(adet)):
		print()

def bosluk(adet):
	for i in range(int(adet)):
		print(" ",end="")

def ustKisim(cap):
	baslangicBosluk=cap/2-1
	for i in range(int(cap/2)):
		bosluk(baslangicBosluk-i)
		sagslash(1)
		bosluk(i*2)
		solslash(1)
		satiratla(1)

def altKisim(cap):
	baslangicBosluk=cap-2
	for i in range(int(cap/2)):
		bosluk(i)
		solslash(1)
		bosluk(baslangicBosluk- (i*2))
		sagslash(1)
		satiratla(1)

def paralelkenarciz(cap):
	ustKisim(cap)
	altKisim(cap)

paralelkenarciz(10)