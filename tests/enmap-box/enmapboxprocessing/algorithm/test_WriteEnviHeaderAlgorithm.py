from osgeo import gdal

from enmapboxprocessing.algorithm.testcase import TestCase
from enmapboxprocessing.algorithm.writeenviheaderalgorithm import WriteEnviHeaderAlgorithm
from enmapboxprocessing.rasterreader import RasterReader
from enmapboxprocessing.rasterwriter import RasterWriter
from enmapboxtestdata import enmap
from qgis.core import QgsProcessingException


class TestWriteEnviHeaderAlgorithm(TestCase):

    def test_tif(self):

        filename = self.filename('enmap.tif')
        ds1: gdal.Dataset = gdal.Open(enmap)
        gdal.Translate(filename, ds1)
        ds2: gdal.Dataset = gdal.Open(filename)

        reader = RasterReader(enmap)
        writer = RasterWriter(ds2)

        writer.setMetadata(reader.metadata())
        for i in range(ds1.RasterCount):
            writer.setMetadata(reader.metadata(i + 1), i + 1)
        writer.close()
        del ds1, ds2, reader, writer

        alg = WriteEnviHeaderAlgorithm()
        alg.initAlgorithm()
        parameters = {
            alg.P_RASTER: filename,
        }
        self.runalg(alg, parameters)
        with open(filename + '.hdr') as file:
            text = file.read()

        if 'fwhm = {6.0' in text:
            return  # skip test because of a value-rounding bug in GDAL

        self.assertEqual(
            """ENVI
file type = TIFF
samples = 220
lines = 400
bands = 177
wavelength units = Nanometer
wavelength = {460.0, 465.0, 470.0, 475.0, 479.0, 484.0, 489.0, 494.0, 499.0, 503.0, 508.0, 513.0, 518.0, 523.0, 528.0, 533.0, 538.0, 543.0, 549.0, 554.0, 559.0, 565.0, 570.0, 575.0, 581.0, 587.0, 592.0, 598.0, 604.0, 610.0, 616.0, 622.0, 628.0, 634.0, 640.0, 646.0, 653.0, 659.0, 665.0, 672.0, 679.0, 685.0, 692.0, 699.0, 706.0, 713.0, 720.0, 727.0, 734.0, 741.0, 749.0, 756.0, 763.0, 771.0, 778.0, 786.0, 793.0, 801.0, 809.0, 817.0, 824.0, 832.0, 840.0, 848.0, 856.0, 864.0, 872.0, 880.0, 888.0, 896.0, 915.0, 924.0, 934.0, 944.0, 955.0, 965.0, 975.0, 986.0, 997.0, 1006.9999999999999, 1018.0, 1029.0, 1040.0, 1051.0, 1063.0, 1074.0, 1086.0, 1097.0, 1109.0, 1120.0, 1132.0, 1144.0, 1155.0, 1167.0, 1179.0, 1191.0, 1203.0, 1215.0, 1227.0, 1239.0, 1251.0, 1263.0, 1275.0, 1287.0, 1299.0, 1311.0, 1323.0, 1522.0, 1534.0, 1545.0, 1557.0, 1568.0, 1579.0, 1590.0, 1601.0, 1612.0, 1624.0, 1634.0, 1645.0, 1656.0, 1667.0, 1678.0, 1689.0, 1699.0, 1710.0, 1721.0, 1731.0, 1742.0, 1752.0, 1763.0, 1773.0, 1783.0, 2044.0, 2053.0, 2062.0, 2071.0, 2080.0, 2089.0, 2098.0, 2107.0, 2115.0, 2124.0, 2133.0, 2141.0, 2150.0, 2159.0, 2167.0, 2176.0, 2184.0, 2193.0, 2201.0, 2210.0, 2218.0, 2226.0, 2234.0, 2243.0, 2251.0, 2259.0, 2267.0, 2275.0, 2283.0, 2292.0, 2300.0, 2308.0, 2315.0, 2323.0, 2331.0, 2339.0, 2347.0, 2355.0, 2363.0, 2370.0, 2378.0, 2386.0, 2393.0, 2401.0, 2409.0}
fwhm = {5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8999999999999995, 5.8999999999999995, 6.0, 6.0, 6.1000000000000005, 6.1000000000000005, 6.2, 6.2, 6.3, 6.4, 6.4, 6.5, 6.6, 6.6, 6.7, 6.8, 6.8999999999999995, 6.8999999999999995, 7.0, 7.1000000000000005, 7.2, 7.3, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 7.9, 8.0, 8.1, 8.200000000000001, 8.3, 8.4, 8.4, 8.5, 8.6, 8.7, 8.7, 8.8, 8.9, 8.9, 9.0, 9.1, 9.1, 9.2, 9.299999999999999, 9.299999999999999, 9.4, 9.4, 9.5, 9.5, 9.6, 9.6, 9.6, 9.6, 9.700000000000001, 9.700000000000001, 9.700000000000001, 11.799999999999999, 11.9, 12.1, 12.200000000000001, 12.4, 12.5, 12.7, 12.8, 12.9, 13.100000000000001, 13.2, 13.299999999999999, 13.4, 13.5, 13.6, 13.700000000000001, 13.799999999999999, 13.899999999999999, 14.0, 14.0, 14.1, 14.1, 14.200000000000001, 14.200000000000001, 14.3, 14.3, 14.3, 14.4, 14.4, 14.4, 14.4, 14.4, 14.4, 14.4, 14.4, 14.4, 14.4, 13.700000000000001, 13.6, 13.6, 13.5, 13.5, 13.4, 13.4, 13.299999999999999, 13.2, 13.2, 13.100000000000001, 13.100000000000001, 13.0, 12.9, 12.9, 12.8, 12.8, 12.7, 12.7, 12.6, 12.5, 12.5, 12.4, 12.4, 12.3, 10.9, 10.8, 10.8, 10.7, 10.7, 10.6, 10.6, 10.5, 10.5, 10.4, 10.4, 10.4, 10.3, 10.3, 10.200000000000001, 10.200000000000001, 10.1, 10.1, 10.1, 10.0, 10.0, 9.9, 9.9, 9.9, 9.799999999999999, 9.799999999999999, 9.700000000000001, 9.700000000000001, 9.700000000000001, 9.6, 9.6, 9.6, 9.5, 9.5, 9.4, 9.4, 9.4, 9.299999999999999, 9.299999999999999, 9.299999999999999, 9.2, 9.2, 9.1, 9.1, 9.1}
bbl = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
data ignore value = -99.0
""",
            text
        )

    def test_envi(self):

        filename = self.filename('enmap.bsq')
        ds1: gdal.Dataset = gdal.Open(enmap)
        gdal.Translate(filename, ds1, format='ENVI')
        ds2: gdal.Dataset = gdal.Open(filename)
        ds2.SetMetadata(ds1.GetMetadata())
        del ds1, ds2

        alg = WriteEnviHeaderAlgorithm()
        alg.initAlgorithm()
        parameters = {
            alg.P_RASTER: filename,
        }
        try:
            self.runalg(alg, parameters)
        except QgsProcessingException as error:
            self.assertEqual(str(error), 'Raster layer is not a GeoTiff')
