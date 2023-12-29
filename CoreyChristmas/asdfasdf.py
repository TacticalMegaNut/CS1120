# import numpy as np
# from numpy import random as rd

# alp = "abcdefghijklmnopqrstuvwxyz"
# inds = rd.permutation(len(alp))
# reordered = np.array(list(alp))[inds]
# cipher = 


def caesar(plaintext, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

print(caesar("what type of cipher is used to ask this question", 1))
print(caesar("pigpen", 1))
print(caesar("caesar", 1))
print(caesar("rail fence", 1))
print(caesar("autokey", 1))