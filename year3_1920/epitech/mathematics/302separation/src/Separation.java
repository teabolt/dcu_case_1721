import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.SortedMap;
import java.util.TreeMap;
import java.util.SortedSet;
import java.util.TreeSet;
import java.util.Arrays;


/**
* Entry point to the 302separation program.
**/
public class Separation {

    private static String parserRegex = "\\s+is\\s+friends\\s+with\\s+";

    // exit with error 84 and a message
    private static void error(String message) {
        System.out.println(message);
        System.exit(84);
    }

    // parse lines into an adjacency list
    public static AdjacencyList readAdjacencyList(String filename) {
        BufferedReader in = null;
        AdjacencyList adj_list = new AdjacencyList();
        try {
            in = new BufferedReader(new FileReader(filename));
            // Could also use Files.readAllLines
        } catch (FileNotFoundException e) {
            error("Could not find file: " + filename);
        }

        try {
            String line;
            while ((line = in.readLine()) != null) {
                line = line.trim();
                if (0 < line.length()) {
                    // only add non-empty lines
                    String names[] = line.split(parserRegex);
                    if (names.length != 2) {
                        error(String.format("Misformatted line (could not read two names): \"%s\"", line));
                    }
                    String p1 = names[0].trim();
                    String p2 = names[1].trim();
                    // we can only trim whitespace AROUND words
                    // not inside words
                    adj_list.addEdge(p1, p2);   
                    adj_list.addEdge(p2, p1);   // Facebook relationships are commutative
                }
            }
            in.close();
        } catch (IOException e) {
            e.printStackTrace();
            error("IO error.");
        }
        return adj_list;
    }

    public static void visualizeGraph() {}

    public static void visualizeConnections() {}

    // return help string
    public static String help() {
        String s;
        s = "USAGE\n" +
            "./302separation file [n | p1 p2]\n" + 
            "DESCRIPTION\n" +
                "\tfile    file that contains the list of Facebook connections\n" + 
                "\tn       maximum length of the paths\n" + 
                "\tpi      name of someone in the file";
        return s;
    }

    public static void main(String[] args) {
        int argc = args.length;
        if (argc == 1 && args[0].equals("-h")) {
            // help flag
            System.out.println(help());
        } else if (argc == 2) {
            // file n
            String filename = args[0];
            Integer n = null;
            try {
                n = Integer.parseInt(args[1]);
            } catch (NumberFormatException e) {
                error("Could not parse argument 2 - maximum length of the paths.");
            }

            // read lines into an adjacency list (easy due to line-by-line relationships)
            AdjacencyList adj_list = readAdjacencyList(filename);

            // print list of people
            for (String name : adj_list.verticesSet()) {
                System.out.println(name);
            }
            System.out.println();
            // convert adjacency list to adjacency matrix and print
            // note that the graph is not allowed to back onto itself
            // i.e. people are not their own friends - edge weight is zero across the diagonal
            Matrix adj_mat = adj_list.toAdjacencyMatrix();
            System.out.println(adj_mat);
            System.out.println();

            // get a "separation" matrix - degrees of separation between all the vertices
            Graph g = new Graph(adj_mat);
            Matrix sep_mat = g.separationMatrix(n);
            System.out.println(sep_mat); 
        } else if (argc == 3) {
            // file p1 p2
            String filename = args[0];
            String p1 = args[1];
            String p2 = args[2];

            // create a graph
            AdjacencyList adj_list = readAdjacencyList(filename);
            Matrix adj_mat = adj_list.toAdjacencyMatrix();
            Graph g = new Graph(adj_mat);

            // find the degree of separation
            List<String> index = adj_list.getIndex();
            int v1 = index.indexOf(p1);
            int v2 = index.indexOf(p2);
            // TODO: optimization
            // TODO: Vertex/Node class
            int degree;
            if (v1 == -1 || v2 == -1) {
                degree = -1;
            } else {
                List<Integer> distances = g.dijkstra(v1);
                degree = distances.get(v2);
            }

            String sep = String.format("Degree of separation between %s and %s: %d", p1, p2, degree);
            System.out.println(sep);
        } else {
            // all other arguments
            String err;
            if (argc == 0) {
                err = "Arguments missing.\n";
            } else {
                err = "Arguments not understood.\n";
            }
            err = "See \"./302separation -h\" for help.";
            error(err);
        }
    }
}