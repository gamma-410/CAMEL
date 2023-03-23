import sys

# CAMELの宣言
CAMEL_CODE_DECLARATION = "@camelCode"

# プログラミング言語のキーワード
keywords = ["input", "output", "let", "add", "sub", "mul", "div"]

# 変数を格納するための辞書
variables = {}

# プログラムを実行する関数
def run_program(file_name):
    with open(file_name, 'r') as f:
        first_line = f.readline()
        if not first_line.startswith(CAMEL_CODE_DECLARATION):
            print("Error: Invalid program declaration.")
            return
        
        for line in f:
            execute_line(line.strip())

# int の判定
def is_num(a):
    try:
        int(a)
    except:
        return False
    return True


# 1行分のコマンドを実行する関数
def execute_line(line):

    if not line:
        return
    
    # コマンドをスペースで分割
    words = line.split()

    # コマンドがコメントアウトの場合
    if words[0] == "#":
        return
    # コマンドが入力コマンドの場合
    if words[0] == "input":
        input_var = input("> ")
        variables[words[1]] = int(input_var)
    # コマンドが出力コマンドの場合
    elif words[0] == "output":
        print(variables[words[1]])
    # コマンドが変数宣言コマンドの場合
    elif words[0] == "let":
        # words[3] が 数字だっら True ... !
        if is_num(words[3]):
            variables[words[1]] = int(words[3])
        else:
            variables[words[1]] = variables[words[3]]

    # コマンドが四則演算コマンドの場合
    elif words[0] in ["add", "sub", "mul", "div"]:
        operand1 = variables[words[1]]
        operand2 = variables[words[2]]
        if words[0] == "add":
            result = operand1 + operand2
        elif words[0] == "sub":
            result = operand1 - operand2
        elif words[0] == "mul":
            result = operand1 * operand2
        elif words[0] == "div":
            result = operand1 / operand2
        variables[words[3]] = result

    # コマンドがキーワードでない場合
    else:
        print(f"Invalid keyword: {words[0]}")

if __name__ == "__main__":
    # コマンドライン引数からファイル名を取得してプログラムを実行
    file_name = sys.argv[1]
    run_program(file_name)
