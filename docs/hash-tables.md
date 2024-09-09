## Hash Tables

lecture 1: hashing and chaining

two types of db system: hash based and search-tree based

motivations (used all over the place)
     database
     compilers and interpreters
     ----uses of hashing----
     substring search
     substring commonalities
     files/dir synchronization (dropbox)


simple approach: 
     direct access table
     -store items in array indexed by key
     badness: 1. keys may not be integers, 2. gigantic memory hog, 3. 

Solution to problem 1 is pre-hashing
     - maps keys to non -ve integers
     - in theory, keys are finite and discrete (string of bits) so anything you have, can be mapped to an integer

but in python, hash(x) is the prehash of x
 - hash('\0B') == hash('\0\0C') but ideally hash(x) == hash(y) iff x == y
also you can use the GetHashCode() method of the underlying framework

Solution of problem 2: hashing
     - reduce universe U of all keys(integers) down to reasonable size M for table

keyspace() ---h()---> hashtable[ 0, 1, 2, 3.... m- 1 ]

- idea is to have m = theta(n).... n = no. of keys in the dictionary
but this would still lead to collision i.e., h(ki) == h(kj)

two methods to deal with hash-collision: chaining and open addressing

hashing function basically maps your universe to {0, 1, 2, ... m-1}
     h: U --> {0 1 2 ... m-1} 

simple uniform hashing
each key is equally likely to be hashed to any slots of the table, independent of where other keys hashing.

analysis: 
     - expected length of a chain: so for n keys and m slots it is 
          = n/m (1/m + 1/m + 1/m ..) = alpha = load factor
          it will be constant: theta(1) if m = theta(n)
     ==> running time = O ( 1 + | length of chain | ) = O (1 + alpha)
               as long as alpha is constant, we have constant time

good hash function

     A division method: h(key) = key mod m  ( simple but bad if m and key are both even, you'll use only half the table)
     in practice is good if m is a PRIME number and if m is not close to power of 2 and 10


     B multiplication method: h(key) = [ (a * key) mod 2^w ] >> (w - r)
                                                k --> w bit machine
                                                a --> random integer of same bits as key

(a.key) : [0101001001] (key) * [1001011011] (a) --> [ | ] (word twice the size of key 2w)

(a.key) mod 2^w : gets you the right half  [-------|1001011011]
[ (a.key) mod 2^w ] >> (w - r) : take r bits from center and to the right
                                                     [-------|1001011011]     (this value will be between 0 to m-1, because m = 2^r
                    a should be odd and not close to power of 2
                    m = 2^r

     C Universal Hashing: h(key) = [ (a * key + b) mod p ] mod m
                                                       a, b --> random between {0 ... p - 1}
                                                       p --> prime number > size of Universe (basically a big prime number)


for worst case keys key-1 != key-2:
                                 probability{ h(k1) == h(k2)} = 1/m probability of hash collision
                                 a, b

example of a string hash function:
     foreach char c in key
          val = (val * prime + c) % length;

lecture - 2 table doubling, karp-rabin
     
     what should m be ?
          we want it to be big enough for n/m to be low and small enough so that we don't waste a lot of space.
          we want m = theta(n) so that alpha = theta(1)

Idea 1: start small: m = 8
            grow and shrink as necessary
          
     if n > m: grow table m --> m' which is or the order: theta (n + m + m')
              - make table of size m'
              - build new hash h' (since m has changed)
              - rehash:
                    for item in T:
                         T'.insert(item)
     Amortization
          -operation takes "T(n) amortized"
            if k operations take  <= k * T(n) time 
            think of meaning ~ "T(n) on average" where the average is taken over all the operations
            therefore in table doubling k inserts take theta(k) ==> theta(1) amortized/insert.
            Also, k inserts and deletes take O(k)
     
     Deletion: 
          A. if m = n/2 then shrink --> m/2 slow because 2 ^ k ---insert---> 2 ^ k + 1 and then 2 ^ k <---delete--- 2 ^ k + 1 this will lead to constant expansion and deletion on insert and delete causing these operation to be theta(n)
          B. if m = n/4 then shrink --> m/2 amortized time --> theta(1)
               n <= m <= 4n  in short deletion constant has to be smaller than the insertion constant

String matching (Karp-Rabin)
     given two strings s and text : does s occur as a substring of text ?

simple algorithm :
     any (s == text [i : i + len(s)]
          for i in range (len(text) - len(s)))     //no. of iterations is len(t) - len(s)
   
     Time: theta(len(s) * len(text - s)) ~ theta( |s| * |text| )

Rolling hash ADT
     given a rolling hash value, lets say r we'd like to append a character
          r.append(c)
               add character c to the end of X
               r.skip(c) delete the first character of X (assumit it is c)
          r maintains a string X
               - r(): hash value of x = h(x)

Karp-Rabin algorithm
for c in s: 
     rs.append(c)
     
for c in text[:len(s)]:
     rt.append(c)
     
if rs() == rt(): ---
for i in range (len(s), len(text)):
     rt.skip( text[i - len(s)]
     rt.append(text[i])

check whether
     s == text[i - len(s) + 1 : i + 1]
equal?
     found match
else
     happens with probability  <= 1/|s|

therefore, O( |s| + |text| + #match * |s| )

we can use the division method to hash: h(key) = key mod m (m --> random prime >= |s|)
     treat X as multidigit number U in base a alphabet size

r.append(c) works as follows
     U -> U * a + ord(c)        multiply by a (shift left) and add by c
Similarly,
     r -> r * a + ord(c) mod m
r.skip() works as follows
     U -> U - c * a ^ |x| - 1


lecture - 3 Open addressing, cryptographic hashing

Open addressing
     no chaining       only one item per slot, m => n, m = # of slots, n = # of elems
     [item 1]
     [item 2]
     [item 3]
          .
          .

Probing
     hash functions specifies order of slots to probe for a key for insert/search/delete
     h : U * { 0, 1, 2, .... m - 1} (trial count)  ( U: universe of keys)

h(k, 1) ; h(k,2) . . . . . h(k, m - 1)
arbitrary key k          to be a permutation of 0, 1, ... m - 1
.
.

probing strategies
     linear probing: h(k, i) = (h'(k) + i) mod m          h' is an ordinary hash function
                                                                                   does satisfy the permutation requirement
     cluster: consecutive groups of occupied slots which keep longer.

double hashing
     h(k, i) = ( h1 (k) + i * h2 (k) ) mod m
          if h2(k) is relatively prime from => permutation
     m = 2 ^ r , h2(k) for all k is odd.


Uniform Hashing Assumption ...... != simple uniform hashing
     each key is equally likely to have any one of the m ! permutations as its probe sequence. 

alpha = n/m  cost of operations insert <= 1 / (1 - alpha)     as alpha tends to 1, this value grows. ( in practice you have to resize table when alpha reaches around 0.5-0.6)
one issue is series of deletes will lead to lots of delete-me flag and hence search will be sluggish 





