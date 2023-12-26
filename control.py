from PyQt5 import uic, QtWidgets

def imc():

    peso = formulario.txtPeso.text()
    peso = float(peso)

    altura = formulario.txtAltura.text()
    altura = float(altura)

    imc = peso / (altura * altura)

    if imc < 16.9:
        formulario.txtresultado.setText(str(f' Muito Abaixo do Peso: {imc:.2f}'))
    elif imc == 17 or imc <= 18.4:    
        formulario.txtresultado.setText(str(f' Abaixo do Peso : {imc:.2f}'))
    elif imc == 18.5 or imc <= 24.9:
        formulario.txtresultado.setText(str(f' Peso Normal : {imc:.2f}'))
    elif imc == 25 or imc <= 29.9:
        formulario.txtresultado.setText(str(f' Acima do Peso : {imc:.2f}')) 
    elif imc == 30 or imc <= 34.9:
        formulario.txtresultado.setText(str(f' Obesidade Grau I : {imc:.2f}'))
    elif imc == 35 or imc <= 40:
        formulario.txtresultado.setText(str(f' Obesidade Grau II : {imc:.2f}'))
    else:
         formulario.txtresultado.setText(str(f' Obesidade Grau III : {imc:.2f}'))


#comando usado para controlar os itens na tela
app = QtWidgets.QApplication([])

#Comando usado para chamar a tela
formulario = uic.loadUi('tela.ui')

#Comando usado acionar o botão calcular e chamar a função principal
formulario.btnCalcular.clicked.connect(imc)

formulario.show()

#comando usando para carregar os itens na tela
app.exec()