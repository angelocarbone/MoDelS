# !/usr/bin/env python3
# -*- coding:utf-8 -*-


import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QPushButton

from config import ROOT_DIR
from model import Model
from controller import Controller
from functools import partial

from core.structures import VehicleCausalFactor, CausalFactor

qt_creator_file = ROOT_DIR + "/view/gui.ui"
print(qt_creator_file)
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)
tick = QtGui.QImage('tick.png')


class Gui(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self._list_of_scenarios = None
        self._list_of_vehicle_causal_factor = None
        self._list_of_sub_scenarios = []
        _current_driver_causal_factor_value = None

        self.setupUi(self)
        self.m_obj = Model()
        self.c_obj = self.make_controller()  # Controller object

        self._init_ui_object()

        self._load_scenarios()
        self._load_ego_causal_factor()
        self._load_vehicle_causal_factor()
        self._load_pedestrian_causal_factor()

        self.attach2controller(self.c_obj)
        self.statusBar().showMessage('Ready')

    def _init_ui_object(self):
        self.radioButton_experience_factor.causal_factor = "experience"
        self.radioButton_mental_or_emotional_factor.causal_factor = "mental_or_emotional"
        self.radioButton_phy_or_phy_factor.causal_factor = "phy_or_phy"

    def _load_ego_causal_factor(self):
        pass

    def _load_vehicle_causal_factor(self):
        self._list_of_vehicle_causal_factor = self.c_obj.list_of_vehicle_causal_factor()
        driver = self._list_of_vehicle_causal_factor.get('cf_driver')
        self.comboBox_driver_causal_factor.addItem("")
        for k in driver.items():
            id = k[1]["id"]
            name = k[1]["name"]
            description = k[1]["description"]
            self.comboBox_driver_causal_factor.addItem(name)

        vehicle = self._list_of_vehicle_causal_factor.get('cf_vehicle')
        self.comboBox_vehicle_causal_factor.addItem("")
        for k in vehicle.items():
            id = k[1]["id"]
            name = k[1]["name"]
            description = k[1]["description"]
            self.comboBox_vehicle_causal_factor.addItem(name)

    def _load_pedestrian_causal_factor(self):
        pass

    def _load_scenarios(self):
        self._list_of_scenarios = self.c_obj.list_of_scenarios()
        self.comboBox_list_of_scenarios.addItem("")
        for s in self._list_of_scenarios:
            self.comboBox_list_of_scenarios.addItem(self._list_of_scenarios[s]["name"])

    def _load_scenario_data(self, index):
        self.label_scenario_description.setText("")
        self.comboBox_select_vehicle.clear()
        self.label_scenario_description.setText(self._list_of_scenarios[index-1]["description"])
        self.comboBox_select_vehicle.addItem(self._list_of_scenarios[index-1]["vehicle_name"],
                                             userData=self._list_of_scenarios[index-1]["vehicle_id"])

        self._load_sub_scenarios(index-1)
        # TODO: Add here all things to fill fields in UI.

    def _load_sub_scenarios(self, index):
        self.tableWidget_related_scenarios.setRowCount(0)

        if str(index) in self._list_of_scenarios:
            if 'sub_scenarios' in self._list_of_scenarios[index]:
                _ = self._list_of_scenarios[index]['sub_scenarios']

                for i in _:
                    # Retrieve text from QLineEdit
                    id = str(i)
                    name = str(_[i]['name'])
                    description = str(_[i]['description'])
                    run_me = QPushButton('Run')
                    # run_me.clicked.connect(lambda: self._run_sub_scenario(id))
                    run_me.clicked.connect(partial(self._run_sub_scenario, id))

                    # Create a empty row at bottom of table
                    numRows = self.tableWidget_related_scenarios.rowCount()
                    self.tableWidget_related_scenarios.insertRow(numRows)
                    # Add text to the row
                    self.tableWidget_related_scenarios.setItem(numRows, 0, QtWidgets.QTableWidgetItem(id))
                    self.tableWidget_related_scenarios.setItem(numRows, 1, QtWidgets.QTableWidgetItem(name))
                    self.tableWidget_related_scenarios.setItem(numRows, 2, QtWidgets.QTableWidgetItem(description))
                    self.tableWidget_related_scenarios.setCellWidget(numRows, 3, run_me)

    def _run_sub_scenario(self, value):
        print("Run sub scenario {}".format(value))
        scenario_to_run = self._list_of_sub_scenarios[value]
        self.c_obj.run_sub_scenario_callback(scenario_to_run)

    def _run_scenario(self):
        scenario_name = self.comboBox_list_of_scenarios.currentText()
        self.c_obj.run_scenario_callback(scenario_name)

    def make_controller(self):
        controller = Controller(self, self.m_obj)
        return controller

    def attach2controller(self, controller):
        # self.action_open_scenario.triggered.connect(self.action_open_file_name_dialog)
        # self.action_exit.triggered.connect(self.action_exit_callback)
        # self.action_about_models.triggered.connect(self.action_about_models_callback)
        # self.action_licenses.triggered.connect(self.action_licenses_callback)
        # self.withdraw_btn.clicked.connect(controller.withdraw_btn_callback)
        # self.deposit_btn.clicked.connect(controller.deposit_btn_callback)
        self.pushButton_run_scenario.clicked.connect(self._run_scenario)
        self.pushButton_update_scenario.clicked.connect(self._update_scenario)
        self.comboBox_list_of_scenarios.currentIndexChanged.connect(self._load_scenario_data)
        self.radioButton_experience_factor.toggled.connect(self._update_human_factor)
        self.radioButton_mental_or_emotional_factor.toggled.connect(self._update_human_factor)
        self.radioButton_phy_or_phy_factor.toggled.connect(self._update_human_factor)
        self.comboBox_driver_causal_factor.currentIndexChanged.connect(self._current_driver_causal_factor)

    def _current_driver_causal_factor(self, index):
        self._current_driver_causal_factor_value = self.comboBox_driver_causal_factor.itemText(index)
        print(self._current_driver_causal_factor_value)

    def _update_scenario(self):
        index = self.comboBox_select_vehicle.currentIndex()
        vehicle_id = self.comboBox_select_vehicle.itemData(index)
        self._list_of_sub_scenarios = self.c_obj.update_scenario_callback(vehicle_id)
        self._load_sub_scenarios_2()

    def _load_sub_scenarios_2(self):
        # TODO: To delete!
        scenario_to_run = []
        self.tableWidget_related_scenarios.setRowCount(0)
        if self._current_driver_causal_factor_value == "DrivingExperience":
            scenario_to_run.append(0)
            scenario_to_run.append(1)
            scenario_to_run.append(2)
            scenario_to_run.append(3)
        elif self._current_driver_causal_factor_value == "Distraction":
            scenario_to_run.append(0)
            scenario_to_run.append(1)
        elif self._current_driver_causal_factor_value == "Fatigued":
            scenario_to_run.append(3)

        for index in scenario_to_run:
            id_ = index
            name = "Sub Scenario {}".format(id)
            description = ""
            run_me = QPushButton('Run')
            run_me.clicked.connect(partial(self._run_sub_scenario, id_))

            # Create a empty row at bottom of table
            numRows = self.tableWidget_related_scenarios.rowCount()
            self.tableWidget_related_scenarios.insertRow(numRows)
            # Add text to the row
            self.tableWidget_related_scenarios.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(id_)))
            self.tableWidget_related_scenarios.setItem(numRows, 1, QtWidgets.QTableWidgetItem(name))
            self.tableWidget_related_scenarios.setItem(numRows, 2, QtWidgets.QTableWidgetItem(description))
            self.tableWidget_related_scenarios.setCellWidget(numRows, 3, run_me)


    def _update_human_factor(self):
        self.comboBox_driver_causal_factor.clear()
        rb = self.sender()
        causal_factor = []
        if rb.isChecked():
            print("causal factor: {}".format(rb.causal_factor))
            if rb.causal_factor == "experience":
                causal_factor = self.c_obj.get_experience_causal_factor()
            elif rb.causal_factor == "mental_or_emotional":
                causal_factor = self.c_obj.get_mental_or_emotional_causal_factor()
            elif rb.causal_factor == "phy_or_phy":
                causal_factor = self.c_obj.get_phy_or_phy_causal_factor()

            self.comboBox_driver_causal_factor.addItem("")
            self.comboBox_driver_causal_factor.addItems(causal_factor)

    def action_exit_callback(self):
        if self.c_obj.action_exit_callback():
            Qt.instance().quit

    @staticmethod
    def action_about_models_callback():
        QtWidgets.QMessageBox.information(None, "Information",
                                "This work is done by <a href='https://www.infotiv.se'>Infotiv AB</a> under <a href='https://valu3s.eu/'>VALU3S</a> project. This project has received funding from the <a href='https://www.ecsel.eu'>ECSEL</a> Joint Undertaking (JU) under grant agreement No 876852. The JU receives support from the European Union’s Horizon 2020 research and innovation programme and Austria, Czech Republic, Germany, Ireland, Italy, Portugal, Spain, Sweden, Turkey. This project is started and currently maintained by Hamid Ebadi.")

    @staticmethod
    def action_licenses_callback():
        license = open('../Licenses/LICENSE_MoDelS', 'r').read()
        # QtWidgets.QScrollArea(QtWidgets.QMessageBox.Information, "Linceses", str(license))

    def action_open_file_name_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "ASAM OpenSCENARIO (*.xosc)", options=options)
        if file_name:
            result = self.c_obj.action_open_scenario_callback(file_name)
            if result:
                print('Ok')
            else:
                print('No Ok')


class Launcher:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Launcher, cls).__new__(cls)
            # Put any initialization here.
            app = QtWidgets.QApplication(sys.argv)
            window = Gui()
            window.show()
            app.exec_()
        return cls._instance
