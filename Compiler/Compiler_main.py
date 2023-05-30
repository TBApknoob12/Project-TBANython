import re

class TBANYTHONCompiler:

    def __init__(self):
        self.variables = {}

    def compile(self, tbanython_code):
        # Split the code into lines
        lines = tbanython_code.split('\n')

        # Initialize the list of Python code lines with import statements and a
        # global dictionary to store variables
        python_lines = [
            'import math',
            'import random',
            'variables = {}'
        ]

        # Process each line of TBANYTHON code
        for line in lines:
            # Remove leading/trailing whitespace and ignore blank lines
            line = line.strip()
            if not line:
                continue

            # Match "derp" statements to assign numerical values to variables
            match = re.match(r'^derp (\w+) = ([\d\.]+)$', line)
            if match:
                variable_name = match.group(1)
                variable_value = match.group(2)
                self.variables[variable_name] = variable_value
                python_lines.append(f'variables["{variable_name}"] = {variable_value}')
                continue

            # Match "smp" statements to perform arithmetic operations on variables
            match = re.match(r'^smp (\w+) (.+) (\w+) = (.+)$', line)
            if match:
                variable_name = match.group(1)
                operator = match.group(2)
                operand_name = match.group(3)
                result_variable_name = match.group(4)

                # Convert the operator symbol to a Python operator
                if operator == '+':
                    python_operator = '+'
                elif operator == '-':
                    python_operator = '-'
                elif operator == '*':
                    python_operator = '*'
                elif operator == '/':
                    python_operator = '/'
                elif operator == '%':
                    python_operator = '%'
                else:
                    raise ValueError(f'Invalid operator: {operator}')

                python_lines.append(f'{result_variable_name} = variables["{variable_name}"] {python_operator} variables["{operand_name}"]')
                python_lines.append(f'variables["{result_variable_name}"] = {result_variable_name}')
                continue

            # Match "sub" statements to print the value of a variable
            match = re.match(r'^sub (\w+)$', line)
            if match:
                variable_name = match.group(1)
                python_lines.append(f'print(variables["{variable_name}"])')
                continue

            # Match "if" statements to conditionally execute code
            match = re.match(r'^if (\w+) (.+) (\w+):$', line)
            if match:
                var1 = match.group(1)
                operator = match.group(2)
                var2 = match.group(3)
                python_lines.append(f'if variables["{var1}"] {operator} variables["{var2}"]:')
                continue
            match = re.match(r'^elif (\w+) (.+) (\w+):$', line)
            if match:
               var1 = match.group(1)
               operator = match.group(2)
               var2 = match.group(3)
               python_lines.append(f'elif variables["{var1}"] {operator} variables["{var2}"]:')
               continue

            # Match "else" statements to provide an alternative execution path
            match = re.match(r'^else:$', line)
            if match:
                python_lines.append('else:')
                continue

            # Match "endif" statements to end an "if" block
            match = re.match(r'^endif$', line)
            if match:
                python_lines.append('pass')
                continue

            # Match "while" statements to loop while a condition is true
            match = re.match(r'^while (\w+) (.+) (\w+):$', line)
            if match:
                var1 = match.group(1)
                operator = match.group(2)
                var2 = match.group(3)
                python_lines.append(f'while variables["{var1}"] {operator} variables["{var2}"]:')
                continue

            # Match "endwhile" statements to end a "while" loop
            match = re.match(r'^endwhile$', line)
            if match:
                python_lines.append('pass')
                continue
            
            # Match "for" loop statements to iterate over a range of values
            match = re.match(r'^for (\w+) in range\((\d+), (\d+)(, (\d+))?\):$', line)
            if match:
                variable_name = match.group(1)
                start_val = match.group(2)
                end_val = match.group(3)
                step = match.group(5) or '1'
                python_lines.append(f'for {variable_name} in range({start_val}, {end_val}, {step}):')
                continue
            match = re.match(r'^return (.+)$', line)
            if match:
                return_value = match.group(1)
                python_lines.append(f'return {return_value}')
                continue


            match = re.match(r'^def (\w+)\((.+)\):$', line)
            if match:
              function_name = match.group(1)
              arguments = match.group(2)
              python_lines.append(f'def {function_name}({arguments}):')
              continue


            match = re.match(r'^import (\w+)$', line)
            if match:
                module_name = match.group(1)
                python_lines.append(f'import {module_name}')
                continue
            
            # If none of the above patterns matched, raise an error
            raise ValueError(f'Invalid TBANYTHON statement: {line}')

        # Construct the final Python code by joining the lines with newlines
               # Add a final line to print the variables dictionary
        python_lines.append('print(variables)')

        # Join the Python code lines into a single string
        python_code = '\n'.join(python_lines)

        # Return the compiled Python code
        return python_code



        