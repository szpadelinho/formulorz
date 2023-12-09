import tkinter as tk
from PIL import Image, ImageTk

win = tk.Tk()
win.title("Formularz zgłoszeniowy do MAFII™©®")
win.minsize(width=600, height=800)

img = Image.open("hard.png")
img2 = img.resize((669, 800))
img3 = ImageTk.PhotoImage(img2)

obraz = tk.Label(win, image=img3)
obraz.place(x=0, y=0)

radio_state = tk.StringVar()
radio_state2 = tk.StringVar()
radio_state3 = tk.StringVar()
check_state = tk.IntVar()
check_state2 = tk.IntVar()
check_state3 = tk.IntVar()
check_state4 = tk.IntVar()

class Header(tk.Label):
    def __init__(self, text, kolumna, rzad):
        super().__init__(win, text=text, font=(("Arial", 10)))
        self.grid(column=kolumna, row=rzad, padx=5, pady=5)

class HeaderTitle(tk.Label):
    def __init__(self, text, kolumna, rzad):
        super().__init__(win, text=text, font=(("Arial", 24)))
        self.grid(column=kolumna, row=rzad, padx=5, pady=5)

class Input(tk.Text):
    def __init__(self, height, width, kolumna, rzad):
        super().__init__(win, height=height, width=width)
        self.grid(column=kolumna, row=rzad, padx=5, pady=5)

class Wybieralka(tk.Spinbox):
    def __init__(self, from_, to, width, kolumna, rzad):
        super().__init__(win, from_=from_, to=to, width=width)
        self.grid(column=kolumna, row=rzad, padx=5, pady=5)

class Radio(tk.Radiobutton):
    def __init__(self, text, value, kolumna, rzad, variable):
        super().__init__(win, text=text, value=value, variable=variable)
        self.grid(column=kolumna, row=rzad, padx=5)

class Skala(tk.Scale):
    def __init__(self, from_, to, orient, kolumna, rzad):
        super().__init__(win, from_=from_, to=to, orient=orient)
        self.grid(column=kolumna, row=rzad, padx=5, pady=5)

class Check(tk.Checkbutton):
    def __init__(self, text, kolumna, rzad, variable):
        super().__init__(win, text=text, variable=variable)
        self.grid(column=kolumna, row=rzad, padx=5)

class Przycisk(tk.Button):
    def __init__(self, text, kolumna, rzad, command):
        super().__init__(win, text=text, command=command)
        self.grid(column=kolumna, row=rzad, padx=5, pady=5)

def send_data():
    f = open("dane.txt", "a")
    f.write(f"DANE PRZESŁANE PRZEZ FORMULARZ:\nimię: {name.get('1.0', tk.END)},\nnazwisko: {surname.get('1.0', tk.END)},\nwiek: {age.get()},\npłeć: {radio_state.get()},\nnumer telefonu: {skala.get()},\nzainteresowania: ser - {check_state.get()}, pizza - {check_state2.get()}, The Sopranos - {check_state3.get()}, Serie A - {check_state4.get()},\nObsługa broni: {radio_state2.get()},\nObsługa pojazdów: {radio_state3.get()},\ndodatkowe uwagi młodego mafiozo: {info.get('1.0', tk.END)},\noficjalny podpis: {autograph.get('1.0', tk.END)}\nJak jest sztywnym gitem to przyjąć")
    f.close()

HeaderTitle(text="Formulorz", kolumna=1, rzad=0)

Header(text="Podaj swoje imię: ", kolumna=0, rzad=1)
name = Input(height=1, width=30, kolumna=1, rzad=1)

Header(text="Podaj swoje nazwisko: ", kolumna=0, rzad=2)
surname = Input(height=1, width=30, kolumna=1, rzad=2)

Header(text="Podaj swój wiek: ", kolumna=0, rzad=3)
age = Wybieralka(from_=0, to=1738, width=5, kolumna=1, rzad=3)

Header(text="Podaj płeć: ", kolumna=0, rzad=4)
Radio(text="Mężczyzna", value="Mężczyzna", kolumna=1, rzad=4, variable=radio_state)

Header(text="Twój numer telefonu (musimy się skontaktować): ", kolumna=0, rzad=5)
skala = Skala(from_=111111111, to=999999999, orient="horizontal", kolumna=1, rzad=5)

Header(text="Co z powyższych rzeczy lubisz? ", kolumna=0, rzad=6)
Check(text="Ser", kolumna=1, rzad=6, variable=check_state)
Check(text="Pizza", kolumna=1, rzad=7, variable=check_state2)
Check(text="The Sopranos", kolumna=1, rzad=8, variable=check_state3)
Check(text="Serie A", kolumna=1, rzad=9, variable=check_state4)

Header(text="Czy potrafisz posługiwać się bronią? ", kolumna=0, rzad=10)
Radio(text="Tak", value="Potrafi posługiwać się bronią", kolumna=1, rzad=10, variable=radio_state2)
Radio(text="Szybko się uczę", value="Potrafi szybko nauczyć się posługiwać bronią", kolumna=1, rzad=11, variable=radio_state2)

Header(text="Czy potrafisz prowadzić pojazdy? (np. lądowe, wodne, powietrzne) ", kolumna=0, rzad=12)
Radio(text="Tak", value="Potrafi sprostać każdemu pojazdowi", kolumna=1, rzad=12, variable=radio_state3)
Radio(text="Szybko się uczę", value="Potrafi szybko nauczyć się prowadzić pojazdy", kolumna=1, rzad=13, variable=radio_state3)

Header(text="Twoje dodatkowe uwagi dla zarządu MAFII™©®", kolumna=0, rzad=14)
info = Input(height=5, width=30, kolumna=1, rzad=14)

Header(text="Oficjalnie oświadczam, iż dane wprowadzone przez\n moją osobę w formularzu są prawdziwe,\n a podanie jest składane w autentycznym celu.\n Zobowiązuje się do kultu oraz bezgranicznej pomocy dla MAFII™©®\n oraz przestrzeganie każdego z poleceń\n Szanownego Pana Tony'ego Soprano.", kolumna=0, rzad=16)
autograph = Input(height=1, width=30, kolumna=1, rzad=16)

Przycisk(text="Wyślij", kolumna=1, rzad=18, command=send_data)

win.mainloop()