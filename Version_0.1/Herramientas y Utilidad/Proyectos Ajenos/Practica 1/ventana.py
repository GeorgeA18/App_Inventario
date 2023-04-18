import tkinter as tk
# from tkinter import tkk
from tkinter import ttk



class Ventana(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master, width = 680,height = 260)
        self.master = master
        self.pack()
        self.create_widgets()

    # Este emtodo se llama la presionar el boton btnuevo,
    def fNuevo(self):
        pass

    def fModificar(self):
        pass

    def fEliminar(self):
            pass
    def fGuardar(self):
            pass
    def fCancelar(self):
            pass




    def create_widgets(self):
        self.create_frame1()
        self.create_frame2()
        self.create_treeView()



    
    def create_frame1(self):
        # Creando el frame de lso botones
        frame1 = tk.Frame(self, bg = "#bfdaff")
        frame1.place(x=0,y=0, width=93,height=259)


        #  Creando los botones
        self.btnNuevo = tk.Button(frame1,text="Nuevo", command=self.fNuevo, bg="blue",fg="white")
        self.btnNuevo.place(x=5,y=50,width=80,height=30)

        self.btnNuevo = tk.Button(frame1,text="Modificar", command=self.fModificar, bg="blue",fg="white")
        self.btnNuevo.place(x=5,y=90,width=80,height=30)

        self.btnNuevo = tk.Button(frame1,text="Eliminar", command=self.fEliminar, bg="blue",fg="white")
        self.btnNuevo.place(x=5,y=130,width=80,height=30)


    def create_frame2(self):
        # Creando el frame de lso botones
        frame2 = tk.Frame(self, bg = "#d3dde3")
        frame2.place(x=95,y=0, width=150,height=259)


        labl1 = tk.Label(frame2,text="ISO3:")
        labl1.place(x=3,y=5)
        self.txtISO3=tk.Entry(frame2)
        self.txtISO3.place(x=3,y=25,width=50,height=20)

        labl2 = tk.Label(frame2,text="Country Name:")
        labl2.place(x=3,y=55)
        self.textCountryName=tk.Entry(frame2)
        self.textCountryName.place(x=3,y=75,width=50,height=20)

        labl3 = tk.Label(frame2,text="Capital:")
        labl3.place(x=3,y=105)
        self.txtCapital=tk.Entry(frame2)
        self.txtCapital.place(x=3,y=125,width=50,height=20)

        labl4 = tk.Label(frame2,text="Currency Code:")
        labl4.place(x=3,y=155)
        self.txtCapital=tk.Entry(frame2)
        self.txtCapital.place(x=3,y=175,width=50,height=20)


        self.btnGuardar = tk.Button(frame2,text="Guardar", command=self.fGuardar, bg="green",fg="white")
        self.btnGuardar.place(x=10,y=210,width=60,height=30)

        self.btnCancela = tk.Button(frame2,text="Cancelar", command=self.fCancelar, bg="red",fg="white")
        self.btnCancela.place(x=80,y=210,width=60,height=30)

    


    def create_treeView(self):
        self.grid = ttk.Treeview(self,columns = ("col1","col2","col3","col4"))
        
        self.grid.column("#0",width=50)
        self.grid.column("col1",width=60, anchor=tk.CENTER)
        self.grid.column("col2",width=90, anchor=tk.CENTER)
        self.grid.column("col3",width=90, anchor=tk.CENTER)
        self.grid.column("col4",width=90, anchor=tk.CENTER)


        self.grid.heading("#0",text="Id",anchor=tk.CENTER)
        self.grid.heading("col1",text="ISO3",anchor=tk.CENTER)
        self.grid.heading("col2",text="Country Name",anchor=tk.CENTER)
        self.grid.heading("col3",text="Capital",anchor=tk.CENTER)
        self.grid.heading("col4",text="Currency Code",anchor=tk.CENTER)

        self.grid.place(x=247,y=0,width=420,height=259)

        self.grid.insert("",tk.END,text="1", values=("ARG", "Argentina", "Buenos Aires", "ARS"))
