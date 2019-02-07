from sys import path

path.append('..\\')
from easyping.core import *


def test(url, quick, n):
    print('\n\rTest {}\n'.format(n))
    
    session = EasyPing()
    session.ping(url, quick)
    
    print('\n\rFine\n')
    
nodes = [
    'google.com',
    'yahoo.com',
    'duckduckgo.com',
    'none.uncorrect'
]


if __name__ == '__main__':
    n = 1
    
    n += 1; test(nodes, False, n)
    n += 1; test(nodes, True, n)
    for i in nodes:
        n += 1; test(i, False, n)
        n += 1; test(i, True, n)
    
    print('\a\n!Congratulations test was passed!')
    
    

