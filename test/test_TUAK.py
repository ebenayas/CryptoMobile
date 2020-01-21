# −*− coding: UTF−8 −*−
#/**
# * Software Name : CryptoMobile 
# * Version : 0.3
# *
# * Copyright 2018. Benoit Michau. P1Sec.
# *
# * This program is free software: you can redistribute it and/or modify
# * it under the terms of the GNU General Public License version 2 as published
# * by the Free Software Foundation. 
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# * GNU General Public License for more details. 
# *
# * You will find a copy of the terms and conditions of the GNU General Public
# * License version 2 in the "license.txt" file or
# * see http://www.gnu.org/licenses/ or write to the Free Software Foundation,
# * Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
# *
# *--------------------------------------------------------
# * File Name : test/test_TUAK.py
# * Created : 2018-12-20
# * Authors : Benoit Michau 
# *--------------------------------------------------------
#*/

########################################################
# CryptoMobile python toolkit
#
# TUAK authentication algorithm
# as proposed by 3GPP as an alternative to Milenage
# algorithm based on SHA-3 (more exactly its KeccakP-1600 permutation)
# see 3GPP TS 35.231, 232 and 233
#######################################################

from time import time

from CryptoMobile.TUAK import TUAK, make_TOPc, keccakp1600

TUAK.KeccakIterations = 1


###
# Keccak: testsets from 3GPP TS 35.232 Rel.15
###

def keccak_testset_1():
    return keccakp1600(b'$v\xd2\xda\xc5\x9e.\x93I\xdf2U\xa9\xda\xb1\xb6\x9e\xb5\xc2\x08\xf1Q\xc70\x9e\x8c\x8f\x17\xdbEm\x0b^\xb0\xaf\xb6\xc7>7\xce\x8c\xcc\xcf \xb7\x9d\x8ag)AI\x17H\t\xe4)p\x930\xc4\xad#\x1d>R\x11\xae\x0b\xd8\x05 \xc4:\xd4\xb46bW\x92\xa7lR\x08\x9d\x0fs\x92q\x15\x1a7YM\xf6m\xe4B\x9f<\x97\n4V\xb6\xce,x\xcd\x11(q\x7fK\xdbs\x1aL\x97\xdb\xe5\xebsS\xfe\x81\xe3|3\xac`\xb8!"\xea\xc6\x11\xa9\x8e\x0etB\xb9\x99du"\x93\xe4\xf9\xc6\x96\xba\x05\xf0z!E\x1f\x90s\x0c\x96x\xc6E\xadK\xe4LM-\x98\x1a4\x12\x08\x1c\x9ck\x05\xc9\x93\xff\x1cV\x1a\r$+G\x06\xd5\x01\xc3Ge\xb3z\x0bP') == \
    b'/\xdcX\xd4\xd9J\x88L\x1c\xb0:\x8ec\xac\xab\x83u\xe8V\xb5a\xba:\x06%\xe80\xac\xdbUsB\x86do\x87\x18\x9bCT%\xb5\xd6eN"\x82(\xb6\x97\xb8\x1c\xbe\xade[q\xaa\xcc\xc2^=~Q\xb5\xcbZ\xc2\'\xf6\x7f*\xd8\xa0b\x97g\x82\xb0\x8a~\xc3\xf1\xb58\xd6\x00\x8c\x0b\xab\xef\x83\xdad6kb\xa5?\x88\xa3\xdc\x06)\xbd\xedy_2 \xf3\xc6\\v\xbd\xd0\x12C\xe8\x8fc\xd6\x91._\xb5\xcd\xa1g\xb7\x1f\x9b\xaa\xa7B\xdc\x19?\xf7\x8c\x17g\xa3\x8a\x1c\x96@\x8c\xce\x16\x929\xb0w\xf2\x90:\x07\xb8\xc4j\x04\x8df1\x8eY^\xa4\xbb\x92\x99,|-=\xcd8\x19u\xb6\xe0_\x85\xba\x18\x15 \x96\xcc0\xed"\x14\x0f\xf3\xb6q\x1e\xa7'

