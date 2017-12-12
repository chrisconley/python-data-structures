
### collections.Counter

Uses `dict` under the hood. Calling `most_common()` uses either the builtin `sorted` method or a heap.

```python
def most_common(self, n=None):
    '''List the n most common elements and their counts from the most
    common to the least.  If n is None, then list all element counts.

    >>> Counter('abcdeabcdabcaba').most_common(3)
    [('a', 5), ('b', 4), ('c', 3)]

    '''
    # Emulate Bag.sortedByCount from Smalltalk
    if n is None:
        return sorted(self.items(), key=_itemgetter(1), reverse=True)
    return _heapq.nlargest(n, self.items(), key=_itemgetter(1))
```

### sorted()

Uses Timsort. Here's the [long description](https://github.com/python/cpython/blob/master/Objects/listsort.txt) and what [Wikipedia](https://en.wikipedia.org/wiki/Timsort) has to say:

> Timsort is a hybrid stable sorting algorithm, derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data. It uses techniques from Peter McIlroy's "Optimistic Sorting and Information Theoretic Complexity", in Proceedings of the Fourth Annual ACM-SIAM Symposium on Discrete Algorithms, pp. 467–474, January 1993. It was implemented by Tim Peters in 2002 for use in the Python programming language. The algorithm finds subsequences of the data that are already ordered, and uses that knowledge to sort the remainder more efficiently. This is done by merging an identified subsequence, called a run, with existing runs until certain criteria are fulfilled. Timsort has been Python's standard sorting algorithm since version 2.3. It is also used to sort arrays of non-primitive type in Java SE 7,[3] on the Android platform,[4] and in GNU Octave.[5]

### dict()

As of Python 3.6, the dictionary object is compact and sorted. The [source code file](https://github.com/python/cpython/blob/master/Objects/dictobject.c) has a nice description with additional links to more information and context.

From the source, the structure is as follows:

```text
+---------------+
| dk_refcnt     |
| dk_size       |
| dk_lookup     |
| dk_usable     |
| dk_nentries   |
+---------------+
| dk_indices    |
|               |
+---------------+
| dk_entries    |
|               |
+---------------+
```