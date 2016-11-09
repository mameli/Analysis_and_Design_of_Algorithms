# Binomiali

Si vuole generalizzare i binomiali sui numeri reali.

## Permutazioni
Per $n$ oggetti in quanti modi si possono mescolare? Per :
$ a_1, a_2 ,a_3,... $

Si indica con $ P_n = $numero di permutazioni di lunghezza $n$

Per esempio se $ n=3 $

$ a_1, a_2 ,a_3 $
$ a_1, a_3 ,a_3 $
$ a_2, a_1 ,a_3 $
$ \ \quad ... $

$ P_3  = 6 $ in questo caso.

Aggiungendo un numero le permutazioni saranno

$ P_{n+1} = (n+1)P_n$  

$ P_0 = P_1 = 1$

Se si sviluppa fino a zero si ha:
$(n+1)P_n = (n+1)n(n-1)\ ...\ P_0 = (n+1)!$  

Quindi $ P_n = n! $

## Disposizioni

Per n oggetti quanti sono i gruppi dato k?
Si indicano con $ D_{n,k} = $ numero di disposizioni di n oggetti in gruppi di k
Per esempio $n=4$ e $k=2$ di $a,b,c,d$ cioè $D_{4,2} = 12$
$(a,b),(b,a),(a,c),(c,a),(a,d),(d,a),(b,c),(c,b),(b,a),(d,b),(c,d),(d,c)$

$ D_{n,k} = n(n-1)(n-2)...(n-k+1) $

## Combinazioni

Si scelgo tra n oggetti gruppi di k senza contare l ordine.

$ C_{n,k} =$ numero di combinazioni di $k$ oggetti su $n$ a disposizione
Si deve dividere per il numero di modi in cui si possono scambiare gli elementi nel gruppo, cioè le permutazioni di $k$ cioè $k!$
$$ C_{n,k} =  \frac{D_{n,k}}{k!} =\frac{n(n-1)(n-2)...(n-k+1)}{k!}$$
Le combinazioni si indicheranno con il binomiale:
$$\binom{n}{k} = C_{n,k}$$

$$\binom{n}{k} =\frac{n(n-1)(n-2)...(n-k+1)(n-k)(n-k-1)...1}{k!(n-k)(n-k-1)...(1)} =  \frac{n!}{k!(n-k)!} $$
### Proprietà dei binomiali
$$ \binom{n}{k}=  \frac{n(n-1)!}{k!(k-1)!(n-k)!}=  \frac{n}{k} \binom{n-1}{k-1} $$

$$ \binom{n}{k} =  \binom{n}{n-k} $$

### Binomiale su reali

Se si guarda $\frac{D_{n,k}}{k!} =\frac{n(n-1)(n-2)...(n-k+1)}{k!}$

$k$ deve essere per forza un intero ma il numeratore si può sviluppare anche sui reali

$ \binom{r}{k} = \frac{r(r-1)(r-2)...(r-k+1)}{k!}  $ con $r$ reale
Si chiamano binomiali per la relazione che c'è tra le potenze dei binomi.
$ (a+b)^n =  \sum_{}^{n}  \binom{n}{k} a^kb^{n-k} $
I binomi si possono anche scrivere come:

$ (a+b)^n = a^n(1+ (\frac{b}{a})^n) $

Si usano gli sviluppi di Taylor

$ f(z) = (1+z)^r =  \sum_{k\geq 0} \frac{f^{(k)}(0)}{k!}z^k $

$ f(z)= (1+z)^r $
$ f^{'}(z) = r(1+z)^{r-1}$
$ f^{''}(z) = r(r-1)(1+z)^{r-2}$
$ f^{k}(z) = r(r-1)(r-2)...(r-k+1)(1+z)^{r-k} $
$ f^{k}(0) = r(r-1)(r-2)...(r-k+1) $

Quindi

$ f(z) = (1+z)^r =  \sum_{k\geq 0} \frac{f^{(k)}(0)}{k!}z^k =  \sum_{k\geq 0}  \frac{r(r-1)(r-2)...(r-k+1) z^k}{k!}$

$$ =  \sum_{k\geq 0}  \binom{r}{k}z^k$$

Ad esempio

$  \binom{1/2}{3}  =  \frac{1/2 (1/2-1)(1/2-2)}{3!} =  \frac{1}{16}$

### Proprietà per i reali

#### Numeri Negativi
$  \binom{-n}{k} =  \frac{-n(-n-1)...(-n-k-1)}{k!}$

$ \qquad = (-1)^k  \frac{n(n+1)(n+2)...(n+k+1)}{k!}  \frac{1*2 ...(n-1)}{1*2 ... (n-1)}$

$ \qquad = (-1)^k  \frac{(n+1-k)!}{k!(n-1)!} = (-1)^k  \binom{n+k-1}{k} $

Se ci da noia un numero negativo quindi si può trasformare

$$ \binom{-n}{k} = (-1)^k  \binom{n+k-1}{k} $$

#### Triangolo di Tartaglia

$  \binom{n}{k} =   \binom{n-1}{k}+ \binom{n-1}{k-1} $

Condizioni iniziali
$  \binom{n}{0} =  \binom{n}{n} = 1 $

| n/k            |  0             |1               |2              | 3             |4             |5             |
| :------------- | :------------- |:-------------  |:------------- | :-------------|:-------------|:-------------|
| 0              | 1              |0               |0              | 0             |0             |0             |
| 1              | 1              |1               |0              | 0             |0             |0             |
| 2              | 1              |2               |1              | 0             |0             |0             |
| 3              | 1              |3               |3              | 1             |0             |0             |
| 4              | 1              |4               |6              | 4             |1             |0             |
| 5              | 1              |5               |10             | 10            |5             |1             |

Si può vedere che il triangolo è simmetrico e che alla riga n la somma degli elementi
corrisponde a $ 2^n $ . La riga rappresenta il numero totale di sottoinsiemi in un
insieme di n elementi, che è ovviamente $ 2^n $ .

I numeri $ c_n =  \binom{2n}{n} $ sono chiamati binomiali centrali. Ad esempio
Se 2n = 4 e n = 2 il binomiale centrale è 6.

Per calcolare il binomio  $\binom{- \frac{1}{2}}{n} $ si usano i coef. centrali.
$\binom{- \frac{1}{2}}{n}  =  \frac{(-1/2)(-3/2)...(-(2n-1)/2)}{n!}  $

$\binom{- \frac{1}{2}}{n}  =  (-1)^n \frac{( \frac{1}{2})(\frac{3}{2})...(( \frac{2n-1}{2}))}{n!}$

Si mette in evidenza il 2 dei denominatori poi si moltiplica per i pari sopra e sotto. Si evidenzia i due dei pari.

$   \frac{(-1)^n}{2^n}  \frac{1*3...(2n-1)}{n!}  \frac{2*4*6...2n}{2*4*6...2n} =  \frac{(-1)^n (2n)!}{2^n(n!) 2^n (n!)}$

$  = \frac{(-1)^n (2n)!}{4^n(n!)(n!)} = \frac{(-1)^n}{4^n} \binom{2n}{n}$

In modo simile per altri valori sarà ad esempio:

 $  \binom{1/2}{n}= \frac{(-1)^{n-1}}{4^n (2n-1)} \binom{2n}{n}$

$  \binom{3/2}{n}= \frac{(-1)^n3}{4^n (2n-1)(2n-3)} \binom{2n}{n}$
