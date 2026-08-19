public class adjacencymatrix2 {
    public static void main(String[] args) {

        int[][] matrix = {
                { 0, 1, 1, 0, 0 },
                { 1, 0, 1, 1, 1 },
                { 1, 1, 0, 1, 1 },
                { 0, 1, 1, 0, 1 },
                { 0, 1, 1, 1, 0 }
        };
        boolean valid = true;

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix.length; j++) {

                if (matrix[i][j] != matrix[j][i]) {
                    valid = false;
                }
            }
        }

        if (valid) {
            System.out.println("Matrix is valid");
        } else {
            System.out.println("Matrix is not valid");
        }
        System.out.println("   A B C D E");

        for (int i = 0; i < matrix.length; i++) {
            System.out.print((char) ('A' + i) + "  ");

            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }

            System.out.println();
        }
    }
}