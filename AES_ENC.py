# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:23:08 2020

@author: moon
"""
import random
import copy

Sbox =  [ 0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67,
        0x2b, 0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59,
        0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7,
        0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1,
        0x71, 0xd8, 0x31, 0x15, 0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05,
        0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83,
        0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29,
        0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
        0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 0xd0, 0xef, 0xaa,
        0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c,
        0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc,
        0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec,
        0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19,
        0x73, 0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee,
        0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32, 0x3a, 0x0a, 0x49,
        0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4,
        0xea, 0x65, 0x7a, 0xae, 0x08, 0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6,
        0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 0x70,
        0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9,
        0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e,
        0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 0x8c, 0xa1,
        0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0,
        0x54, 0xbb, 0x16]

RC = [ 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

key = [ 0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, \
            0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c ]
 
block = [ 0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d, \
            0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34 ]
    
def block2state(block):
    state=[]
    for x in range(4):        
        col=[block[x*4+i] for i in range(4)]
        state.append(col)   
    return state

def subbyest(state):
    new_state= []
    for x in range(4):
        new_col = [Sbox[state[x][i]] for i in range(4)]
        new_state.append(new_col)
    return new_state

def SubByte_Col(col):
    new_col = [ Sbox[col[i]] for i in range(4) ]
    return new_col

def Xor_Col(c1, c2):
    new_col = [ c1[i]^c2[i] for i in range(4) ]
    return new_col

def Rotl(col):
    new_col = [ col[1], col[2], col[3], col[0]]
    return new_col

def KeySR(col, round):
    new_col = Rotl(col)
    round_constant = [ RC[round-1], 0, 0, 0]
    new_col2 = SubByte_Col(new_col)
    new_col3 = Xor_Col(new_col2, round_constant)
    return new_col3

def key_schedule_Enc(key_state):
    rkey = [ copy.deepcopy(key_state) ]
    for round in range(1,11):
        new_state = []
        new_w0 = Xor_Col(rkey[round-1][0], KeySR(rkey[round-1][3], round))
        new_state.append(new_w0)
        new_w1 = Xor_Col(rkey[round-1][1], new_w0)
        new_state.append(new_w1)
        new_w2 = Xor_Col(rkey[round-1][2], new_w1)
        new_state.append(new_w2)
        new_w3 = Xor_Col(rkey[round-1][3], new_w2)
        new_state.append(new_w3)
        rkey.append(new_state)
    return rkey

def AddRoundkey(state , rkey):
    new_state = []
    for col in range(4):
        new_col = [state[col][i] ^ rkey[col][i] for i in range(4)]
        new_state.append(new_col)
    return new_state

def shiftrows(state):
    new_state=[]
    for x in range(4):
        new_col=[state[(x+i)%4][i] for i in range(4)]
        new_state.append(new_col)
    return new_state

#다항식으로 봤을떄 x 를 곱해서 비트를 옮기는 연산
def xtime(x):
    y = (x<<1)&0xff
    if x>=128:
         y^=0x1b
    return y 



    
#0x02 곱하기 연산
def m02(x) :
    return xtime(x)
#0x03 곱하기 연산
def m03(x) :
    return m02(x)^x


# 한 열 믹스컬럼 함수
def MC_Col(col):
    new_col=[0]*4
    new_col[0]=m02(col[0])^m03(col[1])^col[2]^col[3]
    new_col[1]=m02(col[1])^m03(col[2])^col[0]^col[3]
    new_col[2]=m02(col[2])^m03(col[3])^col[0]^col[1]
    new_col[3]=m02(col[3])^m03(col[0])^col[2]^col[1]
    return new_col

# 4번 열 믹스 시행함수
def MIX_Column(state):
    new_state = []
    for col in range(4):
        new_col=MC_Col(state[col])
        new_state.append(new_col)
    return new_state

def hex_print(state):
    print('[',end='')
    for i in range(4):
        print('[0x%02x, 0x%02x, 0x%02x, 0x%02x]' %(state[i][0], state[i][1], state[i][2], state[i][3]), end='')
    if i<3:
        print(", ",end = " ")
    print("]")

def AES_Round(state, rkey):
    new_state = copy.deepcopy(state)
    new_state2 = subbyest(new_state)
    new_state3 = shiftrows(new_state2)
    new_state4 = MIX_Column(new_state3)
    new_state5 = AddRoundkey(new_state4, rkey)
    return new_state5

def AES_ENC(plaintext, key):
    rkey = key_schedule_Enc(key)
    state = copy.deepcopy(plaintext)
    new_state = AddRoundkey(state, rkey[0])
    for i in range (1,10):
        out_state = AES_Round(new_state, rkey[i])
        new_state = copy.deepcopy(out_state)
        print(i,' ',end = '')
        hex_print(new_state)
    new_state2 = subbyest(new_state)
    new_state3 = shiftrows(new_state2)
    new_state4 = AddRoundkey(new_state3, rkey[10])
    return new_state4

#운영모드 실습중
#--4 
#16
def state2block(in_state):
    new_block=[]
    for i in range(4):
        new_block +=in_state[i]
    return new_block


#패딩함수
def padding(pt):
    if (len(pt)%16==0):
        return pt
    
    else:
        block_size = 16
        pad_num = block_size - (len(pt)%block_size)
        block_num = (len(pt)+block_size)//block_size
        pad_pt = [0 for i in range(block_num * block_size)]
        pad_pt[0:len(pt)] = pt
        pad_pt[len(pad_pt)-1]= pad_num
        return pad_pt
    

#운영모드
def ECB(pt, key):
    ct=[]
    pad_pt = padding(pt)
    key_state = block2state(key)
    block_num = (len(pad_pt)+16-1)//16
    
    #블롣 단위로 평문 암호화
    for i in range(block_num):
        i_th_in_state = block2state(pad_pt[16*i : 16*i+16])
        print(i, "th plaintext block")
        hex_print(i_th_in_state)
        
        new_state = AES_ENC(i_th_in_state, key_state)
        print(i,"th ciphertext block =")
        hex_print(new_state)
        ct += state2block(new_state)
    return ct


#--난수 생성 iv
def get_nonce():
    nonce = [0 for i in range(16)]#랜덤 변수저장
    for i in range(16):
        nonce[i] = random.randint(0, 255)#8비트는 0~255까지 가능해서
    return nonce
#cbc모드
def cbc(pt,key):
    ct=[]
    tmp=[]
    pad_pt = padding(pt)
    key_state = block2state(key)#키를 변형
    block_num = (len(pad_pt)+16-1)//16
    nonce = get_nonce()#iv받아오기
    #블록단위 암호화
    for i in range(block_num):
        tmp[0:16]= pad_pt[16*i: 16*i+16]
        for j in range(16):
            tmp[j]^=nonce[j]
        i_th_in_state = block2state(tmp)
        print(i, "th plaintext block")
        hex_print(i_th_in_state)
        new_state=AES_ENC(i_th_in_state, key_state)
        print(i,"th ciphertext block =")
        hex_print(new_state)
        nonce = state2block(new_state)
        ct += nonce
    return ct
  

#cfb모드 
def CFB(pt, key):
    ct=[]
    nonce = get_nonce()
    key_state = block2state(key)
    block_num = (len(pt)+16-1)//16
    inputs = block2state(nonce)
    
    for i in range(block_num-1):
        new_state = AES_ENC(inputs, key_state)
        i_th_state = block2state(pt[16*1: 16*i+16])
        new_state2 =AddRoundkey(new_state, i_th_state)
        inputs = new_state2
        ct += state2block(new_state2)
        
        
    new_state = AES_ENC(inputs, key_state) 
    new_block = state2block(new_state)
    for i in range(len(pt)-16*(block_num-1)):
        ct += [pt[16*(block_num-1)+i]^new_block[i]]
    return ct
    
    
#     ofb모드
def OFB(pt,ket):
    ct = []
    nonce = get_nonce()
    key_state = block2state(key)
    block_num = (len(pt)+16-1)//16
    inputs = block2state(nonce)
    
    for i in range(block_num-1):#마지막은 따로 처리해주자
        new_state = AES_ENC(inputs, key_state)    
        inputs=new_state
        i_th_state = block2state(pt[16*i:16*i+16])
        new_state2 = AddRoundkey(new_state, i_th_state)
        ct += state2block(new_state2)
    
    
    new_state = AES_ENC(inputs, key_state)
    new_block = state2block(new_state)
    for i in range(len(pt)-16*(block_num-1)):
        ct += [pt[16*(block_num-1)+i]^new_block[i]]
    return ct
#======================
def get_counter(nonce):
    nonce[15]=(nonce[15]+1)%256
    for i in range(15,0,-1):
        if (nonce[i]==0):
            c=1
            nonce[i-1]=(nonce[i-1]+c)%256
        else:
            c=0
            return nonce
        return nonce

#=========================
def CTR(pt, key):
    ct= []
    key_state = block2state(key)
    block_num = (len(pt)+16-1)//16#블록의 갯수를 구할수있음
    print("key=")
    hex_print(key_state)
    nonce=get_nonce()
    
    for i in range(block_num-1):
        i_th_in_state=block2state(pt[16*i:16*i+16])
        print(i,"plain text")
        hex_print(i_th_in_state)
        nonce=get_counter(nonce)
        new_state=AES_ENC(block2state(nonce), key_state)
        new_state=AddRoundkey(new_state, i_th_in_state)
        print(i,"ciper text")
        hex_print(new_state)
        ct +=state2block(new_state)
        
    #마지막 블록
    nonce = get_counter(nonce)
    new_state=AES_ENC(block2state(nonce), key_state)
    ct +=state2block(new_state)
    
    for j in range(len(pt)-16*(block_num-1)):
        ct[16*(block_num-1)+j]^=pt[16*(block_num-1)+j]
    
    return ct
        
    

#=======================
key = block2state(key)
key = key_schedule_Enc(key)
for i in range(11):
    hex_print(key[i])
'''
import os

import PIL.Image as pilimg
import numpy as np


def main():
    
    block = [ 0x6b, 0xc1, 0xbe, 0xe2, 0x2e, 0x40, 0x9f, 0x96,\
            0xe9, 0x3d, 0x7e, 0x11, 0x73, 0x93, 0x17, 0x2a,\
            0xae, 0x2d, 0x8a, 0x57, 0x1e, 0x03, 0xac, 0x9c,\
            0x9e, 0xb7, 0x6f, 0xac,0x45, 0xaf, 0x8e, 0x51] 


    key = [ 0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, \
            0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c ]


    #im=pilimg.open("sample_02.png")
    #pix=np.array(im)
   #print(pix.shape)
    #grayscale=im.convert("L")
    #grayscale.save("sample_02_black.png")




    

    #ct=ECB(np.ravel(grayscale,order="C"),key)

    #ct = ECB(block, key)
    #ct = cbc(block, key)
    #ct = CFB(block, key)
    #ct = OFB(block,key)
    #ct = CTR(block,key)
    for i in range(len(ct)):
        if (i%16) == 0:
            print()
        print("%02f, " % ct[i], end=" ")
   
    #b=np.reshape(ct,(256,256))
    #new_p=pilimg.fromarray(b)
    #new_p=new_p.convert("L")
    #new_p.save("sample_02_ECB.png")
    #new_p.show()











    state = block2state(block)
    key_state = block2state(key) 

    print("plaintext") 
    hex_print(state)
    print("key")
    hex_print(key_state)

    new_state = AES_ENC(state, key_state) 
    hex_print(new_state)

#if __name__== "__main__":
    #main()

'''

















































