package ar.edu.itba.ss.tp5.match;

import ar.edu.itba.ss.tp5.utils.Position;
import ar.edu.itba.ss.tp5.utils.Teams;

import java.util.HashMap;
import java.util.Map;

public class Player {
    private final String id;
    private final Teams team;
    private final Map<String, Position> positionMap;

    public Player(String id, Teams team) {
        this.id = id;
        this.team = team;
        this.positionMap = new HashMap<>();
    }

    public void addPosition(double time, Position position) {
        this.positionMap.put(String.format("%.2f", time), position);
    }

    public Position getPosition(Double time) {
        return this.positionMap.get(String.format("%.2f", time));
    }

    public boolean isSubstitute(Double time) {
        return Double.isNaN(this.positionMap.get(String.format("%.2f", time)).x()) || Double.isNaN(this.positionMap.get(String.format("%.2f", time)).y());
    }
}
