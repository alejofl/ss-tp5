package ar.edu.itba.ss.tp5.match;

import ar.edu.itba.ss.tp5.utils.Position;
import ar.edu.itba.ss.tp5.utils.Teams;

import java.util.HashMap;
import java.util.Map;

public class Player {
    private final String id;
    private final Teams team;
    private final Map<Double, Position> positionsMap;

    public Player(String id, Teams team) {
        this.id = id;
        this.team = team;
        this.positionsMap = new HashMap<>();
    }

    public void addPosition(double time, Position position) {
        this.positionsMap.put(time, position);
    }
}
