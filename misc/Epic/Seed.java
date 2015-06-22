/*

<http://www.careercup.com/question?id=13146677>

Find the seed of a number.

Eg: 1716 = 143 * 1 * 4 * 3 = 1716 so 143 is the seed of 1716. Find all
possible seed for a given number.

Brute force.

 */

import java.util.ArrayList;

public class Seed {

    public static ArrayList<Integer> getAllDigits(int n) {
        ArrayList<Integer> digits = new ArrayList<Integer>();
        while (n > 0) {
            digits.add(n % 10);
            n /= 10;
        }
        return digits;
    }

    public static ArrayList<Integer> getAllSeeds(int n) {
        ArrayList<Integer> seeds = new ArrayList<Integer>();

        for (int seed = (int) Math.sqrt(n); seed <= n; seed++) {
            if (n % seed != 0) {
                continue;
            }

            int n2 = seed;
            ArrayList<Integer> digits = getAllDigits(n2);
            for (int d : digits) {
                n2 *= d;
            }
            if (n2 == n) {
                seeds.add(seed);
            }
        }

        return seeds;
    }
}
