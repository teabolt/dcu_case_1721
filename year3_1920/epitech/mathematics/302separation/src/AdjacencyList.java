import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.SortedMap;
import java.util.TreeMap;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;


/**
* Adjacency list data structure for graphs in Java.
* The graph is directed.
**/
public class AdjacencyList {

    public SortedMap<String, SortedSet<String>> _map;

    public AdjacencyList() {
        _map = new TreeMap<>();
    }

    // get a map (list) from indices to sorted names in a matrix
    public List<String> getIndex() {
        List<String> index = new ArrayList<>(_map.keySet());
        return index;
    }

    // get an ordered set of all the vertices
    public Set<String> verticesSet() {
        return _map.keySet();
    }

    public Set<Map.Entry<String, SortedSet<String>>> edgesSet() {
        return _map.entrySet();
    }

    // get size of list (number of vertices)
    public int size() {
        return _map.size();
    }

    // string representation for list
    public String toString() {
        return "Adjacency List:\n" + _map.toString();
    }

    // add edge from v1 to v2
    // TODO: generic methods with types instead of just String
    public void addEdge(String v1, String v2) {
        SortedSet<String> neighbours = _map.get(v1);
        if (neighbours == null) {
            // fresh edge
            neighbours = new TreeSet<String>();
        }
        neighbours.add(v2);   // add vertex to set
        _map.put(v1, neighbours);   // update map
    }

    // convert adjacency list to an adjacency matrix
    public Matrix toAdjacencyMatrix() {
        List<String> index = getIndex();
        Matrix adj_mat = new Matrix(size());   // initialize matrix

        for (Map.Entry<String, SortedSet<String>> entry : edgesSet()) {
            String p1 = entry.getKey();
            SortedSet<String> related = entry.getValue();
            int row = index.indexOf(p1);
            for (String p2 : related) {
                int col = index.indexOf(p2);
                adj_mat.put(row, col, 1);
            }
        }
        return adj_mat;
    }
}