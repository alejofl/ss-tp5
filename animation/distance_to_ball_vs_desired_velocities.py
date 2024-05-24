import csv
import matplotlib.pyplot as plt
import numpy as np
import os.path


########### CONSTANT VARIABLES ###########
DESIRED_VELOCITIES = [0.1] + list(range(1, 14, 1))
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
xs = []
ys = []
errors = []

files = [open(os.path.join(os.path.dirname(__file__), "..", "output_velocity_{:.1f}.txt".format(velocity))) for velocity in DESIRED_VELOCITIES]
for file, desired_velocity in zip(files, DESIRED_VELOCITIES):
    virtual_player_data = list(csv.reader(file, delimiter=" "))[:-1]
    file.close()

    distances = []
    for player, ball in zip(virtual_player_data, ball_positions):
        player_x, player_y = convert_xy_to_system_reference(player[1], player[2], False)
        distances.append(distance(player_x, player_y, ball[0], ball[1]))

    # print(distances)
    xs.append(desired_velocity)
    ys.append(np.mean(distances))
    errors.append(np.std(distances, ddof=1))

ax.errorbar(xs, ys, yerr=errors, fmt='o', capsize=5)

ax.set_xlabel("Velocidad deseada $\\left( m/s \\right)$", fontdict={"weight": "bold"})
ax.set_ylabel("Promedio de distancia loco-pelota $\\left( m \\right)$", fontdict={"weight": "bold"})
# ax.ticklabel_format(axis="y", style="sci", useMathText=True)

# Display the animation
plt.show()
