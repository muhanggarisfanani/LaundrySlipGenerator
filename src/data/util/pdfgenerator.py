from datetime import date
from datetime import datetime
from datetime import timedelta

from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import legal
from reportlab.lib.units import cm

from reportlab.platypus import Table
from reportlab.platypus import Image
from reportlab.platypus import TableStyle
from reportlab.lib import colors

import os
import os.path
import sys
import math

import data.util.dbcontroller
import data.gui.start

def loadDatabase():
	global database
	prog_call = sys.argv[0]
	prog_location = os.path.split(prog_call)[0]
	database = data.util.dbcontroller.dbConnect(os.path.join(prog_location,"data/db/database.db"))

def closeDatabase():
	data.util.dbcontroller.dbDisconnect(database)

def countTimeBetween2(StrTime1, StrTime2):
	Time1 = datetime.strptime(StrTime1, '%H:%M')
	Time2 = datetime.strptime(StrTime2, '%H:%M')
	return Time2-Time1

def countTimeBetween4(StrTime1, StrTime2, StrTime3, StrTime4):
	Time1 = datetime.strptime(StrTime1, '%H:%M')
	Time2 = datetime.strptime(StrTime2, '%H:%M')
	Time3 = datetime.strptime(StrTime3, '%H:%M')
	Time4 = datetime.strptime(StrTime4, '%H:%M')
	return (Time2-Time1)+(Time4-Time3)

def countTimeBetween6(StrTime1, StrTime2, StrTime3, StrTime4, StrTime5, StrTime6):
	Time1 = datetime.strptime(StrTime1, '%H:%M')
	Time2 = datetime.strptime(StrTime2, '%H:%M')
	Time3 = datetime.strptime(StrTime3, '%H:%M')
	Time4 = datetime.strptime(StrTime4, '%H:%M')	
	Time5 = datetime.strptime(StrTime5, '%H:%M')
	Time6 = datetime.strptime(StrTime6, '%H:%M')
	return (Time2-Time1)+(Time4-Time3)+(Time6-Time5)

def countTimeBetween8(StrTime1, StrTime2, StrTime3, StrTime4, StrTime5, StrTime6, StrTime7, StrTime8):
	Time1 = datetime.strptime(StrTime1, '%H:%M')
	Time2 = datetime.strptime(StrTime2, '%H:%M')
	Time3 = datetime.strptime(StrTime3, '%H:%M')
	Time4 = datetime.strptime(StrTime4, '%H:%M')	
	Time5 = datetime.strptime(StrTime5, '%H:%M')
	Time6 = datetime.strptime(StrTime6, '%H:%M')	
	Time7 = datetime.strptime(StrTime7, '%H:%M')
	Time8 = datetime.strptime(StrTime8, '%H:%M')
	return (Time2-Time1)+(Time4-Time3)+(Time6-Time5)+(Time8-Time7)

