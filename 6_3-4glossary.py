#Excercise 6-3,6-4 Glossary
terms = {
    'Algorithm' : 'An algorithm is a set of instructions or rules designed to solve a definite problem. \nThe problem can be simple like adding two numbers or a complex one, \nsuch as converting a video file from one format to another.',
    'Program' : 'A computer program is termed as an organized collection of instructions, \nwhich when executed perform a specific task or function. A program is processed \nby the central processing unit (CPU) of the computer before it is executed. \nAn example of a program is Microsoft Word, which is a word processing \napplication that enables users to create and edit documents. \nThe browsers that we use are also programs created to help us browse the internet.',
    'API' : 'Application Programming Interface (API) is a set of rules, routines, and protocols \nto build software applications. APIs help in communication with third party \nprograms or services, which can be used to build different software. \nCompanies such as Facebook and Twitter actively use APIs to help developers \ngain easier access to their services.',
    'Argument' : 'Argument or arg is a value that is passed into a command or a function. For example, \nif SQR is a routine or function that returns the square of a number, then SQR(4) will return 16. Here, \nthe value 4 is the argument. Similarly, if the edit is a function that edits a file, \nthen in edit myfile.txt, ‘myfile.txt’ is the argument.',
    'ASCI' : 'American Standard Code for Information Interexchange (ASCII) is a standard that assigns letters, \nnumbers and other characters different slots, available in the 8-bit code. \nThe total number of slots available is 256. The ASCII decimal number is derived from binary, \nwhich is assigned to each letter, number, and character. For example, the ‘$’ sign is \nassigned ASCII decimal number 036, while the lowercase ‘a’ character is assigned 097.',
    'Boolean' : 'A Boolean expression or Boolean logic is an expression used for creating statements that are either TRUE or FALSE. \nBoolean expressions use AND, OR, XOR, NOT and NOR operators with conditional statements in programming, \nsearch engines, algorithms, and formulas. Boolean expressions are also called comparison expressions, \nconditional expressions, and relational expressions.',
    }

for k, v in terms.items() :
    print (f"{k}:\n{v}\n")
