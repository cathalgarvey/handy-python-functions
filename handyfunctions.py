# Some really useful functions for Python 3

# Handy when you want to split a string into chunks,
# not just get every nth character. Works as a generator,
# so you first create it by calling it:
# $ >>> mystring = 'This string has a multiple of five characters'
# $ >>> mychunks = chunks(mystring, 5)
# Then use the generator for something:
# $ >>> for i in mychunks:
# $ >>>     print(i)
# $ This 
# $ strin
# $ g has
# ...etc.
def chunks(l, n):
    "Yield successive n-sized chunks from l."
    for i in range(0, len(l), n): yield l[i:i+n]

# Great for removing multiples of something from a list, helps
# to prevent nasty errors due to repeated operations when a list
# is iterated over.
# How does that magic "and not seen.add(x) bit work?
# Simple hack: If first item in an "and" expression evals False,
# the second is bypassed and never called. So if it evals True,
# (i.e. not in seen), seen.add(x) is called. Because set.add()
# doesn't return anything, applying "not" to it defaults to
# "not None" (presumably), which is True, so X is added to list.
def uniquify(self, seq):
    '''This is a fast, order-preserving function for removing duplicates 
    from a sequence/list, by "Dave Kirby"
    Found here: http://www.peterbe.com/plog/uniqifiers-benchmark'''
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]

# A missing feature from standard string methods is to return the indices
# of all instances of a substring; the standard methods only return the first!
def allindices(string, sub, offset=0):
    'Returns a list of ALL indices of a substring, not just first.'
    listindex = []
    i = string.find(sub, offset)
    while i >= 0: # Because find returns -1 when it finds nothing.
        listindex.append(i)
        i = string.find(sub, i + 1)
    return listindex
