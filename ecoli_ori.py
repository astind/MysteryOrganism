from builtins import *

def main():
    with open("C:\\Users\\Seth\\PycharmProjects\\BioInformaticsProjects\\ecoli.fasta", "r") as g:
        for line in g:
            if not line.startswith('<'):
                print(line)

if __name__ == '__main__':
    main()