def keccak_testset_2():
    return keccakp1600(b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00') == \
    b'D\xe0\xe5\x8c\xa9h\x97\\L%\x92\xa1W\xf5?!$Q\x9b\x01\x0b\x89\xe1^0\x1e\xf5\x8fvP\x1d\xb5\x9c\xde\x06\x7f\x1f\xde\t\xc0\xa4\xb5\xc2\x10\xa6\xa1\x9f\x06\xbaL\x8f\x0co\xc8h\xf0\xfc\x80\xa6;%Sy\x1eA\xc8"x\xad\x11^\xfcp\xf7\x1dd\x1f\xf0wJ\xa5\xd5G\xb6\xd9\x91I\x14\x02,QLE\xfc\xec\xa6\x1c\xb6k\x0f\x03\x13\xe3I\x88\xae\r6s~,\x05)\x90\x7f\xe6S\xfcN\x18]\x07\xf3\x96\x1f\x82k\xb8\x801\xaf\x84M\x9e}\x98v\x17\x03c\xfd\xe7g\x86\xc5\x8c\xcb\xcf\\:\x01\xbb\x91L\x1b\x02\x08\xa2|{\xe3\xbb\xbb\xbb\x99v\xe0@1z\xfc*\xfb\xfa\xdc{\xa7\xfc#r5\xc6UQ\xaa19d\x1f\xa8\xdb.d\x83\xf2\x87@\xb3\x1ba'

def keccak_testset_3():
    return keccakp1600(b'\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8') == \
    b']\xd0\xe3\xdd\x9eF\xdb!\x87\xa9\xe1\xa4DB}z\x83/\xef)\x919\x90\xe0\x15\xea\x8d\x1f?\x1f\xa6A?\xfb\xbcXoZMiM\xd6\x06h\xfb\xf3\xb4\xbb\xdaIE\xc9\xea\x0c\xbe\xe2\x11s^\xbf\xa89\x9ba:\xff4\xd1\xddG\xfa9\x8cx\xf4\x8a\x91\xa6e})\x03l\x87\xf7s_C\xe2\xab\xb7j\x13PE\xb7\x0eB\xc5\x9d\x80\x92\x14\xa4\xcd0\x1f\x18W0\nU\xd0\x1d26[j\xbd\xa5\x1e\xaduA\xdb{\xed\xdcF\xe4\x85r|;+]\x83\xb5\x9eZzb\xe0\x13\x16\x14\xba\r{\xfa\xcdN\xbaqb2\x80\x88Y\xf0\x03\x85_\\G\x01\nP\xe1&/\x9e\x9e\x81.l\xb3\xddR\xd9\xad\xb7\xbe\x19\x10Bv4\x02R1\x96\x8d\xe0\xb4?\xa2KK>'

def keccak_testset_4():
    return keccakp1600(b'\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab') == \
    b"\x00R\xf0\x0e\xb4\t\xb5\xce_x\xe9S \xeejq_[\x1a\n~[\xed\x03C\xd6\x91\x130\xab\xe2\xfcW\xb6o\xb5\xba\x9e\xf2\x88\x0b\x05u\xed\n\x98p\xc5\x0cfW\x83\x8a\x1d2\xf3\x88\xfd\xc3\xa4\xe72F\xdd\xd9VXtw\xc4\xc8\xd4\x1a\xd4\x19\x14\x04R\xcc\x17\x13#\xae\x1f\xf0\x91\x0c\xe1\xc3'\x8bb\xc6Hu\x91+\x7f|!\xcf\xa0R\xe0\xb0@!L_;\x81\xc3 u\x87\x92\xce\xa0\xc8\xd1\xe4.\x92\xe1\xef<\xf0f\xbe\x16\xc6\x1e\xe4M\xddi\xdbr\x9a\x82]M\xbb\xfd\x9f\x97\xdaF\xc6\x10=Z_\x8c\x8d!\xbdB}X\xafKA\x11x\xbe\xdeZ\x19\x86\xa0\xc9\x1d8\xc4\x85\xee-Tr\xbd\xd0\xa5\xb9\xfa\xab\xf7\x07s\x13\xca\xf9\xf3\n\x1eF\xac\x8e\x12X"

def keccak_testset_5():
    return keccakp1600(b'\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd\xcd') == \
    b'\xc1l\xa0m\xef:\xddE\xb2\x0c\xcf\xd6z\xa8\xf9\x12\x15\xc2\xe8u\x1e\xdd\x02\xa5\x10?a\xbao{\xf3\xbb\xb2Y_A\x1b\xafj\xab\x16S\xf1~\x95\x1e-\xc8\x8d\xfb\xf7hg\x94\nc8`\x82\x18\xf8\xdf\xf1A{\xdb<oE"d\x87\xa9\xa6\x07\x8bej7\xff\x86\x1d\xfay0w\xc0\x88\x03\xa8\xb9b\xdag$\xdd\xc8m\x10\x93\xff\xd0\x05\x88\xa2\x8el\x1b\x80\x1fsTc\xbc\x05X\x1e\xd5\x97\xbd\xbf7\xa4Y)\x7fe\x059\x98\x9e\xfcJz\x9c\x8b"3\xc0 \xde\xa3\x004\xc1\xf2\xc6\xcf^\x0c\xcc\xccSU@\x87\x18\x03\xed= \xb0\xc5\x10\x13\xa3\x02J\xc5k3\xafZ&\x11#=S}\x11\x80N\xf0.\xb5Yx\xff\xd4=\x9a~H\x84Bd\xde\xce\x8f\xa8'

def keccak_testset_6():
    return keccakp1600(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00') == \
    b'V\r\xbeA\xf6\xa7Z}3\xe1]k\xfe\x0b\xdcd}\xe5T4\x1c\xe0\xd0a\xbb\xbd\xf1\xbeuvI\xde\xe7A\xb1\xfd7A\x8d\xa6\xf3Z\xb7\x0e\x15\x87\xcc6\x8c\x1b\x89\xad\xcc\xce\x1d\x07\xad\x92\rM\x9d\x08\xa0C\x94l/o\xe1\xa5\x17\xa2I\xce<\x8a_\x83N\xec\xfa/\xaa\xad\xde\xe82\xe6\xdb$\xd4*+\x04\xa7\x84c\xa9\xb2\xdfm/\x02\xfc\\)s*\x12e\x14\xfb\x15\xebz\xbe\x7f\xbfW\x18\x91f\x91\xc7\xc2\xf8CF\x00\xda~/\x9bve\xa5\x9caA\x11U\x05\xc9\xd9\xe9\xf8\x05\xafo\x9ek\xc4\xf1\x9ce\xc6\x0e\xa9r\xa6\xe4\xfa\x01\x85})\x8a\t&\x83\x90\xd5t\xf6=Ov\xfbmm\xfc\xd178\xc4\x98H\xac\xd5\x1eN\xd7\x83\xaf\xa1\xbaR\x0f\xa37'

