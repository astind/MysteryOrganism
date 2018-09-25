from builtins import *


def main():
    dna = ""
    with open("ecoli.fasta", "r") as g:
        for line in g:
            if not line.startswith('<'):
                dna = dna + line.strip("\n")
    starting_pos = int(minimum_skew(dna))
    dnaSplice = dna[starting_pos:starting_pos + 500]
    dnaaBox = []
    for c in range(0,500 - 9):
        temp = approx_pattern(dnaSplice[c:c + 10], dnaSplice)
        if len(temp) > 3:
            dnaaBox.append(temp)
    for s in dnaaBox:
        print(s)

def approx_pattern(compStr, fullStr):
    mismatch = 1
    starters = []
    for c in range(0,len(fullStr) - len(compStr)):
        cnt = 0
        cnt2 = 0
        for d in range(0,len(compStr)):
            if compStr[d] != fullStr[c + d]:
                cnt = cnt + 1
            rev = reverse_complement(compStr)
            if rev[d] != fullStr[c + d]:
                cnt2 = cnt2 + 1
        if cnt <= int(mismatch):
            starters.append(compStr)
        elif cnt2 <= int(mismatch):
            starters.append(rev)
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
    return skew_loc[0]

if __name__ == '__main__':
    main()



