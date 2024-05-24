import csv
import os
import matplotlib.pyplot as plt
import matplotlib.patches as ptchs
from PIL import Image
from matplotlib.animation import FuncAnimation, FFMpegWriter

########### CONSTANT VARIABLES ###########
VIRTUAL_PLAYER_FILENAME = "output_velocity_5.0.txt"
HOME_FILENAME = "TrackingData_Local.csv"
AWAY_FILENAME = "TrackingData_Visitante.csv"
LIMIT_X = 105
LIMIT_Y = 68
PEOPLE_RADIUS = 0.75
BALL_RADIUS = 0.5
START_PLAYERS_INDEX = 1433
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
    home_data = list(csv.reader(home_file, delimiter=","))[START_PLAYERS_INDEX:]
    away_data = list(csv.reader(away_file, delimiter=","))[START_PLAYERS_INDEX:]

    fig, ax = plt.subplots()
    court_texture = Image.open(os.path.join(os.path.dirname(__file__), "textures", "canchita.jpg"))

    def update(i):
        ax.clear()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.set_xlim(0, LIMIT_X)
        ax.set_ylim(0, LIMIT_Y)

        ax.imshow(
            court_texture,
            extent=(0, LIMIT_X,
                    0, LIMIT_Y)
        )
        ax.add_patch(ptchs.Circle((convert_xy_to_system_reference(virtual_player_data[i][1], virtual_player_data[i][2], False)), PEOPLE_RADIUS, color="fuchsia"))
        for j in range(3, 27, 2):
            if away_data[i][j] != "NaN" and away_data[i][j+1] != "NaN":
                ax.add_patch(ptchs.Circle((convert_xy_to_system_reference(away_data[i][j], away_data[i][j+1])), PEOPLE_RADIUS, facecolor="yellow", edgecolor="blue", linewidth=3))
        for j in range(3, 31, 2):
            if home_data[i][j] != "NaN" and home_data[i][j+1] != "NaN":
                ax.add_patch(ptchs.Circle((convert_xy_to_system_reference(home_data[i][j], home_data[i][j+1])), PEOPLE_RADIUS, facecolor="white", edgecolor="red", linewidth=3))
        if home_data[i][31] != "NaN" and home_data[i][32] != "NaN":
            ax.add_patch(ptchs.Circle((convert_xy_to_system_reference(home_data[i][31], home_data[i][32])), BALL_RADIUS, facecolor="white", edgecolor="black", linewidth=1.5))
        elif home_data[i][27] != "NaN" and home_data[i][28] != "NaN":
            ax.add_patch(ptchs.Circle((convert_xy_to_system_reference(away_data[i][27], away_data[i][28])) , BALL_RADIUS, facecolor="white", edgecolor="black", linewidth=1.5))
        return ax

    # Create the animation
    ani = FuncAnimation(fig, update, frames=len(virtual_player_data), blit=False, interval=1)

    # Display the animation
    plt.show()
    # Save the animation
    # ani.save("../animation.mp4", writer=FFMpegWriter(fps=30))
