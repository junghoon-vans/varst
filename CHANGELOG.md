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
