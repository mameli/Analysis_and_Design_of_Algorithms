# Funzioni di ricorrenza del Quicksort

$ C_n = n+1 + \frac{2}{n}  \sum_{j=0}^{n-1} C_j $

$ S_n = \frac{n-2}{6}+  \frac{2}{n} \sum_{j=0}^{n-1}(S_{j})$

$ nC_n = n(n+1)2 \sum_{j=0}^{n-1} C_j \qquad$ con $C_0 = 0$ e $C_1 = 2$

Si applica la linearità
$G(nC_{n}) =  G(n(n+1))+ 2  G( \sum_{j=0}^{n-1}C_j)$ -->shift indietro poi convoluzione

>$  G(a_{n+p}) =   \frac{ G(a_{n})-a_0-a_1t-...a_{p-1}t^{p-1}}{t^p} =  
\sum_{k \geq 0}^{}a_{k+p}t^k $ shift in avanti
$  G(a_{n-p}) =  \sum_{k\geq p}^{} a_{k-p}t^k =
a_0t^p+a_{1}t^{p+1}+a_{2}t^{p+2}+... =$ shift indietro
Si deve passare da  $G(a_{n-p})$ a  $G(a_{n})$ con  $G(a_{n})$
$  G(a_{n})=  G(a_{n-p})t^p +a_0+a_1t+...+a_{p-1}t^{p-1} $ quindi riprendendo $G(a_{n-p})$:
  $ G(a_{n-p}) = t^p(a_0+a_1t+a_2t^2+...)$
  $ =  t^pG(a_{n}) $


$ tDG(C_n) = G(n^2)+ G(n) +2t  G( \sum_{j=0}^{n}C_j)$
Si usa la formula di Eulero $  G( \sum_{k=0}^{n}a_k) =  \frac{1}{1-t} G(a_{n})$

$ tDG(C_n) = G(n^2)+ G(n) +2t  \frac{1}{1-t}  G(C_n)$
$ tDG(C_n) =  \frac{t+t^2}{(1-t)^3} +  \frac{t}{(1-t)^2} + 2t\frac{1}{1-t}  G(C_n)   $
>$ G(n) = G(n \cdot 1) = tD G(1) = tD  \frac{1}{1-t} = \frac{t}{(1-t)^2} $
>$ G(n^2) = G(n\cdot n) = tDG(n) = tD \frac{t}{(1-t)} = \frac{t+t^2}{(1-t)^3}$  

$ G(C_{n}) = C(t) $
$ C'(t) =  \frac{1+t+(1-t)}{(1-t)^3} + \frac{2}{1-t}C(t) $  
$ C'(t) = \frac{2}{(1-t)^3} +  \frac{2}{(1-t)}C(t) \qquad $ con $C_0= C(0) =0 $

Si deve risolvere l equazione differenziale, prendendo l equazione omogenea associata.

