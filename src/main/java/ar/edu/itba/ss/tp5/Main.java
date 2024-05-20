package ar.edu.itba.ss.tp5;

import ar.edu.itba.ss.tp5.match.Ball;
import ar.edu.itba.ss.tp5.match.Match;
import ar.edu.itba.ss.tp5.match.Player;
import ar.edu.itba.ss.tp5.utils.Position;
import ar.edu.itba.ss.tp5.utils.Teams;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {

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
                String[] fields = line.split(";");
                final double time = Double.parseDouble(fields[2]);
                for (int i = 0; i < homePlayers.size(); i++) {
                    homePlayers.get(i).addPosition(time, new Position(Double.parseDouble(fields[3 + i * 2]), Double.parseDouble(fields[3 + i * 2 + 1])));
                }
                double ballX = Double.parseDouble(fields[31]);
                double ballY = Double.parseDouble(fields[32]);
                if (!Double.isNaN(ballX) && !Double.isNaN(ballY)) {
                    ball.addPosition(time, new Position(ballX, ballY), Teams.HOME);
                }
            });
            away.forEach(line -> {
                String[] fields = line.split(";");
                final double time = Double.parseDouble(fields[2]);
                for (int i = 0; i < awayPlayers.size(); i++) {
                    awayPlayers.get(i).addPosition(time, new Position(Double.parseDouble(fields[3 + i * 2]), Double.parseDouble(fields[3 + i * 2 + 1])));
                }
                double ballX = Double.parseDouble(fields[27]);
                double ballY = Double.parseDouble(fields[28]);
                if (!Double.isNaN(ballX) && !Double.isNaN(ballY)) {
                    ball.addPosition(time, new Position(ballX, ballY), Teams.AWAY);
                }
            });
        } catch (IOException e) {
            System.err.println("Error reading file");
            System.exit(2);
        }

        // Simulation
        final Match match = new Match(players, ball);
    }
}
