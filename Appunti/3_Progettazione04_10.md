# Lezione 4 Ottobre

Formula degli scambi
$S_{n} =  \frac{n-2}{6}+  \frac{1}{n} \sum_{j=1}^{n}(S_{j-1}+S_{n-j})$

$\frac{n-2}{6}$ è il numero medio di scambi che il $SQ$ esegue durante il partizionamento
La seconda parte è analoga a quella dei confronti
$ \frac{1}{n} $ è la probabilità che il perno sia $j$

$[\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \ |j \ ]$
$[\underbrace{\ \ \ \ \ \ \ \ \ \ \ \ \ \ \  }_\text{<j}|j|  \underbrace{\ \ \ \ \ \ \ \ \ \ \ \ \ \ \  }_\text{>j}]$

> NB l ultimo scambio del perno non viene contato

$ p_{k}^{j} $ è la probabilità di fare $k$ scambi quando il perno è $j$
Per fare $k$ scambi nel partizionamento nella prima parte del vettore ci
sono $k$ elementi più gradi del perno e nella seconda parte $k$ elementi più piccoli.

Gli elementi più grandi del perno sono $n-j$ e quindi le possibilità sono il binomiale di $ \binom{n-j}{k} $, mentre $ \binom{j-1}{k} $ sono i modi di scegliere i più piccoli di $j$.
$$ p_{k}^{j} =  \frac{\binom{n-j}{k} \ \binom{j-1}{k} (j-1)!(n-j)!}{(n-1)!} $$
Si devono moltiplicare per il numero di permutazioni con j in ultima posizione. Le permutazioni dei $k$ elementi maggiori di $>j$ tra i primi $j-1$ elementi e le permutazioni dei $k$ elementi $< j$ tra gli ultimi $n-j$ elementi.

Numero medio di scambi quando il perno è $j$ :
$  \sum_{k \geq 0}^{} k p_{k}^{j} $ e la chiamiamo $ P^j $ si sviluppa in questo modo:

$  P^j=\frac{1}{ \binom{n-1}{j-1}}\sum_{k \geq 0} k  \binom{n-j}{k} \binom{j-1}{k}$

>N.B 1. $  \binom{n}{k} =  \frac{n!}{k! (n-k)!} $ e 2. $  \binom{n}{k} =  \binom{n}{n-k} $

sviluppando la parte $ \frac{(j-1)!(n-j)!}{(n-1)!} $ si arriva a $ \frac{1}{ \binom{n-1}{j-1}} $ e dato che non compare k allora si porta fuori dalla sommatoria.

Si sfrutta la formula di Vandermonde per semplificare la sommatoria.

$$  \sum_{k>0} \binom{r}{k} \binom{s}{n-k} =  \binom{r+s}{n} $$

# Sviluppo di $P^j$

$  P^j=\frac{1}{ \binom{n-j}{j-1}}\sum_{k \geq 0} k  \binom{n-j}{k} \binom{j-1}{k}$

Si scrive $\binom{j-1}{k}$ usando uguaglianza $ \binom{n}{k}=  \frac{n}{k} \binom{n-1}{k-1}$ come :
$$  \frac{(j-1)(j-2)!}{k(k-1)!(j-1-k)!} =  \frac{j-1}{k}  \binom{j-2}{k-1} $$

$ p^j= \frac{1}{ \binom{n-1}{j-1}}\sum_{k \geq 0} k  \binom{n-j}{k} \binom{j-1}{k}$ si sostituisce l ultima parte con $\frac{j-1}{k}  \binom{j-2}{k-1} $
$ k $ si semplifica e $j-1$ si porta fuori dalla sommatoria
$$\frac{j-1}{ \binom{n-j}{j-1}}\sum_{k \geq 0}   \binom{n-j}{k}  \binom{j-2}{k-1}$$

Si applica l'uguaglianza  $\binom{n}{k} =  \binom{n}{n-k} $ sul secondo elemento della sommatoria

Quindi $\binom{j-2}{k-1} =  \binom{j-2}{j-2-(k-1)} =  \binom{j-2}{j-1-k}$ da cui:

$$ \frac{j-1}{ \binom{n-1}{j-1}}\sum_{k \geq 0}   \binom{\overbrace{n-j}^\text{r}}{k}\binom{\overbrace{j-2}^\text{s}}{\underbrace{j-1-k}_\text{n - k}} $$

Usando l uguaglianza con la formula di Vandermonde si toglie la sommatoria e diventa:
$$\Rightarrow \frac{j-1}{ \binom{n-1}{j-1}}  \binom{n-2}{j-1}$$

Prendendo $r$ come $ n-j $ $, s $ come $ j-2 $ e $ n $ come $ j-1 $

I due binomiali si possono semplificare

$ P^j \ = (j-1) \frac{(n-2)!}{(j-1)!(n-1-j)!}  \frac{(j-1)!(n-j)!}{(n-1)!}$
$$ P^j= \frac{(j-1)(n-j)}{n-1}$$

questa è la probabilità quando $j$ è il perno.

Si deve capire qual è il numero medio di scambi tenendo conto della probabilità di $j$

$$  \frac{1}{n} \sum_{j=1}^{n}p^j $$

Numero medio di scambi durante il partizionamento (prima che i puntatori si incrorocino)

$  \frac{1}{n} \sum_{j=1}^{n} \frac{(j-1)(n-j)}{n-1} $

che si può semplificare

$  \frac{1}{n(n-1)}  \sum_{j=1}^{n}jn-j^2-n+j  $

