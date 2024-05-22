package ar.edu.itba.ss.tp5;

import ar.edu.itba.ss.tp5.match.Ball;
import ar.edu.itba.ss.tp5.match.Match;
import ar.edu.itba.ss.tp5.match.Player;
import ar.edu.itba.ss.tp5.utils.Position;
import ar.edu.itba.ss.tp5.utils.Teams;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.sql.Array;
import java.util.*;
import java.util.stream.Stream;

public class Main {

    public static void findOptimumTime() {
        final List<Double> timesWithoutBall = new ArrayList<>();
        final List<Double> timesWithSamePlayers = new ArrayList<>();

        try (
                Stream<String> home = Files.lines(Paths.get("TrackingData_Local.csv")).skip(3);
                Stream<String> away = Files.lines(Paths.get("TrackingData_Visitante.csv")).skip(3)
        ) {
            home.forEach(line -> {
                String[] fields = line.split(",");
                final double time = Double.parseDouble(fields[2]);
                double ballX = Double.parseDouble(fields[31]) * 105;
                double ballY = Double.parseDouble(fields[32]) * 68;
                if (Double.isNaN(ballX) || Double.isNaN(ballY)) {
                    timesWithoutBall.add(time);
                }
            });
            away.forEach(line -> {
                String[] fields = line.split(",");
                final double time = Double.parseDouble(fields[2]);
                double ballX = Double.parseDouble(fields[27]) * 105;
                double ballY = Double.parseDouble(fields[28]) * 68;
                if (!Double.isNaN(ballX) && !Double.isNaN(ballY)) {
                    for (int i = 0; i < timesWithoutBall.size(); i++) {
                        if (Math.abs(timesWithoutBall.get(i) - time) < 0.001) {
                            timesWithoutBall.remove(i);
                        }
                    }
                }
            });
        } catch (IOException e) {
            System.err.println("Error reading players' file");
            System.exit(2);
        }

        Double maxTime = 0.0;
        Double maxTimeStart = 0.0;
        Double maxTimeEnd = 0.0;
        for (int i = 0; i < timesWithoutBall.size() - 1; i++) {
            if (timesWithoutBall.get(i + 1) - timesWithoutBall.get(i) > 0.04 + 0.001) {
                if (maxTime < (timesWithoutBall.get(i + 1) - timesWithoutBall.get(i))) {
                    maxTime = timesWithoutBall.get(i + 1) - timesWithoutBall.get(i);
                    maxTimeStart = timesWithoutBall.get(i);
                    maxTimeEnd = timesWithoutBall.get(i + 1);
                }
                System.out.println("Time without ball: " + timesWithoutBall.get(i) + " - " + timesWithoutBall.get(i + 1) + " = " + (timesWithoutBall.get(i + 1) - timesWithoutBall.get(i)));
            }
        }

        System.out.println("MaxTime with ball: " + maxTimeStart + " - " + maxTimeEnd + " - Duration: " + maxTime);

        try (
                Stream<String> home = Files.lines(Paths.get("TrackingData_Local.csv")).skip(3);
                Stream<String> away = Files.lines(Paths.get("TrackingData_Visitante.csv")).skip(3)
        ) {
            List<String> homePlayers = home.toList();
            List<String> awayPlayers = away.toList();
            List<Map.Entry<String, String>> players = new ArrayList<>();
            for (int i = 0; i < homePlayers.size(); i++) {
                StringBuilder playersString = new StringBuilder();
                String[] homeFields = homePlayers.get(i).split(",");
                String[] awayFields = awayPlayers.get(i).split(",");
                for (int j = 3; j < 31; j += 2) {
                    if (homeFields[j].equals("NaN") && homeFields[j+1].equals("NaN")) {
                        playersString.append("0");
                    } else {
                        playersString.append("1");
                    }
                }
                for (int j = 3; j < 27; j += 2) {
                    if (awayFields[j].equals("NaN") && awayFields[j+1].equals("NaN")) {
                        playersString.append("0");
                    } else {
                        playersString.append("1");
                    }
                }
                final double time = Double.parseDouble(homeFields[2]);
                players.add(new AbstractMap.SimpleEntry<>(String.format("%.2f", time), playersString.toString()));
            }

            for (int i = 0; i < players.size(); ) {
                String currentPlayers = players.get(i).getValue();
                boolean didBreak = false;
                for (int j = i + 1; !didBreak && j < players.size(); j++) {
                    if (!currentPlayers.equals(players.get(j).getValue())) {
                        System.out.println("Time with same players: " + players.get(i).getKey() + " - " + players.get(j).getKey() + " = " + (Double.parseDouble(players.get(j).getKey()) - Double.parseDouble(players.get(i).getKey())));
                        timesWithSamePlayers.add(Double.parseDouble(players.get(j).getKey()) - Double.parseDouble(players.get(i).getKey()));
                        i = j;
                        didBreak = true;
                    }
                }
                if (!didBreak) {
                    int j = players.size() - 1;
                    System.out.println("Time with same players: " + players.get(i).getKey() + " - " + players.get(j).getKey() + " = " + (Double.parseDouble(players.get(j).getKey()) - Double.parseDouble(players.get(i).getKey())));
                    timesWithSamePlayers.add(Double.parseDouble(players.get(j).getKey()) - Double.parseDouble(players.get(i).getKey()));
                    break;
                }
            }

            System.out.println("Max time with same players = " + Collections.max(timesWithSamePlayers));

        } catch (IOException e) {
            System.err.println("Error reading players' file");
            System.exit(2);
        }
    }

