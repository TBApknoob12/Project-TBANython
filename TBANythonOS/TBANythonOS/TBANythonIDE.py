import tkinter as tk

class TBANYTHONIDE:

    def __init__(self):

        self.window = tk.Tk()

        self.window.title("TBANYTHON IDE")

        

        # Text box for code

        self.code_text = tk.Text(self.window, height=20, width=50)

        self.code_text.grid(row=0, column=0, padx=5, pady=5)

        

        # Output box

        self.output_text = tk.Text(self.window, height=10, width=50)

        self.output_text.grid(row=1, column=0, padx=5, pady=5)

        

        # Button to run code

        self.run_button = tk.Button(self.window, text="Run", command=self.run_code)

        self.run_button.grid(row=2, column=0, padx=5, pady=5)

        # Button to save code

        self.save_button = tk.Button(self.window, text="Save", command=self.save_code)

        self.save_button.grid(row=3, column=0, padx=5, pady=5)

        # Button to open code

        self.open_button = tk.Button(self.window, text="Open", command=self.open_code)

        self.open_button.grid(row=4, column=0, padx=5, pady=5)

    def run_code(self):

        code = self.code_text.get("1.0", "end-1c").split()

        variables = {}

        output = []

        

        i = 1

        while i < len(code):

            if code[i].lower() == "derp":

                variables[code[i+1]] = float(code[i+2])

                i += 3

            elif code[i].lower() == "smp":

                var1 = variables[code[i+1]]

                var2 = variables[code[i+3]]

                operator = code[i+2]

                result = eval(f"{var1} {operator} {var2}")

                variables[code[i+1]] = result

                i += 4

            elif code[i].lower() == "sub":

                output.append(variables[code[i+1]])

                i += 2

            elif code[i].lower() == "if":

                var1 = variables[code[i+1]]

                var2 = variables[code[i+3]]

                operator = code[i+2]

                if eval(f"{var1} {operator} {var2}"):

                    i += 4

                else:

                    i += 5

            elif code[i].lower() == "else":

                i += 1

            elif code[i].lower() == "endif":

                i += 1

            elif code[i].lower() == "while":

                var1 = variables[code[i+1]]

                var2 = variables[code[i+3]]

                operator = code[i+2]

                while eval(f"{var1} {operator} {var2}"):

                    i += 4

                    inner_i = i

                    while inner_i < len(code) and code[inner_i].lower() != "endwhile":

                        if code[inner_i].lower() == "derp":

                            variables[code[inner_i+1]] = float(code[inner_i+2])

                            inner_i += 3

                        elif code[inner_i].lower() == "smp":

                            var1 = variables[code[inner_i+1]]

                            var2 = variables[code[inner_i+3]]

                            operator = code[inner_i+2]

                            result = eval(f"{var1} {operator} {var2}")

                            variables[code[inner_i+1]] = result

                            inner_i += 4

                        elif code[inner_i].lower() == "sub":

                            output.append(variables[code[inner_i+1]])

                            inner_i += 2

                        else:

                            inner_i += 1

                    i = inner_i + 1

                i += 5

                

        self.output_text.delete("1.0", "end")

        self.output_text.insert("1.0", "\n".join(str(val) for val in output))

    def save_code(self):

        code = self.code_text.get("1.0", "end-1c")

        with open('code.tby', 'w') as f:

            f.write(code)

    def open_code(self):

        with open('code.tby', 'r') as f:

            code = f.read()

        self.code_text.delete("1.0", "end")

        self.code_text.insert("1.0", code)

        

    def start(self):

        self.window.mainloop()

if __name__ == "__main__":

    ide = TBANYTHONIDE()

    ide.start()
