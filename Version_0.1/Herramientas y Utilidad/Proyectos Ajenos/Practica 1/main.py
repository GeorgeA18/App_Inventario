import tkinter as tk
import ventana



def main():
    root = tk.Tk()
    root.wm_title("Crud python Mysql")

    app = ventana.Ventana(root)
    app.mainloop()





if __name__ == "__main__":
    main()