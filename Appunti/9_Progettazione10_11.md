$ A = $ { insieme di strutture combinatorie}

 Insieme finito o numerabile di oggetti sul quale è definita una misura
$ \forall \alpha \in A, |\alpha| $

$ a(t) =     \sum_{}^{} t^{|\alpha|} = \sum_{}^{} a_nt^{n} $

$ a_n $ è il numero di oggetti $\alpha$ di $A$ tale che $|\alpha| = n $

Dati $A$ e $B$ classi di strutture si può fare l unione delle due classi.

e la funzione generatrice è determinabile facendo la somma delle funzioni generatrici.

$ A \cup B \qquad c(t) = a(t)+b(t)$

Per il prodotto cartesiano si ottiene invece il prodotto delle funzioni generatrici.

$ A \times B\qquad c(t) = a(t) \cdot b(t) =  \sum_{n\geq0}^{}\ \sum_{k=0}^{n} a_k b_{n-k} t^k $

Prendendo $\beta =$ { insieme stringhe binarie}
$|\beta| =$ lunghezza della stringa

$ \beta = \{\epsilon\} \cup \{0,1\} \times B \rightarrow b(t) = t^0+2t b(t)$
$ b(t) =  \frac{1}{1-2t} $
$t^0$ rappresenta epsilon
$t^2$ rappresenta {0,1}

---
Prendendo $\beta =$ { insieme stringhe binarie che non contengono 2bit 0 consecutivi}
$|\beta| =$ lunghezza della stringa

$ \beta = \{\epsilon\} \cup \{0\} \cup \{01,1\} \times \beta $
$ \rightarrow b(t) = t^0 + t + (t+t^2)b(t)  $
$ b(t) = \frac{1+t}{1-t-t^2}$ che assomiglia a fibonacci
quindi possiamo riscrivere $b(t)$
$ =  \frac{1}{1-t-t^2} +  \frac{t}{1-t-t^2} =  \frac{1}{t} F(t) + F(t) $

Con $F(t)  = 0+t+t^2+2t^3+3t^4+...$
$ G(t) = \frac{F(t)}{t} = 1+t+2t^2+3t^3+... $

$ F_3 = 2 $ e $ G_2 = 2 $  
C'è uno spostamento quindi $ G_n = F_{n+1} $

$ b_n = F_{n+1} +F_n = F_{n+2} $

---
Concatenazione di A si definisce come
$ C= S(A) = \epsilon \cup \{A\} \cup \{A \times A\} \cup \{A \times A \times A\} \cup... $

In generale la funzione generatrice $ C(t) = 1+a(t)+a(t^2)+ ... =  \sum_{k\geq0}^{} at^k =  \frac{1}{1-t}\  \circ  a(t) =  \frac{1}{1-a(t)} $

$ A=\{0,1\} \quad a(t) = 2t$
$ C(t) =  \frac{1}{1-2t} $

> Notazione $ A \times A = A^2$  

---
$ C= S_k(A) = A \times A \times A ... = A^k $ sequenze con esattamente k componenti
$ C(t) = a(t)^k $

---
$ C= S_{\geq k} =A^k \cup A^{k+1} ... $
$C(t)= a(t)^k +a(t)^{k+1}+... = a(t)^k(1+a(t)+a(t)^2) =  \frac{a(t)^k}{1-a{t}}$

---
$I=\{1,2,3,4,...\}$ interi maggiori o uguali di 1

$ x \in I , |x| = x $

$I(t) = t+t^2+t^3+... = t(1+t+t^2+...) =  \frac{t}{1-t}$

Si può anche ricavare in questo modo:
$ I = \{ \cdot,\cdot\cdot,\cdot\cdot\cdot,\cdot\cdot\cdot\cdot, etc.\}  = S_{\geq 1}(\{\cdot\}) =  \frac{t}{1-t}$

