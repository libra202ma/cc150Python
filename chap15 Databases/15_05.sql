/*

What is denormalization? Explain the pros and cons.

Pros: more efficient for frequent queries and operations.

Cons: data redundant. Careful when update records.

-- Referenced Answer

Denormalization is a database optimization technique in which we add redundant data to one or more table. This can help us avoid costly joins in a relational database.

By contrast, in a traditional normalized database, we store data in separate logical tables and attempt to minimize redundant data. We may strive to have only one copy of each piece of data in the database.

For example, in a normalized database, we might have a Courses table and a Teachers table. Each entry in Courses would store the teacherID for a course but not the teacherName. When we need to retrive a list of all Courses with the Teacher name, we would do a join between these two tables.

In some ways, this is great; if a teacher changes his or her name, we only have to update the name in one place.

The drawback, however, is that if the tables are large, we may spend an unnecessarily long time doing joins on tables.

Denormalization, then, strives a different compromise. Under denormalization, we decide that we're okay with some redundancy an some extra effort to update the database in order to get the efficiency advantages of fewer joins.

Pros of Denormalization:

- Retriving data is faster since we do fewer joins.
- Queries to retrive can be simpler (and therefore less likely to have bugs), since we need to look at fewer tables.

Cons of Denormalization:
- Updates and inserts are more expensive.
- Denormalization can make update and insert code harder to write.
- Data may be inconsistent. Which is the "correct" value for a piece of data?
- Data redundancy necessiates more storage.

In a system that demands scalability, like that of any major tech companies, we almost always use elements of both normalized and denormalized databases.

*/
