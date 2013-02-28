'''
Created on Feb 23, 2013

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

class Queue:
    
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    def push(self, obj):
        self.in_stack.append(obj)
    def pop(self):
        if not self.out_stack:
            self.in_stack.reverse()
            self.out_stack = self.in_stack
            self.in_stack = []
        return self.out_stack.pop()


class loadGen:
#     the host name for the VM in EC2
#    ec2-54-234-233-105.compute-1.amazonaws.com
#    ec2-54-242-76-139.compute-1.amazonaws.com
#    ec2-54-234-222-169.compute-1.amazonaws.com
#    ec2-23-20-3-241.compute-1.amazonaws.com  
    
# Set path and filename for the input file
    inputFile1 = r"C:\Users\Joseph\Desktop\test.txt"
    inputFile2 = r"C:\Users\Joseph\Desktop\test.txt"
    inputFile3 = r"C:\Users\Joseph\Desktop\test.txt"
    inputFile4 = r"C:\Users\Joseph\Desktop\test.txt"
    inputFile5 = r"C:\Users\Joseph\Desktop\test.txt"
    
    input = 'testCase1'
    
# Set path and filename for the parsed output file
    outputFile = r"C:\Users\Joseph\Desktop\outputFile.txt"     

#this is all the global variables that go thourghout the function    
    global parsedData 
    parsedData = []
    global data
    global time     #this is the current time
    global size     #this is the size of the file coming in
    global totalMb  #this is the total size of the queue
    
    def parse(self, input):
        self.input = input
        
#this is where the test cases are decided
    if input == 'testCase1':
        text = open(inputFile1).read()
    elif input == 'testCase2':
        text = open(inputFile2).read()
    elif input == 'testCase3':
        text = open(inputFile3).read()
    elif input == 'testCase4':
        text = open(inputFile4).read()
    elif input == 'testCase5':
        text = open(inputFile5).read()
        
# intialize the global variables        
    totalMb = 0 
    time = 0
    
    delimitter = ","
    
    
    data = Data()
    listOfData = Queue()
    
    with open(inputFile1) as f:
        for line in f:
            li=line.strip()
            if not li.startswith('#'):
                line.rstrip()
                line = line.split(delimitter) # split based on the delimiter decided 
                line=[int(i) for i in line]
                parsedData.append(line)
    
    numInArray = 0
    for i in parsedData:
      
        print numInArray
        timeToSend = parsedData[numInArray]
        f = open('newfile',"wb")

        numOfMb = timeToSend.pop()
        dataToSend = numOfMb * 1048576 # this is the number of mb times number of bytes to make the file

        size = dataToSend
        data.setDataSize(dataToSend)

        data.setFile('newfile')
        
        totalMb+= numOfMb        #this adds to the total MB in the queue
        listOfData.push(data)       #this is the queue
        
        timeSend = timeToSend.pop()
    
        if time != timeSend:
            time = timeSend     #this is where you would wait or iterate the time
        
        f.seek(dataToSend-1)
        f.write("\0")
        f.close()
        import os
        os.stat("newfile").st_size
    
        numInArray+=1       # iterate the array after everything is done
        
if __name__ == '__main__':
    loadGen = loadGen()   
    print 'hey'
    

        
