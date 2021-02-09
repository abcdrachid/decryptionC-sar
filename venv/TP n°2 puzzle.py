import random
import string

from pprint import pprint

handle = open('/etc/dictionaries-common/words')
words = handle.readlines()
handle.close()
words = [ random.choice(words).upper().replace ("'", '').strip ]
