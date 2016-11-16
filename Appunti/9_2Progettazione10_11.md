# Operatore inverso delle funzioni generatrici

$G(f_{n}) =  \sum_{n\geq0}^{}f_nt^n= f(t)$
$ [t^n] $ operatore "coefficiente di"
$ [t^n]  G(f_{n}) = f_n$
+ *linearità*: $ [t^n] (\alpha f(t)+ \beta g(t)) = \alpha [t^n]f(t)+\beta[t^n]g(t)$
+ *spostamento*: $ [t^n] t f(t) = [t^{n-1}]f(t)$
  $tf(t) = t  \sum_{k\geq0}^{}f_kt^k = \sum_{k\geq0}^{}f_kt^{k+1}$
+ *convoluzione*: $[t^n] f(t)g(t) =  \sum_{k=0}^{n}f_kg_{n-k}$
+ *composizione*: $[t^n] f(t) \circ g(t) =  \sum_{k\geq0}^{}f_k [t^n] g_t $

---
$f(t) =  \frac{1+t}{1-t-t^2}$

$[t^n] f(t) = [t^n]  \frac{1}{1-t-t^2}+ [t^n]  \frac{t}{1-t-t^2}$

$[t^n]  \frac{1}{1-t-t^2} = [t^n]t^{-1}  \frac{t}{1-t-t^2} = [t^{n+1}]  \frac{t}{1-t-t^2} = F_{n+1} $

$[t^n] f(t) = [t^n]  \frac{1}{1-t-t^2}+ [t^n]  \frac{t}{1-t-t^2} = F_{n+1}+F_n = F_{n+2}$

---
$ f(t) =  \frac{1-t}{1-2t}  $
$[t^n] f(t) = [t^n]  \frac{1}{1-2t}+ [t^n]  \frac{t}{1-2t} = 2^n - [t^{n-1}]  \frac{1}{1-2t} = 2^n-2^{n-1} = 2^{n-1}(2-1) = 2^{n-1}$

---
$ (1-t-t^2)F(t) = 1+t $   
$ [t^n] (1-t-t^2)F(t) = [t^n] (1+t) $
$ [t^n] F(t)-[t^n]tF(t-[t^n]t^2F(t) = [t^n] (1+t) $
Per $n>1 \ \ \ \ F_n -F_{n-1}-F_{n-2} = 0$
