import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;

import static org.hamcrest.CoreMatchers.*;
import static org.junit.matchers.JUnitMatchers.*;
import static org.junit.Assert.*;

public class SeedTest {

    @Test
    public void testGetAllDigits() throws Exception{
        ArrayList<Integer> target = new ArrayList<Integer>(Arrays.asList(3, 4, 1));
        assertThat(Seed.getAllDigits(143), equalTo(target));
    }

    @Test
    public void testGetAllSeeds() throws Exception {
        ArrayList<Integer> target = new ArrayList<Integer>(Arrays.asList(143));
        assertThat(Seed.getAllSeeds(1716), equalTo(target));
        target = new ArrayList<Integer>(Arrays.asList(11));
        assertThat(Seed.getAllSeeds(11), equalTo(target));
    }
}
