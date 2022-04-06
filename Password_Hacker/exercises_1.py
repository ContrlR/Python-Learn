#!/bin/env python

# Jetbrains academy Password hacker project
# Below are exercises done in stage 1
import argparse


# Byte Basics

word = [chr(int(input('Enter 4 unicode characters in decimal: '))) for _ in range(4)]
print('The charcters you entered in ACSII are ' + *word , sep='')

encode = int(input('Lets encode a phrase. enter a number 0 - 9: '))
print(''.join([chr(ord(i) + encode) for i in input('Enter your phrase: ')]))

# If you couldnt tell I like lists
print('Let\'s calculate the sum of Unicode code points of two given characters. ')
letters = [ord(input('Enter a character: ')) for _ in range(2)]
print(sum(letters))


num = int(input('Enter a number in the printable range: '))
start, end = 32, 127
cars = list(range(start, end))
print(chr(num) if num in cars else 'False')

parser = argparse.ArgumentParser(description="Sends a message to an address and port then prints the response ")
parser.add_argument("-a", "--address")
parser.add_argument("-p", "--port")
parser.add_argument("-m", "--message")
args = parser.parse_args()
