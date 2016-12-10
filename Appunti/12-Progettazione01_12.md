1. $ [t^n] (\alpha f(t) +\beta g(t)) = \alpha[t^n] f(t) + \beta [t^n g(t)] $
2. $ [t^n] t^S f(t) = [t^{n-s}] f(t) $  
3. $ [t^n] f'(t) = (n+1) f_{n+1} , \quad [t^n] f(t) =  \frac{1}{n}[t^{n-1}] f(t)$
4. $ [t^n] f(t) g(t) =  \sum_{k=0}^{n}f_kg_{n-k}$
5. $ [t^n] f(t)\circ g(t) = [t^n]  \sum_{k \geq 0}^{}f_k g(t)^k =  \sum_{k \geq 0}^{} f_k [t^n]g(t)^k $

### Regola di newton
$ [t^n](1+ \alpha t)^r =  \binom{r}{n}\alpha ^n$

---
### $ f(t) =  \frac{1}{1-t} $
$[t^n]  \frac{1}{1-t} = [t^n] (1-t)^{-1} =  \binom{-1}{n}(-1)^n$
>  Proprietà binomiali
   $ \binom{n}{k} =  \binom{n}{n-k}$

>   $ \binom{-n}{k} =  \binom{n+k-1}{k}(-1)^k$

$\binom{-1}{n}(-1)^n =  \binom{1+n-1}{n} =  \binom{n}{n} = 1$

### $ f(t) = \frac{1}{1-ct} $  
$ [t^n]  \frac{1}{1-ct} = [t^n](1-ct)^{-1} =  \binom{-1}{n}(-c)^n=  \binom{1+n-1}{n}(-1)^n(-c)^n=  \binom{n}{n}c^k = c^n $

### $ f(t) = \frac{t}{(1-t)^2} $  
$ [t^n] \frac{t}{(1-t)^2} = [t^{n-1}](1-t)^2 =  \binom{-2}{n-1}(-1)^{n-1} =  \binom{2+n-1-1}{n-1}=  \binom{n}{n-1} =  \frac{n!}{(n-1)!()} $

---
$ [t^n]( \frac{t^2}{(1-t)^2}+ \frac{2t}{(1-t)}) =$ $[t^{n-2}(1-t)^{-2}]+2[t^n-1](1-t)^{-1} =$ $\binom{-2}{n-2}(-1)^{n-2} +2  \binom{-1}{n-1}(-1)^{n-1} =$  
$\binom{2+n-2-1}{n-2} +2  \binom{1+n-1-1}{}  = $ $\binom{n-1}{n-2} +2  \binom{n-1}{n-1} = $

---
### Fibonacci in formula chiusa
$ f(t) =  \frac{t}{1-t-t^2} $
Trattiamo una funzione razionale fratta. Dobbiamo trovare $ [t^n] = f(t) $
+ Si può trovare la ricorrenza per $ F_n $
+ Oppure la formula esplicita per $ F_n $

$ (1-t-t^2)f(t)=t $
La condizione iniziale è $f(t) = 0$ se $t = 0$    

$ [t^{n}](1-t-t^2)f(t) = [t^{n}]t $
$ [t^{n}]f(t)-[t^{n-1}]f(t)-[t^{n-2}]f(t) = \delta_{n,1}$

$ F_n -F_{n-1}-F_{n-2} = \delta_{n,1}$

$ \forall n\geq 2 \quad F_n = F_{n-1}+F_{n-2}$ perché il delta vale zero

$ F_0 = 0 \quad F_1 = 1 $ per le condizioni iniziali

In questo modo abbiamo trovato la ricorrenza.

---
Altro esempio per trovare la ricorrenza di $f(t)$
$ f(t) =  \frac{t+t^2}{1-2t-3t^3} $     

$ (1-2t-3t^3)f(t) = t+t^2 $
$[t^{n}] (1-2t-3t^3) f(t) = [t^{n}](t+t^2) $
$[t^{n}]f(t) -2 [t^{n-1}]f(t) -3 [t^{n-3}]f(t) = \delta_{n,1}+\delta_{n,2} $
Scriviamo $ [t^{n-3}] $ perchè l'esponente di t è 3
$ f_n -2f_{n-1} -3f_{n-3} = \delta_{n,1}+\delta_{n,2}$
$ \forall n \geq 3 \quad f_n = 2f_{n-1}+3f_{n-3}$

