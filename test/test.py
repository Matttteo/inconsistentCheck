
from  fakeData import *

generator = genFakeWordPair()
generator.readFile('definitions.txt')
generator.genAndWrite()