---
Composizioni di interi
$x=4$ in quanti modi posso arrivare a 4 facendo le composizioni degli interi positivi?
$4,3+1,2+2,1+3,1+1+2,2+1+1,1+2+1,1+1+1+1$

$C_n$ numero di composioni di n
$ C_4 = 8$
$ C= S(I) = \{\epsilon\} \cup I \cup I^2 \cup I^3$
$ C(t) =  \frac{1}{1-I(t)} =  \frac{1}{1-\frac{t}{1-t}} =  \frac{1-t}{1-2t}$
$ C(t) = \frac{1-t}{1-2t} = 1+t+2t^2+4t^3+8t^4+16t^5$
Nel caso $t^4$ si trova infatti 8

## Alberi binari

$ B_{n+1} =  \sum_{k=0}^{n}B_xB_{n-k}$

$ B= $ {insieme degli alberi binari}

$ |b|=$ numero dei nodi interni
$ B= \{\square\} \cup \{\circ\}\times B\times B $
i due $B$ indicano i due rami che partono da un nodo

$ B(t) = t^0+tB(t)^2 =1+tB(t)^2 $
$ =  \frac{1 \pm \sqrt{1-4t}}{2t}  $  
si esclude il caso positivo per le condizioni iniziali

$ \lim_{t\rightarrow 0} \frac{1 \pm \sqrt{1-4t}}{2t}  \frac{1+\sqrt{1-4t}}{1+\sqrt{1-4t}} = \lim_{t\rightarrow 0}  \frac{1-1+4t}{2t(1+\sqrt{1-4t})}$
$B(0) = B(1) = 1$
$ B_n =  \frac{1}{n+1}  \binom{2n}{n} $

---
Prendendo $ |b| = $ numero di nodi esterni $ \square $

$ B(t) = t+t^0B(t)^2 $
$ B(t) = t+B(t)^2 $
$ B(t)^2 -B(t)+t = 0$  
$ B(t) =  \frac{1 \pm \sqrt{1-4t}}{2} $

$B(0) = 0$ con questa condizione si prendono entrambi i casi.
C'è uno shift di uno rispetto al caso precedente
$ B_n =  \frac{1}{n}  \binom{2(n-1)}{(n-1)} $

> Le due funzioni si possono unire
  $t$ per nodi interni $\circ$
  $w$ per nodi esterni $\square$
  $B(t,w) = w+tB(t,w)^2$

## Alberi s-ari

$B = \{$L'insieme di alberi s-ari$\}$
$ |b|=$ numero dei nodi interni
$ B= \{\square\} \cup \{\circ\}\times B\times B \times ... \times B $ con s prodotti

$ B(t) =1+tB(t)^s $
$ B_n =  \frac{1}{(s-1)n+1} \binom{sn}{n} $

## Alberi ordinati

Un albero è un nodo (la radice) connesso ad una sequenza di alberi (foresta)

$G$ è la classe degli alberi ordinati
$F$ è la classi delle foreste

$F = S(G) = \{\epsilon\} \cup \{G\} \cup G \times G \cup G \times G \times G \cup...$

$ F(t) =  \frac{1}{1-G(t)} $

$ G= \{\circ\} \times F $
$ G(t) = tF(t) $ si sostituisce con l equazione di $F$

$ F(t) =  \frac{1}{1-tF(t)}  $
$ F(t)-tF(t)^2 -1 =0 $
$ = tF(t)^2 -F(t)+1 = 0$
$ F(t) =  \frac{1 \pm \sqrt{1-4t}}{2t} =  \frac{1-\sqrt{1-4t}}{2t} $

$ G(t) = tF(t) = \frac{1-\sqrt{1-4t}}{2}$

$ G_n = B_{n-1} $ con $  B_n =  \frac{1}{n+1} \binom{2n}{n} $

Quindi ha la stessa funzione degli alberi binari meno uno, infatti c'è una relazione tra alberi ordinati e alberi binari
