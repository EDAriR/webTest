import os
from os.path import join, abspath
import chardet

def get_path(directory, file):
    return abspath(join(directory, file))

# Put your directory here
directory = "/home/ed/Downloads/SL275_第一次分享-new"



for res in os.walk(directory):

    r = res[0].split(' ')[0]
    if os.path.isdir(r):

        print('isdir==========isdir=============isdir=============isdir')
        print(r)
        print('isdir==========isdir=============isdir=============isdir')
    else:
        f = open(res,'r')
        print(chardet.detect())


# Sample = os.listdir(directory)
# print(Sample)
#
# Sample2 = os.listdir(directory+'/02_Sample_part2')
# Sample4 = os.listdir(directory+'/04_Sample_part4')
# Sample1 = os.listdir(directory+'/01_Sample_part1')
# Sample3 = os.listdir(directory+'/03_Sample_part3_JDK1.5')
#
# print(Sample1)
# print(Sample2)
# print(Sample3)
# print(Sample4)
#
# for s in Sample4:
#     cd = chardet.detect(s.)
#     print(cd)
#     print(type(s))