def keccak_testsets():
    return keccak_testset_1() & keccak_testset_2() & \
            keccak_testset_3() & keccak_testset_4() & \
            keccak_testset_5() & keccak_testset_6()


def tuak_testset_61():
    K    = b'\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab'
    RAND = b'BBBBBBBBBBBBBBBB'
    SQN  = b'\x11\x11\x11\x11\x11\x11'
    AMF  = b'\xff\xff'
    TOP  = b'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU'
    
    tuak = TUAK(TOP)
    tuak.LEN_MAC = 64
    TOPc = make_TOPc(K, TOP)
    tuak.set_topc(TOPc)
    
    return TOPc == b'\xbd\x04\xd9S\x0e\x87Q<]\x83z\xc2\xad\x95F#\xa8\xe23\x0c\x11S\x05\xa7>\xb4]\x1f@\xcc\xcb\xff' and \
    tuak.f1(K, RAND, SQN, AMF) == b'\xf9\xa5Nj\xea\xa8a\x8d' and \
    tuak.f1star(K, RAND, SQN, AMF) == b'\xe9KM\xc6\xc7)}\xf3'

def tuak_testset_62():
    K    = b'\xff\xfe\xfd\xfc\xfb\xfa\xf9\xf8\xf7\xf6\xf5\xf4\xf3\xf2\xf1\xf0\xef\xee\xed\xec\xeb\xea\xe9\xe8\xe7\xe6\xe5\xe4\xe3\xe2\xe1\xe0'
    RAND = b'\x01#Eg\x89\xab\xcd\xef\x01#Eg\x89\xab\xcd\xef'
    SQN  = b'\x01#Eg\x89\xab'
    AMF  = b'\xab\xcd'
    TOP  = b'\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f'
    
    tuak = TUAK(TOP)
    tuak.LEN_MAC = 128
    TOPc = make_TOPc(K, TOP)
    tuak.set_topc(TOPc)
    
    return TOPc == b'0T%B~\x18\xc5\x03\xc8\xa4\xb2\x94\xear\xc9]\x0c6\xc6\xc6\xb2\x9d\x0ce\xdeYt\xd5\x97\x7f\x85$' and \
    tuak.f1(K, RAND, SQN, AMF) == b'\xc0\xb8\xc2\xd4\x14\x8e\xc7\xaa_\x1dx\xa9~M\x1dX' and \
    tuak.f1star(K, RAND, SQN, AMF) == b'\xef\x81\xafr\x90\xf7\x84,l\xea\xfaS\x7f\xa0t['

