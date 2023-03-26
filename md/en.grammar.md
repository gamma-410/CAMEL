# A Tour of CAMEL
CAMEL (Computation And Mathematics Expression Language) is a programming language developed for performing simple mathematical calculations.

## CAMEL Code Declaration
When starting to write code in CAMEL, the following declaration is necessary:
```css
@camelCode
```

## Types
CAMEL has two types: "string" and "integer".
- "String" is represented as "str".
- "Integer" is represented as "int".

## Variable Declaration
Declare a variable and assign an initial value to it. The value can be an integer or the value of another variable.
```bash
let variable_name type = value
```

## Variable Deletion
Delete the data of a variable.
```css
del type variable_name
```

## Variable Duplication
Duplicate the data of a variable to another variable.
```go
copy type original_variable_name duplicated_variable_name
```

## Input
Input a value from the keyboard and assign it to a variable. The input value becomes the specified type.
```arduino
get variable_name type message
```

## Output
Display the value of a variable.
```bash
show type variable_name
```

## Arithmetic Operations
Perform arithmetic operations on variable_name1 and variable_name2, and assign the result to a specified variable.
```java
+ variable_name1 variable_name2 = result_variable_name
- variable_name1 variable_name2 = result_variable_name
* variable_name1 variable_name2 = result_variable_name
/ variable_name1 variable_name2 = result_variable_name
% variable_name1 variable_name2 = result_variable_name
```

## Output All Variables
Output string-type and integer-type variables respectively.
```
showAll
```

## File Operations
The argument can be "r", "w", or "a".  
"r" is used for reading. The entire file is output.  
"w" and "a" can be used for writing. The difference is whether to save completely or save with additional content.  
The data to be written to the file is assigned to a variable and then used.  
```bash
file argument file_name
file argument file_name type variable_name
```

## Commenting
Lines starting with "!" are commented out. Commented-out lines are not executed.
```diff
! comment
```

## Error Handling
If there is an error in the CAMEL program, an error message is displayed.

- Declaration error
- Type error
- Variable error
- Command error