from MainWindow import *
from PyQt4.QtGui import *
from AboutWindow import *
from PyQt4 import QtCore, QtGui
from DownloadCompleted import *
from BeautifulSoup import BeautifulSoup
import sys, mechanize, cookielib, webbrowser, urllib2, urllib, subprocess, time, os


#Url Yang dipake
theurl = 'https://dosen.amikom.ac.id/index.php/'

#identity 
browser = mechanize.Browser()
browser.open(theurl)

#cookies Option
cj = cookielib.LWPCookieJar()
browser.set_cookiejar(cj)

# Browser options
browser.set_handle_equiv(True)
browser.set_handle_redirect(True)
browser.set_handle_referer(True)
browser.set_handle_robots(False)


app = QtGui.QApplication(sys.argv)

class MainForm(QtGui.QMainWindow):
	def __init__(self, parent=None):
	       	QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)


class DownloadCompleted(QtGui.QWidget):
   	def __init__(self,parent=None):
        	QtGui.QWidget.__init__(self,parent)
        	self.ui=Ui_Dialog()
        	self.ui.setupUi(self)


class AboutForm(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_aboutDialog()
        self.ui.setupUi(self)



main = MainForm()
finish = DownloadCompleted()
about=AboutForm()
main.ui.splash.show()
time.sleep(5)
main.show()


main.setWindowIcon(main.ui.icon)
main.ui.splash.finish(main)

os.chdir('Materi')

def login():
	browser.select_form(name="flogin")
	browser["usr"] = main.ui.user.text()
	browser["pwd"] = main.ui.pswd.text()
	browser.submit()
	print browser.geturl()
	if(browser.geturl() == "https://dosen.amikom.ac.id/index.php/login"):
		 QtGui.QMessageBox.warning(None, 'Error', 'Username atau Password Salah')
		 main.close()
  		 finish.close()
		 about.close()

	else:
		print "Anda Berhasil Login"


	#masukin list dosen
	dosurl = "https://dosen.amikom.ac.id/"
	page = urllib2.urlopen(dosurl)
	soup = BeautifulSoup(page.read())
	universitas = soup.findAll('a')

	for data in universitas:
		suozo = data['href']
		if suozo.find("https://dosen.amikom.ac.id/index.php/profil/") == 0:
			hapus_sepasi = suozo.replace("https://dosen.amikom.ac.id/index.php/profil/", "")
			item = QListWidgetItem(hapus_sepasi)
			main.ui.list_dosen.addItem(item)

def pilih_dosen():
	indeks = main.ui.list_dosen.currentItem()
	gantisepasi = indeks.text().replace(" ","%20")
	matdosurl = "https://dosen.amikom.ac.id/index.php/materi/"+gantisepasi
	convlink = str(matdosurl)
	pagedosen = urllib2.urlopen(convlink)
	sopdosen = BeautifulSoup(pagedosen.read())
	materi = sopdosen.findAll('a')
	main.ui.list_materi.clear()
	ready =  convlink.split('/')
	for matdos in materi:
		limateri = matdos['href']			
		if limateri.find("http://elearning.amikom.ac.id/index.php/materi/") == 0:
			main.ui.list_materi.addItem(limateri)

def download_sekarang():
	indeks = main.ui.list_materi.currentItem()
	masuk = indeks.text().replace(" ","%20")
	ganti = str(masuk)
	pagemateri = urllib2.urlopen(ganti)
	sopmateri = BeautifulSoup(pagemateri.read())
	findmateri = sopmateri.findAll('a')
	for materilist in findmateri:
		foundmateri = materilist['href']
		if foundmateri.find("http://elearning.amikom.ac.id/index.php/download/materi/") == 0:
			target = foundmateri
			
			file_name = target.split('/')[-1]
			u = urllib2.urlopen(target)
			f = open(file_name, 'wb')
			meta = u.info()
			file_size_dl = 0
			block_sz = 8192
			size =  len(urllib2.urlopen(target).read());
			main.ui.prog.setMaximum(size)
			

			while True:
    				buffer = u.read(block_sz)
   			        if not buffer:
        				break
				
				file_size_dl += len(buffer)
				f.write(buffer)
				main.ui.prog.setValue(file_size_dl)
				
			f.close()

			QtGui.QMessageBox.information(None, 'Download Completed', 'File Download Successfully')
			main.ui.prog.setValue(0)
		 	

def aboutClose():
	about.close()

def option():
	finish.show()	

def Caption():
	file = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
	finish.ui.path.setText(file)
	os.chdir(file)

def finishOption():
	finish.close()

def CloseWindow():
	main.close()
	finish.close()
	about.close()

app.connect(main.ui.btn_login,QtCore.SIGNAL('clicked()'),login)
app.connect(main.ui.list_dosen,QtCore.SIGNAL('itemSelectionChanged()'),pilih_dosen)
app.connect(main.ui.btn_download,QtCore.SIGNAL('clicked()'),download_sekarang)
app.connect(main.ui.btn_option,QtCore.SIGNAL('clicked()'), option)
app.connect(main.ui.btn_exit,QtCore.SIGNAL('clicked()'), CloseWindow)
app.connect(finish.ui.select,QtCore.SIGNAL('clicked()'),Caption)
app.connect(finish.ui.oke,QtCore.SIGNAL('clicked()'),finishOption)
app.connect(main.ui.btn_about,QtCore.SIGNAL('clicked()'),about.show)
app.connect(about.ui.cancelButton,QtCore.SIGNAL('clicked()'), aboutClose)

sys.exit(app.exec_())
