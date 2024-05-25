import csv
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

########### CONSTANT VARIABLES ###########
VIRTUAL_PLAYER_FILENAME = "output.txt"
HOME_FILENAME = "TrackingData_Local.csv"
AWAY_FILENAME = "TrackingData_Visitante.csv"
LIMIT_X = 105
LIMIT_Y = 68
START_PLAYERS_INDEX = 1433
END_PLAYERS_INDEX = 4446
MAX_VELOCITY = 5.5
##########################################


def convert_xy_to_system_reference(x_arg, y_arg, multiply=True):
    x, y = float(x_arg), float(y_arg)
    if multiply:
        x = x * LIMIT_X
        y = y * LIMIT_Y
    return x, LIMIT_Y - y


with (open(os.path.join(os.path.dirname(__file__), "..", f"{VIRTUAL_PLAYER_FILENAME}")) as virtual_player_file,
      open(os.path.join(os.path.dirname(__file__), "..", f"{HOME_FILENAME}")) as home_file,
      open(os.path.join(os.path.dirname(__file__), "..", f"{AWAY_FILENAME}")) as away_file):

    virtual_player_data = list(csv.reader(virtual_player_file, delimiter=" "))
    home_data = list(csv.reader(home_file, delimiter=","))[START_PLAYERS_INDEX:END_PLAYERS_INDEX]
    away_data = list(csv.reader(away_file, delimiter=","))[START_PLAYERS_INDEX:END_PLAYERS_INDEX]

    # Entre cada i e i+1, calcular la distancia entre el jugador y la pelota
    vel_crazy_guy = []
    for i in range(len(virtual_player_data) - 1):
        distance = np.sqrt((float(virtual_player_data[i][1]) - float(virtual_player_data[i+1][1]))**2 +
                              (float(virtual_player_data[i][2]) - float(virtual_player_data[i+1][2]))**2)
        vel_crazy_guy.append(distance/0.04)

    # Tomare los jugadores 1, 6 y 11 del equipo local

    vel_player_1 = []
    vel_player_6 = []
    vel_player_11 = []
    for i in range(len(home_data) - 1):
        p1_x, p1_y = convert_xy_to_system_reference(home_data[i][5], home_data[i][6])
        p1_x_next, p1_y_next = convert_xy_to_system_reference(home_data[i+1][5], home_data[i+1][6])
        distance_p1 = np.sqrt((p1_x - p1_x_next)**2 + (p1_y - p1_y_next)**2)

        p6_x, p6_y = convert_xy_to_system_reference(home_data[i][15], home_data[i][16])
        p6_x_next, p6_y_next = convert_xy_to_system_reference(home_data[i+1][15], home_data[i+1][16])
        distance_p6 = np.sqrt((p6_x - p6_x_next)**2 + (p6_y - p6_y_next)**2)

        p11_x, p11_y = convert_xy_to_system_reference(home_data[i][3], home_data[i][4])
        p11_x_next, p11_y_next = convert_xy_to_system_reference(home_data[i+1][3], home_data[i+1][4])
        distance_p11 = np.sqrt((p11_x - p11_x_next)**2 + (p11_y - p11_y_next)**2)

        vel_player_1.append(distance_p1/0.04)
        vel_player_6.append(distance_p6/0.04)
        vel_player_11.append(distance_p11/0.04)

    velocities_crazy_guy = [v for v in vel_crazy_guy if v <= MAX_VELOCITY]
    velocities_player_1 = [v for v in vel_player_1 if v <= MAX_VELOCITY]
    velocities_player_6 = [v for v in vel_player_6 if v <= MAX_VELOCITY]
    velocities_player_11 = [v for v in vel_player_11 if v <= MAX_VELOCITY]

    # Estimación de la densidad de kernel
    kde_1 = gaussian_kde(velocities_crazy_guy, bw_method='scott')
    kde_2 = gaussian_kde(velocities_player_1, bw_method='scott')
    kde_3 = gaussian_kde(velocities_player_6, bw_method='scott')
    kde_4 = gaussian_kde(velocities_player_11, bw_method='scott')

    # Calcular el número de puntos usando la regla de Sturges redondeando hacia arriba
    n_bins_crazy_guy = int(np.ceil(np.log2(len(velocities_crazy_guy)) + 1))
    n_bins_player_1 = int(np.ceil(np.log2(len(velocities_player_1)) + 1))
    n_bins_player_6 = int(np.ceil(np.log2(len(velocities_player_6)) + 1))
    n_bins_player_11 = int(np.ceil(np.log2(len(velocities_player_11)) + 1))

    # Valores para evaluar la PDF uniformemente
    x_vals_crazy_guy = np.linspace(0, MAX_VELOCITY, n_bins_crazy_guy)
    x_vals_player_1 = np.linspace(0, MAX_VELOCITY, n_bins_player_1)
    x_vals_player_6 = np.linspace(0, MAX_VELOCITY, n_bins_player_6)
    x_vals_player_11 = np.linspace(0, MAX_VELOCITY, n_bins_player_11)

    # Calcula la PDF en los valores dados
    pdf_crazy_guy = kde_1(x_vals_crazy_guy)
    pdf_player_1 = kde_2(x_vals_player_1)
    pdf_player_6 = kde_3(x_vals_player_6)
    pdf_player_11 = kde_4(x_vals_player_11)

    fig, ax = plt.subplots()

    # Grafica la PDF
    ax.scatter(x_vals_crazy_guy, pdf_crazy_guy)
    ax.scatter(x_vals_player_1, pdf_player_1)
    ax.scatter(x_vals_player_6, pdf_player_6)
    ax.scatter(x_vals_player_11, pdf_player_11)

    ax.plot(x_vals_crazy_guy, pdf_crazy_guy, label='PDF del loco')
    ax.plot(x_vals_player_1, pdf_player_1,  label='PDF del jugador 1')
    ax.plot(x_vals_player_6, pdf_player_6, label='PDF del jugador 6')
    ax.plot(x_vals_player_11, pdf_player_11, label='PDF del jugador 11')

    ax.set_xlabel("Velocidad$\\left( m/s \\right)$", fontdict={"weight": "bold"})
    ax.set_ylabel("Densidad de probabilidad $\\left( s \\right)$", fontdict={"weight": "bold"})
    ax.legend()
    plt.xlim(0, MAX_VELOCITY)
    plt.show()