def tuak_testset_63():
    K    = b'\xff\xfe\xfd\xfc\xfb\xfa\xf9\xf8\xf7\xf6\xf5\xf4\xf3\xf2\xf1\xf0\xef\xee\xed\xec\xeb\xea\xe9\xe8\xe7\xe6\xe5\xe4\xe3\xe2\xe1\xe0'
    RAND = b'\x01#Eg\x89\xab\xcd\xef\x01#Eg\x89\xab\xcd\xef'
    SQN  = b'\x01#Eg\x89\xab'
    AMF  = b'\xab\xcd'
    TOP  = b'\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f'
    
    tuak = TUAK(TOP)
    tuak.LEN_MAC = 256
    TOPc = make_TOPc(K, TOP)
    tuak.set_topc(TOPc)
    
    return TOPc == b'0T%B~\x18\xc5\x03\xc8\xa4\xb2\x94\xear\xc9]\x0c6\xc6\xc6\xb2\x9d\x0ce\xdeYt\xd5\x97\x7f\x85$' and \
    tuak.f1(K, RAND, SQN, AMF) == b"\xd9{u\xa1w`e'\x1b\x1e!+\xc3\xb1\xbf\x17?C\x8b!\xe6\xc6JU\xa9l7.\x08^\\\xc5" and \
    tuak.f1star(K, RAND, SQN, AMF) == b'B{\xbf\x07\xc6\xe3\xa8lT\xf8\xc5!d\x99\xf3\x90\x9ao\xd4\xa1d\xc9\xfe#[\x15P%\x81\x11\xb8!'

def tuak_testset_64():
    K    = b'\xb8\xda\x83zPe-j\xc7\xc9}\xa1Oj\xcca'
    RAND = b'h\x87\xe5T%\xa9f\xbd\x86\xc9f\x1a_\xa7+\xe8'
    SQN  = b'\r\xea.\xe2\xc5\xaf'
    AMF  = b'\xdf\x1e'
    TOP  = b'\tR\xbe\x13Ul2\xeb\xc5\x81\x95\xd9\xdd\x93\x04\x93\xe1*\x90\x03f\x99\x88\xff\xde_\xa1\xf0\xfe5\xcc\x01'
    
    tuak = TUAK(TOP)
    tuak.LEN_MAC = 128
    TOPc = make_TOPc(K, TOP)
    tuak.set_topc(TOPc)
    
    return TOPc == b"+\xc1n\xb6W\xa6\x8e\x1fDo\x08\xf5|\x0e\xfb\x1dI5'\xa2\xe6R\xce(\x1e\xb6\xca\x0eD\x87v\n" and \
    tuak.f1(K, RAND, SQN, AMF) == b't\x92\x14\x08yX\xdd\x8fX\xbf\xcd\xf8i\xd8\xae?' and \
    tuak.f1star(K, RAND, SQN, AMF) == b'a\x9e\x86Z\xfe\x80\xe3\x82\xae\xe10c\xf9\xdf\xb5m'