+ eq. omogenea
$ \rho'(t) =  \frac{2}{(1-t)}\rho(t) $
$  \frac{\rho'(t)}{\rho(t)} =  \frac{2}{1-t} $
$ \log{\rho(t)} = -2\log(1-t) = \log\frac{1}{(1-t)^2} $
$\rho(t) = \frac{1}{(1-t)^2}$


+ $ ( \frac{C(t)}{\rho(t)})' =
\frac{C'(t)\rho(t)-C(t)\rho'(t)}{\rho'(t)^2} $
  $ =  \frac{\rho(t) [ C'(t)-C(t)\frac{\rho'(t)}{\rho(t)}]}{\rho(t)^2}$ sostituisco la frazione di $\rho$
  $ =  \frac{C'(t)-C(t)\frac{2}{1-t}}{\rho(t)}$  dato che $ C'(t) = \frac{2}{(1-t)^3} +  \frac{2}{(1-t)}C(t)$
  $ =   \frac{\ \frac{2}{(1-t)^3}}{\frac{1}{(1-t)^2}} =  \frac{2}{1-t}$

  $ \frac{C(t)}{\rho(t)}=   -2\log(1-t)+k$ con $k=0$
  Si porta il meno dentro il log e si sostiuisce con il risultato trovato
  $ C(t) = 2\rho(t) \log(\frac{1}{1-t}) =  \frac{2}{(1-t)^2}\log(\frac{1}{1-t})$

$  C(t) = \frac{2}{(1-t)^2}\log(\frac{1}{1-t})$ assomiglia ai numeri armonici
$ G(H_n) = \frac{1}{1-t} \log(\frac{1}{1-t}) =  G( \sum_{}^{} \frac{1}{k})$

$ C(t) =  \frac{2}{(1-t)^2}\log(\frac{1}{1-t}) = \frac{2}{(1-t)}  
\frac{1}{1-t}\log(\frac{1}{1-t})$ Si scompone il primo elemento
$ \frac{2}{(1-t)}  G(H_{n}) = 2G( \sum_{k=0}^{n}H_k) $

ma dato che $  G(C_{n}) = C(t)$
allora $C_n= 2  \sum_{k=0}^{n}H_k = 2(n+1)(H_{n+1}-1)$
Per $f_n = g_n \forall n \leftrightarrow  G(f_n)= G(g_n)$

---

$ nS_n = \frac{n(n-2)}{6}+  2 \sum_{j=0}^{n-1}(S_{j})$
$n=0$ si ha $0 = 0+0$ quindi vale per zero
$n=1 \quad 0= -\frac{1}{6}$ per uno invece si ha un problema
si usa il delta per aggiustare
$ nS_n = \frac{n(n-2)}{6}+  2 \sum_{j=0}^{n-1}(S_{j}) + \frac{1}{6}\delta_{n,1}$

$  G(nS_{n}) =  \frac{1}{6}G(n^2)- \frac{1}{3}G(n)+2tG( \sum_{}^{}S_j) +
  \frac{1}{6}G(\delta_{n,1})$
$ tS'(t) =  \frac{1}{6} \frac{t+t^2}{(1-t)^3}- \frac{1}{3} \frac{1}{(1-t)^2}+
\frac{2t}{1-t}G(S_n)+ \frac{1}{6}t$ Si applica eulero

$S'(t) =  \frac{1+t-2(1-t)+(1-t)^3}{6(1-t)^3} +  \frac{2}{1-t}G(S_n)$
$S'(t) =  \frac{t^2(3-t)}{6(1-t)^3} + \frac{2}{1-t}G(S_n)$

+ eq. omogenea
  $ \rho'(t) = \frac{2}{1-t}\rho(t) $
  $ \rho(t) =  \frac{1}{(1-t)^2}$
+ $( \frac{S(t)}{\rho(t)})' =  \frac{S'(t)\rho(t)-S(t)\rho'(t)}{\rho(t)^2} $
  $ =  \frac{\rho(t)[S'(t)-S(t) \frac{\rho'(t)}{\rho(t)}]}{\rho(t)^2}$
  $ =  \frac{S'(t)- \frac{2}{1-t}S(t)}{\rho(t)}$
  $ =  \frac{t^2(3-t)}{6(1-t)^3} (1-t)^2 =  \frac{t^2(3-t)}{6(1-t)}$ la parte $(1-t)^2$ è il denominatore $\rho$ che moltiplica

$ \frac{S(t)}{\rho(t)} = \int{\frac{t^2(3-t)}{6(1-t)} dt}$
Si deve trasformare prima l espressione per usare i tratti semplici
$  \frac{t^2(2+1-t)}{6(1-t)} =  \frac{2t^2}{6(1-t)}+\frac{(1-t)t^2}{6(1-t)} $
$ = \frac{2t^2}{6(1-t)}+ \frac{1}{6}t^2 $
$ =   \frac{2t^2-2+2}{6(1-t)}+\frac{1}{6}t^2 =  \frac{2(t^2-1)}{6(1-t)}+
\frac{2}{6(1-t)}+\frac{1}{6}t^2$
$ = \frac{2(t-1)(t+1)}{6(1-t)} + \frac{1}{3(1-t)} +\frac{1}{6}t^2 $
$ =  -\frac{1}{3}(1+t) + \frac{1}{3(1-t)} +\frac{1}{6}t^2$

Quindi  $\int{\frac{t^2(3-t)}{6(1-t)} dt} = \int{-\frac{1}{3}(1+t) +
\frac{1}{3(1-t)} +\frac{1}{6}t^2} dt  $
$ =  -\frac{t^2}{6}- \frac{1}{3}t +  \frac{t^3}{18}- \frac{1}{3}\log(1-t) $

$S(t) =  \frac{1}{3} \frac{1}{(1-t)^2} \log( \frac{1}{1-t})+  
\frac{t^3-3t^2-6t}{18(1-t)^2}$

l ultimo termine non è altro che:
$  \frac{t^2}{18}  \frac{t}{(1-t)^2} -  \frac{t}{6} \frac{t}{(1-t)^2} -  
\frac{1}{3}\frac{t}{(1-t)^2}$ cioè
$  \frac{t^2}{18}   G(n-2) -  \frac{t}{6} G(n-1) -  
\frac{1}{3}G(n)$
