'''
Created on Feb 23, 2013

@author: Joseph
'''
import time

#this is the class for how the data is going to come in
#it has a file location and a file size
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

#this is the queue that just does push and pop
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


#this is the class that will do loadgen
class loadGen:

#     the host name for the VM in EC2
#    ec2-54-234-233-105.compute-1.amazonaws.com
#    ec2-54-242-76-139.compute-1.amazonaws.com
#    ec2-54-234-222-169.compute-1.amazonaws.com
#    ec2-23-20-3-241.compute-1.amazonaws.com  
    
	
# Set path and filename for the input file
#this is where all the input file test cases will be
    inputFile1 = r"C:\Users\Joseph\Desktop\test.txt"
    inputFile2 = r"C:\Users\Joseph\Desktop\test.txt"
    inputFile3 = r"C:\Users\Joseph\Desktop\test.txt"
    inputFile4 = r"C:\Users\Joseph\Desktop\test.txt"
    inputFile5 = r"C:\Users\Joseph\Desktop\test.txt"
    
#this is all the global variables that go thourghout the function    
    global parsedData #this is the list of the data
    parsedData = []
    global listOfServers #this is the list of the servers
    listOfServers = []
    global data
    global time     #this is the current time
    global size     #this is the size of the file coming in
    global totalMb  #this is the total size of the queue
    global key = 'uci_key.pem'
    global userName = 'ubuntu'    
	global input = 'testCase1' #this is the input that the parser is going to set up
    
   
    #this intiailizes all the variables
    def __init__(self):
            self.parsedData = []
            self.listOfServers = []
            self.totalMb = 0
            self.size = 0
            
            
    #this will be the function that sets up all the parsed values for load gen
    #and the QLB
    def parse(self, input):
            self.input = input 
        
#input files are of the format (time to send file, size of file)			
#this is where the test cases are decided
    if input == 'testCase1':
        inputFile = inputFile1
    elif input == 'testCase2':
        inputFile = inputFile2
    elif input == 'testCase3':
        inputFile = inputFile3
    elif input == 'testCase4':
        inputFile = inputFile4
    elif input == 'testCase5':
        inputFile = inputFile5  
  
    
	#the delimitter for the file
    delimitter = "," 
	

    
	#this opens the specified input file and ignores the comments and puts it all in parsed data
    with open(inputFile) as f:
        for line in f:
            li=line.strip()
            if not li.startswith('#'):
                line.rstrip()
                line = line.split(delimitter) # split based on the delimiter decided 
                line=[int(i) for i in line]
                parsedData.append(line)
    
	#this sets up the data to have the information input and the list that will store all the data
    data = Data()
    listOfData = Queue()
    numInArray = 0
	
    for i in parsedData:
      
        timeToSend = parsedData[numInArray]
        f = open('newfile',"wb")		#this is for the file creation

        numOfMb = timeToSend.pop() 		#this pops the second value which should be the size in the data file
        dataToSend = numOfMb * 1048576  #this is the number of mb times number of bytes to make the file

        size = dataToSend				#this is the size that the file will be
        data.setDataSize(dataToSend)	#this sets the data's size
	
        data.setFile('newfile')			#this should be the file location
        
        totalMb+= numOfMb       		#this adds to the total MB in the queue
        listOfData.push(data)       	#this is the queue
        
        timeSend = timeToSend.pop()		#pops the value that should have time that the file should go out
    
        if time != timeSend:
            time = timeSend     		#this is where you would wait or iterate the time
        
        f.seek(dataToSend-1)			#this until the os.stat is for the file craetion
        f.write("\0")
        f.close()
        import os
        os.stat("newfile").st_size
        
        ssh_connect('test',username,key, port =23)		#this is the ssh connections to connect and send
        
    
        numInArray+=1       # iterate the array after everything is done

#connect to remote ec2 server		
        def ssh_connect(host, username, private_key, port=22):
            #Helper function to initiate an ssh connection to a host."""
            transport = paramiko.Transport((host, port))
            
            if os.path.exists(private_key):
                rsa_key = paramiko.RSAKey.from_private_key_file(private_key)
                transport.connect(username=username, pkey=rsa_key)
            else:
                raise TypeError("Incorrect private key path")
            
            return transport
        
        def sftp_connect(transport):
            """Helper function to create an SFTP connection from an SSH
            connection.
        
            Once a connection is established, a user can use
            conn.get(remotepath) or conn.put(localpath, remotepath) to
            transfer files.
            """
            return transport.open_sftp()
        
        def exec_cmd(transport, command):
            """Executes a command on the same server as the provided
            transport
            """
            channel = transport.open_session()
            channel.exec_command(command)
            output = channel.makefile('rb', -1).readlines()
            return output        
        
if __name__ == '__main__':
    loadGen = loadGen()   
    loadGen.parse('testCase1')
    print 'hey'
    

        
