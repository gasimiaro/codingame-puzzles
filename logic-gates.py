#https://www.codingame.com/ide/puzzle/logic-gates

logic = {
    "AND": lambda a, b: a == b == "-",           
    "OR" : lambda a, b: a == "-" or b == "-",      
    "XOR": lambda a, b: a != b,                
    "NAND": lambda a, b: not (a == b == "-"),   
    "NOR": lambda a, b: not (a == "-" or b == "-"),
    "NXOR": lambda a, b: a == b                
}
n = int(input())
m = int(input())
_input ={}
for i in range(n):
    input_name, input_signal = input().split()
    _input[input_name] = input_signal
for i in range(m):
    output_name, _type, input_name_1, input_name_2 = input().split()
    res = ""
    for j in range(len(_input[input_name_1])):
        res += ("-" if logic[_type](_input[input_name_1][j],_input[input_name_2][j]) else "_")
    print(output_name,res)
