from builtins import *

def main():
    with open("C:\\Users\\Seth\\PycharmProjects\\BioInformaticsProjects\\ecoli.fasta", "r") as g:
        for line in g:
            if not line.startswith('<'):
                print(line)

if __name__ == '__main__':
    main()



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