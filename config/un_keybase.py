#!/usr/bin/env python
'''
Predator Pain
'''

__description__ = 'Keybase Config Extractor'
__author__ = 'Code based on Kevin Breen un...something - Th4nat0s'
__version__ = '0.2'
__date__ = '2017/12/05'


# Standard Imports Go Here
import os
import sys
import base64
import string
from struct import unpack
from optparse import OptionParser


#Non Standard Imports
try:
    import pype32
except ImportError:
    print "[+] Couldn't Import pype32 'https://g...content-available-to-author-only...b.com/crackinglandia/pype32'"

# Main Decode Function Goes Here
'''
data is a read of the file
Must return a python config_dict of values
'''
def run(data):
        config_dict = {}
        pe = pype32.PE(data=data)
        print "  [-] Collecting Strings"
        string_list = get_strings(pe, 2)
        for string in string_list:
            if string.startswith('http'):
                config_dict['URI'] = string
        for string in string_list:
            if "." in string:
                if ("#" in string) or ("$" in string):
                    string = (string.replace("#",""))
                    string = string.replace("$","")
                    if ("?" in string):
                        config_dict['PATH'] = string.split('?')[0]
        return config_dict

        
#Helper Functions Go Here

def string_clean(line):
    return ''.join((char for char in line if 32< ord(char) < 127))
    
# Get a list of strings from a section
def get_strings(pe, dir_type):
    counter = 0
    string_list = []
    m = pe.ntHeaders.optionalHeader.dataDirectory[14].info
    for s in m.netMetaDataStreams[dir_type].info:
        for offset, value in s.iteritems():
            string_list.append(value)
        counter += 1
    return string_list


# Main
if __name__ == "__main__":
    parser = OptionParser(usage='usage: %prog inFile outConfig\n' + __description__, version='%prog ' + __version__)
    (options, args) = parser.parse_args()
    # If we dont have args quit with help page
    if len(args) > 0:
        pass
    else:
        parser.print_help()
        sys.exit()

    try:
        print "[+] Reading file"
        fileData = open(args[0], 'rb').read()
    except:
        print "[+] Couldn't Open File {0}".format(args[0])
    #Run the config extraction
    print "[+] Searching for Config"
    config = run(fileData)
    #If we have a config figure out where to dump it out.
    if not config:
        print "[!] Config not found"
        sys.exit()
    #if you gave me two args im going to assume the 2nd arg is where you want to save the file
    if len(args) == 2:
        print "[+] Writing Config to file {0}".format(args[1])
        with open(args[1], 'a') as outFile:
            for key, value in sorted(config.iteritems()):
                clean_value = string_clean(value)
                outFile.write("Key: {0}\t Value: {1}\n".format(key,clean_value))
    # if no seconds arg then assume you want it printing to screen
    else:
        print "[+] Printing Config to screen"
        for key, value in sorted(config.iteritems()):
            clean_value = string_clean(value)
            print "   [-] Key: {0}\t Value: {1}".format(key,clean_value)
        print "[+] End of Config"
