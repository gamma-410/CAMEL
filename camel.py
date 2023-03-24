import sys

CAMEL_CODE_DECLARATION = "@camelCode"

str_variable = {}
int_variable = {}


def run_program(file_name):
    with open(file_name) as f:
        first_line = f.readline()
        if not first_line.startswith(CAMEL_CODE_DECLARATION):
            print("DeclarationError: Invalid program declaration.")
            return

        for line in f:
            execute_line(line.strip())


def execute_line(line):

    if not line:
        return

    words = line.split()

    if words[0] == "!":
        return

    if words[0] == "get":
        if words[2] == "str":
            try:
                input_var = input(words[3])
                str_variable[words[1]] = str(input_var)
            except:
                print("TypeError: Type is not 'String'.")
        elif words[2] == "int":
            try:
                input_var = input(words[3])
                int_variable[words[1]] = int(input_var)
            except:
                print("TypeError: Type is not 'Int'.")
    elif words[0] == "show":
        if words[1] == "str":
            try:
                print(str_variable[words[2]])
            except:
                print(f"VariableError: Variable '{words[2]}' not found.")
        elif words[1] == "int":
            try:
                print(int_variable[words[2]])
            except:
                print(f"VariableError: Variable '{words[2]}' not found.")

    elif words[0] == "let":
        if words[2] == "str":
            str_variable[words[1]] = str(words[4])
        elif words[2] == "int":
            int_variable[words[1]] = int(words[4])

    elif words[0] in ["+", "-", "*", "/", "%"]:
        op1 = int_variable[words[1]]
        op2 = int_variable[words[2]]
        if words[0] == "+":
            ans = op1 + op2
        elif words[0] == "-":
            ans = op1 - op2
        elif words[0] == "*":
            ans = op1 * op2
        elif words[0] == "/":
            ans = op1 / op2
        elif words[0] == "%":
            ans = op1 % op2
        int_variable[words[4]] = ans

    elif words[0] == "del":
        if words[1] == "str":
            del str_variable[words[2]]
        elif words[1] == "int":
            del int_variable[words[2]]
        else:
            print(f"CommandError: Variable '{words[2]}' not found.")

    elif words[0] == "copy":
        if words[1] == "str":
            copyVariableNameA = str_variable[words[2]]
            str_variable[words[3]] = copyVariableNameA

        elif words[1] == "int":
            copyVariableNameA = int_variable[words[2]]
            int_variable[words[3]] = copyVariableNameA

    elif words[0] == "showAll":
        print("\nString Variables:\n")
        for key, value in str_variable.items():
            print(f"- {key} : {value}")
        print("\nInteger Variables:\n")
        for key, value in int_variable.items():
            print(f"- {key} : {value}")
        print("\n")

    elif words[0] == "file":
        if words[1] == "r":
            f = open(words[2], 'r')
            data = f.read()
            print(data)
            f.close()
        elif words[1] == "w":
            f = open(words[2], 'w')
            if words[3] == "str":
                val_name = str_variable[words[4]]
                f.write(val_name+"\n")
                f.close()
            elif words[3] == "int":
                val_name = int_variable[words[4]]
                f.write(val_name+"\n")
                f.close()
        elif words[1] == "a":
            f = open(words[2], 'a')
            if words[3] == "str":
                val_name = str_variable[words[4]]
                f.write(val_name+"\n")
                f.close()
            elif words[3] == "int":
                val_name = int_variable[words[4]]
                f.write(val_name+"\n")
                f.close()
    else:
        print(f"CommandError: Invalid keyword: '{words[0]}'.")


if __name__ == "__main__":
    file_name = sys.argv[1]
    run_program(file_name)
