import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

/**
*   Graph implementation in Java.
**/
public class Graph {

    // TODO: create graph instances from matrices
    // check if matrix is square

    private Matrix _adj_mat;  // underlying representation
    public int numVertices;  // number of vertices

    /**
    * Create a graph from an adjacency matrix representation.
    **/
    public Graph(Matrix adjacency_matrix) {
        if (!adjacency_matrix.isSquare()) {
            System.out.println("Invalid adjacency matrix (not square).");
            System.exit(84);
        } else {
            _adj_mat = adjacency_matrix;
            numVertices = adjacency_matrix.rows;
        }
        
    }

    /**
    * Return index of vertex with smallest distance from a list of allowed indices.
    **/
    public static int nearestVertex(List<Integer> distances, List<Integer> allowed) {
        // TODO: check non-empty
        int min = allowed.get(0); // guess
        for (int i = 1; i < distances.size(); i++) {
            if (allowed.contains(i) && (distances.get(i) < distances.get(min))) {
                min = i; // update guess
            }
        }
        return min;
    }

    /**
    * Shortest path to nodes
    * Starting from source_node
    **/
    public List<Integer> dijkstra(int source_vertex) {
        // TODO: validate source vertex
        // TODO: A vertex/node data structure
        // currently we use indices/integers to represent vertices.
        List<Integer> distances = new ArrayList<>(numVertices); // shortest distance to each vertex
        List<Integer> remaining_graph = new ArrayList<>(numVertices); // indices not yet in the "found" list (SPT)
        // TODO: use set instead of list, or booleans instead of ints

        // initialize remaining vertex list and distances
        for (int i = 0; i < numVertices; i++) {
            remaining_graph.add(i);
            distances.add(Integer.MAX_VALUE);   // could also use Double.POSITIVE_INFINITY
        }
        distances.set(source_vertex, 0);    // source vertex has distance 0

        while (!remaining_graph.isEmpty()) {
            int new_vertex = nearestVertex(distances, remaining_graph); // find nearest vertex
            remaining_graph.remove(new Integer(new_vertex)); // include new vertex in SPT

            // update each neighbour's distance (that are not in the SPT)
            for (int i = 0; i < _adj_mat.rows; i++) {
                if (remaining_graph.contains(i)) {
                    // not in SPT
                    int weight = _adj_mat.get(i, new_vertex);
                    if (weight != 0) {
                        // an edge exists
                        int new_weight = distances.get(new_vertex) + weight;
                        if (distances.get(i) > new_weight) {
                            // going through the new node is shorter
                            distances.set(i, new_weight);
                        }
                    }
                }
            }
        }
        return distances;
    }

    /**
    * Set distances greater than limit to 0.
    **/
    private static void limitDistance(int[] distances, int limit) {
        for (int i = 0; i < distances.length; i++) {
            if (distances[i] > limit) {
                distances[i] = 0;
            }
        }
    }

    public Matrix separationMatrix(int n) {
        int[][] sep_arr = new int[numVertices][numVertices];
        for (int i = 0; i < numVertices; i++) {
            List<Integer> distances = dijkstra(i);
            int[] distances_arr = Utils.integerListToArray(distances);
            limitDistance(distances_arr, n);
            sep_arr[i] = distances_arr;
        }
        return new Matrix(sep_arr);
    }

}