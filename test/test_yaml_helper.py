# -*- coding: utf-8 -*-
import unittest
import datetime
import os
import shutil

from cartografo import yaml_helper as helper

RIGHT_FOLDER_PATH = 'test/k8s/'
WRONG_FOLDER_PATH = 'test/wrong/'
CONFIG_MAP_FILE = 'test/k8s/my_configmap.yaml'
SECRETS_FILE = 'test/k8s/my_secrets.yaml'

TMP_FOLDER = 'test/tmp_yaml_helper'

class TestK8SYamlHelper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting Up Yaml Tests ....")
        if os.path.exists(TMP_FOLDER):
            shutil.rmtree(TMP_FOLDER)
        os.makedirs(TMP_FOLDER)

    @classmethod
    def tearDownClass(cls):
        print("Tearing down Yaml Tests ....")
        if os.path.exists(TMP_FOLDER):
            shutil.rmtree(TMP_FOLDER)

    def setUp(self):
        pass
        

    def tearDown(self):
        pass

    def test_get_data_from_existing_yaml(self):
        expected = {'kind': 'ConfigMap', 'data': {'game.properties': 'enemies=aliens\nlives=3\nenemies.cheat=true\nenemies.cheat.level=noGoodRotten\nsecret.code.passphrase=UUDDLRLRBABAS\nsecret.code.allowed=true\nsecret.code.lives=30\n', 'ui.properties': 'color.good=purple\ncolor.bad=yellow\nallow.textmode=true\nhow.nice.to.look=fairlyNice'}, 'apiVersion': 'v1', 'metadata': {'uid': 'b4952dc3-d670-11e5-8cd0-68f728db1985', 'resourceVersion': '516', 'creationTimestamp': datetime.datetime(2016, 2, 18, 18, 52, 5), 'namespace': 'default', 'selfLink': '/api/v1/namespaces/default/configmaps/game-config', 'name': 'game-config'}}
        data = helper.read_yaml_file(CONFIG_MAP_FILE)
        self.assertEqual(data, expected)

    def test_get_data_from_non_existing_yaml(self):
        expected = {'kind': 'ConfigMap', 'apiVersion': 'v1', 'data': {}, 'metadata': {'name': 'type the name'}}
        data = helper.read_yaml_file(CONFIG_MAP_FILE + ".wrong")
        self.assertEqual(data, expected)    

    def test_save_yaml(self):
        data = {'kind': 'ConfigMap', 'apiVersion': 'v1', 'data': {'name': 'test'}}
        yaml_path = os.path.join(TMP_FOLDER, "my_yaml.yaml")
        helper.write_yaml_file(yaml_path, data)
        self.assertTrue(os.path.isfile(yaml_path))

    def test_save_yaml_that_already_exists(self):
        data = {'kind': 'ConfigMap', 'apiVersion': 'v1', 'data': {'name': 'test'}}
        yaml_path = os.path.join(TMP_FOLDER, "my_yaml2.yaml")
        open(yaml_path, 'w').close()
        helper.write_yaml_file(yaml_path, data)
        self.assertTrue(os.path.isfile(yaml_path))


if __name__ == '__main__':
    unittest.main()        