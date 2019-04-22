# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 18:48:14 2019

@author: Chris
"""
import math
#Master Def for Encryptor
filename = 'sample.txt.'
outfilename = 'outsample.txt'
keysq =   ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
           'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
           'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', '1', '2', '3', '4', '5', '6',
           '7', '8', '9', '0', ',', '.', "'", ' ']

def encrypt(filename, keysq):
    keysqdim = int(math.sqrt(len(keysq)))
    infile = open(filename, "r")
    encbody = []
    for body in infile.readline():
        for i in range(len(body)):
            index = keysq.index(body[i])
            x = index // keysqdim + 1
            y = (index % keysqdim) + 1
            encbody.append(str(x) + str(y))
    return encbody

def decrypt(filename, keysq):
    infile = open(filename, "r")
    keysqdim = int(math.sqrt(len(keysq)))
    decbody = []
    for encbody in infile.readlines():
        for i in range(int(len(encbody)/2)):
            index = (int(encbody[(i * 2)]) - 1) * keysqdim + (int(encbody[i * 2 + 1]) - 1)
            decbody.append(keysq[index])
    result = ''.join(decbody)
    return result

def encbifid(filename, keysq):
    rows = []
    cols = []
    encbody = encrypt(filename, keysq)
    for i in range(len(encbody)):
        coordinate = encbody[i]
        rows.append(coordinate[0])
        cols.append(coordinate[1])
    biencbody = rows + cols
    pair = []
    for i in range(len(rows)):
        pair.append(''.join(biencbody[(i * 2):(i * 2 + 2)]))
    biencbody = pair
    keysqdim = int(math.sqrt(len(keysq)))
    decbody = []
    for encbody in biencbody:
        for i in range(int(len(encbody)/2)):
            index = (int(encbody[(i * 2)]) - 1) * keysqdim + (int(encbody[i * 2 + 1]) - 1)
            decbody.append(keysq[index])
    result = ''.join(decbody)
    return result

def decbifid(filename, keysq):
    biencbody = encrypt(filename, keysq)
    presep = ''.join(biencbody)
    rows = list(presep[:len(presep)//2])
    cols = list(presep[len(presep)//2:len(presep)])
    postsep = ''
    for i in range(len(rows)):
        postsep = postsep + (rows[i] + cols[i])
    keysqdim = int(math.sqrt(len(keysq)))
    decbody = []
    postsep = [postsep[i:i + 2] for i in range(0, len(postsep), 2)]
    for encbody in postsep:
        for i in range(int(len(encbody)/2)):
            index = (int(encbody[(i * 2)]) - 1) * keysqdim + (int(encbody[i * 2 + 1]) - 1)
            decbody.append(keysq[index])
    result = ''.join(decbody)
    return result

def encwrite(filename, outfilename, keysq):
    result = encbifid(filename, keysq)
    target = open(outfilename, 'a')
    target.write(result)
    target.close()

def decwrite(filename, outfilename, keysq):
    result = decbifid(filename, keysq)
    target = open(outfilename, 'a')
    target.write(result)
    target.close()