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
MAX_VELOCITY = 8
BIN_WIDTH = 0.4
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
        crazy_guy_x, crazy_guy_y = convert_xy_to_system_reference(virtual_player_data[i][1], virtual_player_data[i][2], False)
        crazy_guy_x_next, crazy_guy_y_next = convert_xy_to_system_reference(virtual_player_data[i+1][1], virtual_player_data[i+1][2], False)
        distance = np.sqrt((crazy_guy_x - crazy_guy_x_next)**2 + (crazy_guy_y - crazy_guy_y_next)**2)
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

    vel = [vel_crazy_guy, vel_player_1, vel_player_6, vel_player_11]
    vel_label = ["PDF del loco", "PDF del Jugador 1", "PDF del Jugador 6", "PDF del Jugador 11"]

    fig, ax = plt.subplots()

    for i in range(len(vel)):
        bins = np.arange(0, np.max(vel[i]) + BIN_WIDTH, BIN_WIDTH)
        hist, bin_edges = np.histogram(vel[i], bins=bins, density=True)
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
        # plt.bar(bin_centers, hist, width=BIN_WIDTH, alpha=0.5)
        plt.plot(bin_centers, hist, marker='o', linestyle='-', label=vel_label[i])

    ax.set_xlabel("Velocidad $\\left( m/s \\right)$", fontdict={"weight": "bold"})
    ax.set_ylabel("Densidad de probabilidad $\\left( s \\right)$", fontdict={"weight": "bold"})
    plt.xlim(0, MAX_VELOCITY)
    plt.yscale("log")
    ax.legend()
    plt.show()
