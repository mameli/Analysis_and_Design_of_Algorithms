# Alberi binari

$ B_{n+1} =  \sum_{k=0}^{n}B_xB_{n-k}$

$ B= $ {insieme degli alberi binari}

$ |b|=$ numero dei nodi interni
$ B= \{\square\} \cup \{o\}\times B\times B $
i due progetti indicano i due rami che partono da un nodo

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
  t per nodi interni o
  w per nodi esterni $\square$
  $B(t,w) = w+tB(t,w)^2$

## Alberi s-ari

B = {L insieme di alberi s-ari}
$ |b|=$ numero dei nodi interni
$ B= \{\square\} \cup \{o\}\times B\times B \times ... \times B $ con s prodotti

$ B(t) =1+tB(t)^s $
$ B_n =  \frac{1}{(s-1)n+1} \binom{sn}{n} $

## Alberi ordinati

Un albero è un nodo (la radice) connesso ad una sequenza di alberi (foresta)

$G$ è la classe degli alberi ordinati
$F$ è la classi delle foreste

$F = S(G) = \{\epsilon\} \cup \{G\} \cup G \times G \cup G \times G \times G \cup...$

$ F(t) =  \frac{1}{1-G(t)} $

$ G= \{o\} \times F $
$ G(t) = tF(t) $ si sostituisce con l equazione di $F$

$ F(t) =  \frac{1}{1-tF(t)}  $
$ F(t)-tF(t)^2 -1 =0 $
$ = tF(t)^2 -F(t)+1 = 0$
$ F(t) =  \frac{1 \pm \sqrt{1-4t}}{2t} =  \frac{1-\sqrt{1-4t}}{2t} $

$ G(t) = tF(t) = \frac{1-\sqrt{1-4t}}{2}$

$ G_n = B_{n-1} $ con $  B_n =  \frac{1}{n+1} \binom{2n}{n} $

Quindi ha la stessa funzione degli alberi binari meno uno, infatti c'è una relazione tra alberi ordinati e alberi binari

---
$G(f_{n}) =  \sum_{n\geq0}^{}f_nt^n= f(t)$
$ [t^n] $ operatore "coefficiente di"
$ [t^n]  G(f_{n}) = f_n$
+ $ [t^n] (\alpha f(t)+ \beta g(t)) = \alpha [t^n]f(t)+\beta[t^n]g(t)$ linearità
+ $ [t^n] t f(t) = [t^{n-1}]f(t)$ spostamento
  $tf(t) = t  \sum_{k\geq0}^{}f_kt^k = \sum_{k\geq0}^{}f_kt^{k+1}$
+ $[t^n] f(t)g(t) =  \sum_{k=0}^{n}f_kg_{n-k}$ convoluzione
+ $[t^n] f(t) o g(t) =  \sum_{k\geq0}^{}f_k [t^n] g_t $ composizione

---
$f(t) =  \frac{1+t}{1-t-t^2}$

$[t^n] f(t) = [t^n]  \frac{1}{1-t-t^2}+ [t^n]  \frac{t}{1-t-t^2}$
$ = [t^n]t^{-1}  \frac{t}{1-t-t^2} = [t^{n+1}]  \frac{t}{1-t-t^2} = F_{n+1} $

$[t^n] f(t) = [t^n]  \frac{1}{1-t-t^2}+ [t^n]  \frac{t}{1-t-t^2} = F_{n+1}+F_n = F_{n+2}$

---
$ f(t) =  \frac{1-t}{1-2t}  $
$[t^n] f(t) = [t^n]  \frac{1}{1-2t}+ [t^n]  \frac{t}{1-2t} = 2^n - [t^{n-1}]  \frac{1}{1-2t} = 2^n-2^{n-1} = 2^{n-1}(2-1) = 2^{n-1}$

---
$ (1-t-t^2)F(t) = 1+t $   
$ [t^n] (1-t-t^2)F(t) = [t^n] (1+t) $
$ [t^n] F(t)-[t^n]tF(t-[t^n]t^2F(t) = [t^n] (1+t) $
Per $n>1 \ \ \ \ F_n -F_{n-1}-F_{n-2} = 0$
