# Befunge_Interpreter
This app is an interpreter written in Python for the esoteric language Befunge-93. To learn about specification see https://esolangs.org/wiki/Befunge.

## Usage
Root directory:
```
python main.py <path> <boolean>
```
```<path>``` is absolute path to the file with source code to interpret, e.g. "python main.py "C:\Users\User\example_file.befunge"".
 
```<boolean>``` determines whether timeout of 60 sec is on 

Supported extensions are: ".be", ".bf", ".b93", ".b98", ".befunge".
