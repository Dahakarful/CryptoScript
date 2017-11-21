# Caesar cipher

This script will encrypt or decrypt your text with the given alphabetical gap, this is Caesar cipher.

For help run ```rot.py -h```.

## Commands

The command always begin with the gap you want to apply ```-g <int>```.

You can add text like parameter with ```-t``` and you'll have the result in your command shell be careful to put your text in quotation marks if there are spaces and make sure you have no return to the line.

Or you can specify an input file with your text (option ```i```) and it will genertate you a new output file (option ```-o```) with the new text.
If you don't sepcify an output file it will be print in your command shell.

Command to generate a text from an input file to an output file:
```shell
rot.py -g <gap> -i <inputfile> -o <outputfile>
```

Command to generate a text from an input file to command shell:
```shell
rot.py -g <gap> -i <inputfile>
```

Command to generate a text from text in command shell:
```shell
rot.py -g <gap> -t <text>
```
