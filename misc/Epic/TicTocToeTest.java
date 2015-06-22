import org.junit.Test;
import static org.hamcrest.CoreMatchers.*;
import static org.junit.matchers.JUnitMatchers.*;
import static org.junit.Assert.*;


public class TicTocToeTest {

    @Test
    public void testCountPoints() throws Exception {
        char[][] board = {
                { 'r', 'r', 'r', 'b' },
                { 'b', 'r', 'b', 'r' },
                { 'b', 'r', 'r', 'b' },
                { 'b', 'r', 'b', 'b' } };
        TicTocToe t = new TicTocToe(board);

        assertThat(t.countPoints('r'), equalTo(5));
        assertThat(t.countPoints('b'), equalTo(1));
    }

    @Test
    public void testGetWinner() throws Exception {
        char[][] board = {
                { 'r', 'r', 'r', 'b' },
                { 'b', 'r', 'b', 'r' },
                { 'b', 'r', 'r', 'b' },
                { 'b', 'r', 'b', 'b' } };
        TicTocToe t = new TicTocToe(board);

        assertThat(t.getWinner(), equalTo('r'));
    }
}
