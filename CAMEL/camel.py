import sys

CAMEL_CODE_DECLARATION = "@camelCode"

str_variable = {}
int_variable = {}

# 型チェック関数
def TypeCheck(typeA, typeB):
    if str(typeA) == str(typeB):
        return True
    else:
        return False

# コマンド関数
def Get(variable_name, type, message):
    if TypeCheck("str", type):
        input_var = input(message)
        str_variable[variable_name] = str(input_var)
    elif TypeCheck("int", type):
        input_var = input(message)
        int_variable[variable_name] = int(input_var)
    else:
        print(f"TypeError: Type '{ type }' not found.")


def Show(type, variable_name):
    if TypeCheck("str", type):
        print(str_variable[variable_name])
    elif TypeCheck("int", type):
        print(int_variable[variable_name])
    else:
        print(f"TypeError: Type '{ type }' not found.")


def Let(variable_name, type, value):
    if TypeCheck("str", type):
        str_variable[variable_name] = str(value)
    elif TypeCheck("int", type):
        int_variable[variable_name] = int(value)
    else:
        print(f"TypeError: Type '{ type }' not found.")


def Math(operator, variable_name1, variable_name2, result_variable_name):
    if operator == "+":
        answer = int_variable[variable_name1] + int_variable[variable_name2]
    elif operator == "-":
        answer = int_variable[variable_name1] - int_variable[variable_name2]
    elif operator == "*":
        answer = int_variable[variable_name1] * int_variable[variable_name2]
    elif operator == "/":
        answer = int_variable[variable_name1] / int_variable[variable_name2]
    elif operator == "%":
        answer = int_variable[variable_name1] % int_variable[variable_name2]
    else:
        print(f"OperatorError: Operator '{ operator }' not found.")

    int_variable[result_variable_name] = answer


def Delete(type, variable_name):
    if TypeCheck("str", type):
        del str_variable[variable_name]
    elif TypeCheck("int", type):
        del int_variable[variable_name]
    else:
        print(f"TypeError: Type '{ type }' not found.")


def Copy(type, original_variable_name, duplicated_variable_name):
    if TypeCheck("str", type):
        str_variable[duplicated_variable_name] = str_variable[original_variable_name]
    elif TypeCheck("int", type):
        int_variable[duplicated_variable_name] = int_variable[original_variable_name]
    else:
        print(f"TypeError: Type '{ type }' not found.")


def ShowAll():
    print("\nString Variables:\n")
    for key, value in str_variable.items():
        print(f"- {key} : {value}")
    print("\nInteger Variables:\n")
    for key, value in int_variable.items():
        print(f"- {key} : {value}")
    print("\n")


def File(argument, file_name, type, variable_name):
    if argument == "r":
        f = open(file_name, "r")
        data = f.read()
        print(data)
        f.close()
    elif argument == "w":
        f = open(file_name, "w")
        if TypeCheck("str", type):
            val_name = str_variable[variable_name]
            f.write(val_name+"\n")
            f.close()
        elif TypeCheck("int", type):
            val_name = str(int_variable[variable_name])
            f.write(val_name+"\n")
            f.close()
        else:
            print(f"TypeError: Type '{ type }' not found.")
    elif argument == "a":
        f = open(file_name, "a")
        if TypeCheck("str", type):
            val_name = str_variable[variable_name]
            f.write(val_name+"\n")
            f.close()
        elif TypeCheck("int", type):
            val_name = str(int_variable[variable_name])
            f.write(val_name+"\n")
            f.close()
        else:
            print(f"TypeError: Type '{ type }' not found.")

# ファイル読み込み
def run_program(file_name):
    with open(file_name) as f:
        first_line = f.readline()
        if not first_line.startswith(CAMEL_CODE_DECLARATION):
            print("DeclarationError: Invalid program declaration.")
            return

        for line in f:
            execute_line(line.strip())


# 処理まとめるくん
def execute_line(line):
    if not line:
        return

    words = line.split()

    if words[0] == "!":
        return
    elif words[0] == "get":
        Get(words[1], words[2], words[3])
    elif words[0] == "show":
        Show(words[1], words[2])
    elif words[0] == "let":
        Let(words[1], words[2], words[4])
    elif words[0] in ["+", "-", "*", "/", "%"]:
        Math(words[0], words[1], words[2], words[4])
    elif words[0] == "del":
        Delete(words[1], words[2])
    elif words[0] == "copy":
        Copy(words[1], words[2], words[3])
    elif words[0] == "showAll":
        ShowAll()
    elif words[0] == "file":
        if words[1] == "r":
            File(words[1], words[2], None, None)
        elif words[1] == "w":
            File(words[1], words[2], words[3], words[4])
        elif words[1] == "a":
            File(words[1], words[2], words[3], words[4])
        else:
            print(f"ArgumentError: Argument '{ words[1] }' not found.")

    else:
        print(f"CommandError: Invalid keyword: '{words[0]}'.")


if __name__ == "__main__":
    file_name = sys.argv[1]
    run_program(file_name)
