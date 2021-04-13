import os

def Encrypt(fileName, key):
	file = open(fileName, "rb")
	data = file.read()
	file.close()

	data = bytearray(data)
	for index, value in enumerate(data):
		data[index] = value ^ key
	
	EncFile = open("EncFile-" + fileName, "wb")
	EncFile.write(data)
	EncFile.close
	os.remove(fileName)
	FileNameAfterEnc = ("EncFile-" + fileName)




fileName = str(input("Enter file name: "))
key = int(input("Enter Key (1-255): "))
Encrypt(fileName, key)
