week-5

**Spacial segregation**
- schellings model
	- as and when people are unhappy because their neighbours are below threshold value, they tend to migrate.

- code
	- [schellingModel.py](./_resources/d99c757231744faa942e1d17d706d473.py)


**Positive and negative relations**
- if a-b & a-c are friends and b-c hate each other, this can have two results
	- either b-c become friends
	- or either a-b remain friends and both hate c or  a-c remain friends and both hate b
- enimies enimy is a friend
- sweating together increases friendship/ love
- cases
	- 1) 3 friendships : stable
	- 2) 2 friendship, 1 hatered : unstable -> case 3 or case 1
	- 3) 1 friendship 2 hatered : stable
	- 4) 3 hatered : unstable -> case 3
- if there is a complete graph with all positive relations and if we intriduse 1 negative relation, then more and more negative relations emerge and cascade

**stable relationship graph**
- only two stable arrangements possible
	- all edges have positive relations
	- there are two groups of positive edges, and there are only negative edges between these two groups


- [balanceTheorem.py](./_resources/20447c74d24245aa9c4cf551e6275b80.py)

