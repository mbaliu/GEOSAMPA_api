# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'geosampa_api_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GEOSAMPA_apiDialogBase(object):
    def setupUi(self, GEOSAMPA_apiDialogBase):
        GEOSAMPA_apiDialogBase.setObjectName("GEOSAMPA_apiDialogBase")
        GEOSAMPA_apiDialogBase.setWindowModality(QtCore.Qt.NonModal)
        GEOSAMPA_apiDialogBase.resize(738, 358)
        self.textBrowser = QtWidgets.QTextBrowser(GEOSAMPA_apiDialogBase)
        self.textBrowser.setGeometry(QtCore.QRect(463, 9, 266, 331))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(266, 0))
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setObjectName("textBrowser")
        self.layoutWidget = QtWidgets.QWidget(GEOSAMPA_apiDialogBase)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 80, 116, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.camada_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camada_2.sizePolicy().hasHeightForWidth())
        self.camada_2.setSizePolicy(sizePolicy)
        self.camada_2.setObjectName("camada_2")
        self.horizontalLayout_3.addWidget(self.camada_2)
        self._camada_2 = QtWidgets.QComboBox(self.layoutWidget)
        self._camada_2.setObjectName("_camada_2")
        self.horizontalLayout_3.addWidget(self._camada_2)
        self.layoutWidget_2 = QtWidgets.QWidget(GEOSAMPA_apiDialogBase)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 120, 116, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.camada_3 = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camada_3.sizePolicy().hasHeightForWidth())
        self.camada_3.setSizePolicy(sizePolicy)
        self.camada_3.setObjectName("camada_3")
        self.horizontalLayout_4.addWidget(self.camada_3)
        self._camada_3 = QtWidgets.QComboBox(self.layoutWidget_2)
        self._camada_3.setObjectName("_camada_3")
        self.horizontalLayout_4.addWidget(self._camada_3)
        self.layoutWidget1 = QtWidgets.QWidget(GEOSAMPA_apiDialogBase)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 49, 116, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.camada = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camada.sizePolicy().hasHeightForWidth())
        self.camada.setSizePolicy(sizePolicy)
        self.camada.setObjectName("camada")
        self.horizontalLayout_2.addWidget(self.camada)
        self._camada = QtWidgets.QComboBox(self.layoutWidget1)
        self._camada.setObjectName("_camada")
        self.horizontalLayout_2.addWidget(self._camada)
        self.button_box = QtWidgets.QDialogButtonBox(GEOSAMPA_apiDialogBase)
        self.button_box.setGeometry(QtCore.QRect(20, 320, 156, 23))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.layoutWidget2 = QtWidgets.QWidget(GEOSAMPA_apiDialogBase)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 269, 191, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self._diretorio = QtWidgets.QLineEdit(self.layoutWidget2)
        self._diretorio.setEnabled(True)
        self._diretorio.setInputMask("")
        self._diretorio.setText("")
        self._diretorio.setObjectName("_diretorio")
        self.horizontalLayout.addWidget(self._diretorio)
        self._diretorio_botao = QtWidgets.QPushButton(self.layoutWidget2)
        self._diretorio_botao.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._diretorio_botao.sizePolicy().hasHeightForWidth())
        self._diretorio_botao.setSizePolicy(sizePolicy)
        self._diretorio_botao.setMaximumSize(QtCore.QSize(50, 23))
        self._diretorio_botao.setObjectName("_diretorio_botao")
        self.horizontalLayout.addWidget(self._diretorio_botao)
        self.line = QtWidgets.QFrame(GEOSAMPA_apiDialogBase)
        self.line.setGeometry(QtCore.QRect(20, 200, 446, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(GEOSAMPA_apiDialogBase)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(10, 250, 51, 16))
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(GEOSAMPA_apiDialogBase)
        self.label.setGeometry(QtCore.QRect(10, 10, 152, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setAcceptDrops(False)
        self.label.setObjectName("label")

        self.retranslateUi(GEOSAMPA_apiDialogBase)
        self.button_box.accepted.connect(GEOSAMPA_apiDialogBase.accept)
        self.button_box.rejected.connect(GEOSAMPA_apiDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(GEOSAMPA_apiDialogBase)

    def retranslateUi(self, GEOSAMPA_apiDialogBase):
        _translate = QtCore.QCoreApplication.translate
        GEOSAMPA_apiDialogBase.setWindowTitle(_translate("GEOSAMPA_apiDialogBase", "GEOSAMPA api"))
        self.textBrowser.setHtml(_translate("GEOSAMPA_apiDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/plugins/croqui_fiscal/resources/spurbanismo-color-small.png\" /><img src=\":/plugins/GEOSAMPA_api/resources/spurbanismo-color-small.png\" /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:11pt; font-weight:600; color:#4d4d4d;\">MODO DE USAR</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">1. PROVEDOR -</span> Selecione o provedor desejado. O do Cidadão é de acesso a todos, já o do Servidor Público é somente válido com acesso ao sistema PRODAM.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">2. ENTRADA DO DADO -</span> Selecione o modo de entrada dos dados; se será pela seleção de feições da geometria ou se será por meio de entrada de texto. ATENÇÃO: na entrada de textos (Lista de SQ) os dados DEVEM ser separados por vírgula e espaço juntos (, ).</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">3. CAMPOS -</span> Caso necessário, escolha os campos para o setor e para a quadra.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">4. SAÍDA -</span> Caso necessário, escolha a pasta de saída dos dados. É possível indicar uma pasta no arquivo &quot;Diretorio_QuadrasFiscais.txt&quot; como pasta padrão.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:11pt; font-weight:600; color:#4d4d4d;\">OBJETIVO</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Visa facilitar a obtenção dos croquis fiscais da cidade de São Paulo, de forma a agilizar o trabalho de servidores públicos e pesquisadores na análise da estrutura fundiária das quadras.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#5f5f5f;\">Reportar erro:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600; color:#5f5f5f;\">Gitbub:</span><span style=\" font-size:7pt; color:#5f5f5f;\">--</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600; color:#5f5f5f;\">Email: </span><span style=\" font-size:7pt; color:#5f5f5f;\">ma.baliu@gmail.com</span></p></body></html>"))
        self.camada_2.setText(_translate("GEOSAMPA_apiDialogBase", "Camada"))
        self.camada_3.setText(_translate("GEOSAMPA_apiDialogBase", "Camada"))
        self.camada.setText(_translate("GEOSAMPA_apiDialogBase", "Camada"))
        self._diretorio.setPlaceholderText(_translate("GEOSAMPA_apiDialogBase", "Selecione a pasta onde salvar os croquis..."))
        self._diretorio_botao.setText(_translate("GEOSAMPA_apiDialogBase", "..."))
        self.label_4.setText(_translate("GEOSAMPA_apiDialogBase", "Salvar em:"))
        self.label.setText(_translate("GEOSAMPA_apiDialogBase", "GeoSampa - API"))

import resources_rc
