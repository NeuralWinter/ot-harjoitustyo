import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        # Ladataan 500 senttiä (5 euroa)
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 15.0)

    def test_ota_rahaa_vahentaa_saldoa_oikein(self):
        # Otetaan 500 senttiä, saldon pitäisi laskea
        vastaus = self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)
        self.assertTrue(vastaus)

    def test_ota_rahaa_ei_vie_saldoa_negatiiviseksi(self):
        # Yritetään ottaa enemmän kuin on saldoa (1500 senttiä)
        vastaus = self.maksukortti.ota_rahaa(1500)
        # Salon pitäisi pysyä 10.0 eurossa
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
        self.assertFalse(vastaus)

    def test_str_palauttaa_oikean_merkkijonon(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")