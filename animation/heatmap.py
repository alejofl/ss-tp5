import csv
import os
import numpy as np
import matplotlib.pyplot as plt

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

    crazy_guy_data = list(csv.reader(virtual_player_file, delimiter=" "))
    home_data = list(csv.reader(home_file, delimiter=","))[START_PLAYERS_INDEX:END_PLAYERS_INDEX]
    away_data = list(csv.reader(away_file, delimiter=","))[START_PLAYERS_INDEX:END_PLAYERS_INDEX]

    print(home_data[0][2])
    print(home_data[-1][2])

    total_seconds = float(home_data[-1][2]) - float(home_data[0][2])
    total_minutes = total_seconds / 60.0
    print(total_seconds)

    # # Primero nos piden el heat map para todos los jugadores sin distinción en el tiempo de estudio que definimos
    # # Para el equipo local tenemos los indices -> 3 - 24 | Para los visitantes también
    # data = []
    # for i in range(len(home_data)):
    #     for j in range(3, 25, 2):
    #         home_x, home_y = convert_xy_to_system_reference(home_data[i][j], home_data[i][j+1])
    #         away_x, away_y = convert_xy_to_system_reference(away_data[i][j], away_data[i][j+1])
    #         data.append((home_x, home_y))
    #         data.append((away_x, away_y))
    #
    #
    # plt.rcParams.update({'font.size': 20})
    # fig, ax = plt.subplots()
    #
    # # Crear un histograma 2D de las posiciones de los jugadores con celdas de 1x1
    # # 1x1
    # # div = 1
    # # Medidas/1.5
    # # div = 1.5
    # # Medidas/1.8
    # # div = 1.8
    # # Medidas/2
    # div = 2
    #
    # heatmap, xedges, yedges = np.histogram2d(np.array(data)[:, 0], np.array(data)[:, 1], bins=[int(np.ceil(LIMIT_X/div)), int(np.ceil(LIMIT_Y/div))], range=[[0, LIMIT_X], [0, LIMIT_Y]])
    #
    # # Normalizar el heatmap por minuto
    # heatmap_per_minute = heatmap / total_minutes
    #
    # # Dibujar el mapa de calor con diferentes colores
    # # plt.imshow(heatmap.T, cmap='tab20', extent=[0, 105, 0, 68], origin='lower', aspect='auto')
    # # plt.imshow(heatmap.T, cmap='hot', extent=[0, 105, 0, 68], origin='lower', aspect='auto')
    # # plt.imshow(heatmap.T, cmap='summer', extent=[0, 105, 0, 68], origin='lower', aspect='auto')
    # # plt.imshow(heatmap.T, cmap='gist_rainbow', extent=[0, 105, 0, 68], origin='lower', aspect='auto')
    # cax = plt.imshow(heatmap_per_minute.T, cmap='plasma', extent=[0, LIMIT_X, 0, LIMIT_Y], origin='lower', aspect='auto')
    # colorbar = fig.colorbar(cax, ax=ax, location='right')
    # colorbar.set_label('Visitas por minuto', rotation=270, labelpad=20, fontdict={"weight": "bold"})
    #
    # ax.set_xlabel("X", fontdict={"weight": "bold"})
    # ax.set_ylabel("Y", fontdict={"weight": "bold"})
    #
    # plt.show()

    # --------------------------------------------------------------------------------------------

    # Para los 3 jugadores que me interesan y el loco

    # # El loco
    # data = []
    # for i in range(len(crazy_guy_data)):
    #     x, y = convert_xy_to_system_reference(crazy_guy_data[i][1], crazy_guy_data[i][2], False)
    #     data.append((x, y))
    #
    # plt.rcParams.update({'font.size': 20})
    # fig, ax = plt.subplots()
    #
    # # Crear un histograma 2D de las posiciones de los jugadores con celdas de 1x1
    # div = 2
    #
    # heatmap, xedges, yedges = np.histogram2d(np.array(data)[:, 0], np.array(data)[:, 1], bins=[int(np.ceil(LIMIT_X/div)), int(np.ceil(LIMIT_Y/div))], range=[[0, LIMIT_X], [0, LIMIT_Y]])
    #
    # heatmap_per_minute = heatmap / total_minutes
    #
    # # Dibujar el mapa de calor con diferentes colores
    # cax = plt.imshow(heatmap_per_minute.T, cmap='plasma', extent=[0, LIMIT_X, 0, LIMIT_Y], origin='lower', aspect='auto')
    # colorbar = fig.colorbar(cax, ax=ax, location='right')
    # colorbar.set_label('Visitas por minuto', rotation=270, labelpad=20, fontdict={"weight": "bold"})
    #
    # ax.set_xlabel("X", fontdict={"weight": "bold"})
    # ax.set_ylabel("Y", fontdict={"weight": "bold"})
    #
    # plt.show()
    # #--------------------------------------------------------------------------------------------


    # # Jugador 1
    # data = []
    # for i in range(len(home_data)):
    #     for j in range(5, 7, 2):
    #         home_x, home_y = convert_xy_to_system_reference(home_data[i][j], home_data[i][j+1])
    #         data.append((home_x, home_y))
    #
    # plt.rcParams.update({'font.size': 20})
    # fig, ax = plt.subplots()
    #
    # # Crear un histograma 2D de las posiciones de los jugadores con celdas de 1x1
    # div = 2
    #
    # heatmap, xedges, yedges = np.histogram2d(np.array(data)[:, 0], np.array(data)[:, 1], bins=[int(np.ceil(LIMIT_X/div)), int(np.ceil(LIMIT_Y/div))], range=[[0, LIMIT_X], [0, LIMIT_Y]])
    #
    # heatmap_per_minute = heatmap / total_minutes
    #
    # # Dibujar el mapa de calor con diferentes colores
    # cax = plt.imshow(heatmap_per_minute.T, cmap='plasma', extent=[0, LIMIT_X, 0, LIMIT_Y], origin='lower', aspect='auto')
    # colorbar = fig.colorbar(cax, ax=ax, location='right')
    # colorbar.set_label('Visitas por minuto', rotation=270, labelpad=20, fontdict={"weight": "bold"})
    #
    # ax.set_xlabel("X", fontdict={"weight": "bold"})
    # ax.set_ylabel("Y", fontdict={"weight": "bold"})
    #
    # plt.show()
    # #--------------------------------------------------------------------------------------------


    # # Jugador 6
    # data = []
    # for i in range(len(home_data)):
    #     for j in range(15, 17, 2):
    #         home_x, home_y = convert_xy_to_system_reference(home_data[i][j], home_data[i][j+1])
    #         data.append((home_x, home_y))
    #
    # plt.rcParams.update({'font.size': 20})
    # fig, ax = plt.subplots()
    #
    # # Crear un histograma 2D de las posiciones de los jugadores con celdas de 1x1
    # div = 2
    #
    # heatmap, xedges, yedges = np.histogram2d(np.array(data)[:, 0], np.array(data)[:, 1], bins=[int(np.ceil(LIMIT_X/div)), int(np.ceil(LIMIT_Y/div))], range=[[0, LIMIT_X], [0, LIMIT_Y]])
    #
    # heatmap_per_minute = heatmap / total_minutes
    #
    # # Dibujar el mapa de calor con diferentes colores
    # cax = plt.imshow(heatmap_per_minute.T, cmap='plasma', extent=[0, LIMIT_X, 0, LIMIT_Y], origin='lower', aspect='auto')
    # colorbar = fig.colorbar(cax, ax=ax, location='right')
    # colorbar.set_label('Visitas por minuto', rotation=270, labelpad=20, fontdict={"weight": "bold"})
    #
    # ax.set_xlabel("X", fontdict={"weight": "bold"})
    # ax.set_ylabel("Y", fontdict={"weight": "bold"})
    #
    # plt.show()
    # #--------------------------------------------------------------------------------------------


    # # Jugador 11
    data = []
    for i in range(len(home_data)):
        for j in range(3, 4, 2):
            home_x, home_y = convert_xy_to_system_reference(home_data[i][j], home_data[i][j+1])
            data.append((home_x, home_y))

    plt.rcParams.update({'font.size': 20})
    fig, ax = plt.subplots()

    # Crear un histograma 2D de las posiciones de los jugadores con celdas de 1x1
    div = 2

    heatmap, xedges, yedges = np.histogram2d(np.array(data)[:, 0], np.array(data)[:, 1], bins=[int(np.ceil(LIMIT_X/div)), int(np.ceil(LIMIT_Y/div))], range=[[0, LIMIT_X], [0, LIMIT_Y]])

    heatmap_per_minute = heatmap / total_minutes

    # Dibujar el mapa de calor con diferentes colores
    cax = plt.imshow(heatmap_per_minute.T, cmap='plasma', extent=[0, LIMIT_X, 0, LIMIT_Y], origin='lower', aspect='auto')
    colorbar = fig.colorbar(cax, ax=ax, location='right')
    colorbar.set_label('Visitas por minuto', rotation=270, labelpad=20, fontdict={"weight": "bold"})

    ax.set_xlabel("X", fontdict={"weight": "bold"})
    ax.set_ylabel("Y", fontdict={"weight": "bold"})

    plt.show()
    # #--------------------------------------------------------------------------------------------
