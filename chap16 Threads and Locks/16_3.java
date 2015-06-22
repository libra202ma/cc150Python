/*

In the famous dining philosophers problem, a bunch of philosophers are sitting around a circular table with one chopstick between each of them. A philosopher needs both chopsticks to eat, and always picks up the left chopstick before the right one. A deadlock could potentially occur if all the philosophers reached for the left chopstick at the same time. Using threads and locks, implementing a simulation of the dining philosophers problem that prevents deadlock.

 */

/*

  The problem could be modeled like this. Init an circle array of forks. Init an circle array of philosophers, and each philosopher is between two folks. Each philosopher will sleep for a random time (for any reason) and then try to get(lock) the forks. First left fork, then right fork. When the philosopher have two forks, he sleep for a random time (to finish eat). Then release the forks.

There is possibility of lock in this approach, i.e., all philosophers have grabbed their left forks and are waiting for right forks.

To solve this, there are two approaches,

- check for locks after each try action. If deadlock is found, let all philosophers release their forks.

- change the try action. When the philosopher try to lock a fork, he will first check for availability of both left and right forks. If both are true, then lock the forks. Else, sleep for a random time.

 */

import java.lang.Runnable;
import java.util.concurrent.locks.ReentrantLock;
import java.util.Random;

class Philosopher implements Runnable {
    int id;  // philosopher id
    ReentrantLock leftCS;
    ReentrantLock rightCS;
    boolean done;  // indicate done or not?
    Random random;

    Philosopher(int id, ReentrantLock leftCS, ReentrantLock rightCS) {
        this.id = id;
        this.leftCS = leftCS;
        this.rightCS = rightCS;
        this.done = false;
        random = new Random();
    }

    public void run() {

        while (!done) {
            // sleep for 0~1s
            try {
                long time = random.nextInt(10);
                System.out.println("Philosopher " + id + " Sleeping for " + time + " ms...");
                Thread.sleep(time);
            } catch (InterruptedException e) {
                System.out.println("Interrupted.");
            }

            if (!leftCS.isLocked() && !rightCS.isLocked()) {
                leftCS.lock();
                rightCS.lock();
                System.out.println("Philosopher " + id +
                                   " Acquired chopsticks.");
                // finish eat
                try {
                    Thread.sleep((long)Math.random() * 1000);
                } catch (InterruptedException e) {
                    System.out.println("Interrupted.");
                }
                done = true;
                leftCS.unlock();
                rightCS.unlock();
            }
        }
    }
}

class Main {
    public static void main(String[] args) {
        int n = 7;
        ReentrantLock[] css = new ReentrantLock[n];   // declare array of chopsticks
        for (int i = 0; i < n; i++) {          // fill array
            css[i] = new ReentrantLock();
        }

        // init philosophers
        Philosopher[] p = new Philosopher[n];
        for (int i = 0; i < n; i++) {
            p[i] = new Philosopher(i, css[i], css[(i + 1) % n]);
        }

        // init threads
        Thread[] t = new Thread[n];
        for (int i = 0; i < n; i++) {
            t[i] = new Thread(p[i]);
        }

        // start threads
        for (int i = 0; i < n; i++) {
            t[i].start();
        }

    }
}

// Local Variables:
// compile-command: "javac 16_3.java && java Main"
// End:
