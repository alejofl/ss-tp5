# Pedestrian Dynamics Simulation

## Introduction

This project is a simulation of pedestrian dynamics in a closed environment. The simulation is based on the social force model proposed by Dirk Helbing and Peter Molnar. 
The model is a physics-based model of a football match. With the players' positions and ball's positions as input, a simulation in which a person enters the field and chases the ball is generated.
The model calculates the forces acting on the person by each player and the ball.
The simulation is implemented in Java, and we used Python for visualization.

## Requirements

- Java 19
- Maven
- Python 3 (only for visualizations to be rendered)

## Building the project

To build the project, `cd` to the root of the project and run the following command:

```
mvn clean package
```

This will compile and package a `.jar` file in the `target` directory.

## Executing the project

> [!NOTE]  
> The following instructions assume that you have built the project as described in the previous section and that the generated `.jar` file is in the current working directory.

```bash
java -jar ss-tp5-1.0-SNAPSHOT.jar
```

The program will execute the simulation described above.

The program expects to have the following files in the current working directory:

1. `TrackingData_Local.csv`: A CSV file with the tracking data of the players and the ball of one of the teams. If the ball is not in possession of this team, then its fields should be `NaN`. If one of the players is not on the field for a given time, its fields should be `NaN`. The file should have the following structure:

    ```csv
    Period,Frame,Time [s],Player11_X,Player11_Y,Player1_X,Player1_Y,Player2_X,Player2_Y,Player3_X,Player3_Y,Player4_X,Player4_Y,Player5_X,Player5_Y,Player6_X,Player6_Y,Player7_X,Player7_Y,Player8_X,Player8_Y,Player9_X,Player9_Y,Player10_X,Player10_Y,Player12_X,Player12_Y,Player13_X,Player13_Y,Player14_X,Player14_Y,Ball_X,Ball_Y
    ```

2. `TrackingData_Visitante.csv`: A CSV file with the tracking data of the players and the ball of the other team. If the ball is not in possession of this team, then its fields should be `NaN`. If one of the players is not on the field for a given time, its fields should be `NaN`. The file should have the following structure:

    ```csv
    Period,Frame,Time [s],Player25_X,Player25_Y,Player15_X,Player15_Y,Player16_X,Player16_Y,Player17_X,Player17_Y,Player18_X,Player18_Y,Player19_X,Player19_Y,Player20_X,Player20_Y,Player21_X,Player21_Y,Player22_X,Player22_Y,Player23_X,Player23_Y,Player24_X,Player24_Y,Player26_X,Player26_Y,Ball_X,Ball_Y
    ```

3. `input.txt`: A text file with the following structure:

    ```text
    {{ distance_to_ball }}
    {{ desired_velocity }}
    {{ relaxation_time }}
    {{ mass }}
    ```

    Where:

    - `distance_to_ball` is the distance from the person to the ball when the simulation starts.
    - `desired_velocity` is the desired velocity of the person.
    - `relaxation_time` is the relaxation time of the person.
    - `mass` is the mass of the person.

The program will generate an output file named `output.txt` in the current working directory. The file will have the following structure:

```text
{{ time }} {{ position_x }} {{ position_y }}
```

Where:

- `time` is the time in seconds.
- `position_x` is the x-coordinate of the person for that given time.
- `position_y` is the y-coordinate of the person for that given time.

## Visualizing the output

> [!NOTE]  
> The following instructions assume that you have executed the project as described in the previous section and that all the input and output files are in the current working directory.

### Installing dependencies

To visualize the output, we must run a Python script. First, we need to install the required dependencies. To do so, run the following command:

```bash
python -m venv venv
source venv/bin/activate
pip install -r animation/requirements.txt
```

### Visualizing the match animation

To visualize an animation of the match, run the following command:

```bash
python animation/animation.py
```

This will generate an animation of the simulated portion of the match, with all the players, the person, and the ball moving according to the simulation.

### Visualizing other plots

- Distance between the person and the ball vs time: `python animation/distance_to_ball_vs_time.py`
- Distance between the person and the ball vs desired velocity: `python animation/distance_to_ball_vs_desired_velocity.py`
- Distance between the person and the ball vs relaxation time: `python animation/distance_to_ball_vs_relaxing_time.py`
- Probability Density Function of the person's velocity: `python animation/pdf.py`
- Heatmap of the field for different players: `python animation/heatmap.py`

## Final Remarks

This project was done in an academic environment, as part of the curriculum of Systems Simulation from Instituto Tecnológico de Buenos Aires (ITBA).

The project was carried out by:

* Alejo Flores Lucey
* Nehuén Gabriel Llanos