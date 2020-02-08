/** 
* Matrix implementation in Java
**/
public class Matrix {
    private int[][] matrix;

    public int rows;
    public int cols;

    /**
    * Initialize to all zeros an empty m*n integer matrix.
    * m is the number of rows, n is the number of columns.
    *
    *    - - - -
    *    - - - -
    *    - - - -
    *    - - - -
    *
    **/
    public Matrix(int m, int n) {
        rows = m;
        cols = n;
        matrix = new int[rows][cols];
    }

    /**
    * Initialize square matrix with m*m dimensions.
    **/
    public Matrix(int m) {
        this(m, m);
    }

    /**
    * Initialize a matrix from a 2D array.
    * NOT safe from empty arrays.
    **/
    public Matrix(int[][] array) {
        rows = array.length;
        if (array.length != 0) {
            cols = array[0].length;   
        } else {
            cols = rows;
        }
        matrix = array;
    }

    /**
    * Access a value at a position in the matrix
    * where i is the row number, and j is the column number.
    * (row major order)
    * 
    *        col
    *      0 1 2 3
    * r 0  - - - -
    * o 1  - - - -
    * w 2  - - - -
    *   3  - - - -
    *
    **/
    public int get(int i, int j) {
        return matrix[i][j];
    }

    /**
    * Set a position in the matrix to a certain value
    * where i is row number, and j is column number.
    **/
    public void put(int i, int j, int v) {
        matrix[i][j] = v;
    }

    /**
    * Return a string representation of the matrix.
    **/
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                sb.append(matrix[i][j]);
                if (j < cols-1) sb.append(" ");
            }
            if (i < rows-1) sb.append("\n");
        }
        return sb.toString();
    }

    public boolean isSquare() { return rows == cols; }
}