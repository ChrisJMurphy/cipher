# cipher
Bifid Cipher Project

Cipher does not process J, j, newline, or any other characters not included in keysquares
	Traditionally, Bifid ciphers put I and J together to complicate solving further, but also to allow for a 5x5 square from 25 letters

New keysquares can be made in the source code, at the moment only squares 8x8 in dimension and smaller work properly
	New keysquares must be added to the if structure on lines 192 and 223 to convert the string input into the keysquare in the code
		ie: 'keysq1' becomes the keysq1 polybius square in the code structure
		These must be defined before CipherGUI() at the end of the code

'\n' addition to a keysquare will cause program to cease encryption or decryption after the first '\n'

encbifid() and decbifid() recieve filename, outfilename, and keysq from the respective Entry boxes in CipherGUI()
	Initiating an encryption or decryption without these values filled will result in an error