si mette in evidenza $j$ e $jn$ e $j$ diventano la prima sommatoria $(n+1) \sum j$ che è la somma dei primi numeri interi.

La sommatoria di $n$ quadrati è uguale a $\sum^n j^2 =  \frac{n(n+1)(2n+1)}{6}$

$ =  \frac{1}{n(n-1)} [(n+1)\sum_{j=1}^{n}j-\sum_{j=1}^{n}j^2 - n\sum_{j=1}^{n} 1 ]$
$ = \frac{1}{n(n-1)}[ \frac{n(n+1)^2}{2}- \frac{n(n+1)(2n+1)}{6}-n^2] =$ $  \ \frac{n-2}{6}$

Una volta trovato $ \frac{n-2}{6} $ si deve sviluppare tutta l espressione.

$S_{n} =  \frac{n-2}{6}+  \frac{1}{n} \sum_{j=1}^{n}(S_{j-1}+S_{n-j})$

$S_{n} =  \frac{n-2}{6}+  \frac{2}{n} \sum_{j=0}^{n-1}(S_{j})$ si somma due volte la stessa quantità

$nS_{n} =  \frac{n(n-2)}{6}+  2 \sum_{j=0}^{n-1}(S_{j})$ si moltiplica per $n$

$n-1$ al posto di $n$

$ (n-1)S_{n-1} =  \frac{(n-1)(n-3)}{6}+  2 \sum_{j=0}^{n-2}(S_{j})$ Si fa la differenza

$ nS_n-(n-1)S_{n-1} =  \frac{n(n-2)}{6}- \frac{(n-1)(n-3)}{6}+2  \sum_{j=0}^{n-1}S_j -2 \sum_{j=0}^{n-2} S_j$

$ \qquad \qquad \qquad \quad \ \ \ \ = \frac{2n-3}{6}+2S_{n-1} $

$ nS_n =  \frac{2n-3}{6} +(n+1)S_{n-1} $

Divido per $n(n+1)$ e poi itero su $S_{n-1}$

$$  \frac{S_n}{n+1} =  \frac{2n-3}{6n(n+1)}+ \frac{S_{n-1}}{n} $$

Si ritrova di nuovo un espressione del tipo $ a_n = a_{n-1} + b_n $

$ a_n =a_{n-2} + b_{n-1}+ b_n = a_{n-3} + b_{n-2}+ b_{n-1} +b_n  = \ ...$

$  \frac{S_n}{n+1} =  \frac{2n-3}{6n(n+1)}+ \frac{2(n-1)-3}{6(n-1)(n+1-1)}+ \frac{S_{n-2}}{n-1} $

Ci si ferma a $S_{n-2}$ perché in questo caso è il primo valore noto.
Si deve praticamente trovare da dove parte k che è il denominatore di $\frac{S_x}{m}$
$$ \frac{S_n}{n+1} =   \sum_{k=3}^{n}  \frac{2k-3}{6k(k+1)}  + \frac{S_2}{3} $$

Condizioni iniziali $S_0 = S_1 =S_2= 0$ quindi

$$ \frac{S_n}{n+1} =   \sum_{k=3}^{n}  \frac{2k-3}{6k(k+1)}$$

Si usano di nuovo i numeri armonici di $H_n$
Il procedimento per spezzare la sommatoria è simile alla scomposizione per gli integrali. , quindi:
$  \frac{2k-3}{k(k+1)} =  \frac{A}{k} +  \frac{B}{k+1} $
$ =  \frac{A(k+1)+Bk}{k(k+1)} =  \frac{(A+B)k+A}{k(k+1)} $

$ A+B = 2$
$B=5 \Rightarrow A=-3 $

$ \frac{S_n}{n+1} =   \sum_{k=3}^{n}  \frac{2k-3}{6k(k+1)}$
$ =  \frac{1}{6} \sum_{k=3}^{n} [ \frac{-3}{k}+ \frac{5}{k+1}] $

$ = -\frac{1}{2}  \sum_{k=3}^{n} \frac{1}{k}+ \frac{5}{6} \sum_{k=4}^{n+1} \frac{1}{k}  $

$ =  -\frac{1}{2} [  \sum_{k=1}^{n} \frac{1}{k}-1- \frac{1}{2}]+  \frac{5}{6} \sum_{k=1}^{n+1} (\frac{1}{k}-1- \frac{1}{2} -\frac{1}{3})$

$ =  -\frac{1}{2}H_n+ \frac{3}{4}+ \frac{5}{6}H_{n+1}- \frac{55}{36} $

Si deve trasformare in $H_{n+1} = H_n +  \frac{1}{n+1}$
$H_{n} = H_{n+1} -  \frac{1}{n+1}$

Si sviluppa ancora:

$ =  -\frac{1}{2}H_{n+1}+  \frac{1}{2(n+1)}+  \frac{5}{6}H_{n+1}- \frac{7}{9} $

$$ \frac{S_n}{n+1} =  \frac{1}{3}H_{n+1}+ \frac{1}{2(n+1)}-  \frac{7}{9}$$

Si cerca di scriverlo il più simile a $S_n$

$ S_n =  \frac{1}{3}(n+1)H_{n+1} - \frac{7}{9}(n+1)+\frac{1}{2} $

Si mette in evidenza $(n+1)$

$$ S_n = \frac{1}{3}(n+1)(H_{n+1}- \frac{7}{3})+ \frac{1}{2} $$
