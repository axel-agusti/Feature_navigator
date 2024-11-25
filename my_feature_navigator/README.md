# Feature Navigator - Complemento para QGIS

**Feature Navigator** es un complemento de QGIS que facilita la navegación entre las entidades de una capa activa. Permite desplazarse de una entidad a otra, visualizar información sobre la entidad seleccionada, y realizar un zoom a la entidad en el mapa. También se guarda el estado actual del complemento para facilitar la reanudación de la navegación.

## Características

- Navegación entre las entidades de una capa activa (Siguiente, Anterior, Primero, Último).
- Visualización de información sobre la entidad actual (Índice de la entidad actual y total de entidades).
- Opción para realizar un zoom a la entidad seleccionada en el mapa.
- Barra de herramientas integrada con botones para abrir el complemento.
- Dock widget interactivo que muestra la información de la entidad y botones de navegación.
- El estado de la navegación se guarda automáticamente para facilitar su reanudación.

## Requisitos

- **QGIS 3.x** (se recomienda usar la versión más reciente de QGIS).
- **Python** (para ejecutar el complemento).

## Instalación

1. Descarga el complemento desde [el repositorio de GitHub](#).
2. Copia el complemento en el directorio de complementos de QGIS:
   - En Windows: `C:\Users\<TuNombreDeUsuario>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins`
   - En Linux: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
3. Abre QGIS y navega a `Complementos` -> `Administrar e instalar complementos`.
4. Haz clic en la pestaña `Instalar desde archivo` y selecciona la carpeta donde descargaste el complemento.
5. Activa el complemento **Feature Navigator** desde la lista de complementos instalados.

## Uso

### Abrir el Navegador de Entidades

1. Una vez instalado y habilitado, verás un botón en la barra de herramientas de QGIS llamado **"Navegador de Entidades"**.
2. Haz clic en este botón para abrir el **Dock Widget** de navegación.

### Navegación entre Entidades

- **Siguiente**: Avanza a la siguiente entidad.
- **Anterior**: Retrocede a la entidad anterior.
- **Primero**: Salta a la primera entidad.
- **Último**: Salta a la última entidad.

### Información de la Entidad

El Dock Widget muestra la siguiente información:
- **Entidad X de Y**: El índice de la entidad actual y el número total de entidades.

### Zoom a la Entidad Seleccionada

Cada vez que seleccionas una entidad, el complemento realiza un zoom sobre ella en el mapa para facilitar su visualización.

## Configuración

El complemento guarda su estado actual en un archivo JSON (`state.json`), lo que permite reanudar la navegación de donde la dejaste la próxima vez que abras QGIS.

## Problemas y Soporte

Si encuentras algún problema con el complemento, por favor, abre un [issue](https://github.com/tuusuario/FeatureNavigator/issues) en GitHub o contacta con el autor para obtener soporte.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir al desarrollo del complemento, puedes hacer un fork de este repositorio, realizar tus cambios y enviar un pull request.

## Licencia

Este complemento está bajo la [Licencia MIT](https://opensource.org/licenses/MIT).

---

*Este complemento ha sido creado como parte de un proyecto de aprendizaje en QGIS y Python. Está diseñado para facilitar la navegación en entidades dentro de QGIS.*
