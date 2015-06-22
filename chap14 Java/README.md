Tell the interviewer, "I am not sure I can recall the answer, but let me see if I can figure it out. Suppose we have this code ..." and try the following approaches,

- Create an example of the scenario, and ask yourself how things should play out.
- Ask yourself how other languages should handle this scenario.
- Consider how you would design this situation if you were the language designer. What would the implications of each choice be?

GOOD POINT!

## Constructor

- Constructors never have an explicit return type.
- Constructors cannot be directly invoked (the keyword "new" invokes them).
- Constructors cannot be synchronized, final, abstract, native or static.

1. Initialize the class variable to default values.
2. Call default constructor of the superclass if no constructor is defined.
3. Initialize member variables to the specific values.
4. Executes the body of the constructor.

## Enhanced for

    for (FormalParameter : Expression) Statement

same as

    for (I #i = Expression.iterator(); #i.hasNext();) {
        TargetType Identifier = #i.next();
        Statement
    }


## Useful collection framework

`ArrayList`: dynamically resizing array, which grows as you insert elements.

    ArrayList<String> myArr = new ArrayList<String>();
    myArr.add("one");
    myArr.add("two");
    System.out.println(myArr.get(0))

`Vector`: almost same as `ArrayList`, except it is synchronized when used in multi-thread.

`LinkedList`: Doubled linked list implementation of the List and Deque interfaces.

    LinkedList<String> myLinkedList = new LinkedList<String>();
    myLinkedList.add("two");
    myLinkedList.one("one");
    Iterator<String> iter = myLinkedList.iterator();
    while (iter.hasNext()) {
        System.out.println(iter.next());
    }

`HashMap`: widely used.

    HashMap<String, String> map = new HashMap<String, String>();
    map.put("one", "uno");
    map.put("two", "dos");
    System.out.println(map.get("one"));
