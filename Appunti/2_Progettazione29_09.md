# Quicksort
Esempio di quicksort con pseudocodice.
Si esaminano i contronti del quicksort. La parte importante è il partizionamento perché poi si effettuano solo due chiamate ricorsive. Ogni partizionamento dovrò confrontare il perno con tutti gli altri valori, quindi $n-1$ poi si dovrà aggiungere anche +2
Costo partizionamento $= n-1+2 = n+1$
perché si fanno una coppia di confronti arrivando allo scambio degli indici $i$ e $j$.

## Dimostrazione caso medio
I partizionamenti sono n.
Per come l algoritmo è sviluppato la posizione degli elementi ha un ruolo fondamentale.
Ci sono tre casi: ottimo, pessimo e medio.
Ottimo:   le partizioni sono più o meno simili.
Pessimo:  Una partizione è vuota e l altra è ha i restanti elementi. (Se il vettore è quasi ordinato o ordinato).

Nel caso pessimo si avrà $C_n$:
$C_n = C_{n-1}+n+1 \ \rightarrow C_n = O(n^2)$

Condizione iniziale $C_0 = 0$

$C_n = C_{n-2}+n +(n+1)$
$\quad \ =  C_{n-3}+(n-1) +n+  (n+1)$
$\quad \ =  C_{n-4}+(n-2) +(n-1)+ n+  (n+1)$
$\quad \ =  C_0 + 2+3+ ... + n + (n+1)$
$\quad \ =  \sum_{k=2}^{n+1} (k)$
Cioè la somma dei primi numeri interi partendo da 2 che è

$\sum_{k=0}^{n} (k) = \frac{n(n+1)}{2}$ è la formula di Gauss normale

$\sum_{k=2}^{n+1} (k)-1 = \frac{(n+2)(n+1)}{2} $ è la formula per $k=2$

# Quicksort caso medio

$a$ vettore di dimensione n
Si ipotizza che il vettore contenga una qualsiasi permutazione di n valori, i possibili input sono n! I valori sono tutti distinti mescolati a caso.
Si può dire che il vettore contiene i numeri da 1 a n (1,2,...,n)
Esaminiamo la versione dell algorimo in cui il perno sia l elemento a destra
$[\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ |j \ ]$
$[\underbrace{\ \ \ \ \ \ \ \ \ \ \ \ \ \ \  }_\text{<j}|j|  \underbrace{\ \ \ \ \ \ \ \ \ \ \ \ \ \ \  }_\text{>j}]$
Il primo sottovettore ha dimensione $j-1$ il secondo sottovettore $n-j$
Probabilità che il perno sia $j (j $ che divide il vettore con i partizionamenti simili$)$ è $\frac 1 n$ cioè $\frac{(n-1)!}{n!}$
Il numero medio di confronti, cioè arrivare a $j$ nel mezzo è
$C_n = (n+1)_{costo Partizionamento}$
$ \qquad  +\frac{1}{n}_{probalita Del Perno}$
$ \qquad * \sum_{j=1}^{n}[C_{j-1}+C_{n-j}]_{costo Chiamate Ricorsive}$

Condizione iniziale è $C_0 = 0$

Condizione iniziale ci porta a dire che $C_1 = 2$
Nella sommatoria ci sono le due quantità, il primo termine assumerà i valori da $C_0$ fino a $C_{n-1}$, il secondo da $C_{n-1}$ fino a $C_0$.
Dato che si somma due volte la stessa cosa si può scrivere
$C_n = (n+1) + \frac{2}{n}  \sum_{j=0}^{n-1}[C_{j}]$ si moltiplica tutto per $n$
$nC_n = n(n+1)+2 \sum_{j=0}^{n-1}[C_{j}]$
Si vuole eliminare la somma e si parte scrivendo la ricorrenza con $n-1$
$(n-1)C_{n-1} = (n-1)n+2 \sum_{j=0}^{n-2}[C_{j}]$
Facendo la differenza
$nC_n - (n-1)C_{n-1} = n(n+1)+2\sum_{j=0}^{n-1}[C_{j}] $ $-(n-1)n-2*\sum_{j=0}^{n-2}[C_{j}]$
$ \qquad \qquad \qquad \qquad \ = n(n+1)-(n-1)n+2*C_{n-1}$
$ \qquad \qquad \qquad \qquad \ = 2n + 2*C_{n-1}$

$nC_n - (n-1)C_{n-1} = 2n + 2*C_{n-1}$

$ \Rightarrow nC_{n} = 2n+(n+1)C_{n-1}$

Si vuole trasformare l espressione dividendo tutto per $n(n+1)$

$\frac{nC_{n}} {n(n+1)} = \frac{2n}{n(n+1)} + \frac{(n+1)C_{n-1}}{n(n+1)}$

$\underbrace{\frac{C_{n}}{n+1}} = \underbrace{\frac{2}{n+1} + \frac{C{n-1}}{n}}$
$\ \ a_{n}\qquad \quad \         a_{n-1}$

L'espressione è più semplice e senza la somma

Si itera su $ \frac{C_{n-1}}{n}$

$ \frac{2}{n+1} +  \frac{C{n-1}}{n} =  \frac{2}{n+1}+ \frac{2}{n}+ \frac{C_{n-2}}{n-1}$ questo passaggio si può iterare fino ad arrivare alla condizione iniziale

$ \frac{C_{n}}{n+1} =  \frac{2}{n+1} + \frac{2}{n} +
                       \frac{2}{n-1}+ \frac{2}{n-2} ...$

$ \ \ \ \quad          =  \sum_{k=3}^{n+1}  \frac{2}{k} +
                        \frac{C_{1}}{2}$

si sostituisce $C_{1}$ con 2 e si cambia il valore di k da cui si inizia la sommatoria
$= \sum_{k=2}^{n+1}\frac{2}{k}$

Si arriva a dire quindi che

$ \frac{C_{n}}{n+1} = 2  \sum_{k=2}^{n+1} \frac{1}{k}$

$H_{n} = \sum_{k=1}^{n}  \frac{1}{k}$ per i numeri armonici
Essendo quasi simile alla sommatoria ripresa dai numeri amonici a meno del K che parte da 2 si inserisce l' n-esimo numero armonico meno 1
$\frac{C_{n}}{n+1} =  2 \sum_{k=2}^{n+1} \frac{1}{k}$

$ \Rightarrow 2 \sum_{k=1}^{n+1} \frac{1}{k} -1$

Si toglie dal denominatore (n+1) e si ha:
${C_n}= 2(n+1)(H_{n+1}-1)$

###### Fine Dimostrazione

La formula precendente è per i confronti si dovrà studiare anche la formula per gli scambi. Si userà sempre lo stesso trucco sulle somme

# Formula degli scambi

$S_{n} =  \frac{n-2}{6}+  \frac{1}{n} \sum_{j=1}^{n}(S_{j-1}+S_{n-j})$