def absenceFormGenerator(listOfAbsence):
	res = []
	leftRes = [['Tanggal','Masuk','Keluar','Total']]
	rightRes = [['Tanggal','Masuk','Keluar','Total']]
	leftStyleRes = []
	rightStyleRes = []
	
	for i in range(len(listOfAbsence)):
		if (i < len(listOfAbsence) // 2): # Setengah tanggal pertama
			if (len(listOfAbsence[i]) % 2 == 1):
				leftRes.append([str(i+1),'#ERROR','#ERROR','#ERROR'])
				leftStyleRes.append(('TEXTCOLOR',(1,i+1),(-1,i+1),colors.red))
			elif (len(listOfAbsence[i]) == 0):
				leftRes.append([str(i+1),'','',''])
				leftStyleRes.append(('BACKGROUND',(0,i+1),(-1,i+1),colors.red))
			elif (len(listOfAbsence[i]) == 2):
				leftRes.append([str(i+1),
					listOfAbsence[i][0],
					listOfAbsence[i][1],
					str(countTimeBetween2(listOfAbsence[i][0],listOfAbsence[i][1]))])
				if (countTimeBetween2(listOfAbsence[i][0],listOfAbsence[i][1]).seconds > 30600): #Lebih dari 8 jam 30 menit
					leftStyleRes.append(('BACKGROUND',(0,i+1),(-1,i+1),colors.yellow))
			elif (len(listOfAbsence[i]) == 4):
				leftRes.append([str(i+1),
					listOfAbsence[i][0]+'\n'+listOfAbsence[i][2],
					listOfAbsence[i][1]+'\n'+listOfAbsence[i][3],
					str(countTimeBetween4(listOfAbsence[i][0],listOfAbsence[i][1],listOfAbsence[i][2],listOfAbsence[i][3]))])
				if (countTimeBetween4(listOfAbsence[i][0],listOfAbsence[i][1],listOfAbsence[i][2],listOfAbsence[i][3]).seconds > 30600): #Lebih dari 8 jam 30 menit
					leftStyleRes.append(('BACKGROUND',(0,i+1),(-1,i+1),colors.yellow))
			elif (len(listOfAbsence[i]) == 6):
				leftRes.append([str(i+1),
					listOfAbsence[i][0]+'\n'+listOfAbsence[i][2]+'\n'+listOfAbsence[i][4],
					listOfAbsence[i][1]+'\n'+listOfAbsence[i][3]+'\n'+listOfAbsence[i][5],
					str(countTimeBetween6(listOfAbsence[i][0],listOfAbsence[i][1],listOfAbsence[i][2],listOfAbsence[i][3],listOfAbsence[i][4],listOfAbsence[i][5]))])
				if (countTimeBetween6(listOfAbsence[i][0],listOfAbsence[i][1],listOfAbsence[i][2],listOfAbsence[i][3],listOfAbsence[i][4],listOfAbsence[i][5]).seconds > 30600): #Lebih dari 8 jam 30 menit
					leftStyleRes.append(('BACKGROUND',(0,i+1),(-1,i+1),colors.yellow))
			elif (len(listOfAbsence[i]) == 8):
				leftRes.append([str(i+1),
					listOfAbsence[i][0]+'\n'+listOfAbsence[i][2]+'\n'+listOfAbsence[i][4]+'\n'+listOfAbsence[i][6],
					listOfAbsence[i][1]+'\n'+listOfAbsence[i][3]+'\n'+listOfAbsence[i][5]+'\n'+listOfAbsence[i][7],
					str(countTimeBetween8(listOfAbsence[i][0],listOfAbsence[i][1],listOfAbsence[i][2],listOfAbsence[i][3],listOfAbsence[i][4],listOfAbsence[i][5],listOfAbsence[i][6],listOfAbsence[i][7]))])
				if (countTimeBetween8(listOfAbsence[i][0],listOfAbsence[i][1],listOfAbsence[i][2],listOfAbsence[i][3],listOfAbsence[i][4],listOfAbsence[i][5],listOfAbsence[i][6],listOfAbsence[i][7]).seconds > 30600): #Lebih dari 8 jam 30 menit
					leftStyleRes.append(('BACKGROUND',(0,i+1),(-1,i+1),colors.yellow))
		else: # Setengah tanggal berikutnya
			if (len(listOfAbsence[i]) % 2 == 1):
				rightRes.append([str(i+1),'#ERROR','#ERROR','#ERROR'])
				rightStyleRes.append(('TEXTCOLOR',(0,(i+1)-len(listOfAbsence)//2),(-1,(i+1)-len(listOfAbsence)//2),colors.red))
			elif (len(listOfAbsence[i]) == 0):
				rightRes.append([str(i+1),'','',''])
				rightStyleRes.append(('BACKGROUND',(0,(i+1)-len(listOfAbsence)//2),(-1,(i+1)-len(listOfAbsence)//2),colors.red))
			elif (len(listOfAbsence[i]) == 2):
				rightRes.append([str(i+1),
					listOfAbsence[i][0],
					listOfAbsence[i][1],
					str(countTimeBetween2(listOfAbsence[i][0],listOfAbsence[i][1]))])
				if (countTimeBetween2(listOfAbsence[i][0],listOfAbsence[i][1]).seconds > 30600): #Lebih dari 8 jam 30 menit
					rightStyleRes.append(('BACKGROUND',(0,(i+1)-len(listOfAbsence)//2),(-1,(i+1)-len(listOfAbsence)//2),colors.yellow))
			elif (len(listOfAbsence[i]) == 4):
				rightRes.append([str(i+1),
					listOfAbsence[i][0]+'\n'+listOfAbsence[i][2],
					listOfAbsence[i][1]+'\n'+listOfAbsence[i][3],
					str(countTimeBetween4(listOfAbsence[i][0],listOfAbsence[i][1],listOfAbsence[i][2],listOfAbsence[i][3]))])
				if (countTimeBetween4(listOfAbsence[i][0],listOfAbsence[i][1],listOfAbsence[i][2],listOfAbsence[i][3]).seconds > 30600): #Lebih dari 8 jam 30 menit
					rightStyleRes.append(('BACKGROUND',(0,(i+1)-len(listOfAbsence)//2),(-1,(i+1)-len(listOfAbsence)//2),colors.yellow))
			elif (len(listOfAbsence[i]) == 6):
				rightRes.append([str(i+1),
					listOfAbsence[i][0]+'\n'+listOfAbsence[i][2]+'\n'+listOfAbsence[i][4],
					listOfAbsence[i][1]+'\n'+listOfAbsence[i][3]+'\n'+listOfAbsence[i][5],
					str(countTimeBetween6(listOfAbsence[i][0],listOfAbsence[i][1],listOfAbsence[i][2],listOfAbsence[i][3],listOfAbsence[i][4],listOfAbsence[i][5]))])
				if (countTimeBetween6(listOfAbsence[i][0],listOfAbsence[i][1],listOfAbsence[i][2],listOfAbsence[i][3],listOfAbsence[i][4],listOfAbsence[i][5]).seconds > 30600): #Lebih dari 8 jam 30 menit
					rightStyleRes.append(('BACKGROUND',(0,(i+1)-len(listOfAbsence)//2),(-1,(i+1)-len(listOfAbsence)//2),colors.yellow))
			elif (len(listOfAbsence[i]) == 8):
				rightRes.append([str(i+1),
					listOfAbsence[i][0]+'\n'+listOfAbsence[i][2]+'\n'+listOfAbsence[i][4]+'\n'+listOfAbsence[i][6],
					listOfAbsence[i][1]+'\n'+listOfAbsence[i][3]+'\n'+listOfAbsence[i][5]+'\n'+listOfAbsence[i][7],
					str(countTimeBetween8(listOfAbsence[i][0],listOfAbsence[i][1],listOfAbsence[i][2],listOfAbsence[i][3],listOfAbsence[i][4],listOfAbsence[i][5],listOfAbsence[i][6],listOfAbsence[i][7]))])
				if (countTimeBetween8(listOfAbsence[i][0],listOfAbsence[i][1],listOfAbsence[i][2],listOfAbsence[i][3],listOfAbsence[i][4],listOfAbsence[i][5],listOfAbsence[i][6],listOfAbsence[i][7]).seconds > 30600): #Lebih dari 8 jam 30 menit
					rightStyleRes.append(('BACKGROUND',(0,(i+1)-len(listOfAbsence)//2),(-1,(i+1)-len(listOfAbsence)//2),colors.yellow))
	res.append(leftRes)
	res.append(rightRes)
	res.append(leftStyleRes)
	res.append(rightStyleRes)
	return res

def hitungTotalJamKerjaSatuKaryawan(listOfAbsence):
	sumMenit = 0
	for absen in listOfAbsence:
		if (len(absen) == 2):
			sumMenit += countTimeBetween2(absen[0],absen[1]).seconds / 60
		elif (len(absen) == 4):
			sumMenit += countTimeBetween4(absen[0],absen[1],absen[2],absen[3]).seconds / 60
		elif (len(absen) == 6):
			sumMenit += countTimeBetween6(absen[0],absen[1],absen[2],absen[3],absen[4],absen[5]).seconds / 60
		elif (len(absen) == 8):
			sumMenit += countTimeBetween8(absen[0],absen[1],absen[2],absen[3],absen[4],absen[5],absen[6],absen[7]).seconds / 60
	return int(sumMenit)

def hitungTotalJamKerjaSemuaKaryawan(karyawanData):
	sumMenit = 0
	for karyawan in karyawanData:
		sumMenit += hitungTotalJamKerjaSatuKaryawan(karyawan[2])
	return sumMenit

def gajiPokokSatuKaryawan(jamKerja, gajiPerjam):
	return int((jamKerja*gajiPerjam)/60)

def gajiPokokSemuaKaryawan(karyawanData, gajiPerjam):
	sumGaji = 0
	for karyawan in karyawanData:
		sumGaji += gajiPokokSatuKaryawan(hitungTotalJamKerjaSatuKaryawan(karyawan[2]),gajiPerjam)
	return sumGaji

def betterStringFormat(number):
	return str(f'{number:,}').replace(',','.')

def getDateNow():
	def reverse(lst):
		return [ele for ele in reversed(lst)]

	datenow = reverse(str(date.today()).split('-'))
	if (datenow[1] == '01'):
		datenow[1] = ' Januari '
	elif (datenow[1] == '02'):
		datenow[1] = ' Februari '
	elif (datenow[1] == '03'):
		datenow[1] = ' Maret '
	elif (datenow[1] == '04'):
		datenow[1] = ' April '
	elif (datenow[1] == '05'):
		datenow[1] = ' Mei '
	elif (datenow[1] == '06'):
		datenow[1] = ' Juni '
	elif (datenow[1] == '07'):
		datenow[1] = ' Juli '
	elif (datenow[1] == '08'):
		datenow[1] = ' Agustus '
	elif (datenow[1] == '09'):
		datenow[1] = ' September '
	elif (datenow[1] == '10'):
		datenow[1] = ' Oktober '
	elif (datenow[1] == '11'):
		datenow[1] = ' November '
	elif (datenow[1] == '12'):
		datenow[1] = ' Desember '

	return "".join(datenow)

def getNama(idName):
	return idName.split()[1][5:(len(idName.split()[1]))]

def generateMultiSlip(resData, miniSlip=False):
	# MENGAMBIL DATA DARI DATABASE
	loadDatabase()
	query = 'SELECT * FROM setting WHERE id=0'
	Tuple = data.util.dbcontroller.getTuple(database,query)
	alamat = Tuple[1]
	website = Tuple[2]
	kabir = Tuple[3]
	if (Tuple[4] == 'default'):
		prog_call = sys.argv[0]
		prog_location = os.path.split(prog_call)[0]
		logoPath = os.path.join(prog_location,"data/logo.png")
	else:
		logoPath = Tuple[4]
	gajiPerjam = Tuple[5]
	closeDatabase()

	# MENGAMBIL DATA DARI TABEL resData
	periode = resData[1]
	pemasukan = int(resData[2])
	karyawanData =	resData[3]
	kota = resData[4]

	# MEMASTIKAN BAHWA TERDAPAT FOLDER OUTPUT
	try:
		os.mkdir(os.getcwd() + '/output')
		print('Start generating...')
	except:
		print('Start generating...')

	try:
		os.mkdir(os.getcwd() + '/output/' + periode)
		print('Output folder created')
	except:
		print('Output folder found')

	for karyawan in karyawanData:
		generatePDFSlip(miniSlip, alamat, website, kabir, logoPath, gajiPerjam, karyawanData, periode, pemasukan, kota, karyawan)


def generatePDFSlip(miniSlip, alamat, website, kabir, logoPath, gajiPerjam, karyawanData, periode, pemasukan, kota, listKaryawan):
	# LOOPING TIAP KARYAWAN
	nama = getNama(listKaryawan[0])
	kasbon = int(listKaryawan[1])
	listOfAbsence = listKaryawan[2]

	# FIXED VALUE TIAP LOOPING
	blank = ' '
	institusi = 'KOPERASI ASRAMA MAHASISWA ITB'
	jamKerjaSemua = hitungTotalJamKerjaSemuaKaryawan(karyawanData)
	pemasukanBersih = pemasukan - gajiPokokSemuaKaryawan(karyawanData,gajiPerjam)
	jamKerja = hitungTotalJamKerjaSatuKaryawan(listOfAbsence)
	if (jamKerjaSemua != 0):
		bonus = int((jamKerja * pemasukanBersih * 0.27) / jamKerjaSemua)
	else:
		bonus = 0
	gajiTotal = gajiPokokSatuKaryawan(jamKerja, gajiPerjam) + bonus - kasbon
	if (miniSlip):
		fileName = 'output\\' + periode + '\\mini-' + 'generated slip ' + nama + ' .pdf'
	else:
		fileName = 'output\\' + periode + '\\' + 'generated slip ' + nama + ' .pdf'

	pdf = SimpleDocTemplate(
		fileName,
		pagesize=legal,
		topMargin=1*cm,
		bottomMargin=1*cm,
		rightMargin=2*cm,
		leftMargin=2*cm
	)

	# Build structure

	# START: Bagian I - Kop Surat
	letterHeadTable = Table(
		[
			[institusi],
			[alamat],
			['Website: '+website],
			[blank]
		],
		14.62*cm
	)

	letterHeadTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Bold'),
		('FONTSIZE', (0,0), (-1,-1), 12),
		('TEXTCOLOR', (0,0), (-1,-1), colors.toColor('rgb(68,114,196)')),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	letterHeadTable.setStyle(letterHeadTableStyle)

	logo = Image(logoPath)
	logo.drawWidth = 2.17*cm
	logo.drawHeight = 2.65*cm
	logoHeadTable = Table(
		[
			[logo]
		],
		logo.drawWidth
	)
	logoHeadTableStyle = TableStyle([
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	logoHeadTable.setStyle(logoHeadTableStyle)

	bagianITable = Table(
		[
			[logoHeadTable,letterHeadTable]
		]
	)
	bagianITableStyle = TableStyle([
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	bagianITable.setStyle(bagianITableStyle)
	# END: Bagian I - Kop Surat

	###################################################

	# START: Bagian II - Judul, Periode, Nama, Subjudul
	titleTable = Table(
		[
			['Slip Gaji Karyawan Laundry']
		]
	)
	titleTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Bold'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('LINEBELOW', (0,0), (-1,-1), 1, colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	titleTable.setStyle(titleTableStyle)

	periodeTable = Table(
		[
			['Periode ' + periode]
		]
	)
	periodeTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	periodeTable.setStyle(periodeTableStyle)

	nameTable = Table(
		[
			['Nama : ' + nama]
		],
		16.79*cm
	)
	nameTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Bold'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 3),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	nameTable.setStyle(nameTableStyle)

	secondTitleTable = Table(
		[
			['Data Absensi']
		],
		16.79*cm
	)
	secondTitleTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Bold'),
		('FONTSIZE', (0,0), (-1,-1), 12),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('LINEABOVE', (0,0), (-1,-1), 0.5, colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	secondTitleTable.setStyle(secondTitleTableStyle)

	bagianIITable = Table(
		[
			[titleTable],
			[periodeTable],
			[nameTable],
			[secondTitleTable]
		],16.79*cm
	)

	bagianIITableStyle = TableStyle([
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	bagianIITable.setStyle(bagianIITableStyle)
	# END: Bagian II - Judul, Periode, Nama, Subjudul

	###################################################

	# START: Bagian III - Tabel Absensi
	leftTableAbsence = Table(
		absenceFormGenerator(listOfAbsence)[0],
		1.95*cm
	)
	leftTableAbsenceStyle = TableStyle([
		('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
		('FONTNAME', (0,1), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('GRID', (0,0), (-1,-1), 0.5, colors.black),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 3),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	] + absenceFormGenerator(listOfAbsence)[2])
	leftTableAbsence.setStyle(leftTableAbsenceStyle)

	rightTableAbsence = Table(
		absenceFormGenerator(listOfAbsence)[1],
		1.95*cm
	)
	rightTableAbsenceStyle = TableStyle([
		('FONTNAME', (0,0), (-1,0), 'Times-Bold'),
		('FONTNAME', (0,1), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('GRID', (0,0), (-1,-1), 0.5, colors.black),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 3),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	] + absenceFormGenerator(listOfAbsence)[3])
	rightTableAbsence.setStyle(rightTableAbsenceStyle)

	redBlock = Table(
		[
			['Blok merah : Tidak masuk/libur']
		]
	)
	redBlockStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BACKGROUND', (0, 0), (-1,-1), colors.red),
		('BOTTOMPADDING',(0,0),(-1,-1), 3),
		('RIGHTPADDING',(0,0),(-1,-1), 6),
		('LEFTPADDING',(0,0),(-1,-1), 6),
	])
	redBlock.setStyle(redBlockStyle)

	yellowBlock = Table(
		[
			['Blok kuning : Kerja lembur']
		]
	)
	yellowBlockStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('BACKGROUND', (0, 0), (-1,-1), colors.yellow),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 3),
		('RIGHTPADDING',(0,0),(-1,-1), 6),
		('LEFTPADDING',(0,0),(-1,-1), 6),
	])
	yellowBlock.setStyle(yellowBlockStyle)

	upperPart = Table(
		[
			[leftTableAbsence,rightTableAbsence]
		]
	)
	upperPartStyle = TableStyle([
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 3),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	upperPart.setStyle(upperPartStyle)

	lowerPart = Table(
		[
			[redBlock,yellowBlock]
		]
	)
	lowerPartStyle = TableStyle([
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	lowerPart.setStyle(lowerPartStyle)

	bagianIIITable = Table(
		[
			[upperPart],
			[lowerPart]
		]
	)
	bagianIIITableStyle = TableStyle([
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	bagianIIITable.setStyle(bagianIIITableStyle)
	# END: Bagian III - Tabel Absensi

	###################################################

	# START: Bagian IV - Deskripsi Jam Kerja dan Judul Perhitungan Gaji
	bagianIVTable = Table(
		[
			['Total Jam Kerja = ' + betterStringFormat(jamKerja) + ' menit'],
			['Total Jam Kerja Semua Karyawan = ' + betterStringFormat(jamKerjaSemua) + ' menit'],
			[blank],
			['Perhitungan Gaji']
		],
		16.79*cm
	)
	bagianIVTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-2), 'Times-Roman'),
		('FONTNAME', (0,-1), (-1,-1), 'Times-Bold'),
		('FONTSIZE', (0,0), (-1,-2), 11),
		('FONTSIZE', (0,-1), (-1,-1), 12),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	bagianIVTable.setStyle(bagianIVTableStyle)
	# END: Bagian IV - Deskripsi Jam Kerja dan Judul Perhitungan Gaji

	###################################################

	# START: Bagian V - Perhitungan Gaji Pokok
	pokokTitleTable = Table(
		[
			[' Pokok']
		],
		3.5*cm
	)
	pokokTitleTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	pokokTitleTable.setStyle(pokokTitleTableStyle)

	rumus1Table = Table(
		[
			['Total Jam Kerja'],
			['60 menit']
		]
	)
	rumus1TableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('LINEABOVE',(-1,-1),(-1,-1), 0.5, colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 3),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	rumus1Table.setStyle(rumus1TableStyle)

	rumus2Table = Table(
		[
			[betterStringFormat(jamKerja) + ' menit'],
			['60 menit']
		]
	)
	rumus2TableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('LINEABOVE',(-1,-1),(-1,-1), 0.5, colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 3),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	rumus2Table.setStyle(rumus2TableStyle)

	pokokAtasTable = Table(
		[
			['=  ', rumus1Table, ' × Rp'+betterStringFormat(gajiPerjam)+'  =  ', rumus2Table, ' × Rp'+betterStringFormat(gajiPerjam)]
		]
	)
	pokokAtasTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	pokokAtasTable.setStyle(pokokAtasTableStyle)

	atas2PokokTable = Table(
		[
			[pokokAtasTable,blank]
		]
	)

	atas2PokokTableStyle = TableStyle([
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	atas2PokokTable.setStyle(atas2PokokTableStyle)

	hasilPokokTable = Table(
		[
			['=  Rp', betterStringFormat(gajiPokokSatuKaryawan(jamKerja,gajiPerjam))]
		]
	)
	hasilPokokTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Bold'),
		('FONTSIZE', (0,0), (-1,-1), 12),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	hasilPokokTable.setStyle(hasilPokokTableStyle)

	perhitunganPokokTable = Table(
		[
			[atas2PokokTable],
			[hasilPokokTable]
		],
		13.27*cm
	)
	perhitunganPokokTableStyle = TableStyle([
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 3),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	perhitunganPokokTable.setStyle(perhitunganPokokTableStyle)

	pokokTable = Table(
		[
			[pokokTitleTable, perhitunganPokokTable]
		]
	)
	pokokTableStyle = TableStyle([
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (0,-1), 'TOP'),
		('VALIGN', (-1,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	pokokTable.setStyle(pokokTableStyle)

	bagianVTable = Table(
		[
			[blank],
			[pokokTable]
		],
		16.79*cm
	)
	bagianVTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-2), 'Times-Roman'),
		('FONTNAME', (0,-1), (-1,-1), 'Times-Bold'),
		('FONTSIZE', (0,0), (-1,-2), 11),
		('FONTSIZE', (0,-1), (-1,-1), 12),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
		('LINEABOVE', (0,0), (-1,0), 0.5, colors.black),
	])
	bagianVTable.setStyle(bagianVTableStyle)
	# END: Bagian V - Perhitungan Gaji Pokok

	###################################################

	# START: Bagian VI - Perhitungan Pemasukan dan Bonus
	pmskTitleTable = Table(
		[
			[' Pemasukan']
		],
		3.5*cm
	)
	pmskTitleTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	pmskTitleTable.setStyle(pmskTitleTableStyle)

	hasilPmskTable = Table(
		[
			['=  Rp', betterStringFormat(pemasukan)]
		]
	)
	hasilPmskTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	hasilPmskTable.setStyle(hasilPmskTableStyle)

	pemasukanTable = Table(
		[
			[pmskTitleTable, hasilPmskTable, blank, blank, blank]
		]
	)
	pemasukanTableStyle = TableStyle([
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	pemasukanTable.setStyle(pemasukanTableStyle)

	pmskBrsTitleTable = Table(
		[
			[' Pemasukan Bersih']
		],
		3.5*cm
	)
	pmskBrsTitleTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	pmskBrsTitleTable.setStyle(pmskBrsTitleTableStyle)

	hasilPmskBrsATable = Table(
		[
			['=  Pemasukan – Gaji Pokok Semua Karyawan  =  Rp', betterStringFormat(pemasukan), ' – Rp', betterStringFormat(gajiPokokSemuaKaryawan(karyawanData,gajiPerjam))],
		]
	)
	hasilPmskBrsATableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	hasilPmskBrsATable.setStyle(hasilPmskBrsATableStyle)

	hasilPmskBrsBTable = Table(
		[
			['=  Rp', betterStringFormat(pemasukanBersih)],
		]
	)
	hasilPmskBrsBTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	hasilPmskBrsBTable.setStyle(hasilPmskBrsBTableStyle)

	hasilPmskBrsTable = Table(
		[
			[hasilPmskBrsATable],
			[hasilPmskBrsBTable]
		]
	)
	hasilPmskBrsTableStyle = TableStyle([
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	hasilPmskBrsTable.setStyle(hasilPmskBrsTableStyle)

	pmskBrsTable = Table(
		[
			[pmskBrsTitleTable, hasilPmskBrsTable, blank]
		]
	)
	pmskBrsTableStyle = TableStyle([
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	pmskBrsTable.setStyle(pmskBrsTableStyle)

	bonusTitleTable = Table(
		[
			[' Bonus']
		],
		3.5*cm
	)
	bonusTitleTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	bonusTitleTable.setStyle(bonusTitleTableStyle)

	rumus3Table = Table(
		[
			['Jam Kerja'],
			['Jam Kerja Semua Karyawan']
		]
	)
	rumus3TableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('LINEABOVE',(-1,-1),(-1,-1), 0.5, colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 3),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	rumus3Table.setStyle(rumus3TableStyle)

	rumus4Table = Table(
		[
			[betterStringFormat(jamKerja) + ' menit'],
			[betterStringFormat(jamKerjaSemua) + ' menit']
		]
	)
	rumus4TableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('LINEABOVE',(-1,-1),(-1,-1), 0.5, colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 3),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	rumus4Table.setStyle(rumus4TableStyle)

	bonusRumusTable = Table(
		[
			['=  ', rumus3Table, ' × 27% × Pemasukan Bersih']
		]
	)
	bonusRumusTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	bonusRumusTable.setStyle(bonusRumusTableStyle)

	bonusHitungTable = Table(
		[
			['=  ', rumus4Table, ' × 27% × Rp', betterStringFormat(pemasukanBersih), blank, blank, blank, blank, blank, blank, blank, blank]
		]
	)
	bonusHitungTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	bonusHitungTable.setStyle(bonusHitungTableStyle)

	hasilBonusTable = Table(
		[
			['=  Rp', betterStringFormat(bonus)]
		]
	)
	hasilBonusTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Bold'),
		('FONTSIZE', (0,0), (-1,-1), 12),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	hasilBonusTable.setStyle(hasilBonusTableStyle)

	perhitunganBonusTable = Table(
		[
			[bonusRumusTable],
			[bonusHitungTable],
			[hasilBonusTable]
		]
	)
	perhitunganBonusTableStyle = TableStyle([
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	perhitunganBonusTable.setStyle(perhitunganBonusTableStyle)

	bonusTable = Table(
		[
			[bonusTitleTable, perhitunganBonusTable, blank, blank, blank]
		]
	)
	bonusTableStyle = TableStyle([
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	bonusTable.setStyle(bonusTableStyle)

	gabPmskBnsTable = Table(
		[
			[pemasukanTable],
			[pmskBrsTable],
			[bonusTable]
		]
	)
	gabPmskBnsTableStyle = TableStyle([
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 3),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	gabPmskBnsTable.setStyle(gabPmskBnsTableStyle)

	bagianVITable = Table(
		[
			[blank],
			[gabPmskBnsTable]
		],
		16.79*cm
	)
	bagianVITableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-2), 'Times-Roman'),
		('FONTNAME', (0,-1), (-1,-1), 'Times-Bold'),
		('FONTSIZE', (0,0), (-1,-2), 11),
		('FONTSIZE', (0,-1), (-1,-1), 12),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
		('LINEABOVE', (0,0), (-1,0), 0.5, colors.black),
	])
	bagianVITable.setStyle(bagianVITableStyle)
	# END: Bagian VI - Perhitungan Pemasukan dan Bonus

	###################################################

	# START: Bagian VII - Perhitungan Akhir
	kasbonTitleTable = Table(
		[
			[' Kasbon']
		],
		3.5*cm
	)
	kasbonTitleTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	kasbonTitleTable.setStyle(kasbonTitleTableStyle)

	nilaiKasbonTable = Table(
		[
			['=  Rp', betterStringFormat(kasbon)]
		]
	)
	nilaiKasbonTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	nilaiKasbonTable.setStyle(nilaiKasbonTableStyle)

	kasbonTable = Table(
		[
			[kasbonTitleTable, nilaiKasbonTable, blank, blank, blank]
		]
	)
	kasbonTableStyle = TableStyle([
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	kasbonTable.setStyle(kasbonTableStyle)

	gajiTotalTitleTable = Table(
		[
			[' Gaji Total']
		],
		3.5*cm
	)
	gajiTotalTitleTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	gajiTotalTitleTable.setStyle(gajiTotalTitleTableStyle)

	hitungGajiTable = Table(
		[
			['=  Pokok + Bonus – Kasbon  =  Rp'+ betterStringFormat(gajiPokokSatuKaryawan(jamKerja,gajiPerjam)) + ' + Rp' + betterStringFormat(bonus) + ' – Rp' + betterStringFormat(kasbon)],
			['=  Rp' + betterStringFormat(gajiTotal)]
		]
	)
	hitungGajiTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	hitungGajiTable.setStyle(hitungGajiTableStyle)

	gajiTable = Table(
		[
			[gajiTotalTitleTable, hitungGajiTable, blank, blank]
		]
	)
	gajiTableStyle = TableStyle([
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	gajiTable.setStyle(gajiTableStyle)

	pembulatanTitleTable = Table(
		[
			[' Pembulatan']
		],
		3.5*cm
	)
	pembulatanTitleTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	pembulatanTitleTable.setStyle(pembulatanTitleTableStyle)

	nilaiPembulatanTable = Table(
		[
			['=  Rp' + betterStringFormat(math.ceil(gajiTotal / 1000) * 1000)]
		]
	)
	nilaiPembulatanTableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Bold'),
		('FONTSIZE', (0,0), (-1,-1), 12),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	nilaiPembulatanTable.setStyle(nilaiPembulatanTableStyle)

	pembulatanTable = Table(
		[
			[pembulatanTitleTable, nilaiPembulatanTable, blank, blank, blank]
		]
	)
	pembulatanTableStyle = TableStyle([
		('ALIGN', (0,0), (-1,-1), 'LEFT'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	pembulatanTable.setStyle(pembulatanTableStyle)

	if (miniSlip):
		gabkasbonGajiTable = Table(
			[
				[gajiTable],
				[pembulatanTable]
			]
		)
	else:
		gabkasbonGajiTable = Table(
			[
				[kasbonTable],
				[gajiTable],
				[pembulatanTable]
			]
		)
	gabkasbonGajiTableStyle = TableStyle([
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 3),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	gabkasbonGajiTable.setStyle(gabkasbonGajiTableStyle)

	bagianVIITable = Table(
		[
			[blank],
			[gabkasbonGajiTable]	
		],
		16.79*cm
	)
	bagianVIITableStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-2), 'Times-Roman'),
		('FONTNAME', (0,-1), (-1,-1), 'Times-Bold'),
		('FONTSIZE', (0,0), (-1,-2), 11),
		('FONTSIZE', (0,-1), (-1,-1), 12),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
		('LINEABOVE', (0,0), (-1,0), 0.5, colors.black),
	])
	bagianVIITable.setStyle(bagianVIITableStyle)
	# END: Bagian VII - Perhitungan Akhir

	###################################################

	# START: Bagian VIII - Footer
	signaturePenerima = Table(
		[
			[blank],
			['Penerima'],
			[blank],
			[blank],
			[blank],
			[nama],
			['Karyawan Laundry']
		]
	)
	signaturePenerimaStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	signaturePenerima.setStyle(signaturePenerimaStyle)

	signatureKabir = Table(
		[
			[kota+', '+getDateNow()],
			['Mengetahui'],
			[blank],
			[blank],
			[blank],
			[kabir],
			['Ketua Biro Laundry']
		]
	)
	signatureKabirStyle = TableStyle([
		('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
		('FONTSIZE', (0,0), (-1,-1), 11),
		('TEXTCOLOR', (0,0), (-1,-1), colors.black),
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	signatureKabir.setStyle(signatureKabirStyle)

	signatureTable = Table(
		[
			[blank, signaturePenerima, blank, blank, signatureKabir, blank]
		]
	)
	signatureTableStyle = TableStyle([
		('ALIGN', (0,0), (-1,-1), 'CENTER'),
		('VALIGN', (0,0), (-1,-1), 'TOP'),
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
	])
	signatureTable.setStyle(signatureTableStyle)

	bagianVIIITable = Table(
		[
			[blank],
			[blank],
			[signatureTable]
		],
		16.79*cm
	)
	bagianVIIITableStyle = TableStyle([
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 0),
		('RIGHTPADDING',(0,0),(-1,-1), 0),
		('LEFTPADDING',(0,0),(-1,-1), 0),
		('LINEABOVE', (0,0), (-1,0), 0.5, colors.black),
	])
	bagianVIIITable.setStyle(bagianVIIITableStyle)

	if (miniSlip):
		mainTable = Table(
			[
				[bagianITable],
				[bagianIITable],
				[bagianIIITable],
				[bagianIVTable],
				[bagianVIITable],
				[bagianVIIITable],
			]
		)
	else:
		mainTable = Table(
			[
				[bagianITable],
				[bagianIITable],
				[bagianIIITable],
				[bagianIVTable],
				[bagianVTable],
				[bagianVITable],
				[bagianVIITable],
				[bagianVIIITable],
			]
		)

	mainTableStyle = TableStyle([
		('TOPPADDING',(0,0),(-1,-1), 0),
		('BOTTOMPADDING',(0,0),(-1,-1), 3),
		('RIGHTPADDING',(0,0),(-1,-1), 3),
		('LEFTPADDING',(0,0),(-1,-1), 3),
	])
	mainTable.setStyle(mainTableStyle)

	elems = []
	elems.append(mainTable)

	try:
		pdf.build(elems)
		data.gui.start.Start_support.LabelStatusVar.set("Successfully generated.")
	except:
		data.gui.start.Start_support.LabelStatusVar.set("ERROR: The file is opened (maybe)")