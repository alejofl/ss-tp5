package ar.edu.itba.ss.tp5.match;

import ar.edu.itba.ss.tp4.integrator.NewVerlet;
import ar.edu.itba.ss.tp4.utils.StateVariables;
import ar.edu.itba.ss.tp5.utils.Position;

import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.Iterator;
import java.util.List;
import java.util.function.BiFunction;

public class Match {
    public static final double GRANULAR_FORCE_K = 1.2E5;
    public static final double SOCIAL_FORCE_A = 2E3;
    public static final double SOCIAL_FORCE_B = 0.08;
    public static final double PLAYER_RADIUS = 0.25;

    private final List<Player> players;
    private final Ball ball;
    private final double distanceToBall;
    private final double desiredVelocity;
    private final double relaxingTime;
    private final double mass;

    private double time;
    private double dataTime;
    private final double dt = 0.004;
    private final double dataDt = 0.04;
    private final int writingInterval = 10;

    public Match(List<Player> players, Ball ball, double distanceToBall, double desiredVelocity, double relaxingTime, double mass, double time) {
        this.players = players;
        this.ball = ball;
        this.distanceToBall = distanceToBall;
        this.desiredVelocity = desiredVelocity;
        this.relaxingTime = relaxingTime;
        this.mass = mass;
        this.time = time;
        this.dataTime = time;
    }

    public void simulate(double endTime, String filename) {
        Position virtualPlayer = new Position(ball.getPosition(time).x() - distanceToBall, ball.getPosition(time).y());

        BiFunction<Double, Double, Double> accelerationX = (r, v) -> {
            Position ballPosition = ball.getPosition(dataTime);
            if (ballPosition == null) {
                return 0.0;
            }
            double normalVersorX = (ballPosition.x() - r) / Math.sqrt(Math.pow(ballPosition.x() - r, 2) + Math.pow(ballPosition.y() - virtualPlayer.y(), 2));
            double drivingForce = mass * (desiredVelocity * normalVersorX - v) / relaxingTime;
            double socialForce = 0;
            double granularForce = 0;
            for (Player player : players) {
                if (player.isSubstitute(dataTime)) {
                    continue;
                }
                Position playerPosition = player.getPosition(dataTime);
                double normalVersorPlayerX = (r - playerPosition.x()) / Math.sqrt(Math.pow(r - playerPosition.x(), 2) + Math.pow(virtualPlayer.y() - playerPosition.y(), 2));
                double distance = Math.sqrt(Math.pow(playerPosition.x() - r, 2) + Math.pow(playerPosition.y() - virtualPlayer.y(), 2)) - 2 * PLAYER_RADIUS;
                socialForce += SOCIAL_FORCE_A * Math.exp(- distance / SOCIAL_FORCE_B) * normalVersorPlayerX;
                granularForce += distance < 0 ? GRANULAR_FORCE_K * -distance * normalVersorPlayerX : 0;
            }
            return (drivingForce + socialForce + granularForce) / mass;
        };
        BiFunction<Double, Double, Double> accelerationY = (r, v) -> {
            Position ballPosition = ball.getPosition(dataTime);
            if (ballPosition == null) {
                return 0.0;
            }
            double normalVersorY = (ballPosition.y() - r) / Math.sqrt(Math.pow(ballPosition.x() - virtualPlayer.x(), 2) + Math.pow(ballPosition.y() - r, 2));
            double drivingForce = mass * (desiredVelocity * normalVersorY - v) / relaxingTime;
            double socialForce = 0;
            double granularForce = 0;
            for (Player player : players) {
                if (player.isSubstitute(dataTime)) {
                    continue;
                }
                Position playerPosition = player.getPosition(dataTime);
                double normalVersorPlayerY = (r - playerPosition.y()) / Math.sqrt(Math.pow(virtualPlayer.x() - playerPosition.x(), 2) + Math.pow(r - playerPosition.y(), 2));
                double distance = Math.sqrt(Math.pow(playerPosition.x() - virtualPlayer.x(), 2) + Math.pow(playerPosition.y() - r, 2)) - 2 * PLAYER_RADIUS;
                socialForce += SOCIAL_FORCE_A * Math.exp(- distance / SOCIAL_FORCE_B) * normalVersorPlayerY;
                granularForce += distance < 0 ? GRANULAR_FORCE_K * -distance * normalVersorPlayerY : 0;
            }
            return (drivingForce + socialForce + granularForce) / mass;
        };

        Iterator<StateVariables> iteratorX = new NewVerlet(time, dt, accelerationX, virtualPlayer.x(), 0).iterator();
        Iterator<StateVariables> iteratorY = new NewVerlet(time, dt, accelerationY, virtualPlayer.y(), 0).iterator();

        try (BufferedWriter writer = Files.newBufferedWriter(
                Paths.get(filename),
                StandardOpenOption.WRITE,
                StandardOpenOption.CREATE,
                StandardOpenOption.TRUNCATE_EXISTING
        )) {
            dataTime -= dataDt;
            for (int i = 0; time < endTime; i++, time += dt) {
                if (i % writingInterval == 0) {
                    dataTime += dataDt;
                }
                StateVariables stateVariablesX = iteratorX.next();
                StateVariables stateVariablesY = iteratorY.next();
                virtualPlayer.set(stateVariablesX, stateVariablesY);
                if (i % writingInterval == 0) {
                    writer.write(String.format("%f %f %f", dataTime, virtualPlayer.x(), virtualPlayer.y()));
                    writer.newLine();
                }
            }
        } catch (IOException e) {
            throw new RuntimeException("Could not write files.");
        }
    }
}
