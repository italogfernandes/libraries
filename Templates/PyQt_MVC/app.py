from PyQt4 import QtGui
import sys
from views import base
import matplotlib.pyplot as plt #biblioteca para plotar as coisa


class RelataLabApp(QtGui.QMainWindow, base.Ui_MainWindow):
    def __init__(self, parent=None):
        super(RelataLabApp, self).__init__(parent)
        self.setupUi(self)
    	self.btn_prox_dados.clicked.connect(self.plotarDados)
    
    def plotarDados(self):
    	print("Ainda to fazendo calma ae");
    
		#TODO:	Receber dados da coluna
		#		Salva-los nos vetores x e y
	   	#Sugestao: self.tabela_dados.item(1,1)
		
		#plotando:
    '''
    	plt.scatter(x,y)
		plt.title("Dados inseridos")
		plt.xlabel("X")
		plt.ylabel("Y")
		plt.autoscale(tight=True)
		plt.grid()
		plt.show()
	'''
    

def main():
    app = QtGui.QApplication(sys.argv)
    form = RelataLabApp()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()
