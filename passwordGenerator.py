import customtkinter as ctk
import string, random

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')

class MultiTableForm(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Table Form")
        self.geometry("400x400")
        self.title('Python Password Generator')

        # lable
        self.lable1 = ctk.CTkLabel(self, text='Enter password lenght: ')
        self.lable1.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        # Entry box
        self.len_entry = ctk.CTkEntry(self)
        self.len_entry.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

        # Choice Check boxes
        self.checkboxVar = ctk.StringVar(value="Choice 1")
        self.choice1 = ctk.CTkCheckBox(self, text="Uppercase", variable=self.checkboxVar, onvalue="upper", offvalue="c1")
        self.choice1.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        self.choice2 = ctk.CTkCheckBox(self, text="Lowercase", variable=self.checkboxVar, onvalue="lower", offvalue="c2")
        self.choice2.grid(row=1, column=1, padx=20, pady=20, sticky="ew")
        self.choice3 = ctk.CTkCheckBox(self, text="Digit", variable=self.checkboxVar, onvalue="digit", offvalue="c3")
        self.choice3.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        self.choice4 = ctk.CTkCheckBox(self, text="Special", variable=self.checkboxVar, onvalue="special", offvalue="c4")
        self.choice4.grid(row=2, column=1, padx=20, pady=20, sticky="ew")

        # Button
        self.generate = ctk.CTkButton(self, text='Generate', command=self.getinputs)
        self.generate.grid(row=3, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

        # result box
        self.displayBox = ctk.CTkTextbox(self, width=200, height=100) 
        self.displayBox.grid(row=4, column=0, columnspan=4, padx=20, pady=20, sticky="nsew")

    # logic fr generating password
    def generate_pass(self, len=12, upper=True, lower=True, digit=True, special=True):
        character = ''
        if upper:
            character += string.ascii_uppercase
        if lower:
            character += string.ascii_lowercase
        if digit:
            character += string.digits
        if special:
            character += string.punctuation

        if character:
            pasword = ''.join(random.choice(character) for _ in range(len))
            self.displayBox.insert("0.0", pasword)
        else:
            self.displayBox.insert("0.0", "Select any of the option above")
            
    # get input
    def getinputs(self):
        self.displayBox.delete("0.0", "200.0")
        try:
            len = int(self.len_entry.get())
            upper = self.choice1.get() == 'upper'
            lower = self.choice2.get() == 'lower'
            digit = self.choice3.get() == 'digit'
            special = self.choice4.get() == 'special'
            self.generate_pass(len, upper, lower, digit, special)
        except Exception as ex:
            self.displayBox.insert("0.0", "Please enter lenght of the password")

if __name__ == "__main__":
    app = MultiTableForm()
    app.mainloop()
