# Funzioni generatrici

In laboratorio abbiamo provato che partendo da
$G(a_{n}) = 1-t-t^2 \rightarrow (a_n)_n = (1,-1,-1,0,0,...)$
si arriva a $ (b_n)_n = (1,1,2,3,5,8,13,...) $ cioè fibonacci.

Applicando le proprietà delle funzioni generatrici è possibile determinare
$  G(F_{n}) = ? $
Per fibonacci $ F_n = F_{n-1} + F_{n-2}+... $   
$ F_0 = F_{-1} +F_{-2} $ che in questo caso non ha senso.
Quindi non vale per ogni N.
$ F_n $ è lineare (i termini non sono quadratici o altro) e a coefficienti costanti (i termini che moltiplicano sono costanti).  

Per farla definire sempre si fa uno shift $ F_{n+2} = F_{n+1}+F_n$
$ F_{n+2} \leftrightarrow  G(F_{n+2}) =  G(F_{n+1}+F_n)$

$G(F_{n+2}) =  G(F_{n+1}+F_n)$
$ G(F_{n+2}) $ e $G(F_{n+1}) $ si possono scrivere come segue:
$ = \frac{ G(F_{n})-F_0-F_1t}{t^2} = \frac{ G(F_{n})-F_0}{t} + G(F_{n}) $ per traslazione di G
$ = \frac{G(F_{n}) -t}{t^2} =  \frac{ G(F_{n})+tG(F_{n})}{t}$ togliendo il t al denominatore
$ =  G(F_{n})-tG(F_{n})-t^2G(F_{n}) = t$
$=(1-t-t^2)G(F_{n}) = t$
$ = G(F_{n}) =  \frac{t}{1-t-t^2} $  

Avendo preso n+2 lo riportiamo a n+1 così:
$ G(F_{n+1}) =  \frac{G(F_{n})-F_0}{t} =  \frac{1}{1-t-t^2} $
$ = 1+t+2t^2+3t^3+5t^4+... $  
In questo modo la funzione è invertibile

Per la sequenza $ a_n= a_{n-1} +a_{n-2}+a_{n-3} $ di Tribonacci
$ 0,1,1,2,4,7,13,24,... $  
Con le condizioni iniziali $ a_0 =0 ,a_1=1,a_2=1 $

Si fa uno shift anche in questo caso
$ a_{n+3} = a_{n+2} +a_{n+1}+a_{n} $

$\frac{G(a_{n})-t-t^2}{t^3}=\frac{G(a_{n})-t}{t^2}+\frac{G(a_{n})}{t}+ G(a_{n}) $

$  G(a_{n})-t-t^2 = t  G(a_{n})-t^2+t^2  G(a_{n})+t^3  G(a_{n}) $
$ = (1-t-t^2-t^3) G(a_{n}) = t $  
$  G(a_{n})=  \frac{t}{1-t-t^2-t^3} $

Si introduce sempre una frazione nella funzione generatrice

---
$ a_n =  \binom{p}{n} $
$  G(a_{n}) =  \sum_{n\geq0}^{} \binom{p}{n}t^n = (1+t)^p $  
analogo a $  \sum_{n\geq0}^{} \binom{n}{k}a^kb^{n-k} = (a+b)^n $   

$  \frac{a_{n+1}}{a_n} =  \binom{p}{n+1} /  \binom{p}{n} =  $
$  \frac{p!}{(n+1)! (p-n-1)!}  \frac{n!(p-n)!}{p!} =  \frac{(p-n)}{n+1} $  

quindi: $ (n+1)a_{n+1} =(p-n)a_n $

Le condizioni iniziali $a_0=  \binom{p}{0}= 1$ e $ a_1 =  \binom{p}{1} = p $
Dato che funziona anche in zero si applica il principio di identità
$  G((n+1)a_{n+1}) =  pG(a_{n}) - G(na_{n}) $
$  DG(a_{n}) = p  G(a_{n}) -t D  G(a_{n})$ si introduce un eq differenziale del primo ordine.

$ (1+t)a'(t) = pa(t) $
$  \frac{a'(t)}{a(t)} =  \frac{p}{1+t} $
$ \log a(t) = p\log (1+t)+k$  
K deve essere 0
quindi : $ a(t) = (1+t)^p $

---
$ a_n =  \binom{2n}{n} $
$  \frac{a_{n+1}}{a_n} =  \binom{2(n+1)}{n+1} /  \binom{2n}{n} =  $
$ =  \frac{(2n+2)!}{(n+1)!(n+1)!}  \frac{n!n!}{(2n)!} $
$ = \frac{(2n+2)(2n+1)}{(n+1)^2} $
$ = \frac{2(n+1)(2n+1)}{(n+1)^2} =  \frac{2(2n+1)}{n+1} $

$ (n+1)a_{n+1} =2(2n+1)a_n $
condizioni iniziali $a_1= 2a_0$

$  G((n+1)a_{n+1}) =  2G(2(2n+1)a_{n}) $
$  G((n+1)a_{n+1}) =  4G(na_{n}) + 2G(a_{n}) $
$ D  G(a_{n}) = 4 tD  G(a_{n}) + 2  G(a_{n}) $
$ (1-4t)a(t) = 2a(t) $
$   \frac{a'(t)}{a(t)} =  \frac{2}{1-4t} $  
$ \log a(t) =  -\frac{1}{2} \log (1-4t) +k $
$ \log a(t) = \log (1-4t)^{ -\frac{1}{2}} $
$ a(t) =  \frac{1}{\sqrt{1-4t}} $
