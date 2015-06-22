#!/usr/bin/env python

"""
Given an image represented by an NxN matrix, where each pexel in
the image is 4 bytes, write a method to rotate the image by 90
degrees. Can you do this in place?

- naive. For every character in one arbitrary quater, swap the
corresponding 4 cells circularly.
"""

# FIXME
# part of the image seems not rotated correctly

def rotate(img):
    N = len(img)
    for i in range(N/2):
        for j in range(i, N - 1 - i):
            tmp = img[i][j]
            img[i][j] = img[N - 1 - j][i]
            img[N - 1 - j][i] = img[N - 1 - i][N - 1 - j]
            img[N - 1 - i][N - 1 - j] = img[j][N - 1 - i]
            img[j][N - 1 - i] = tmp

def test_rotate():
    from pylab import *
    img = imread('Lenna.png')
    rotate(img)
    imshow(img)
    show()
