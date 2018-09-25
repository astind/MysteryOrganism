from builtins import *


def main():
    with open("ecoli.fasta", "r") as g:
        for line in g:
            if not line.startswith('<'):
                print(line)


if __name__ == '__main__':
    main()

def approx_pattern(compStr, fullStr):
    mismatch = 1
    starters = []
    for c in range(0,len(fullStr) - len(compStr)):
        cnt = 0
        for d in range(0,len(compStr)):
            if compStr[d] != fullStr[c + d]:
                cnt = cnt + 1
        if cnt <= int(mismatch):
            starters.append(c)
    return starters

def reverse_complement(input):
    reverse = input[::-1]
    complement = ""
    for x in reverse:
        if x == "A":
            complement += "T"
        if x == "T":
            complement += "A"
        if x == "C":
            complement += "G"
        if x == "G":
            complement += "C"
    return complement


def minimum_skew(dna):
    skew_count = 0
    skew_min = 0
    skew_loc = []
    i = 1
    for x in dna:
        if x == "C":
            skew_count -= 1
        elif x == "G":
            skew_count += 1

        if skew_count < skew_min:
            skew_loc = []
            skew_min = skew_count
            skew_loc.append(i)
        elif skew_count == skew_min:
            skew_loc.append(i)

        i += 1
    return skew_loc



