/*
N * N matrix is given with input red or black. You can move horizontally, vertically or diagonally. If 3 consecutive
same color found, that color will get 1 point. So if 4 red are vertically then point is 2. Find the winner.

Brute force. Horizontally, Vertically, Diagonally. Works at O(n^2).
 */

public class TicTocToe {
    private char[][] board;
    private int n;

    public TicTocToe(char[][] board) {
        this.board = board;
        this.n = board[0].length;
    }

    public int countPoints(char c) {
        int points = 0;

        // check horizontally
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - 2; j++) {
                if (board[i][j] == c && board[i][j + 1] == c && board[i][j + 2] == c) {
                    points++;
                }
            }
        }

        // check vertically
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < n - 2; i++) {
                if (board[i][j] == c && board[i + 1][j] == c && board[i + 2][j] == c) {
                    points++;
                }
            }
        }

        // check diagonally
        for (int i = 0; i < n - 2; i++) {
            for (int j = 0; j < n - 2; j++) {
                if (board[i][j] == c && board[i + 1][j + 1] == c && board[i + 2][j + 2] == c) {
                    points++;
                }
            }
        }
        for (int i = 0; i < n - 2; i++) {
            for (int j = 2; j < n; j++) {
                if (board[i][j] == c && board[i + 1][j - 1] == c && board[i + 2][j - 2] == c) {
                    points++;
                }
            }
        }

        return points;
    }

    public char getWinner() {
        int pointRed = countPoints('r');
        int pointBlack = countPoints('b');

        if (pointRed > pointBlack) {
            return 'r';
        } else {
            return 'b';
        }
    }
}
