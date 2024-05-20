package ar.edu.itba.ss.tp5.utils;

import ar.edu.itba.ss.tp4.utils.StateVariables;

public class Position {
    private double x;
    private double y;

    public Position(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double x() {
        return x;
    }

    public double y() {
        return y;
    }

    public void set(StateVariables variablesX, StateVariables variablesY) {
        this.x = variablesX.position();
        this.y = variablesY.position();
    }
}
