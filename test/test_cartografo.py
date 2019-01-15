# -*- coding: utf-8 -*-
import unittest
import os
import shutil

from cartografo import cartografo

TMP_FOLDER = 'test/tmp_cartografo'

class TestK8SFilesFolder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting Up Cartografo Tests ....")
        if os.path.exists(TMP_FOLDER):
            shutil.rmtree(TMP_FOLDER)
        os.makedirs(TMP_FOLDER)

    @classmethod
    def tearDownClass(cls):
        print("Tearing down Cartografo Tests ....")
        if os.path.exists(TMP_FOLDER):
            shutil.rmtree(TMP_FOLDER)

    def setUp(self):
        pass

    def tearDown(self):
        pass     

    def test_get_data_transformer_secret(self):
        data, expected = "Hola", "SG9sYQ=="
        transformer = cartografo.get_data_transformer("Secret")
        self.assertEqual(expected, transformer(data))

    def test_get_data_transformer_configmap(self):
        data, expected = "Hola", "Hola"
        transformer = cartografo.get_data_transformer("ConfigMap")
        self.assertEqual(expected, transformer(data))        
        


if __name__ == '__main__':
    unittest.main()        