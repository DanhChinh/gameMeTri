import PyPDF2
from PyPDF2 import PdfReader
import re
def getTextFromPdf(URL = r'C:\Users\Administrator\Pictures\a.pdf'):
	try:
		pdf_file = open(URL, 'rb')
		pdf_reader = PdfReader(pdf_file)
		text = ''
		for page in pdf_reader.pages:
			text+= page.extract_text()
		return text
	except:
		return None
def showMess():
	text = getTextFromPdf()
	if not text:
		return "a.pdf không tồn tại trong thư mục Picture" 
	dates = re.findall(r'\d{2}-\d{2}-\d{4}', text)
	retext = text.replace("\n","")
	nv = "???\n"
	if 'Thời lượng: CHINH' in retext:
		nv = "CHINH\n"
	elif 'Thời lượng: HOANG0411' in retext:
		nv = "HOANG0411\n"
	else:
		pass
	f70 = text.count("\n70,000")
	f100 = text.count("\n100,000")
	if f70%2 !=0 or f100%2 !=0:
		return f"{dates[-1]}\n"+nv + "Định dạng dữ liệu không hợp lệ!"
	if not f70 and not f100:
		return f"{dates[-1]}\n"+nv + "Không tìm thấy lịch sử nạp 70k hoặc 100k"
	f70 = int(f70/2)
	f100 = int(f100/2)
	s70 = f70*12
	s100 = f100*15
	text = f"{dates[-1]}\n"+nv+ "_________________________\n"
	t1 = f"12K x {f70} = {s70}K\n"
	t2 = f"15K x {f100} = {s100}K\n"
	t3 = f"Tổng:      {s70+s100}K\n"
	return text + t1 + t2 + t3


