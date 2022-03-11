## Vinculum Lang Documentation

Vinculum is a scientific computing language developed in Python. 

### Current Features

+ Simple Addition, Subtraction, Multiplication, Division, Order of Operations

### Planned Features

+ Full Library of Simple Math Operations
+ CAS
+ Stat Prob
+ Numerical Methods for Aproximation
+ Physics

### Documentation

##### Grammar

+ expression
    - := term ((PLUS|MINUS) term)*

+ term        
    - := factor ((MUL|DIV) factor)*

+ factor    
    - := (PLUS_MINUS) factor*
    - := atom

+ atom
    - := quark (POWER factor)*

+ quark
    - := INT|Float
    - := LPAREN expression RPAREN

##### Standard Library

| Operation | Description | Input | Output | Additional Detail |
| -- | -------------- | ----- | ----- | ----- | 
| +  | Addition       | node + node | values.Number (float) | | |
| -  | Subtraction    | node - node | values.Number (float) | | |
| *  | Multiplication | node * node | values.Number (float) | | |
| /  | Division       | node / node | values.Number (float) | | |
| %  | Modulo         | node % node | values.Number (float) | | |
| + (Unary)  | Unary Positive Operation | +node | values.Number (float) | | |
| - (Unary)  | Unary Negation Operation | -node | values.Number (float) | | |
| () | Left \& Right Parenthesis to Change Priority of Operations | ( expression ) | | | |
