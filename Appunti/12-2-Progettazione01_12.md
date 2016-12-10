$ G( \binom{2n}{n}) =  \frac{1}{\sqrt{1-4t}} \qquad \qquad  G( \frac{1}{n+1} \binom{2n}{n}) =  \frac{1- \sqrt{1-4t}}{2t} $

$[t^{n}]  \frac{1}{\sqrt{1-4t}} = [t^{n}] (1-4t)^{-1/2} =  \binom{-1/2}{n}(-4)^n$

$ \Rightarrow  \binom{-1/2}{n} =  \frac{(-1)^n}{4^n}  \binom{2n}{n} $

---
$[t^{n}]  \frac{1- \sqrt{1-4t}}{2t} =  \frac{1}{2}[t^{n}] t^{-1} (1- \sqrt{1-4t})$
$ \qquad \qquad =  \frac{1}{2}[t^{n+1}] 1- \frac{1}{2}[t^{n+1}](1-4t)^{1/2}  $
$ \qquad \qquad =  \frac{-1}{2}  \binom{1/2}{n+1}(-4)^{n+1} $
> $ \qquad \qquad \binom{1/2}{n} =\frac{(-1)^n}{4^{n}2(n+1)} \binom{2n}{n} $

$ \qquad \qquad =  \frac{-1}{2}  \frac{(-1)^n}{4^{n+1}(2(n+1)-1)} \binom{2(n+1)}{n+1}(-4)^{n+1}$


$ \qquad \qquad =   \frac{(-1)^{n+1}}{2*4^{n+1}(2n+1)}  \binom{2(n+1)}{n+1}(-4)^{n+1}$
$ \qquad \qquad =  \frac{1}{2(2n+1)} \binom{2(n+1)}{n+1} $
$ \qquad \qquad = \frac{1}{2(2n+1)}  \frac{(2n+1)!}{((n+1)!)^2} \\  
  \qquad \qquad =  \frac{1}{2(2n+1)}  \frac{(2n+2)(2n+1)(2n)!}{(n+1)n!(n+1)n!}\\
  \qquad \qquad =  \frac{2n!}{(n+1)n!n!} =$  
$$  \frac{1}{n+1} \binom{2n}{n} $$

---
## Formula dei confronti del quicksort

$ c(t) =  \frac{2}{(1-t)^2} ln  \frac{1}{1-t}$
$ c_n = 2(n+1)(H_{n+1}-1) $

è un prodotto di due funzioni

$ c(t) = 2  \frac{1}{1-t}  \frac{1}{1-t} ln( \frac{1}{1-t}) $

>Chiamiamo $g(t) = \frac{1}{1-t} ln( \frac{1}{1-t})$

Si usa la convoluzione
$[t^{n}] \frac{1}{1-t} g(t) =  \sum_{k=0}^{n}g_{n-k} =  \sum_{k=0}^{n}g_k$

$ c(t) = 2  \frac{1}{1-t} g(t) $
$ [t^{n}]c(t) = 2 [t^{n}] \frac{1}{1-t} g(t) = 2  \sum_{k=0}^{n}g_k  $
$ [t^{n}]g(t) = [t^{n}] \frac{1}{1-t} ln  \frac{1}{1-t} $
> Chiamiamo $h(t) =ln  \frac{1}{1-t} $

$ \qquad \quad \  =  [t^{n}] \frac{1}{1-t}h(t) =  \sum_{k=0}^{n}h_k$

$ [t^{n}]h(t) = [t^{n}] ln  \frac{1}{1-t} $  usiamo la derivata
$ \qquad \qquad =  \frac{1}{n}[t^{n-1}](1-t)  \frac{1}{(1-t)^2} = $
$ \qquad \qquad =  \frac{1}{n}[t^{n-1}] \frac{1}{1-t} =  \frac{1}{n} $

$  \sum_{}^{}h_k =  \sum_{k=0}^{n} \frac{1}{k} = H_n = g_n  $
$ 2  \sum_{}^{}g_k = 2  \sum_{k=0}^{n} H_k  $

$$c(t) = 2   \sum_{k=0}^{n}H_k$$  

Il risultato è un po' diverso da quello trovato ma si può manipolare.

$ c(t) =  \underbrace{\frac{2}{1-t}}_\text{f(t)}  \underbrace{\frac{1}{1-t}ln  \frac{1}{1-t}}_\text{g(t)}$

$ g'(t) =  \frac{1}{(1-t)^2}ln  \frac{1}{1-t} +  \frac{1}{(1-t)}(1-t)  \frac{1}{(1-t)^2} \\
\qquad =   \frac{1}{(1-t)^2}ln  \frac{1}{1-t}+  \frac{1}{(1-t)^2} \\
\qquad =  \frac{1}{2}c(t) + \frac{1}{(1-t)^2}$

$ c(t) = 2g'(t) -2\frac{1}{(1-t)^2} $
$ g(t) =  G(H_{n}) $

$ [t^{n}]g'(t) = (n+1)g_{n+1} = (n+1)H_{n+1} $
$ [t^{n}]c(t) = 2 [t^{n}]g'(t) -2 [t^{n}](1-t)^{-2} $  
>$ [t^{n}](1-t)^{-2} = [t^{n}]t^{-1} \frac{t}{(1-t)^2} = [t^{n+1}] \frac{t}{(1-t)^2} = n+1$

$ \qquad \qquad = 2(n+1)H_{n+1} \\
\qquad \qquad = 2(n+1)H_{n+1}-2(n+1) $

$\qquad \qquad = \boxed{2(n+1)(H_{n+1}-1)} \qquad \qquad \blacksquare$
