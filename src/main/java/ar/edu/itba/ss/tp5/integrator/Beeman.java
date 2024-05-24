package ar.edu.itba.ss.tp5.integrator;

import ar.edu.itba.ss.tp4.integrator.IntegratorMethod;
import ar.edu.itba.ss.tp4.utils.StateVariables;

import java.util.Iterator;
import java.util.function.BiFunction;

public class Beeman implements IntegratorMethod {
    private final double t0;
    private final double dt;
    private final BiFunction<Double, Double, Double> acceleration;
    private final double r0;
    private final double v0;

    public Beeman(
            double t0,
            double dt,
            BiFunction<Double, Double, Double> acceleration,
            double r0,
            double v0
    ) {
        this.t0 = t0;
        this.dt = dt;
        this.acceleration = acceleration;
        this.r0 = r0;
        this.v0 = v0;
    }

    @Override
    public Iterator<StateVariables> iterator() {
        return new Iterator<>() {
            private double t = t0;
            private double r = r0;
            private double v = v0;
            private double previousR = r - dt * v + 0.5 * acceleration.apply(r, v) * Math.pow(dt, 2);
            private double previousV = v - dt * acceleration.apply(r, v);

            @Override
            public boolean hasNext() {
                return true;
            }

            @Override
            public StateVariables next() {
                final StateVariables returnValue = new StateVariables(t, r, v);

                final double newR = r + v * dt + 2.0 / 3.0 * acceleration.apply(r, v) * Math.pow(dt, 2) - 1.0 / 6.0 * acceleration.apply(previousR, previousV) * Math.pow(dt, 2);
                final double predictedV = v + 3.0 / 2.0 * acceleration.apply(r, v) * dt - 1.0 / 2.0 * acceleration.apply(previousR, previousV) * dt;
                final double newV = v + 1.0 / 3.0 * acceleration.apply(newR, predictedV) * dt + 5.0 / 6.0 * acceleration.apply(r, v) * dt - 1.0 / 6.0 * acceleration.apply(previousR, previousV) * dt;

                t += dt;
                previousR = r;
                previousV = v;
                r = newR;
                v = newV;

                return returnValue;
            }
        };
    }
}
