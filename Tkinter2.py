####### Import à soumettre ######
import pandas as pd
import sklearn
import json
import matplotlib.pyplot as plt
import seaborn as sns
import math
import tkinter as tk
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from tkinter import *

def figure_1():
    "dessiner un graphique"
    # Effacer d'abord tout dessin préexistant :
    can.delete(ALL)

    app = tk.Tk()
    app.wm_title("Graphique d'un test")

    fig = Figure(figsize=(7, 5), dpi=50)
    ax = fig.add_subplot(111)
    ax.plot(range(10), [5, 9, 2, 6, 9, 8, 7, 1, 2, 3])

    graph = FigureCanvasTkAgg(fig, master=app)
    canvas = graph.get_tk_widget()
    canvas.grid(row=0, column=0)


def figure_2():
    "Dessiner un diagramme circulaire"
    # Effacer d'abord tout dessin préexistant :
    plt.clf()
    can.delete(ALL)
    app = tk.Tk()
    fig, ax = plt.subplots()
    app.wm_title("Graphique d'un test")
    ax.axis("equal")
    ax.pie([24, 18],
    labels = ["Femmes", "Hommes"],
    autopct="%1.2f pourcents")

    graph = FigureCanvasTkAgg(fig, master=app)
    canvas = graph.get_tk_widget()
    canvas.grid(row=0, column=0)

def figure_3():
    "dessiner un histogramme"
    plt.clf()
    can.delete(ALL)
    # Clear all graphs drawn in figure
    app = tk.Tk()
    fig, ax = plt.subplots()
    data = [1,2,2,3,3,3,4,4,5]

    plt.hist(data)
    plt.title('Exemple d un histogramme', fontsize=10)

    graph = FigureCanvasTkAgg(fig, master=app)
    canvas = graph.get_tk_widget()
    canvas.grid(row=0, column=0)


##### Programme principal : ############

fen = Tk()
can = Canvas(fen, width =400, height =400, bg ='ivory')
can.pack(side =TOP, padx =5, pady =5)

b1 = Button(fen, text ='dessin 1', command =figure_1)
b1.pack(side =LEFT, padx =3, pady =3)

b2 = Button(fen, text ='dessin 3', command =figure_3)
b2.pack(side =RIGHT, padx =3, pady =3)

b3 = Button(fen, text ='dessin 2', command =figure_2)
b3.pack(side =BOTTOM, padx =3, pady =3)

fen.mainloop()
