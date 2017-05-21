import random
import sys
from collections import namedtuple

from lxml import etree


Entry = namedtuple('Entry', ['filename', 'line', 'length'])


if __name__ == '__main__':
    filename = sys.argv[-1]
    min_length = 1
    entries = []

    tree = etree.parse(filename)
    root = tree.getroot()
    packages = root.find('packages')

    for package in packages.getchildren():
        classes = package.find('classes')
        for klass in classes.getchildren():
            lines = klass.find('lines')

            for line in lines.getchildren():
                if line.attrib['hits'] == '0':
                    entries.append(Entry(
                        filename=klass.attrib['filename'],
                        line=line.attrib['number'],
                        length=1
                    ))

    choice = random.choice(entries)
    print(f'Write a test covering line {choice.line} in file "{choice.filename}"!')
