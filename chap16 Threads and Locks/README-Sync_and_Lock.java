/*

  `synchronized` keyword applied to methods and code blocks to restricts multiple threads from executing the code simultaneously on the same object.

*/


/* Lock

Use to synchronize access to a shared resource by associating the resource with the lock. A thread gets access to a shared resources by first acquiring the lock associated with the resource. At at given time, at most one thread can hold the lock and, therefore, only one thread can access the shared resource.

 */

public class LockedATM {
    private Lock lock;
    private int balance = 100;

    public LockedATM {
        lock = new ReentrantLock();
    }

    public int withdraw(int value) {
        lock.lock();
        int temp = balance;
        try {
            Thread.sleep(100);
            temp = temp - value;
            Thread.sleep(100);
            balance = temp;
        } catch (InterruptedException e) {
            lock.unlock();
            return temp;
        }
    }

    public int deposit(int value) {
        lock.lock();
        int temp = balance;
        try {
            Thread.sleep(100);
            temp = temp + value;
            Thread.sleep(100);
            balance = temp;
        } catch (InterruptedException e) {
            lock.unlock();
            return temp;
        }
    }
}

/* Deadlock

A deadlock is a situation where a thread is waiting for an object that another thread holds, and this second thread is waiting for an object lock that the first thread holds(or an equivalent situation with several threads). Since each thread is waiting for the other thread to relinquish a lock, they both remain waiting forever.

- Mutual exclusion.
- Hold and wait.
- No preemption.
- Circular wait.

 */
