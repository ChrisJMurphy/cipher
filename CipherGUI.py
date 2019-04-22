# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:04:02 2019

@author: Chris
"""
#Needed for GUI creation
from graphics import *
#Allows for file browser to open to allow for writing and reading outside of the file the pycache is currently looking at
from tkinter.filedialog import askopenfilename
#Needed for basic ecryption with polybius squares math.sqrt()
import math
#Needed for progress bars and crashing failsafe
import time

#Primary function to draw the program and run the underlying functions for enc/decryption
def CipherGUI():
    #Draw Window and set dimensions, background -> Black
    win = GraphWin('Bifid Cipher Tool', 400, 300)
    win.setCoords(0, 0, 4, 3)
    win.setBackground('black')
    #Draw Decryptor Button
    DEbutton = Rectangle(Point(0.5, 0.5), Point(1, 0.75))
    DEbutton.setOutline('lime')
    DEtxt = Text(Point(0.75, 0.625), 'Decrypt')
    DEtxt.setSize(10)
    DEtxt.setFill('lime')
    DEtxt.draw(win)
    DEbutton.draw(win)
    #Draw Encryptor Button
    ENbutton = DEbutton.clone()
    ENbutton.move(0, 0.5)
    ENtxt = DEtxt.clone()
    ENtxt.setText('Encrypt')
    ENtxt.move(0, 0.5)
    ENtxt.draw(win)
    ENbutton.draw(win)
    #Draw 'Title': Instructions on General Usage
    intro = Text(Point(2, 2.5), 'First: File to be Encrypted/Decrypted,')
    intro.setFill('lime')
    intro.draw(win)
    intro2 = intro.clone()
    intro2.move(0, -0.2)
    intro2.setText('Second: File to be Written to.')
    intro2.draw(win)
    intro3 = intro.clone()
    intro3.move(0, 0.2)
    intro3.setText('Press: Select Files')
    intro3.draw(win)
    #Output File Section: Originally 'Key' section
        #File to be written TO
    keytxt = ENtxt.clone()
    keytxt.move(0, 0.65)
    keytxt.setText('Output:')
    keytxt.draw(win)
    RNDbutton = Rectangle(Point(1.6, 1.4), Point(2.4, 1.6))
    RNDbutton.setOutline('lime')
    RNDbutton.draw(win)
    RNDtxt = keytxt.clone()
    RNDtxt.setText('Select Files')
    RNDtxt.move(1.25, -0.275)
    RNDtxt.draw(win)
    #Entry Line for File
        #File to be read FROM
    filetxt = keytxt.clone()
    filetxt.move(0, 0.25)
    filetxt.setText('File:')
    filetxt.draw(win)
    fileentry = Entry(Point(2, 2.07), 22)
    fileentry.draw(win)
        #Output File Line
            #Drawn on its own to prevent text display issues involved with the move() function
    outputentry = Entry(Point(2, 1.77), 22)
    outputentry.draw(win)
    #Status Message
        # Later modified during processing to display 'Processing' and 'Done!'
    message = Text(Point(3.5, 0.625), 'Ready')
    message.draw(win)
    message.setFill('lime')
    message2 = message.clone()
    message2.move(0, 0.5)
    message2.draw(win)
    #Exit Button
        #Dimensions for checkMouse() should be X >= 3.6 and Y >= 2.6
    exitbutton = Rectangle(Point(3.6, 2.7), Point(4, 3))
    exitbutton.setOutline('lime')
    exitbutton.draw(win)
    exittext = Text(Point(3.8, 2.85), 'Exit')
    exittext.setFill('lime')
    exittext.draw(win)
    #Encryptor and Decryptor 'Progress' Bars
        #Simple time functions during processing to 'fake' progress bars with the setFill() function
        #Potential function for this section had issues differentiating
    progress1 = ENbutton.clone()
    progress1.setWidth(0)
    progress1.move(0.75, 0)
    progress1.draw(win)
    progress2 = progress1.clone()
    progress2.move(0.2, 0)
    progress2.draw(win)
    progress3 = progress2.clone()
    progress3.move(0.2, 0)
    progress3.draw(win)
    progress4 = progress3.clone()
    progress4.move(0.2, 0)
    progress4.draw(win)
    progress5 = progress4.clone()
    progress5.move(0.2, 0)
    progress5.draw(win)
    progress6 = progress5.clone()
    progress6.move(0.2, 0)
    progress6.draw(win)
    progress7 = progress6.clone()
    progress7.move(0.2, 0)
    progress7.draw(win)
    #Progress Bar for Decryptor
    progress1d = progress1.clone()
    progress1d.move(0, -0.5)
    progress1d.draw(win)
    progress2d = progress1d.clone()
    progress2d.move(0.2, 0)
    progress2d.draw(win)
    progress3d = progress2d.clone()
    progress3d.move(0.2, 0)
    progress3d.draw(win)
    progress4d = progress3d.clone()
    progress4d.move(0.2, 0)
    progress4d.draw(win)
    progress5d = progress4d.clone()
    progress5d.move(0.2, 0)
    progress5d.draw(win)
    progress6d = progress5d.clone()
    progress6d.move(0.2, 0)
    progress6d.draw(win)
    progress7d = progress6d.clone()
    progress7d.move(0.2, 0)
    progress7d.draw(win)
    progressbar1 = Rectangle(Point(1.25, 1), Point(2.95, 1.25))
    progressbar1.setOutline('lime')
    progressbar1.draw(win)
    progressbar2 = progressbar1.clone()
    progressbar2.move(0, -0.5)
    progressbar2.draw(win)
    #Get Mouse for buttons: checkMouse() used instead to allow continuous clicking by user
        #while function used to prevent program from jumping outside if statements and crashing
            #temp -> temporary
    temp = 1
    while temp == 1:
        #Forces screen update to prevent freezing and as a failsafe for the sleep() function
        update(30) 
        mouseclick = win.checkMouse()
        #Checks for user key 'Escape' to the exit the program, in case checkMouse() for the exit button fails
        keypress = win.checkKey()
        if temp == 1:
            if mouseclick: #Program fails to find mouseclick/intiate if structure without this line
                #Decryption Button
                if mouseclick.getX() >= 0.5:
                    if mouseclick.getX() <= 1:
                        if mouseclick.getY() >= 0.5:
                            if mouseclick.getY() <= 0.75:
                                #'Fake' progress bar and processing section
                                message.setText('Processing')
                                #Initiates progress bar before running the writing function to show the program has started
                                time.sleep(1)
                                progress1d.setFill('lime')
                                decwrite(fileentry.getText(), outputentry.getText(), keysq)
                                time.sleep(1)
                                progress1d.setFill('lime')
                                time.sleep(1)
                                progress2d.setFill('lime')
                                time.sleep(1)
                                progress3d.setFill('lime')
                                time.sleep(1)
                                progress4d.setFill('lime')
                                time.sleep(1)
                                progress5d.setFill('lime')
                                time.sleep(1)
                                progress6d.setFill('lime')
                                time.sleep(1)
                                progress7d.setFill('lime')
                                message.setText('Done!')
                #Encryption Button
                if mouseclick.getX() >= 0.5:
                    if mouseclick.getX() <= 1:
                        if mouseclick.getY() >= 1:
                            if mouseclick.getY() <= 1.25:
                                message2.setText('Processing')
                                time.sleep(1)
                                progress1.setFill('lime')
                                encwrite(fileentry.getText(), outputentry.getText(), keysq)
                                time.sleep(1)
                                progress1.setFill('lime')
                                time.sleep(1)
                                progress2.setFill('lime')
                                time.sleep(1)
                                progress3.setFill('lime')
                                time.sleep(1)
                                progress4.setFill('lime')
                                time.sleep(1)
                                progress5.setFill('lime')
                                time.sleep(1)
                                progress6.setFill('lime')
                                time.sleep(1)
                                progress7.setFill('lime')
                                message2.setText('Done!')
                #File Selector Button
                    #Runs both file selections 1 after the other, intro text explains this
                    #Separating this may improve clarity but may needlessly complicate code
                if mouseclick.getX() >= 1.6:
                    if mouseclick.getX() <= 2.4:
                        if mouseclick.getY() >= 1.4:
                            if mouseclick.getY() <= 1.6:
                                file1 = askopenfilename()
                                fileentry.setText(file1)
                                file2 = askopenfilename()
                                outputentry.setText(file2)
                #Exit Button
                    #Fails on occassion following decryption/encryption, non-reproducible and random
                if mouseclick.getX() >= 3.6:
                    if mouseclick.getX() <= 4:
                        if mouseclick.getY() >= 2.6:
                            if mouseclick.getY() <= 3:
                                win.close()
        #Exit failsafe
        if keypress == 'Escape':
            win.close()

#Default filename for debugging and testing purposes
filename = 'sample.txt.'
#Default writing filename for debuging and testing purposes
outfilename = 'outsample.txt'
#Default 8x8 polybius square
    #Difficult to enter as a user so functionality is removed from main program
    #Can be changed in code, adding a keysq selector may be useful?
    #New or modified versions simply shuffle where the intended digits are in the square ->variety
keysq =   ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
           'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
           'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', '1', '2', '3', '4', '5', '6',
           '7', '8', '9', '0', ',', '.', "'", ' ']

#Encryption function to read the square, does not include bifid shifting
def encrypt(filename, keysq):
    #Sets to 8, allows for other keysq usage in the future of any dimensions
    keysqdim = int(math.sqrt(len(keysq)))
    #Opens the file to be read from
    infile = open(filename, "r")
    encbody = []
    #readline() to prevent the file from being interpreted as 1 member of a list
    for body in infile.readline():
        for i in range(len(body)):
            index = keysq.index(body[i])
            #Gets X coordinate from keysq // to ensure integer
            x = index // keysqdim + 1
            #Gets Y coordinate from keysq % to make it the opposite of the X coordinate for that value
            y = (index % keysqdim) + 1
            #Recombines the coordinates
            encbody.append(str(x) + str(y))
    return encbody

#Decryption function to translate encrypt() outputs backwards
def decrypt(filename, keysq):
    infile = open(filename, "r")
    keysqdim = int(math.sqrt(len(keysq)))
    decbody = []
    for encbody in infile.readlines():
        #Halves value read from the encrypted text
        for i in range(int(len(encbody)/2)):
            #Multiplies the taken values to add back to their original, keysqdim needed
            index = (int(encbody[(i * 2)]) - 1) * keysqdim + (int(encbody[i * 2 + 1]) - 1)
            decbody.append(keysq[index])
    #Returns the text to its original readable form
    result = ''.join(decbody)
    return result

#Takes encrypt() output for the target file and splits the numbers into rows
    #ie: 23 becomes V
        #rows = ['2']
        #cols = ['3']
    #Shifts numbers by 2 spaces and reshuffles
    #Sequence is then decrypted into letters and symbols
def encbifid(filename, keysq):
    #Initiate empty row list
    rows = []
    #Initiate empty column list
    cols = []
    encbody = encrypt(filename, keysq)
    #Separates the encrypted text at every other number
    for i in range(len(encbody)):
        coordinate = encbody[i]
        rows.append(coordinate[0])
        cols.append(coordinate[1])
    #Stacks separated into one string
        #ie: 234567-> 246357
    biencbody = rows + cols
    #Initiate empty pairing list for reseparating into polybius coordinates
    pair = []
    #Reseparates into 2-digit coordinates for decryption
    for i in range(len(rows)):
        pair.append(''.join(biencbody[(i * 2):(i * 2 + 2)]))
    biencbody = pair
    #Redefines keysq dimension as 8, allows for later addition of more keysquares without having this as a set number
    keysqdim = int(math.sqrt(len(keysq)))
    #Modified form of the decryption function due to the intended file already having been read from
    decbody = []
    for encbody in biencbody:
        for i in range(int(len(encbody)/2)):
            index = (int(encbody[(i * 2)]) - 1) * keysqdim + (int(encbody[i * 2 + 1]) - 1)
            decbody.append(keysq[index])
    result = ''.join(decbody)
    return result

def decbifid(filename, keysq):
    #Re-encrypts the text so it can be unshuffled
    biencbody = encrypt(filename, keysq)
    #Converts the list into a single string
    presep = ''.join(biencbody)
    #Retrieves row values (First half)
    rows = list(presep[:len(presep)//2])
    #Retrieves column values (Second half)
    cols = list(presep[len(presep)//2:len(presep)])
    #Initiates empty string for recombination
    postsep = ''
    #Combines the rows and columns at every other number to unshuffle
    for i in range(len(rows)):
        postsep = postsep + (rows[i] + cols[i])
    keysqdim = int(math.sqrt(len(keysq)))
    decbody = []
    #Converts string into a list of the individual numbers to be decrypted
    postsep = [postsep[i:i + 2] for i in range(0, len(postsep), 2)]
    #Modified form of the decryption function
    for encbody in postsep:
        for i in range(int(len(encbody)/2)):
            index = (int(encbody[(i * 2)]) - 1) * keysqdim + (int(encbody[i * 2 + 1]) - 1)
            decbody.append(keysq[index])
    result = ''.join(decbody)
    return result

#Runs the encryption functions and prints the result to 'outfilename': already extant file
    #'w+' instead of 'a' would allow file creation but would not allow for specifying a file to write to
        #Would limit capabilities to very basic text files
def encwrite(filename, outfilename, keysq):
    result = encbifid(filename, keysq)
    target = open(outfilename, 'a')
    target.write(result)
    target.close()

#Runs the decryption functions and prints the result to 'outfilename': already extant file
    #Changing 'a' to 'w+' may allow the program to create a new file but this may interfere with processing
def decwrite(filename, outfilename, keysq):
    result = decbifid(filename, keysq)
    target = open(outfilename, 'a')
    target.write(result)
    target.close()

#Run the GUI function which contains all of the above functions when pressing buttons
CipherGUI()