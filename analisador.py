from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from UiMain import Ui_MainWindow



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

    def run(self):
        self.MainWindow.show()  # Mostrar a janela principal
        self.app.exec_()  # Executar o loop de eventos do aplicativo

    def abrir_arquivo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self.MainWindow, "Abrir Arquivo", "", "Todos os Arquivos (*);;Texto (*.txt)", options=options)
        
        if file_name:
            with open(file_name, "r") as file:
                self.ui.textEntrada.setPlainText(file.read())
                print(f"Arquivo aberto: {file_name}")

    def salvar_arquivo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self.MainWindow, "Salvar Arquivo", "", "Todos os Arquivos (*);;Texto (*.txt)", options=options)
        
        if file_name:
            with open(file_name, "w") as file:
                file.write(self.ui.textEntrada.toPlainText())
                print(f"Arquivo salvo: {file_name}")
    def processar(self):
        print("Processando")
        text = "Este deve aparecer"
        self.ui.textSaida.setPlainText(text)




if __name__ == "__main__":
    secondary_app = Main()
    secondary_app.run()