    public static void main(String[] args) {
        //findOptimumTime();
        final Player homePlayer11 = new Player("Player11", Teams.HOME);
        final Player homePlayer1 = new Player("Player1", Teams.HOME);
        final Player homePlayer2 = new Player("Player2", Teams.HOME);
        final Player homePlayer3 = new Player("Player3", Teams.HOME);
        final Player homePlayer4 = new Player("Player4", Teams.HOME);
        final Player homePlayer5 = new Player("Player5", Teams.HOME);
        final Player homePlayer6 = new Player("Player6", Teams.HOME);
        final Player homePlayer7 = new Player("Player7", Teams.HOME);
        final Player homePlayer8 = new Player("Player8", Teams.HOME);
        final Player homePlayer9 = new Player("Player9", Teams.HOME);
        final Player homePlayer10 = new Player("Player10", Teams.HOME);
        final Player homePlayer12 = new Player("Player12", Teams.HOME);
        final Player homePlayer13 = new Player("Player13", Teams.HOME);
        final Player homePlayer14 = new Player("Player14", Teams.HOME);
        final List<Player> homePlayers = List.of(homePlayer11, homePlayer2, homePlayer1, homePlayer3, homePlayer4, homePlayer5, homePlayer6, homePlayer7, homePlayer8, homePlayer9, homePlayer10, homePlayer12, homePlayer13, homePlayer14);

        final Player awayPlayer25 = new Player("Player25", Teams.AWAY);
        final Player awayPlayer15 = new Player("Player15", Teams.AWAY);
        final Player awayPlayer16 = new Player("Player16", Teams.AWAY);
        final Player awayPlayer17 = new Player("Player17", Teams.AWAY);
        final Player awayPlayer18 = new Player("Player18", Teams.AWAY);
        final Player awayPlayer19 = new Player("Player19", Teams.AWAY);
        final Player awayPlayer20 = new Player("Player20", Teams.AWAY);
        final Player awayPlayer21 = new Player("Player21", Teams.AWAY);
        final Player awayPlayer22 = new Player("Player22", Teams.AWAY);
        final Player awayPlayer23 = new Player("Player23", Teams.AWAY);
        final Player awayPlayer24 = new Player("Player24", Teams.AWAY);
        final Player awayPlayer26 = new Player("Player26", Teams.AWAY);
        final List<Player> awayPlayers = List.of(awayPlayer25, awayPlayer15, awayPlayer16, awayPlayer17, awayPlayer18, awayPlayer19, awayPlayer20, awayPlayer21, awayPlayer22, awayPlayer23, awayPlayer24, awayPlayer26);

        final List<Player> players = Stream.concat(homePlayers.stream(), awayPlayers.stream()).toList();
        final Ball ball = new Ball();

        try (
                Stream<String> home = Files.lines(Paths.get("TrackingData_Local.csv")).skip(3);
                Stream<String> away = Files.lines(Paths.get("TrackingData_Visitante.csv")).skip(3)
        ) {
            home.forEach(line -> {
                String[] fields = line.split(",");
                final double time = Double.parseDouble(fields[2]);
                for (int i = 0; i < homePlayers.size(); i++) {
                    homePlayers.get(i).addPosition(time, new Position(Double.parseDouble(fields[3 + i * 2]) * 105, Double.parseDouble(fields[3 + i * 2 + 1]) * 68));
                }
                double ballX = Double.parseDouble(fields[31]) * 105;
                double ballY = Double.parseDouble(fields[32]) * 68;
                if (!Double.isNaN(ballX) && !Double.isNaN(ballY)) {
                    ball.addPosition(time, new Position(ballX, ballY), Teams.HOME);
                }
            });
            away.forEach(line -> {
                String[] fields = line.split(",");
                final double time = Double.parseDouble(fields[2]);
                for (int i = 0; i < awayPlayers.size(); i++) {
                    awayPlayers.get(i).addPosition(time, new Position(Double.parseDouble(fields[3 + i * 2]) * 105, Double.parseDouble(fields[3 + i * 2 + 1]) * 68));
                }
                double ballX = Double.parseDouble(fields[27]) * 105;
                double ballY = Double.parseDouble(fields[28]) * 68;
                if (!Double.isNaN(ballX) && !Double.isNaN(ballY)) {
                    ball.addPosition(time, new Position(ballX, ballY), Teams.AWAY);
                }
            });
        } catch (IOException e) {
            System.err.println("Error reading players' file");
            System.exit(2);
        }

        List<String> input = null;
        try (Stream<String> stream = Files.lines(Paths.get("input.txt"))) {
            input = stream.toList();
        } catch (Exception e) {
            System.err.println("Error reading input file");
            System.exit(2);
        }
        if (input.size() != 4) {
            throw new IllegalStateException();
        }

        final double distanceToBall = Double.parseDouble(input.get(0));
        final double desiredVelocity = Double.parseDouble(input.get(1));
        final double relaxingTime = Double.parseDouble(input.get(2));
        final double mass = Double.parseDouble(input.get(3));

        // Simulation
        final Match match = new Match(players, ball, distanceToBall, desiredVelocity, relaxingTime, mass, 57.24);
        match.simulate(177.76, "output.txt");
    }
}