$ f_0 = 0 $
$ f_1-2f_0-3f_{-2} = 1 \Rightarrow\quad f_1 = 1+2f_0=1$
$ f_{-2} = 0 $ perchè per i numeri negativi si prende 0
$ f_2-2f_1-3f_{-1} = 1 \Rightarrow\quad f_2 = 1+2f_1=1$

---
Troviamo ora la formula esplicita per $ F_n $
$ f(t) =  \frac{t}{1-t-t^2} $

Vogliamo trasformare il denominatore in:
$ 1-t-t^2 = (1-\phi t)(1-\hat{\phi}t)$
Con $$ \phi =  \frac{1-\sqrt{5}}{2} \qquad \hat{\phi} =  \frac{1-\sqrt{5}}{2} $$

$ f(t) =  \frac{t}{(1-\phi t)(1-\hat{\phi}t)} =  \frac{A}{(1-\phi t)}+ \frac{B}{(1-\hat{\phi}t)} $

Si trovano le radici del denominatore.
$ 1-t-t^2 = 0 $

$ t_{1,2} =  \frac{1\pm \sqrt{1+4}}{-2}$
$ t_{1} =  \frac{1 + \sqrt{5}}{-2}\quad t_{2} =  \frac{1 - \sqrt{5}}{-2}$

Sappiamo che le radici $ x_1 \cdot x_2 =  \frac{c}{a}$ in $ ax^2+bx+c=0 $  
Possiamo inoltre scrivere $ ax^2+bx+c = 0  $ in
$$ a(x-x_1)(x -x_2)=0 $$

Sviluppando l'equazione
$ a(-x_1(1+ \frac{x}{-x_1}))(-x_2(1+ \frac{x}{-x_2})) = 0 $
$ \underbrace{ax_1x_2}_\text{C}  (1+ \frac{x}{-x_1})(1+ \frac{x}{-x_2})=0$  

$ t_1t_2 = -1 $
$  \frac{1}{t_1} = -t_2 \quad \frac{1}{t_2} = -t_1$
$1-t-t^2 = -(t-t_1)(t-t_2) \\
  \qquad \qquad = (1- \frac{t}{t_1})(1- \frac{t}{t_2})\\
  \qquad \qquad = (1+t_2t)(1+t_1t) \\
  \qquad \qquad = (1-\hat{\phi}t)(1-{\phi}t)\qquad \blacksquare$
---
Quindi abbiamo che $ 1-t-t^2 = (1+t_1t)(1+t_2t)$
$ f(t) =  \frac{t}{(1+t_1t)(1+t_2t)} =  \frac{A}{(1+t_1t)}+ \frac{b}{(1+t_2t)}\\
\qquad \qquad =  \frac{A(1+t_2t)+B((1+t_1t))}{(1+t_1t)(1+t_2t)} \\
\qquad \qquad =  \frac{A+B+ (At_2+Bt_1)t}{(1+t_1t)(1+t_2t)}$

$
\begin{cases}
 A+B = 0 \\ At_2+Bt_1 = 1
\end{cases}
\begin{cases}
 A= -B \\ -Bt_2+Bt_1 = 1
\end{cases}
\begin{cases}
 A=  \frac{1}{t_2-t_1} \\ B =  \frac{1}{t_1-t_2}
\end{cases}
$

$ t_1-t_2 = -( \frac{1+\sqrt5}{2})+(\frac{1-\sqrt5}{2}) = -\sqrt5$
$$ B =  -\frac{1}{\sqrt5} \qquad \qquad A= \frac{1}{\sqrt5} $$

$ [t^{n}]  \frac{1}{\sqrt5}( \frac{1}{1+t_1t})-\frac{1}{\sqrt5}( \frac{1}{1+t_2t}) = \frac{1}{\sqrt5}[t^{n}](1+t_1t)^{-1} - \frac{1}{\sqrt5}[t^{n}](1+t_2t)^{-1} $  

$ \qquad \qquad= \frac{1}{\sqrt5}  \binom{-1}{n}t^n_1 -\frac{1}{\sqrt5}  \binom{-1}{n}t^n_2$
$ \qquad \qquad= \frac{1}{\sqrt5}  \binom{1+n-1}{n}(-1)^nt^n_1 -\frac{1}{\sqrt5}  \binom{1+n-1}{n}(-1)^nt^n_2$
$ \qquad \qquad= \frac{1}{\sqrt5}(-t_1)^n -\frac{1}{\sqrt5} (-t_2)^n$
$ \qquad \qquad=  \frac{1}{\sqrt5}(\phi^n-\hat{\phi})^n$ forma esplicita

$$ \approx  \frac{\phi^n}{\sqrt5}$$

Per n grandi
