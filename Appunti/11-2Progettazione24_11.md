# Esempio
$ E::= T|AT$
$ T::= F|TAF$
$ F::= P|FMP $
$ P::= a|(E) $
$ M::= *|/ $
$ A::= +|- $
$ NT= \{E,T,F,P,M,A\} $
Terminali $= \{n,(,),*,/,+,-\}$

Genera espressioni aritmetiche. La grammatica è non ambigua.
Prendiamo $t$ come lunghezza dell espressione, $z$ per tenere traccia del numero di simboli '$n$' e si tiene traccia dei simboli parentesi con $w$.

$ E= E(t,z,w) $
$ E = T+A\cdot T $
$ T = F + TA \cdot F $
$ F = P+F \cdot M \cdot P $
$ P = tz +t^2w^2E$
Si contano tutte e due le parentesi, aperte o chiuse.
$ M = 2t $
$ A = 2t $
$ E= E(t,z,w) =zt+2zt^2+z(w^2+4z)t^3+4z(2z+w^2)t^4...$

1. $n$
2. $+n,-n$
3. $(n),n+n,n-n,n*n,n/n$
4. $+n+n,-n+n,-n-n,+n-n,+n*n,-n*n,+n/n,-n/n, $
   $(-n),(+n,)$
   $ -(n),+(n) $
Mettendo a 1 w e z si può trovare direttamente la funzione con solo $t$.
$E(t,1,1) = t+2t^2+5t^3+12t^4...$
---
$G(f_{n}) =  \sum_{n\geq0}^{}f_nt^n= f(t)$
$ [t^n] $ operatore "coefficiente di"
$ [t^n]  G(f_{n}) = f_n$
+ *linearità*: $ [t^n] (\alpha f(t)+ \beta g(t)) = \alpha [t^n]f(t)+\beta[t^n]g(t)$
+ *spostamento*: $ [t^n] t f(t) = [t^{n-1}]f(t)$
  $tf(t) = t  \sum_{k\geq0}^{}f_kt^k = \sum_{k\geq0}^{}f_kt^{k+1}$
+ *convoluzione*: $[t^n] f(t)g(t) =  \sum_{k=0}^{n}f_kg_{n-k}$
+ *composizione*: $[t^n] f(t) \circ g(t) =  \sum_{k\geq0}^{}f_k [t^n] g_t $

# Regola di Newton
$ [t^n] (1+\alpha t)^r =  \binom{r}{n}\alpha^n$
###### [Dim]
$ [t^n]f'(t) = (n+1)f_{n+1}$
$ [t^{n-1}]f'(t) = (n)f_{n}$
$ f_n =  \frac{1}{n}[t^{n-1}]f'(t) $
$ [t^n]f(t)=  \frac{1}{n}[t^{n-1}] f'(t)$ derivazione
$ [t^{n}](1+\alpha t)^r =  \frac{1}{n}[t^{n-1}]r\alpha (1+\alpha t)^{r-1} =  \frac{\alpha r}{n}[t^{n-1}](1+\alpha t)^{r-1}   $
$ =  \frac{\alpha r}{n} \frac{1}{n-1}[t^{n-2}](r-1)(1+\alpha t)^{r-2}   $
$ =  \frac{\alpha r}{n} \frac{\alpha(r-1)}{n-1} \frac{\alpha(r-2)}{n-2}... \frac{\alpha (r-n+1)}{1}[t^{n-n}](1+\alpha t)^{r-n}   $
$ =  \frac{a^n r(r-1) (r-n+1)}{n!} = \alpha^n\binom{r}{n} $
