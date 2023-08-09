from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from UiMain import Ui_MainWindow
from analisadorLexico import processaALexico



class Main:
    def __init__(self):
        self.app = QApplication([])  # Instanciar o aplicativo Qt

        self.MainWindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        #Definir funções botão
        self.ui.buttonAbrir.clicked.connect(self.abrir_arquivo)
        self.ui.buttonSalvar.clicked.connect(self.salvar_arquivo)
        self.ui.buttonProcessar.clicked.connect(self.processar)

        self.textoEntrada = ""


    def run(self):
        self.MainWindow.show()  # Mostrar a janela principal
        self.app.exec_()  # Executar o loop de eventos do aplicativo

    def abrir_arquivo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self.MainWindow, "Abrir Arquivo", "", "Todos os Arquivos (*);;Texto (*.txt)", options=options)
        
        if file_name:
            with open(file_name, "r") as file:
                self.textoEntrada = file.read()
                self.ui.textEntrada.setPlainText(self.textoEntrada)
                print(f"Arquivo aberto: {file_name}")

    def salvar_arquivo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self.MainWindow, "Salvar Arquivo", "", "Todos os Arquivos (*);;Texto (*.txt)", options=options)
        
        if file_name:
            with open(file_name, "w") as file:
                file.write(self.ui.textSaida.toPlainText())
                print(f"Arquivo salvo: {file_name}")
    
    def processar(self):
        print( self.ui.textEntrada.toPlainText() )
        text = processaALexico( self.ui.textEntrada.toPlainText() )
        self.ui.textSaida.setPlainText(text)

if __name__ == "__main__":
    secondary_app = Main()
    secondary_app.run()