def tuak_testset_65():
    K    = b'\x15t\xcaV\x88\x1d\x05\xc1\x89\xc8(\x80\xf7\x89\xc9\xcdBD\x95_D&\xaa+i\xc2\x9f\x15w\x0eZ\xa5'
    RAND = b'\xc5p\xaa\xc6\x8c\xdee\x1f\xb1\xe3\x08\x83"I\x8b\xef'
    SQN  = b'\xc8\x9b\xb7\x1f:A'
    AMF  = b')}'
    TOP  = b'\xe5\x9fn\xb1\x0e\xa4\x06\x81?I\x91\xb0\xb9\xe0/\x18\x1e\xdfL~\x17\xb4\x80\xf6m4\xda5\xee\x88\xc9^'
    
    tuak = TUAK(TOP)
    tuak.LEN_MAC = 64
    TOPc = make_TOPc(K, TOP)
    tuak.set_topc(TOPc)
    
    return TOPc == b'<`R\xe4\x152\xa2\x8aG\xaa<\xbb\x89\xf2#\xe8\xf3\xaa\xa9v\xae\xcdH\xbc>}ae\xa5^\xffb' and \
    tuak.f1(K, RAND, SQN, AMF) == b'\xd74\r\xad\x02\xb4\xcb\x01' and \
    tuak.f1star(K, RAND, SQN, AMF) == b'\xc6\x02\x1e.f\xac\xcb\x15'

def tuak_testset_66():
    TUAK.KeccakIterations = 2
    K    = b'\x15t\xcaV\x88\x1d\x05\xc1\x89\xc8(\x80\xf7\x89\xc9\xcdBD\x95_D&\xaa+i\xc2\x9f\x15w\x0eZ\xa5'
    RAND = b'\xc5p\xaa\xc6\x8c\xdee\x1f\xb1\xe3\x08\x83"I\x8b\xef'
    SQN  = b'\xc8\x9b\xb7\x1f:A'
    AMF  = b')}'
    TOP  = b'\xe5\x9fn\xb1\x0e\xa4\x06\x81?I\x91\xb0\xb9\xe0/\x18\x1e\xdfL~\x17\xb4\x80\xf6m4\xda5\xee\x88\xc9^'
    
    tuak = TUAK(TOP)
    tuak.LEN_MAC = 256
    TOPc = make_TOPc(K, TOP)
    tuak.set_topc(TOPc)
    
    ret = ( TOPc == b'\xb0Jf\xf2lb\xfc\xd6\xc8-\xe2*\x17\x9a\xb6U\x06\xec\xf4\x7fV$\\\xd1I\x96l\xfa\x9c\xeczQ' and \
    tuak.f1(K, RAND, SQN, AMF) == b'\x90\xd2(\x9e\xd1\xca\x1c=\xbc"G\xbbH\rC\x1a\xc7\x1d.Jvw\xf6\xe9\x97\xcf\xdd\xb0\xcb\xad\x88\xb7' and \
    tuak.f1star(K, RAND, SQN, AMF) == b'BsU\xdb\xac0\xe8%\x06:\xbaa\xb5V\xe8u\x83\xab\xacc\x8e:\xb0\x1cL\x88J\xd9\xd4X\xdc/' )
    
    TUAK.KeccakIterations = 1
    return ret

def tuak_testsets_6():
    return tuak_testset_61() and tuak_testset_62() and \
        tuak_testset_63() and tuak_testset_64() and \
        tuak_testset_65() and tuak_testset_66()


def tuak_testset_71():
    K    = b'\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab\xab'
    RAND = b'BBBBBBBBBBBBBBBB'
    TOP  = b'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU'
    
    tuak = TUAK(TOP)
    tuak.LEN_CK  = 128
    tuak.LEN_IK  = 128
    tuak.LEN_RES = 32
    TOPc = make_TOPc(K, TOP)
    tuak.set_topc(TOPc)
    
    return tuak.f2345(K, RAND) == (b'ez\xcdd', b'\xd7\x1a\x1e\\l\xaf\xfe\x98j&\xf7\x83\xe5\xc7\x8b\xe1',
        b'\xbe\x84\x9f\xa2VO\x86\x9a\xec\xeeob\xd43~r', b'q\x9f\x1e\x9b\x90T') and \
        tuak.f5star(K, RAND) == b'\xe7\xafk=\x0e8'

