'''
Created on Feb 26, 2013

@author: Joseph
'''
class Data:
    def __init__(self):
        dataSize = 0
        file = ''
    def setDataSize(self, size):
        self.dataSize = size
    def setFile(self, fileLoc):
        self.file = fileLoc
    def getSize(self):
        return self.dataSize
    def getFile(self):
        return self.file

