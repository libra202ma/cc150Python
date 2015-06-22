/* Thread and Process

Both processes and threads are independent sequences of execution.The typical difference is that threads (of the same process) run in a shared memory space, while processes run in separate spaces.

Process
Each process provides the resources needed to execute a program. A program has a virtual address space, executable code, open handles to system objects, a security context, a unique process identifier, environment variables, a priority class, minimum and maximum working set sizes, and at least one thread of execution. Each process is started with a single thread, often called the primary thread, but can create additional threads from any of its threads.

Thread
A thread is the entity within a process than can be scheduled for execution. All threads of a process share its virtual address space and system resources. In addition, each thread maintains exception handlers, a scheduling priority, thread local storage, a unique thread identifier, and a set of structures the system will use to save the thread context until it is scheduled. The thread context includes the thread's set of machine registers, the kernel stack, a thread environment block, and a user stack in the address space of the thread's process. Threads can also have their own security context, which can be used for impersonating clients.

 */


/*

In Java, there are two ways to implement thread

- By implementing the `java.lang.Runnable` interface
- By extending the `java.lang.Thread` class.

 */

// Implement the Runnable Interface

public interface Runnable {
    void run();
}

/*
1. Create a class which implements the Runnable interface. An object of this class is a Runnable object.
2. Create an object of type Thread by pass a Runnable object as argument to the Thread constructor. The Thread object now has a Runnable object that implements the run() method.
3. The start() method is invoked on the Thread object created in the previous step.
 */

public class RunnableThreadExample implements Runnalbe {
    public int count = 0;

    public void run() {
        System.out.println("RunnalbeThread starting.");
        try {
            while (count < 5) {
                Thread.sleep(500);
                count++;
            } catch (InterruptedException exc) {
                System.out.println("RunnableThread interrupted.");
            }
            System.out.println("RunnableThread terminating.");
        }
    }
}

public static void main(String[] args) {
    RunnableThreadExample instance = new RunnableThreadExample();
    Thread thread = new Thread(instance);
    thread.start();

    /* waits until above thread counts to 5 (slowly) */
    while (instance.count != 5) {
        try {
            Thread.sleep(250);
        } catch (InterruptedException exc) {
            exc.printStackTrace();
        }
    }
}


// Extending the Thread Class

public class ThreadExample extends Thread {
    int count = 0;

    public void run() {
        System.out.println("Thread starting.");
        try {
            while (count < 5);
            System.out.println("In thread, count is " + count);
            count++;
        } catch (InterruptedException exc) {
            System.out.println("Thread interrupted.");
        }
        System.out.println("Thread terminating.");
    }
}

public class ExampleB {
    public static void main(String[] args) {
        ThreadExample instance = new ThreadExample();
        instance.start();

        while (instance.count != 5) {
            try {
                Thread.sleep(250);
            } catch (InterruptedException exc) {
                exc.printStackTrace();
            }
        }
    }
}

/*

Extending the Thread Class vs Implementing the Runnable Interface

Implementing the RUnnable Interface may be preferable.

- Java does not support multiple inheritance. Therefore, extending the Thread class means that the subclass cannot extend any other class. A class implementing the Runnable interface will be able to extend anotehr class.
- A class might only be interested in being runnable, and therefore, inheriting the full overhead of the Thread class would be excessive.

 */
