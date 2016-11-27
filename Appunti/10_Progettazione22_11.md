# Medoto simbolico

$ A, \alpha \in A , |\alpha| $
$ a(t) =     \sum_{\alpha \in A}^{} t^{|\alpha|} = \sum_{\geq0}^{} a_nt^{n} $

Si applica il metodo per i linguaggi, in particolare per linguaggi regolari o context free.
Si può fare unione di espressioni regolari $ e_1 \cup e_2 $ oppure usare la star $(*)$ o la concatenazione $ e_1 \cdot e_2 $

La funzione generatrice associata all unione è la somma $ e_3(t)= e_1(t)+e_2(t) $, per la star $ 1+e_1(t)+e_1(t)^2+... =  \frac{1}{1-e_1(t)} $

+ Esempio
  $e = (1+01+00+0001)^*(\epsilon+0+00+000)$
  Non ci sono più di 3 zeri consecutivi
  $ |\alpha| =$ lunghezza della parola
  $1+01+001+0001 \rightarrow t+t^2+t^3+t^4$
  $e_1 = (1+01+001+0001)^* \rightarrow  \frac{1}{t+t^2+t^3+t^4}$
  $e_2 = (\epsilon+0+00+000) \rightarrow t+t^2+t^3$
  $\sum_{i=0}^{k}t^i = \frac{1-t^{k+1}}{1-t} $
  $ e = e_1 \cdot e_2 \rightarrow  \frac{t+t^2+t^3}{1-(t+t^2+t^3+t^4)}    =  \frac{ \frac{1-t^4}{1-t}}{1-t \frac{1-t^4}{1-t}} = \frac{1-t^4}{1-t}  \frac{1-t}{1-t-t-t^5} =  \frac{1-t^4}{1-2t+t^5} $
  $\ \ = 1+2t+4t^2+8t^3+15t^4+29t^5+\dots$

Parole del linguaggio che contengono $ abb $
$ A = {a,b} $
Si usa un automa a stati finiti che accetta la stringa $abb$ con d stato finale

```{mermaid}
graph LR
a --a--> a;
a --a-->b;
b --a-->b;
b --b-->c;
c --a-->b;
c --b-->d;
d --ab-->d
```
$b^* (a^+b)^+b(a \cup b)^*$
$ b \rightarrow t $
$ b^*  \rightarrow  \frac{1}{1-t}$
$ (a^+b)\rightarrow   \frac{t}{1-t}t =  \frac{t^2}{1-t}$
$ (a^+b)^+ \rightarrow  \frac{t^2}{1-t} / (1- \frac{t^2}{1-t})$
$ (a \cup b) \rightarrow 2t$
$ (a \cup b)^* \rightarrow  \frac{1}{1-2t} $
$ e \rightarrow  \frac{1}{1-t}  \frac{ \frac{t^2}{1-t}}{1-\frac{t^2}{1-t}} t  \frac{1}{1-2t}=   \frac{t^3}{(1-t)(1-2t)(1-t-t^2)}$

$ L_0 :: = aL_1 | bL_0$ $\rightarrow$ $L_0(t) = tL_1(t)+tL_0(t) $
$ L_1 :: = aL_1 | bL_2$ $\rightarrow$ $L_1(t) = tL_1(t)+tL_2(t) $
$ L_2 :: = aL_1 | bL_3$ $\rightarrow$ $ L_2(t) = tL_1(t)+tL_3(t) $
$ L_3 :: = aL_3 | bL_3$ $\rightarrow$ $ L_3(t) = tL_3(t)+tL_3(t) $

Si associa ad ogni simbolo non terminale una gunzione generatrice $L_i(t)$ e l'unione diventa una somma. Traduco la grammatica i un sistema di formule e si vuole trovare $L_0(t)$

$ T = \left
  (\begin{array}{ccc}
  1 & 1 & 0 & 0 \\
  0 & 1 & 1 & 0 \\
  0 & 1 & 0 & 1 \\
  0 & 0 & 0 & 2
  \end{array}\right) $ $ L = \left
    (\begin{array}{ccc}
    L_0(t)\\
    L_1(t)\\
    L_2(t)\\
    L_3(t)    
    \end{array}\right) $

$ T(i,j)$ = in quanti modi mi sposto da $ L_i \rightarrow L_j $ = Matrice di transazione di stato.
$ u = (1,0,0,0) $ prima colonna
$ v = (0,0,0,1)^t $
$ L_0 = u( I-tT)^{-1} v $

$ \left
  (\begin{array}{ccc}
  L_0(t)\\
  L_1(t)\\
  L_2(t)\\
  L_3(t)    
  \end{array}\right) =
  t
  \left
    (\begin{array}{ccc}
    1 & 1 & 0 & 0 \\
    0 & 1 & 1 & 0 \\
    0 & 1 & 0 & 1 \\
    0 & 0 & 0 & 2
    \end{array}\right)
  \left
      (\begin{array}{ccc}
      L_1(t)\\
      L_1(t)\\
      L_1(t)\\
      L_1(t)    
  \end{array}\right)+
  \left
    (\begin{array}{ccc}
    0\\
    0\\
    0\\
    1    
    \end{array}\right)
$

$ I L-tTL   = v $ in cui $I$ è la matrice identità
$ (I -tT)L  = v $
$ L = (I-tT)^{-1} v  $

$u$ serve per prendere sola la prima componente $ \Rightarrow L_0 = u(I-tT)^{-1}v $
$ v $ contiene tutti $0$  tranne nella posizione che corrisponde allo stato finale.
---
G automa deterministico a stati finiti
$Q = \{q_1,q_2,q_3,...q_5\}$ insieme degli stati
$ q_0 $ stato iniziale
$ \dot Q = \{\dot q_1,\dot q_2\} $ insieme degli stati finali

La f.g del linguaggio accettato dell'automa è una f.g. razionale fratta che in forma matriciale si può esprimere nel modo seguente:
$ L(t) = u (I-tT)^{-1}v $
dove $ T_{i,j} = card\{ \alpha \in A,$ t.c. esiste un arco da $q_i \rightarrow q_j $ etichettato $\alpha \} $  
$ u = (1,0,\dots,0) $
$ v = (v_0,\dots,v_j)^t $
$ v_i = [ q_i \in \dot Q] = 1 $ se $q_i$ è stato finale 0 altrimenti  

---
$p = abb $
$ f(t) =  \frac{t^3}{(1-t)(1-2t)(1-t-t^2)} $ f.g. che conta le parole su $A= \{a,b\}$ che contengono p = abb
Qual è la funzione generatrice delle parole su $A=\{a,b\}$ che non contengono p?
$(a \cup b)^* \qquad  g(t)=\frac{1}{1-2t}$
$ h(t) = g(t)-f(t) $ f.g. che conta le parole che non contengono p

# Guibas e Oblyzko
Prendiamo $p = abb $  e costruiamo il seguente diagramma

$
\begin{array}{lcr}
\mbox{abb} & CodaPattern & esito \\
\mbox{abb} &  & 1 \ L_0\\
\mbox{ab} & b & 0 \ L_1\\
\mbox{a} & bb & 0 \ L_2\\
\end{array}
$
Metto 1 o 0 a seconda se c'è corrispondenza tra le stringhe
$ L(t) =  \sum_{}^{}c_it^i = c_0t^0+c_1t^1+c_2t^2=1$ Polinomio di correlazione

Per trovare la funzione generatrice di un linguaggio che evita un pattern basta trovare il polinomio di correlazione, poi $ L(t) =  \frac{c(t)}{t^k+(1-mt)c(t)} $
con $k = $cardinalità di $p = |p|$ e $m= |A|$

Per $p = abb$ abbiamo $k = 3$ e $m = 2$
$L(t) =  \frac{1}{t^3+(1-2t)*1}$
$  \frac{1}{1-2t} -  \frac{t^3}{(1-t)(1-2t)(1-t-t^2)} =  \frac{1}{1-2t+t^3} \qquad\blacksquare$
