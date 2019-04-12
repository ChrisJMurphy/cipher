# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:04:02 2019

@author: Chris
"""
from graphics import *

def CipherGUI():
    win = GraphWin('Cipher Tool', 400, 300)
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
    #Draw 'Title'
    intro = Text(Point(2, 2.5), 'Enter Key or, if no key, hit randomize.')
    intro.setFill('lime')
    intro.draw(win)
    #Key Section
    keytxt = ENtxt.clone()
    keytxt.move(0, 0.65)
    keytxt.setText('Key:')
    keytxt.draw(win)
    RNDbutton = Rectangle(Point(1.6, 1.4), Point(2.4, 1.6))
    RNDbutton.setOutline('lime')
    RNDbutton.draw(win)
    RNDtxt = keytxt.clone()
    RNDtxt.setText('Randomize')
    RNDtxt.move(1.25, -0.275)
    RNDtxt.draw(win)
    #Entry Line for Key
        #Needs to be randomizer enabled
    #Encryptor and Decryptor 'Progress' Bars
    #File Path Locator for filename
    #Prevent Freezing
    win.getMouse()
    win.close()
CipherGUI()