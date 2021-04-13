import os

def Decrypt(fileName, key):
	FileNameAfterEnc = ("EncFile-" + fileName)
	file = open(FileNameAfterEnc, "rb")
	data = file.read()
	file.close()

	data = bytearray(data)
	for index, value in enumerate(data):
		data[index] = value ^ key
	
	EncFile = open(fileName, "wb")
	EncFile.write(data)
	EncFile.close
	os.remove("EncFile-" + fileName)


fileName = str(input("Enter file name: "))
key = int(input("Enter Key (1-255): "))
Decrypt(fileName, key)
