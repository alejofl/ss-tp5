package ar.edu.itba.ss.tp5.match;

import ar.edu.itba.ss.tp5.utils.Position;
import ar.edu.itba.ss.tp5.utils.Teams;

import java.util.HashMap;
import java.util.Map;

public class Ball {
    private final Map<Double, Position> positionMap;
    private final Map<Double, Teams> possessionMap;

    public Ball() {
        this.possessionMap = new HashMap<>();
        this.positionMap = new HashMap<>();
    }

    public void addPosition(Double time, Position position, Teams team) {
        this.positionMap.put(time, position);
        this.possessionMap.put(time, team);
    }
}
