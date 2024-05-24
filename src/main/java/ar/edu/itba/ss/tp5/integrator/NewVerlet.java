package ar.edu.itba.ss.tp5.integrator;

import ar.edu.itba.ss.tp4.integrator.IntegratorMethod;
import ar.edu.itba.ss.tp4.utils.StateVariables;

import java.util.Iterator;
import java.util.function.BiFunction;

public class NewVerlet implements IntegratorMethod {
    private final double t0;
    private final double dt;
    private final BiFunction<Double, Double, Double> acceleration;
    private final double r0;
    private final double v0;

    public NewVerlet(
            final double dt,
            final BiFunction<Double, Double, Double> acceleration,
            final double r0,
            final double v0
    ) {
        this.t0 = 0;
        this.dt = dt;
        this.acceleration = acceleration;
        this.r0 = r0;
        this.v0 = v0;
    }

    public NewVerlet(
            final double t0,
            final double dt,
            final BiFunction<Double, Double, Double> acceleration,
            final double r0,
            final double v0
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

            @Override
            public boolean hasNext() {
                return true;
            }

            @Override
            public StateVariables next() {
                final StateVariables returnValue = new StateVariables(t, r, v);

                final double newR = 2 * r - previousR + acceleration.apply(r, v) * Math.pow(dt, 2);
                final double newNewR = 2 * newR - r + acceleration.apply(newR, v) * Math.pow(dt, 2);
                final double newV = (newNewR - r) / (2 * dt);

                t += dt;
                previousR = r;
                r = newR;
                v = newV;

                return returnValue;
            }
        };
    }
}
