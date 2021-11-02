import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(-1, -1)
        self.varasto3 = Varasto(10, 12)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uuden_varaston_tilavuus_neg_syotteella_0(self):
        self.assertEqual(self.varasto2.tilavuus, 0)

    def test_uuden_varaston_saldo_neg_syotteella_0(self):
        self.assertEqual(self.varasto2.saldo, 0)

    def test_uuteen_varastoon_ei_enempaa_kuin_tilavuus(self):
        self.assertEqual(self.varasto3.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_varastoon_ei_enempaa_kuin_tilavuus(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.lisaa_varastoon(-3)

        self.assertEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varaston_tilanne_ei_muutu_neg_arvolla(self):
        self.varasto.lisaa_varastoon(6)
        self.varasto.ota_varastosta(-6)

        self.assertEqual(self.varasto.saldo, 6)

    def test_varastosta_saa_vain_sen_mita_siella_on(self):
        self.varasto.lisaa_varastoon(6)
        saatu_maara = self.varasto.ota_varastosta(8)

        self.assertEqual(saatu_maara, 6)


    def test_varasto_tilanne_tulostuu_oikein(self):
        self.varasto.lisaa_varastoon(3)
        viesti = str(self.varasto)
        self.assertEqual(viesti, "saldo = 3, vielä tilaa 7")
