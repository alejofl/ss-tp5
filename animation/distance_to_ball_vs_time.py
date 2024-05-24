import csv
import matplotlib.pyplot as plt
import numpy as np
import os.path


########### CONSTANT VARIABLES ###########
VIRTUAL_PLAYER_FILENAMES = ["output_velocity_{:.1f}.txt".format(x) for x in [0.1, 5, 7.5, 10, 13]]
LEGENDS = ["v = 0.1 m/s", "v = 5 m/s", "v = 7.5 m/s", "v = 10 m/s", "v = 13 m/s"]
HOME_FILENAME = "TrackingData_Local.csv"
AWAY_FILENAME = "TrackingData_Visitante.csv"
LIMIT_X = 105
LIMIT_Y = 68
START_PLAYERS_INDEX = 1433
##########################################


def convert_xy_to_system_reference(x_arg, y_arg, multiply=True):
    x, y = float(x_arg), float(y_arg)
    if multiply:
        x = x * LIMIT_X
        y = y * LIMIT_Y
    return x, LIMIT_Y - y


def distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


home_file = open(os.path.join(os.path.dirname(__file__), "..", f"{HOME_FILENAME}"))
away_file = open(os.path.join(os.path.dirname(__file__), "..", f"{AWAY_FILENAME}"))
home_data = list(csv.reader(home_file, delimiter=","))[START_PLAYERS_INDEX:]
away_data = list(csv.reader(away_file, delimiter=","))[START_PLAYERS_INDEX:]
home_file.close()
away_file.close()

ball_positions = []
for home, away in zip(home_data, away_data):
    if home[31] != "NaN" and home[32] != "NaN":
        ball_positions.append(convert_xy_to_system_reference(home[31], home[32]))
    else:
        ball_positions.append(convert_xy_to_system_reference(away[27], away[28]))

plt.rcParams.update({'font.size': 20})
fig, ax = plt.subplots()
legends = []

files = [open(os.path.join(os.path.dirname(__file__), "..", f"{filename}")) for filename in VIRTUAL_PLAYER_FILENAMES]
for file, legend in zip(files, LEGENDS):
    virtual_player_data = list(csv.reader(file, delimiter=" "))[:-1]
    file.close()

    xs = []
    ys = []
    for player, ball in zip(virtual_player_data, ball_positions):
        xs.append(float(player[0]))
        ys.append(distance(float(player[1]), float(player[2]), ball[0], ball[1]))

    line, = ax.plot(xs, ys, linewidth=2.0, label=legend)
    legends.append(line)

ax.set_xlabel("Tiempo  $\\left( s \\right)$", fontdict={"weight": "bold"})
ax.set_ylabel("Distancia loco-pelota  $\\left( m \\right)$", fontdict={"weight": "bold"})
ax.legend(handles=legends)
# ax.ticklabel_format(axis="y", style="sci", useMathText=True)

# Display the animation
plt.show()
