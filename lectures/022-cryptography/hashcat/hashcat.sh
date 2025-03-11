#!/usr/bin/env bash

# Hashcat Examples
wget https://raw.githubusercontent.com/hashcat/hashcat/refs/heads/master/example0.hash
wget https://raw.githubusercontent.com/hashcat/hashcat/refs/heads/master/example.dict
# -a7 = hybrid mask + wordlist
# This cracks with 4 variations of 4 charsets for the first 4 characters
hashcat -m 0 -t 32 -a 7 example0.hash ?a?a?a?a example.dict


wget https://raw.githubusercontent.com/hashcat/hashcat/refs/heads/master/rules/dive.rule
hashcat -m 0 -a 0 -r dive.rule example0.hash example.dict   


# generate 8 character passwords
# yay -S pwgen
# for i in {1..100}; do
#     pwgen -cAny -1 >> 8char4charset_passwords.txt
# done
# 
# MD5
# while IFS= read -r line; do
#     echo "$line" | md5
# done < "8char4charset_passwords.txt" > "8char4charset_MD5.txt"
# 
# SHA256   
# while IFS= read -r line; do
#     echo "$line" | sha256sum
# done < "8char4charset_passwords.txt" > "8char4charset_SHA2-256.txt"
 

# MD5
hashcat -m0 8char4charset_MD5.txt -a3 '?a?a?a?a?a?a?a?a'
# SHA-256
hashcat -m1400 8char4charset_SHA2-256.txt -a3 '?a?a?a?a?a?a?a?a'


# rockyou.txt
# get rockyou.txt
wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
