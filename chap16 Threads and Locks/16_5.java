/*

Suppose we have the following code:

public class Foo {
    public Foo() {...}
    public void first() {...}
    public void second() {...}
    public void third() {...}
}

The same instance of Foo will be passed to three different threads. ThreadA will call first, threadB will call second, and ThreadC will call third. Design a mechanism to ensure that first is called before second and second is called before third.

Use lock as status of method call.

Semaphore?

 */

import java.lang.Runnable;
import java.util.concurrent.locks.ReentrantLock;
import java.util.Random;

class Foo implements Runnable {
    ReentrantLock lock1;
    ReentrantLock lock2;
    ReentrantLock lock3;
    Random random;

    public Foo() {
        lock1 = new ReentrantLock();
        lock2 = new ReentrantLock();
        lock3 = new ReentrantLock();
        random = new Random();
    }

    public void first() {
        System.out.println("first(): Calling method first()...");
        // do something
        System.out.println("first(): Finishing method first()...");
        lock1.lock();
    }

    public void second() {
        System.out.println("second(): Calling method second()...");
        // wait for first()
        while (!lock1.isLocked()) {
            System.out.println("second(): Waiting for first()...");
            try {
                Thread.sleep(1);
            } catch (InterruptedException e) {
                System.out.println("Interrupted.");
            }
        }

        // do something

        System.out.println("second(): Finishing method second()...");
        lock2.lock();
    }

    public void third() {
        System.out.println("third(): Calling method third()...");
        // wait for second()
        while (!lock2.isLocked()) {
            System.out.println("third(): Waiting for second()...");
                try {
                    Thread.sleep(1);
                } catch (InterruptedException e) {
                    System.out.println("Interrupted.");
                }
        }
        // do something

        System.out.println("third(): Finishing method third()...");
        lock3.lock();
    }

    public void run() {
        // dispatch based on thread name
        if (Thread.currentThread().getName().equals("ThreadA")) {
            try {
                long time = (long)random.nextInt(10);
                System.out.println("ThreadA: sleeping for " + time);
                Thread.sleep(time);
            } catch (InterruptedException e) {
                System.out.println("Interrupted.");
            }
            first();
        } else if (Thread.currentThread().getName().equals("ThreadB")) {
            try {
                long time = (long)random.nextInt(10);
                System.out.println("ThreadB: sleeping for " + time);
                Thread.sleep(time);
            } catch (InterruptedException e) {
                System.out.println("Interrupted.");
                    }
            second();
        } else if (Thread.currentThread().getName().equals("ThreadC")) {
            try {
                long time = (long)random.nextInt(10);
                System.out.println("ThreadC: sleeping for " + time);
                Thread.sleep(time);
            } catch (InterruptedException e) {
                System.out.println("Interrupted.");
            }
            third();
        }
    }
}


class Main {
    public static void main(String[] args) {
        Foo foo = new Foo();
        Thread threadA = new Thread(foo, "ThreadA");
        Thread threadB = new Thread(foo, "ThreadB");
        Thread threadC = new Thread(foo, "ThreadC");

        threadA.start();
        threadB.start();
        threadC.start();
    }
}



// Local Variables:
// compile-command: "javac 16_5.java && java Main"
// End:
