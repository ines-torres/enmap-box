from enmapbox import initAll
from enmapbox.gui.enmapboxgui import EnMAPBox
from enmapbox.gui.widgets.multiplerasterbandselectionwidget.multiplerasterbandselectionwidget import \
    MultipleRasterBandSelectionWidget
from enmapbox.testing import start_app
from enmapboxtestdata import enmap
from qgis.core import QgsRasterLayer

qgsApp = start_app()
initAll()

enmapBox = EnMAPBox(None)
widget = MultipleRasterBandSelectionWidget()
layer = QgsRasterLayer(enmap)
widget.mBand.setLayer(layer)
widget.show()

qgsApp.exec_()
