/*

Implement a `CircularArray` class that supports an array-like data structure which can be efficiently rotated. The class should use a genertic type, and should support iteration via the standard for (Obj O : circularArray) notation.

The enhanced for statement is merely syntactic suger, it works the same as traditional iterator method. So `.iterator()` should be implemented in the `CircularArray` class.

As for efficient rotating, one possible solution would be keep starting index of an array. When the array need to be rotated, just update the starting index. Of course, the iterator shall be specially tailored so that the array behaviors normally.

FIXME: the following code does not work, with the following exception

> Exception in thread "main" java.lang.ClassCastException: [Ljava.lang.Object; cannot be cast to [Ljava.lang.Integer;
>         at Main.main(14_6.java:62)

 */

import java.util.Iterator;
import java.lang.Iterable;

class CircularArrayIterator<T> implements Iterator<T> {
    CircularArray<T> ca;
    int i;

    public CircularArrayIterator(CircularArray<T> ca) {
        this.ca = ca;
        this.i = ca.start;
   }

    public boolean hasNext() {
        if (i < ca.start + ca.arr.length) {
            return true;
        } else {
            return false;
        }
    }

    public T next() {
        return ca.arr[i++ % ca.arr.length];
    }
}

class CircularArray<T> implements Iterable {
    public T[] arr;
    public int start = 0;

    public CircularArray(int size) {
        arr = (T[]) new Object[size];

        // for(int i = 0; i < arr.length; i++) {
        //     arr[i] = (T)0;
        // }
    }

    public void rotate(int r) {
        start = r % arr.length;
    }

    public Iterator<T> iterator() {
        return new CircularArrayIterator<T>(this);
    }
}

class Main {
    public static void main(String[] args) {
        CircularArray<Integer> ca = new CircularArray<Integer>(10);
        System.out.println(ca.arr[0]);
    }
}

// Local Variables:
// compile-command: "javac 14_6.java && java Main"
// End:
