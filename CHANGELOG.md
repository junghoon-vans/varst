## v1.6.0 (2023-01-12)

### Feat

- **parser**: Check if substitutions are provided or not

## v1.5.0 (2022-12-28)

### Feat

- **parser**: Print version of program

## v1.4.0 (2022-12-27)

### Feat

- **parser**: Allow more than one equals sign

## v1.3.0 (2022-12-26)

### Feat

- **substitution**: Make update method pass directive_type
- **substitution**: Add directive_type method
- **substitution**: Add directive param to substitution_def method

## v1.2.1 (2022-12-22)

### Refactor

- **parser**: Update help message for substitution argument
- **parser**: Rename argument to substitutions
- Rename parameters in subsitution utils
- Rename function to create substition definition

## v1.2.0 (2022-11-28)

### Feat

- Set default value of output path as input path

### Refactor

- Change variable initialization to be done in init method
- Rename variable in parser to sub_pairs

## v1.1.2 (2022-11-26)

### Refactor

- Add missing typing to methods

## v1.1.1 (2022-11-24)

### Fix

- Resolve key error when subsitutions were finded with whitespace

## v1.1.0 (2022-11-24)

### Feat

- Update application module to replace substitutions

### Fix

- Resolve failure to get variables

### Refactor

- Update parser to change help message

## v1.0.0 (2022-11-23)

### Feat

- Drop rst_document module

## v0.5.0 (2022-11-23)

### Feat

- Add _file_type method to allow only supported file extensions
- Add update function to substitution
- Add find function to substitution
- Add substitution module to handle substitutions
- Add rst_file module to handle rst file

## v0.4.1 (2022-11-16)

### Refactor

- Rename rst module to rst_document

## v0.4.0 (2022-11-16)

### Feat

- Add save function to save documnet object as rst file
- Add replace_substitution function
- Add substitution_text function to find substitution text
- Add substitution_def_node function to find substitution_def node
- Create rst module to read input file as document

### Refactor

- Update rst.py to add missing typing

## v0.3.0 (2022-11-10)

### Feat

- Add _parse_kv function to parse key-value pair
- Add _variable_type to parser to check type of variables

### Fix

- Allow multiple character to variable type

### Refactor

- Update _VARIABLE_PATTERN to add ignore pattern
- Update print format of argument_type_error in _pattern_type function
- Create constant for pattern of variable in parser
- Update pattern in _pattern_type function to allow all of char as input
- Change parsed values so that parser object have them

## v0.2.0 (2022-11-06)

### Feat

- Add cli module for this project
- Add appliaction module
- Update parser to set default value
- Add parser for cli
