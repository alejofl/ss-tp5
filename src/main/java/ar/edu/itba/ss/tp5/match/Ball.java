package ar.edu.itba.ss.tp5.match;

import ar.edu.itba.ss.tp5.utils.Position;
import ar.edu.itba.ss.tp5.utils.Teams;

import java.util.HashMap;
import java.util.Map;

public class Ball {
    private final Map<String, Position> positionMap;
    private final Map<String, Teams> possessionMap;

    public Ball() {
        this.possessionMap = new HashMap<>();
        this.positionMap = new HashMap<>();
    }

    public void addPosition(Double time, Position position, Teams team) {
        this.positionMap.put(String.format("%.2f", time), position);
        this.possessionMap.put(String.format("%.2f", time), team);
    }

    public Position getPosition(Double time) {
        return this.positionMap.get(String.format("%.2f", time));
    }
}
