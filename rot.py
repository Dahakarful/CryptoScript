# For help run rot.py -h
# The command always begin with the gap you want to apply -g <int>
# You can add text like parameter with -t and you'll have the result in your command shell be careful to put your text in quotation marks if there are spaces
# and make sure you have no return to the line
# Or you can specify an input file with your text (option -i) and it will genertate you a new output file (option -o) with the new text
# If you don't sepcify an output file it will be print in your command shell
import sys, getopt

def rot(text, int):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    newText = ""
    for c in text:
        try:
            index = alphabet.index(c)
            res = (index + int) % 26
            newText += alphabet[res]
        except ValueError:
            newText += c
    return newText

def textFromFile(file):
    try:
        with open(file, 'r') as aFile:
            data=aFile.read().replace('\n', '')
        return data
    except FileNotFoundError:
        raise FileNotFoundError

def textToFile(file, text):
    open(file, 'w').write(text)

def main(argv):
    inputfile = ''
    outputfile = ''
    gap = ''
    text = ''
    try:
        opts, args = getopt.getopt(argv,"hg:i:o:t:",["gap=","ifile=","ofile=","text="])
    except getopt.GetoptError:
        print('Bad parameters ! Run command with -h option for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Command to generate a text from an input file to an output file:\nrot.py  -g <gap> -i <inputfile> -o <outputfile>\n')
            print('Command to generate a text from an input file to command shell:\nrot.py -g <gap> -i <inputfile>\n')
            print('Command to generate a text from text in command shell:\nrot.py -g <gap> -t <text>\n')
            sys.exit()
        elif opt in ("-g", "--gap"):
            try:
                gap = int(arg)
            except ValueError:
                print('-g: Option gap need to be an int')
                return
        elif opt in ("-t", "--text"):
            text = arg
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    try:
        if gap != '':
            if inputfile != '':
                text = textFromFile(inputfile)
                newText = rot(text, gap)
                if outputfile != '':
                    textToFile(outputfile, newText)
                    print('New text was write into file', outputfile)
                else:
                    print(newText)
            elif text != '':
                newText = rot(text, gap)
                print(newText)
        else:
            print('Run command with -h option for help')
    except FileNotFoundError:
        print('-i: the file', inputfile, ' was not found')

if __name__ == "__main__":
    main(sys.argv[1:])