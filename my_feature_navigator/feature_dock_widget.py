from qgis.PyQt.QtWidgets import QDockWidget, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton
from qgis.PyQt.QtCore import Qt

class FeatureDockWidget(QDockWidget):
    def __init__(self, plugin, parent=None):
        super().__init__("Navegador de Entidades", parent)
        self.plugin = plugin
        self.setFeatures(QDockWidget.NoDockWidgetFeatures)  # Evita el arrastre del dock
        self.setAllowedAreas(Qt.RightDockWidgetArea | Qt.LeftDockWidgetArea)

        # Crear el contenido del dock widget
        self.widget = QWidget(self)
        self.layout = QVBoxLayout(self.widget)
        self.setWidget(self.widget)

        # Etiqueta para mostrar la información de la entidad
        self.info_label = QLabel("Entidades: 0 de 0", self)
        self.layout.addWidget(self.info_label)

        # Botones para navegar entre entidades
        self.navigation_layout = QHBoxLayout()
        self.prev_button = QPushButton("<", self)
        self.next_button = QPushButton(">", self)
        self.navigation_layout.addWidget(self.prev_button)
        self.navigation_layout.addWidget(self.next_button)

        self.layout.addLayout(self.navigation_layout)

        # Conectar botones a las acciones de navegación
        self.prev_button.clicked.connect(self.on_previous_clicked)
        self.next_button.clicked.connect(self.on_next_clicked)

    def update_info(self, feature, index, total):
        """Actualizar la información de la entidad en el dock widget."""
        self.info_label.setText(f"Entidad {index + 1} de {total}")
        # Aquí podrías agregar más información sobre la entidad (atributos, etc.)
        
    def on_previous_clicked(self):
        """Navegar a la entidad anterior."""
        self.plugin.navigate(-1)
        
    def on_next_clicked(self):
        """Navegar a la siguiente entidad."""
        self.plugin.navigate(1)
