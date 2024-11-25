from qgis.PyQt.QtWidgets import QAction, QDockWidget, QLabel, QVBoxLayout, QPushButton, QWidget, QSizePolicy, QHBoxLayout
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtCore import Qt
from qgis.utils import iface
from qgis.core import QgsProject, Qgis
import os
import json


class FeatureNavigator:
    def __init__(self, iface):
        self.iface = iface
        self.layer = None
        self.index = 0
        self.feature_list = []
        self.state_file = os.path.join(os.path.dirname(__file__), "state.json")
        self.load_state()

        self.dock_widget = None
        self.icon_path = os.path.join(os.path.dirname(__file__), 'icons', 'navigator_icon.png')
        self.toolbar = self.iface.addToolBar("Navegador de Entidades")

    def initGui(self):
        """Inicializa la barra de herramientas y los controles de navegación."""
        icon = QIcon(self.icon_path) if os.path.exists(self.icon_path) else QIcon()
        self.toggle_action = QAction(icon, "Abrir Navegador de Entidades", self.iface.mainWindow())
        self.toggle_action.triggered.connect(self.toggle_plugin)
        self.toolbar.addAction(self.toggle_action)

        self.iface.layerTreeView().currentLayerChanged.connect(self.on_layer_changed)

    def toggle_plugin(self):
        """Abre o cierra el dock widget."""
        if not self.dock_widget:
            self.dock_widget = FeatureDockWidget(self)
            self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dock_widget)
        else:
            self.iface.removeDockWidget(self.dock_widget)
            self.dock_widget = None

    def load_state(self):
        """Carga el estado guardado del plugin."""
        if os.path.exists(self.state_file):
            with open(self.state_file, "r") as f:
                state = json.load(f)
                self.index = state.get("index", 0)

    def save_state(self):
        """Guarda el estado actual del plugin."""
        state = {"index": self.index}
        with open(self.state_file, "w") as f:
            json.dump(state, f)

    def unload(self):
        """Limpia los recursos al desactivar el plugin."""
        self.save_state()
        if self.dock_widget:
            self.iface.removeDockWidget(self.dock_widget)
            self.dock_widget = None
        if self.toolbar:
            self.toolbar.clear()
            self.toolbar = None

    def load_layer(self):
        """Carga la capa activa y las entidades."""
        self.layer = self.iface.activeLayer()
        if not self.layer:
            self.iface.messageBar().pushMessage("Error", "No hay capa activa.", level=Qgis.Critical)
            return
        self.feature_list = list(self.layer.getFeatures())
        if not self.feature_list:
            self.iface.messageBar().pushMessage("Error", "La capa no tiene entidades.", level=Qgis.Critical)
            return
        self.index = 0
        if self.dock_widget:
            self.dock_widget.update_info(self.feature_list[self.index], self.index, len(self.feature_list))

    def navigate(self, step):
        """Navega entre las entidades."""
        if not self.layer or not self.feature_list:
            self.load_layer()
        if self.feature_list:
            self.index = (self.index + step) % len(self.feature_list)
            self.show_feature(self.feature_list[self.index])
            if self.dock_widget:
                self.dock_widget.update_info(self.feature_list[self.index], self.index, len(self.feature_list))

    def show_feature(self, feature):
        """Selecciona y muestra la entidad en el mapa."""
        if self.layer:
            self.layer.removeSelection()
            self.layer.selectByIds([feature.id()])
            if self.layer.selectedFeatureCount() > 0:
                self.iface.mapCanvas().zoomToSelected(self.layer)
            else:
                self.iface.messageBar().pushMessage("Error", "No se pudo seleccionar la entidad.", level=Qgis.Warning)

    def on_layer_changed(self, layer):
        """Actualiza la capa activa y las entidades."""
        if layer:
            self.layer = layer
            self.load_layer()


class FeatureDockWidget(QDockWidget):
    def __init__(self, navigator):
        super().__init__("Navegador de entidades")
        self.navigator = navigator

        # Elementos de UI
        self.label = QLabel("No hay entidades seleccionadas.")
        
        # Crear un layout con botones de navegación
        button_layout = self.create_navigation_buttons()

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(button_layout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setWidget(widget)

    def update_info(self, feature, index, total):
        """Actualiza la información mostrada en el dock."""
        self.label.setText(f"Entidad {index + 1} de {total}")

    def create_navigation_buttons(self):
        """Crea los botones de navegación y sus acciones."""
        actions = [
            ("<< Primero", lambda: self.navigator.navigate(-self.navigator.index)),
            ("◁ Anterior", lambda: self.navigator.navigate(-1)),
            ("Siguiente ▷", lambda: self.navigator.navigate(1)),
            ("Último >>", lambda: self.navigator.navigate(len(self.navigator.feature_list) - self.navigator.index - 1))
        ]

        button_layout = QHBoxLayout()
        for text, action in actions:
            button = self.create_navigation_button(text, action)
            button_layout.addWidget(button)

        return button_layout

    @staticmethod
    def create_navigation_button(text, action):
        """Crea un botón de navegación con su acción conectada."""
        button = QPushButton(text)
        button.clicked.connect(action)
        return button
