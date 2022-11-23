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