def tuak_testset_72():
    K    = b'\xff\xfe\xfd\xfc\xfb\xfa\xf9\xf8\xf7\xf6\xf5\xf4\xf3\xf2\xf1\xf0\xef\xee\xed\xec\xeb\xea\xe9\xe8\xe7\xe6\xe5\xe4\xe3\xe2\xe1\xe0'
    RAND = b'\x01#Eg\x89\xab\xcd\xef\x01#Eg\x89\xab\xcd\xef'
    TOP  = b'\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f'
    
    tuak = TUAK(TOP)
    tuak.LEN_CK  = 128
    tuak.LEN_IK  = 128
    tuak.LEN_RES = 64
    TOPc = make_TOPc(K, TOP)
    tuak.set_topc(TOPc)
    
    return tuak.f2345(K, RAND) == (b'\xe9\xd7I\xdcN\xea\x005', b"\xa4\xcboe)\xab\x17\xf83\x7f'\xba\xa8#MG",
        b'"t\x15\\\xcfA\x99\xd5\xe2\xab\xcb\xf6!\x90\x7f\x90', b'H\n\x93E\xcc\x1e') and \
        tuak.f5star(K, RAND) == b'\xf8N\xb38\x84\x8c'

def tuak_testset_73():
    K    = b'\xff\xfe\xfd\xfc\xfb\xfa\xf9\xf8\xf7\xf6\xf5\xf4\xf3\xf2\xf1\xf0\xef\xee\xed\xec\xeb\xea\xe9\xe8\xe7\xe6\xe5\xe4\xe3\xe2\xe1\xe0'
    RAND = b'\x01#Eg\x89\xab\xcd\xef\x01#Eg\x89\xab\xcd\xef'
    TOP  = b'\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f'
    
    tuak = TUAK(TOP)
    tuak.LEN_CK  = 128
    tuak.LEN_IK  = 256
    tuak.LEN_RES = 64
    TOPc = make_TOPc(K, TOP)
    tuak.set_topc(TOPc)
    
    return tuak.f2345(K, RAND) == (b'\x07\x02\x1cs\xe7c\\}', b'MY\xacyh4\xeb\x85\xd1\x1f\xa1H\xa5\x05\x8c<',
        b'\x12mGP\x016\xfd\xc5\xdd\xfd\x14\xf1\x9e\xbf\x16t\x9c\xe4\xb6CS#\xfb\xb5qZ:yj`\x82\xbd',
        b'\x1df"\xc4\xe5\x9a') and tuak.f5star(K, RAND) == b'\xf8N\xb38\x84\x8c'

def tuak_testset_74():
    K    = b'\xb8\xda\x83zPe-j\xc7\xc9}\xa1Oj\xcca'
    RAND = b'h\x87\xe5T%\xa9f\xbd\x86\xc9f\x1a_\xa7+\xe8'
    TOP  = b'\tR\xbe\x13Ul2\xeb\xc5\x81\x95\xd9\xdd\x93\x04\x93\xe1*\x90\x03f\x99\x88\xff\xde_\xa1\xf0\xfe5\xcc\x01'
    
    tuak = TUAK(TOP)
    tuak.LEN_CK  = 128
    tuak.LEN_IK  = 128
    tuak.LEN_RES = 128
    TOPc = make_TOPc(K, TOP)
    tuak.set_topc(TOPc)
    
    return tuak.f2345(K, RAND) == (b'@A\xceC\x8e>8\xe8\xaa\x96V.\xed\x83\xacC',
        b">;\xc0\x1b\xea\x0c\xd9\x14\xc4\xc2\xc8<\xe2\xd9'W", b'fj\x8eoW{\x1a\xa7{\x7f\xd5<\xeb\xb8\xa3\xd6',
        b'\x1f\x88\r\x00Q\x19') and tuak.f5star(K, RAND) == b'E\xe6\x17\xd7\x7f\xe5'

