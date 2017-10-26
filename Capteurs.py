import serial
import csv

ser = serial.Serial(port='COM7')  # open serial port
print(ser.name)  

adresse_mac=[]
adresse_mac_triee=[]
liste_remplie=False
en_cours = True

while en_cours:
	ligne = ser.readline().decode("utf-8").replace('\r\n', "")
	print(ligne) 
	
	while ligne != " ---- " and not liste_remplie:
		adresse_mac.append(ligne.split(" & ")[1])
		ligne = ser.readline().decode("utf-8").replace('\r\n', "")
		if ligne == " ---- ":
			print(adresse_mac)
			liste_remplie=True

	if ligne != " ---- " and not ligne.split(" & ")[1] in adresse_mac_triee:
		if float(ligne.split(" & ")[2]) >= 35 and float(ligne.split(" & ")[2]) < 70:
			adresse_mac_triee.append(ligne.split(" & ")[1])
			if len(adresse_mac) == len(adresse_mac_triee):
				en_cours = False
	print(adresse_mac_triee)

ser.close()  

f = open("Bus de test.csv", "w")
c = csv.writer(f)
c.writerow(["index", "Adresse Mac"])
cpt = 0
for el in adresse_mac_triee:
	c.writerow([cpt, el])
	cpt += 1
f.close()

 

