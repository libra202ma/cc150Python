"""
Imagine a web server for a simplified search engine. This system
has 100 machines to respond to search queries, which may then call out
using processSearch(string query) to another cluster of matchines to
actually get the result. The machine which responds to a given query
is chosen at random, so you can not guarantee that the same machine
will always respond to the same request. The method processSearch is
very expensive. Design a caching methanism to cache the results of the
most recent queries. Be sure to explain how you would update the cache
when data changes.
"""
