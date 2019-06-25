# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'croqui_fiscal_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SP_CroquiFiscalDialogBase(object):
    def setupUi(self, SP_CroquiFiscalDialogBase):
        SP_CroquiFiscalDialogBase.setObjectName("SP_CroquiFiscalDialogBase")
        SP_CroquiFiscalDialogBase.resize(598, 328)
        self.button_box = QtWidgets.QDialogButtonBox(SP_CroquiFiscalDialogBase)
        self.button_box.setGeometry(QtCore.QRect(220, 290, 171, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.label = QtWidgets.QLabel(SP_CroquiFiscalDialogBase)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(SP_CroquiFiscalDialogBase)
        self.line.setGeometry(QtCore.QRect(10, 190, 381, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.setor = QtWidgets.QComboBox(SP_CroquiFiscalDialogBase)
        self.setor.setEnabled(False)
        self.setor.setGeometry(QtCore.QRect(50, 150, 131, 31))
        self.setor.setObjectName("setor")
        self.label_2 = QtWidgets.QLabel(SP_CroquiFiscalDialogBase)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(SP_CroquiFiscalDialogBase)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(200, 160, 47, 13))
        self.label_3.setObjectName("label_3")
        self.quadra = QtWidgets.QComboBox(SP_CroquiFiscalDialogBase)
        self.quadra.setEnabled(False)
        self.quadra.setGeometry(QtCore.QRect(250, 150, 131, 31))
        self.quadra.setObjectName("quadra")
        self.textBrowser = QtWidgets.QTextBrowser(SP_CroquiFiscalDialogBase)
        self.textBrowser.setGeometry(QtCore.QRect(400, 10, 191, 311))
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(SP_CroquiFiscalDialogBase)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(70, 230, 281, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(SP_CroquiFiscalDialogBase)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(10, 230, 71, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(SP_CroquiFiscalDialogBase)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(360, 230, 31, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(QPackageDialogBase.diretorio)

        self.O_selectedFeatures = QtWidgets.QRadioButton(SP_CroquiFiscalDialogBase)
        self.O_selectedFeatures.setGeometry(QtCore.QRect(30, 40, 161, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.O_selectedFeatures.setFont(font)
        self.O_selectedFeatures.setChecked(True)
        self.O_selectedFeatures.setObjectName("O_selectedFeatures")
        self.buttonGroup = QtWidgets.QButtonGroup(SP_CroquiFiscalDialogBase)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.O_selectedFeatures)
        self.O_selectedFeatures_2 = QtWidgets.QRadioButton(SP_CroquiFiscalDialogBase)
        self.O_selectedFeatures_2.setEnabled(False)
        self.O_selectedFeatures_2.setGeometry(QtCore.QRect(30, 120, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.O_selectedFeatures_2.setFont(font)
        self.O_selectedFeatures_2.setObjectName("O_selectedFeatures_2")
        self.buttonGroup.addButton(self.O_selectedFeatures_2)
        self.O_selectedFeatures_3 = QtWidgets.QRadioButton(SP_CroquiFiscalDialogBase)
        self.O_selectedFeatures_3.setEnabled(False)
        self.O_selectedFeatures_3.setGeometry(QtCore.QRect(30, 70, 161, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.O_selectedFeatures_3.setFont(font)
        self.O_selectedFeatures_3.setChecked(False)
        self.O_selectedFeatures_3.setObjectName("O_selectedFeatures_3")
        self.buttonGroup.addButton(self.O_selectedFeatures_3)
        self.label_5 = QtWidgets.QLabel(SP_CroquiFiscalDialogBase)
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QtCore.QRect(190, 89, 47, 13))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.quadra_2 = QtWidgets.QComboBox(SP_CroquiFiscalDialogBase)
        self.quadra_2.setEnabled(False)
        self.quadra_2.setGeometry(QtCore.QRect(250, 80, 131, 31))
        self.quadra_2.setObjectName("quadra_2")

        self.retranslateUi(SP_CroquiFiscalDialogBase)
        self.button_box.accepted.connect(SP_CroquiFiscalDialogBase.accept)
        self.button_box.rejected.connect(SP_CroquiFiscalDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(SP_CroquiFiscalDialogBase)

    def retranslateUi(self, SP_CroquiFiscalDialogBase):
        _translate = QtCore.QCoreApplication.translate
        SP_CroquiFiscalDialogBase.setWindowTitle(_translate("SP_CroquiFiscalDialogBase", "Croqui Fiscal"))
        self.label.setText(_translate("SP_CroquiFiscalDialogBase", "CROQUI FISCAL"))
        self.label_2.setText(_translate("SP_CroquiFiscalDialogBase", "Setor:"))
        self.label_3.setText(_translate("SP_CroquiFiscalDialogBase", "Quadra:"))
        self.textBrowser.setHtml(_translate("SP_CroquiFiscalDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:11pt; font-weight:600; color:#4d4d4d;\">DESCRIÇÃO</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\';\">Este plugin baixará as </span><span style=\" font-family:\'arial\'; font-weight:600;\">plantas de croqui fiscal</span><span style=\" font-family:\'arial\';\"> do site &lt;&gt;.</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\';\">Elas serão salvas na pasta: &lt;&gt;</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:11pt; font-weight:600; color:#4d4d4d;\">INSTRUÇÃO</span></p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'arial\';\"><br /></p></body></html>"))
        self.label_4.setText(_translate("SP_CroquiFiscalDialogBase", "Salvar em:"))
        self.pushButton.setText(_translate("SP_CroquiFiscalDialogBase", "..."))
        self.O_selectedFeatures.setText(_translate("SP_CroquiFiscalDialogBase", "Usar feições selecionadas"))
        self.O_selectedFeatures_2.setText(_translate("SP_CroquiFiscalDialogBase", "Campos de Setor e Quadra"))
        self.O_selectedFeatures_3.setText(_translate("SP_CroquiFiscalDialogBase", "Campo de SQ"))
        self.label_5.setText(_translate("SP_CroquiFiscalDialogBase", "SQ:"))

