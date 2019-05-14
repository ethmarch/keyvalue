import unittest
import os
from keyvalue.simple_keyvalue import SimpleKeyValueStore

class TestSimpleKeyValueStore(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.source = 'test_simple_key_value_store_source'
        f = open(self.source, 'w')
        f.close()
        self.store = SimpleKeyValueStore(self.source)

    def test_set(self):
        self.store.set('test', 'case')
        self.store.set('number', 42)
        self.store.set('test', 'again')

        with open(self.source) as f:
            lines = f.readlines()
            
            self.assertEqual(lines[0], 'test,case\n')
            self.assertEqual(lines[1], 'number,42\n')
            self.assertEqual(lines[2], 'test,again\n')

    def test_get(self):
        self.store.set('test', 'case')
        self.store.set('number', 42)
        self.store.set('test', 'again')

        self.assertEqual(self.store.get('number'), '42')
        self.assertEqual(self.store.get('test'), 'again')
        self.assertEqual(self.store.get('nonexistent'), 'null')
        
    @classmethod
    def tearDownClass(self):
        os.remove(self.source)

if __name__ == '__main__':
    unittest.main()





