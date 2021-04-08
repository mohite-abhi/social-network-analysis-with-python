week-10

- rich become richer
	- so how come rich people come to be in the first place?
- download distribution of songs in different forems 
	- are different
	- due to rich get richer phenomenon
- questions raised
	- how can we subtract popularity obtained by rich get rich phenomynon, and detect right talent
	- how does one judge true value of entity
-more selling books to less selling books
	-  ![b49db7063c6b136fef790defb596f5ac.png](./_resources/62885d7590b349f393f96617e2fcd7f1.png)
	- ![f2e4cd13630a010304a282cce6529a76.png](./_resources/ba732f047d2e48ffa7533a756d779659.png)
	- this is known as long tail phenomenon
	
**Epidemic**
- is similar to diffusion of ideas in a network, except
	- here we don't have choice to not accepting
	- here we can't know who exactly gave us this disease

- spreadness of epidemic
	- degree of contagiousness
	- density of network
- simple branching process for modeling epidemic
	- if every node has k children
	- and probability of passing is p
	- then no. of spreads per node is pk
	- ![0a41eadbaff0f79949735a7b2207cc00.png](./_resources/0c59f74a3928435e8275a2074a959979.png)
	- this pk is called R<sub>0</sub>, basic reproductive number
	- meaning that if it is less than 1 then the epidemic will eventually die away
	- if R0 >= 0, then disease becomes epidemic

- knife edge property
	- the R0 is a very important number because if it is even a little more than 1 like 1.01, the disease will keep on growing, but even if it is like very less on left of 1, like 0.999, then we know for sure that the disease will eventually die away.
	- we can reduce this number by reducing pk, now we can reduce p with the help of measures like masks, social distance etc. while we can reduce k with the help of quaranteen

- relating studied model to covid scenario
	- https://www.youtube.com/watch?v=F9rBqddjypI

- graph models

	- sir model
		- susceptible (can get affected)
		- infected (can spread)
			- has a time Ti of being affecting
		- recovered/removed (can no longer spread)

	- sis model 
		- suseptible, infected, susceptible



- difference b/w sir & sis
	- sir
		- has two end configurations
			- either all nodes are recovered
			- or contagion dies out
	- sis
		- here only stops if contagion dies
		- can keep running forever
- percolation model
	- ![ac37bcc64fabd0a2bc212268fb318160.png](./_resources/1b03aaa54ad24253af3baf7a470e6654.png)
	- we flip coins for all the edges in the beginning itself
	- then wherever we got heads we open the pipes else we close them
	- now, we can predict if a node is affecteed by trasversing the open pipes from root

- analyzing basic reproductive number
	- ![9e1f9c85cb39a08e0a82eb22feb8b3db.png](./_resources/85556680b23745c1aed8351397072094.png)
	- ![c194110a413a37d1c7a53cbb4f7c387a.png](./_resources/4a420f0fac664d3ba78b221f2e8e341b.png)
	- ![8875d47e65069be6d7fbd2286055b9c7.png](./_resources/ec48e3130de04746bb1a39c508f6ebff.png)
	- above we have to prove first two statements
	- ![ce16548f266b2d8899f32e599044e0fd.png](./_resources/cf5003ebdbc44d2aa2bcadb1a92c4afc.png)
	- ![cb134f0dc48f26672953c176517a18b9.png](./_resources/a4974d6a392a413bb6355e3973f8d3b8.png)
	- ![613b9287b992e92411afde911790c399.png](./_resources/f789fa7f0c6640bdb0a506cab76bfeb6.png)
	- finding slope of the above function
	- ![231b8972d3d03cde2949ac6e7e855d4e.png](./_resources/511bd83007dc49d8bf5f86f7bb439747.png)
	- ![764714f9257b528a0867ef6a9d974266.png](./_resources/a44fa28a4b66461ba2ef8d06d4117d48.png)
	- ![544a98f20408c7206035407afdcdd37f.png](./_resources/9fe5edcdec0f4ac4b4e255b5211bd019.png)