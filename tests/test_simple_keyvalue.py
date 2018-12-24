import unittest
from keyvalue.simple_keyvalue import SimpleKeyValueStore

class TestSimpleKeyValueStore(unittest.TestCase):

    def setUp(self):
        source = 'test_simple_key_value_store_source'
        f = open(source, 'w')
        f.close()
        self.store = SimpleKeyValueStore(source)

    def test_set(self):
        self.store.set('test', 'case')


