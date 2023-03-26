# A Tour of CAMEL
CAMEL（Computation And Mathematics Expression Language）は、簡単な数学的計算を行うために開発されたプログラミング言語です。

## CAMEL CODE 宣言
CAMEL では、コードを書き始める時に、必ず以下の宣言が必要です。  
```css
@camelCode
```

## 型
CAMELには、"string"と"integer"の2つの型があります。
- "String"は"str"として表されます。
- "Integer"は"int"として表されます。

## 変数の宣言
変数を宣言し、初期値を代入します。値は整数または他の変数の値となります。 
```bash
let 変数名 型 = 値
```
 
## 変数の削除
変数のデータを削除します。  
```css
del 型 変数名
```

## 変数の複製
変数のデータを別の変数に複製します。 
```go
copy 型 複製元の変数名 複製する変数名 
```

## 入力
キーボードから値を入力し、変数に代入します。入力値は指定した型となります。  
```arduino
get 変数名 型 文字列
```

## 出力
変数の値を表示します。
```bash
show 型 変数名
```  

## 演算処理
変数名1と変数名2を四則演算し、結果を指定した変数に代入します。  
```java
+ 変数名1 変数名2 = 結果を格納する変数名
- 変数名1 変数名2 = 結果を格納する変数名
* 変数名1 変数名2 = 結果を格納する変数名
/ 変数名1 変数名2 = 結果を格納する変数名
% 変数名1 変数名2 = 結果を格納する変数名
```

## 全変数を出力
文字列型の変数と数値型の変数をそれぞれ出力します。
```
showAll
```

## ファイルの操作
引数には「r」「w」「a」が入ります。  
読み込みでは「r」を使用します。ファイル全体を出力します。  
書き込みでは「w」と「a」が使用できます。違いは完全に保存するか、追記保存するかです。  
ファイルに書き込むデータは変数に代入してから使用します。 
```bash
file 引数 ファイル名
file 引数 ファイル名 型 変数名
``` 

## コメントアウト
!から始まる行は、コメントアウトされます。コメントアウトされた行は、実行されません。  
```diff
! コメント文
```

## エラー処理
CAMELプログラムにエラーがあった場合、エラーメッセージが表示されます。  
- 宣言エラー
- 型エラー
- 変数エラー
- コマンドエラー