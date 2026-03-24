import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000) # 10 euroa

    # Alkutilanteen tarkistus
    def test_luodun_kassapaatteen_tila_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # Käteismaksut
    def test_syo_edullisesti_kateisella_toimii_kun_raha_riittaa(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_kateisella_toimii_kun_raha_riittaa(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_edullisesti_kateisella_hylatty_kun_raha_ei_riita(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.edulliset, 0)

    # Korttimaksut
    def test_syo_edullisesti_kortilla_toimii_kun_saldo_riittaa(self):
        tulos = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertTrue(tulos)
        self.assertEqual(self.kortti.saldo_euroina(), 7.6)
        self.assertEqual(self.kassapaate.edulliset, 1)
        # Korttimaksu ei kerrytä kassan käteisvarantoa
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_syo_maukkaasti_kortilla_toimii_kun_saldo_riittaa(self):
        tulos = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertTrue(tulos)
        self.assertEqual(self.kortti.saldo_euroina(), 6.0)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_edullisesti_kortilla_hylatty_kun_saldo_ei_riita(self):
        koyha_kortti = Maksukortti(100)
        tulos = self.kassapaate.syo_edullisesti_kortilla(koyha_kortti)
        self.assertFalse(tulos)
        self.assertEqual(koyha_kortti.saldo_euroina(), 1.0)
        self.assertEqual(self.kassapaate.edulliset, 0)

    # Rahan lataus
    def test_lataa_rahaa_kortille_kasvattaa_saldoa_ja_kassaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(self.kortti.saldo_euroina(), 15.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1005.0)

    def test_lataa_negatiivinen_summa_kortille_ei_muuta_tilaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.kortti.saldo_euroina(), 10.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)


    #Puuttuvia testejä
    def test_syo_maukkaasti_kateisella_hylatty_kun_raha_ei_riita(self):
        # Yritetään ostaa maukas (400s) 300 sentillä
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtoraha, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kortilla_hylatty_kun_saldo_ei_riita(self):
        # Luodaan kortti, jolla on vain 2 euroa (maukas maksaa 4e)
        koyha_kortti = Maksukortti(200)
        tulos = self.kassapaate.syo_maukkaasti_kortilla(koyha_kortti)
        self.assertFalse(tulos)
        self.assertEqual(koyha_kortti.saldo_euroina(), 2.0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
