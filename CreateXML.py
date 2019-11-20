'''
Created on 20-Nov-2019

@author: clementjohnshaji
'''
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET

# Sample data creation
root=Element('Data')
tree=ElementTree(root)



#print ET.tostring(root)
tree.write(open(r'/Users/clementjohnshaji/Desktop/Projects/Python/Hiwijob/Data.XML','w'))

def writemsg():
    tree = ET.parse('Data.xml')
    root = tree.getroot()
    #Not creating any attributes as it is not mentioned in the task
    attrib = {}
    #Creating an element and attaching to root
    element = root.makeelement('Message', attrib)
    root.append(element)
    #Adding text message to the element created
    element.text = raw_input("Enter your message")
    # Writing to the same file
    tree.write(open('Data.xml','w'))
    # Can use tree.write(open('Newfile.xml','w')) if wanted to write to new file
    
def Readmsg():
    try:
        tree = ET.parse('Data.xml')
        root = tree.getroot()
        #Checking the length of Xml file
        No=len(root)
        if No==0:
            print ("Empty file")
        else:
            for elem in root:
                if elem is None:
                    print("No messages")
                else:
                    print(elem.text)
    except ET.ParseError:
        # log error
        pass
           
def deletemsg():    
    #Getting user inputed msg to delete.
    msgdlt=raw_input("Enter the message you want to delete")
    
    tree = ET.parse('Data.xml')
    root = tree.getroot()
    find=False
    # If wanted to filter with the attribultes, use for child in root. 
    for message in root.iter("Message"):
        if message.text==msgdlt:
            find=True
            print(message.text)
            ch=raw_input("Enter yes to delete")
            if ch=='yes':
                root.remove(message)
                tree.write(open('Data.xml','w'))
                Readmsg()
            else:
                print("Wrong input,Try again")
    if find==False:
        print("Message didn't found. Try again")
    
def findmsg():
    userfilter=raw_input("Enter the message you want to check")
    tree = ET.parse('Data.xml')
    root = tree.getroot()
    find=False
    for message in root.iter("Message"):
        # if we want to check with the attributes use message.attrib to get the attributes.
        if message.text==userfilter:
            find=True
            print(message.text+ " found")
    if find==False:
        print("Message didn't found")


Choice= 1

while Choice !=4:
    Choice = raw_input("Hello, Enter 0-for Add Message, 1-for Delete message, 2-for Read the messages, 3-for Find a Message, & 4-To exit ")
    try:
        choiceno=int(Choice)
        if choiceno ==0:
            writemsg()
           
        elif choiceno== 1:
            Readmsg()
            deletemsg()
        elif choiceno==2:
            Readmsg()
            
        elif choiceno == 3:
            Readmsg()
            findmsg()
        elif choiceno== 4:
            break
        else:
            print "Enter a valid number"
    except ValueError:
        print("Enter a valid number")