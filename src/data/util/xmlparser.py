def convertXmlFileToListOfData(filePath):
	f = open(filePath,'r')
	f1 = f.readlines()
	# diambil line 105 s/d len(f1)-37
	xmlLines = []
	for i in range(104,len(f1)-37):
		xmlLines.append(f1[i])
	splittedXmlLines = []
	for line in xmlLines:
		splittedXmlLines.append(line.split())
	xmlLines = []
	for lineList in splittedXmlLines:
		line = ''
		for i in range(len(lineList)):
			line += lineList[i]
			if(i != len(lineList)-1):
				line += ' '
		xmlLines.append(line)
	reducedXmlLines = []
	for line in xmlLines:
		if ('Row' not in line and '"String"' in line):
			reducedXmlLines.append(line)
	# Banyaknya hari pada bulan tersebut
	dayCount = int(reducedXmlLines[0][22:24]) + 1
	# Banyaknya orang pada bulan tersebut
	personDataCount = 0
	for line in reducedXmlLines:
		if ('ID' in line and 'Name' in line and 'Dpmt' in line and 'Shift' in line):
			personDataCount += 1
	# Memisahkan jadwal masing Karyawan
	listOfDataKaryawan = []
	for i in range(len(reducedXmlLines)):
		if ('ID' in reducedXmlLines[i] and 'Name' in reducedXmlLines[i] and 'Dpmt' in reducedXmlLines[i] and 'Shift' in reducedXmlLines[i]):
			listOfKaryawanKasbonJadwal = []	
			# Data Karyawan
			listOfKaryawanKasbonJadwal.append(takeDataInElementTag(reducedXmlLines[i]))
			# Kasbon
			listOfKaryawanKasbonJadwal.append(0)
			# Jadwal
			listOfJadwal = []
			for j in range(dayCount):
				listOfJadwal.append(takeDataInElementTag(reducedXmlLines[i+1]).split())
				i += 1
			listOfKaryawanKasbonJadwal.append(listOfJadwal)
			listOfDataKaryawan.append(listOfKaryawanKasbonJadwal)

	# Membuat result list
	# FORMAT: [ dayCount, personCount, [ list of [karyawan, kasbon, [ listofAbsence ] ] ] ]
	resultList = [dayCount, personDataCount, listOfDataKaryawan]

	return resultList

def takeDataInElementTag(Element):
	if (len(Element) == 0):
		return ''
	else:
		if (Element[0] != '<'):
			return Element
		else: #Element[0] == '<'
			# Mencari apa tag yg ada
			tag = ''
			i = 0
			while (Element[i] != ' '):
				if (Element[i] != '<' and Element[i] != ' '):
					tag += Element[i]
				i += 1
			# indeks penutup open tag
			idxDataStart = 0
			while (Element[idxDataStart] != '>'):
				idxDataStart +=1
			idxDataStart += 1
			# Mencari index data terakhir sebelum close tag
			idxDataEnd = len(Element)-len('</'+tag+'>')

			tData = Element[idxDataStart:idxDataEnd]

			# Rekursif
			return takeDataInElementTag(tData)
