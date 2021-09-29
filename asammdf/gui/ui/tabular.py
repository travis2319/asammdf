# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabular.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TabularDisplay(object):
    def setupUi(self, TabularDisplay):
        TabularDisplay.setObjectName("TabularDisplay")
        TabularDisplay.resize(821, 618)
        self.verticalLayout = QtWidgets.QVBoxLayout(TabularDisplay)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tree = QtWidgets.QTreeWidget(TabularDisplay)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        self.tree.setFont(font)
        self.tree.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tree.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tree.setUniformRowHeights(True)
        self.tree.setAllColumnsShowFocus(True)
        self.tree.setObjectName("tree")
        self.tree.headerItem().setText(0, "1")
        self.tree.header().setHighlightSections(True)
        self.tree.header().setSortIndicatorShown(False)
        self.horizontalLayout.addWidget(self.tree)
        self.tree_scroll = QtWidgets.QScrollBar(TabularDisplay)
        self.tree_scroll.setMaximum(9999)
        self.tree_scroll.setSingleStep(1)
        self.tree_scroll.setPageStep(10)
        self.tree_scroll.setOrientation(QtCore.Qt.Vertical)
        self.tree_scroll.setInvertedAppearance(False)
        self.tree_scroll.setObjectName("tree_scroll")
        self.horizontalLayout.addWidget(self.tree_scroll)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.format_selection = QtWidgets.QComboBox(TabularDisplay)
        self.format_selection.setObjectName("format_selection")
        self.format_selection.addItem("")
        self.format_selection.addItem("")
        self.format_selection.addItem("")
        self.horizontalLayout_2.addWidget(self.format_selection)
        self.sort = QtWidgets.QCheckBox(TabularDisplay)
        self.sort.setObjectName("sort")
        self.horizontalLayout_2.addWidget(self.sort)
        self.time_as_date = QtWidgets.QCheckBox(TabularDisplay)
        self.time_as_date.setObjectName("time_as_date")
        self.horizontalLayout_2.addWidget(self.time_as_date)
        self.remove_prefix = QtWidgets.QCheckBox(TabularDisplay)
        self.remove_prefix.setObjectName("remove_prefix")
        self.horizontalLayout_2.addWidget(self.remove_prefix)
        self.prefix = QtWidgets.QComboBox(TabularDisplay)
        self.prefix.setMinimumSize(QtCore.QSize(200, 0))
        self.prefix.setEditable(True)
        self.prefix.setObjectName("prefix")
        self.horizontalLayout_2.addWidget(self.prefix)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.toggle_filters_btn = QtWidgets.QPushButton(TabularDisplay)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toggle_filters_btn.setIcon(icon)
        self.toggle_filters_btn.setObjectName("toggle_filters_btn")
        self.horizontalLayout_2.addWidget(self.toggle_filters_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.filters_group = QtWidgets.QGroupBox(TabularDisplay)
        self.filters_group.setObjectName("filters_group")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.filters_group)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.add_filter_btn = QtWidgets.QPushButton(self.filters_group)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_filter_btn.setIcon(icon1)
        self.add_filter_btn.setObjectName("add_filter_btn")
        self.gridLayout_3.addWidget(self.add_filter_btn, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        self.apply_filters_btn = QtWidgets.QPushButton(self.filters_group)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/filter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.apply_filters_btn.setIcon(icon2)
        self.apply_filters_btn.setObjectName("apply_filters_btn")
        self.gridLayout_3.addWidget(self.apply_filters_btn, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(559, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 3, 1, 1)
        self.filters = MinimalListWidget(self.filters_group)
        self.filters.setMaximumSize(QtCore.QSize(16777215, 150))
        self.filters.setObjectName("filters")
        self.gridLayout_3.addWidget(self.filters, 1, 0, 1, 4)
        self.groupBox = QtWidgets.QGroupBox(self.filters_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.query = QtWidgets.QTextEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.query.sizePolicy().hasHeightForWidth())
        self.query.setSizePolicy(sizePolicy)
        self.query.setMinimumSize(QtCore.QSize(0, 7))
        self.query.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        self.query.setFont(font)
        self.query.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.query.setReadOnly(True)
        self.query.setObjectName("query")
        self.gridLayout.addWidget(self.query, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 1, 4)
        self.gridLayout_3.setColumnStretch(3, 1)
        self.verticalLayout.addWidget(self.filters_group)
        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(TabularDisplay)
        QtCore.QMetaObject.connectSlotsByName(TabularDisplay)

    def retranslateUi(self, TabularDisplay):
        _translate = QtCore.QCoreApplication.translate
        TabularDisplay.setWindowTitle(_translate("TabularDisplay", "Form"))
        self.format_selection.setItemText(0, _translate("TabularDisplay", "phys"))
        self.format_selection.setItemText(1, _translate("TabularDisplay", "hex"))
        self.format_selection.setItemText(2, _translate("TabularDisplay", "bin"))
        self.sort.setText(_translate("TabularDisplay", "Enable column sorting"))
        self.time_as_date.setText(_translate("TabularDisplay", "Time as date"))
        self.remove_prefix.setText(_translate("TabularDisplay", "Remove prefix"))
        self.toggle_filters_btn.setText(_translate("TabularDisplay", "Show filters"))
        self.filters_group.setTitle(_translate("TabularDisplay", "Filters"))
        self.add_filter_btn.setText(_translate("TabularDisplay", "Add new filter"))
        self.apply_filters_btn.setText(_translate("TabularDisplay", "Apply filters"))
        self.groupBox.setTitle(_translate("TabularDisplay", "pandas DataFrame query"))
from asammdf.gui.widgets.list import MinimalListWidget
from . import resource_rc
