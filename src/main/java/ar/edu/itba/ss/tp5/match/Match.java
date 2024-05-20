package ar.edu.itba.ss.tp5.match;

import java.util.List;

public class Match {
    private final List<Player> players;
    private final Ball ball;

    public Match(List<Player> players, Ball ball) {
        this.players = players;
        this.ball = ball;
    }
}
