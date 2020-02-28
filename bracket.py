def balanced(expr):

    s = []

    for i in range(len(expr)):
        
        if (expr[i] == '(' or
			expr[i] == '[' or expr[i] == '{'):

            s.append(expr[i])
            continue

        if len(s) == 0:
            return False

        if expr[i] == ')':

            x = s.pop()

            if x == '{' or x == '[':
                return False
                
        elif expr[i] == '}':

            x = s.pop()

            if x == '(' or x == '[':
                return False

        elif x == ']':

            x = s.pop()

            if x == '(' or x == '{':
                return False

                
    if len(s):
        return True
    else:
        return False


text = input("Digite a sequência: ")

if (balanced(text)):
    print("Sim")
else:
    print("Não")

