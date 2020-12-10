# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:41:55 2020

@author: ELDrago
"""

import pytube
print('Type "STOP" if done Downloading \n')
while True :
    url = input('Please Enter Url : ')
    if url in ['STOP','stop','Stop'] : break
    print('Please wait... Searching for Videos on URL')
    video = pytube.YouTube(url)
    c = 1
    tags = []
    print('Gathering Data... \nPlease select Option of Video Quality from below : ')
    for stream in video.streams :
        s = str(stream).split()
        a = s[6]
        if not a.startswith('acodec=') : break
        #print(stream)
        tags.append(int(s[1][6:8]))
        print(c,'-', s[3][5:-1])
        c += 1
    qua = int(input())
    if qua > len(tags) : 
        print('Incorrect Selection of Option ...')
        print('Please try again ... ')
        continue
    #print(tags)
    stream = video.streams.get_by_itag(tags[qua-1])
    print('Downloading... Facts : Waiting depends on your internet connection')
    stream.download()
    print('DONE... Thanks for waiting')