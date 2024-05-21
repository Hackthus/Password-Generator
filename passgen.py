import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import string
import random


class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Welcome User  :)")
        self.geometry("800x500")
     #   self.configure(background="white")  # Définir le fond de la fenêtre en blanc

        self.create_widgets()

    def create_widgets(self):
        l_minuscules = "azertyuiopqsdfghjklmwxcvbn"
        l_majuscules = string.ascii_uppercase
        chiffres = string.digits
        special_char = string.punctuation

        def generate_password():
            use_majuscule = majuscule_var.get()
            use_minuscule = minuscule_var.get()
            use_chiffres = chiffres_var.get()
            use_ponctuation = ponctuation_var.get()
            longueur_pass = longueur_pass_entry.get()

            char = ""
            if use_majuscule:
                char += l_majuscules
            if use_minuscule:
                char += l_minuscules
            if use_chiffres:
                char += chiffres
            if use_ponctuation:
                char += special_char

            if char == "":
                messagebox.showerror("Erreur", "Vous devez sélectionner au moins un type de caractère.")
                return

            try:
                longueur_pass = int(longueur_pass)
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer un nombre entier pour la longueur du mot de passe.")
                return

            mdp = "".join(random.choices(char, k=longueur_pass))
            password_output.delete(0, tk.END)
            password_output.insert(tk.END, mdp)

        def quit_app():
            self.quit()

        def copy_password():
            password = password_output.get()
            self.clipboard_clear()
            self.clipboard_append(password)
            messagebox.showinfo("Copié", "Mot de passe copié dans le presse-papiers.")

        password_generator_frame = tk.Frame(self, bg="white")  # Fond blanc pour le cadre du générateur de mot de passe
        password_generator_frame.pack(pady=20)
 
        majuscule_var = tk.BooleanVar(value=True)
        minuscule_var = tk.BooleanVar(value=True)
        chiffres_var = tk.BooleanVar(value=True)
        ponctuation_var = tk.BooleanVar(value=False)

        majuscule_check = tk.Checkbutton(password_generator_frame, text="Lettres Majuscules", variable=majuscule_var, bg="white")  
        majuscule_check.grid(row=1, column=0, sticky="w")

        minuscule_check = tk.Checkbutton(password_generator_frame, text="Lettres Minuscules", variable=minuscule_var, bg="white")  
        minuscule_check.grid(row=2, column=0, sticky="w")

        chiffres_check = tk.Checkbutton(password_generator_frame, text="Chiffres", variable=chiffres_var, bg="white")  
        chiffres_check.grid(row=3, column=0, sticky="w")

        ponctuation_check = tk.Checkbutton(password_generator_frame, text="Caractères Spéciaux", variable=ponctuation_var, bg="white")  
        ponctuation_check.grid(row=4, column=0, sticky="w")

        longueur_pass_label = tk.Label(password_generator_frame, text="Longueur du mot de passe :", bg="white")  
        longueur_pass_label.grid(row=5, column=0, pady=(10, 0), sticky="w")

        longueur_pass_entry = tk.Entry(password_generator_frame)
        longueur_pass_entry.grid(row=6, column=0, pady=(0, 10))

        generate_button = tk.Button(password_generator_frame, text="Générer", command=generate_password, bg="blue", fg="white")  
        generate_button.grid(row=7, column=0, pady=(10, 0))

        password_output_label = tk.Label(password_generator_frame, text="Mot de passe généré :", bg="white")  
        password_output_label.grid(row=8, column=0, pady=(20, 0), sticky="w")

        password_output = tk.Entry(password_generator_frame, width=50)
        password_output.grid(row=9, column=0, pady=(0, 20))

        # Bouton pour copier le mot de passe
        copy_button = tk.Button(password_generator_frame, text="Copier le mot de passe", command=copy_password, bg="green", fg="white")
        copy_button.grid(row=10, column=0, pady=(10, 0))

        # Ajouter le message en bas de la fenêtre
        bottom_label = tk.Label(self, text="By H@ckthus, Email: hackthus@gmail.com", bg="white", fg="blue")  
        bottom_label.pack(side="bottom", pady=10)

        #  bouton rouge pour quitter l'application
        quit_button = tk.Button(self, text="Quitter", command=quit_app, bg="red", fg="white") 
        quit_button.pack(side="bottom", pady=10)


if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()
