# -*- coding: utf-8 -*-
import unittest

from cartografo import files_folder_helper as helper

RIGHT_FOLDER_PATH = 'test/files/'
WRONG_FOLDER_PATH = 'test/wrong/'
FILES = ['test/files/a.txt', 'test/files/b.json', 'test/files/c.tsv', 'test/files/d']

class TestK8SFilesFolder(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_files_from_right_folder(self):
        fs = helper.get_files_from_folder(RIGHT_FOLDER_PATH)
        fs.sort()
        self.assertEqual(fs, FILES)

    def test_get_files_from_wrong_folder(self):
        self.assertIsNone(helper.get_files_from_folder(WRONG_FOLDER_PATH))

    def test_read_existing_file(self):
        expected = 'kljaslñdjkalkasñlknasdflñkasdflkajsdf\n\nalkjasfasdfads654ḱla9ai.ñlkjaañljkadf\nñlkajñlkasdf.\n\n\nñlkansdñlknasdpfoiuqi90jqlñknañlfkvnañldkasdf.'
        data = helper.read_file(FILES[0])
        self.assertEqual(data, expected)        

    def test_read_non_existing_file(self):
        self.assertIsNone(helper.read_file(FILES[1] + ".wrong"))           


if __name__ == '__main__':
    unittest.main()        