def tuak_testset_75():
    K    = b'\x15t\xcaV\x88\x1d\x05\xc1\x89\xc8(\x80\xf7\x89\xc9\xcdBD\x95_D&\xaa+i\xc2\x9f\x15w\x0eZ\xa5'
    RAND = b'\xc5p\xaa\xc6\x8c\xdee\x1f\xb1\xe3\x08\x83"I\x8b\xef'
    TOP  = b'\xe5\x9fn\xb1\x0e\xa4\x06\x81?I\x91\xb0\xb9\xe0/\x18\x1e\xdfL~\x17\xb4\x80\xf6m4\xda5\xee\x88\xc9^'
    
    tuak = TUAK(TOP)
    tuak.LEN_CK  = 256
    tuak.LEN_IK  = 128
    tuak.LEN_RES = 256
    TOPc = make_TOPc(K, TOP)
    tuak.set_topc(TOPc)
    
    return tuak.f2345(K, RAND) == (b'\x84\xd8\x9bA\xdb\x18g\xff\xd4\xc7\xba\x1d\x82\x16?MRj \xfb\xaeT\x18\xfb\xb5&\x94\x0b\x1e\xeb\x90\\',
        b"\xd4\x19gj\xfeZ\xb5\x8c\x1d\x8b\xee\rCR:M/R\xef\x0b1\xa4gj\x0c3D'\xa9\x88\xfee",
        b' U3\xe5\x05f\x1ba\xd0\\\xc0\xea\xc8x\x18\xf4', b'\xd7\xb3\xd2\xd4\x98\n') and \
        tuak.f5star(K, RAND) == b'\xca\x96U&I\x86'

def tuak_testset_76():
    TUAK.KeccakIterations = 2
    K    = b'\x15t\xcaV\x88\x1d\x05\xc1\x89\xc8(\x80\xf7\x89\xc9\xcdBD\x95_D&\xaa+i\xc2\x9f\x15w\x0eZ\xa5'
    RAND = b'\xc5p\xaa\xc6\x8c\xdee\x1f\xb1\xe3\x08\x83"I\x8b\xef'
    TOP  = b'\xe5\x9fn\xb1\x0e\xa4\x06\x81?I\x91\xb0\xb9\xe0/\x18\x1e\xdfL~\x17\xb4\x80\xf6m4\xda5\xee\x88\xc9^'
    
    tuak = TUAK(TOP)
    tuak.LEN_CK  = 256
    tuak.LEN_IK  = 256
    tuak.LEN_RES = 256
    TOPc = make_TOPc(K, TOP)
    tuak.set_topc(TOPc)
    
    ret = tuak.f2345(K, RAND) == (b'\xd6~ndY\r"\xee\xcb\xa72J\xfaJ\xf4F\x0c\x93\xf0\x1b$Pmn\x12\x04}x\x9a\x94\xc8g',
        b'\xed\xe5~\xdf\xc5|\xdf\xfe\x1a\xaeu\x06j\x1bty\xbb\xc3\x83t8\xe8\x8d7\xa8\x01\xcc\xcc\x9f\x97+\x89',
        b'H\xed\x92\x99\x12nPW@/\xe0\x1f\x92\x01\xcf%$\x9f\x9c\\\x0e\xd2\xaf\xcf\x08GU\xda\xff\x1d9\x99',
        b'j\xae\x8d\x18\xc4H') and tuak.f5star(K, RAND) == b'\x8c_3\xb6\x1fN'
    
    TUAK.KeccakIterations = 1
    return ret

def tuak_testsets_7():
    return tuak_testset_71() and tuak_testset_72() and \
        tuak_testset_73() and tuak_testset_74() and \
        tuak_testset_75() and tuak_testset_76()

def testall():
    return keccak_testsets() and tuak_testsets_6() and tuak_testsets_7()

def testperf():
    a = None
    T0 = time()
    for i in range(10000):
        a = testall()
    print('10000 full testsets in %.3f seconds' % (time()-T0, ))

def test_TUAK():
    assert( testall() )

if __name__ == '__main__':
    testperf()
