'''
Created on Aug 8, 2014

@author: abhiagar90
'''

import decoder
from utilFunc import resetInstrFlag, printAllRegs, printAllFlags
import utilFunc

            
def main():
    print "---Started---"
    #"52800102"
    hexes = ['d2800041', '94000002', 'd2800040', '52800063', 'd65f03c0']
    for hexcode in hexes:
        print 'inst: '+utilFunc.hexToBin(hexcode)
        resetInstrFlag()
        #utilFunc.set_Z_flag()
        decoder.decodeInstr(hexcode)
    printAllRegs()
    printAllFlags()
        
main()