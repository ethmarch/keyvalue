from keyvalue.keyvalue import KeyValueStore
import re

class SimpleKeyValueStore(KeyValueStore):

    def __init__(self, source):
        self.source = source

    def set(self, key: str, value: str) -> str:
        data = str(key) + ',' + str(value)
        with open(self.source, 'a') as f:
            f.write(data)

    def get(self, key: str) -> str:
        with open(self.source, 'r') as f:
            contents = f.read()
            regx = str(key) + ',(.*)$'
            matches = re.findall(regx, contents)
            if matches:
                return matches[-1].groups(0)
            else:
                return 'null'

