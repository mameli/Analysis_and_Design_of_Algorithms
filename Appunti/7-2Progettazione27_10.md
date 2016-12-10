# Numeri di Catalan
$ a_n =  \frac{1}{n+1} \binom{2n}{n}$
$  G( \binom{2n}{n}) =  \frac{1}{\sqrt{1-4t}} $

$  \frac{a_{n+1}}{a_n} = \frac{1}{(n+2)}\binom{2(n+1)}{n+1} /\frac{1}{n+1} \binom{2n}{n} $
$ =  \frac{(2n+2)!}{(n+1)!(n+1)!(n+2)}  \frac{n!n!}{(2n)!} $
$ = \frac{(2n+2)(2n+1)(n+1)}{(n+1)^2(n+2)} $
$ = \frac{(n+1)2(n+1)(2n+1)}{(n+1)^2(n+1)} =$
$ =  \frac{2(2n+1)}{n+1}  \frac{n+1}{n+2} =  \frac{2(2n+1)}{n+2} $

$ (n+2)a_{n+1} = 2(2n+1)a_n $
Condizioni iniziali : $ 2a_1 = 2a_0 $

$  G((n+2)a_{n+1}) = 4  G(na_{n})+2  G(a_{n}) $
$  G((n+1)a_{n+1}) + G(a_{n+1}) = 4  G(na_{n}) +2  G(a_{n})  $

$ a'(t) +  \frac{a(t)-a_0}{t} = 4ta'(t)+ 2a(t) $
$ ta'(t) +a(t) -1 = 4t^2a(t)+2ta(t) $
$ (t-4t^2)a'(t) + (1-2t)a(t) = 1 $

Si deve risolvere l equazione differenziale
$ A(t) a'(t)+B(t)a(t) = C(t) $
+ Si considera l equazione omogenea associata
  $ A(t) \rho '(t) - B(t)\rho (t) = 0 $
  Si riscrive l' equazione in questo modo e si indica con $ \rho $ per non confondere le due equazioni. Le soluzioni non sono uguali ma:

  $  \frac{\rho '(t)}{\rho (t)} =  \frac{B(t)}{A(t)} $    
  $ \rho(t) $ soluzione dell eq. omogenea associata con una qualsiasi condizione iniziale.

+ $(\frac{a(t)}{\rho(t)})' =  \frac{a'(t)\rho(t)-a(t)\rho'(t)}{\rho(t)^2}$  raggruppando per $\rho(t)$
  $ = \frac{\rho(t) (a'(t)-a(t) \frac{\rho'(t)}{\rho(t)})}{\rho(t)^2}  $ sostituendo $  \frac{\rho '(t)}{\rho (t)}$ ed semplificando $\rho(t)$
  $ = \frac{a'(t)-a(t) \frac{B(t)}{A(t)}}{\rho(t)} $
  $ = \frac{A(t)a'(t)-a(t)B(t)}{\rho(t)A(t)} =  \frac{C(t)}{\rho(t)A(t)} $
  Nell ultimo passaggio tutto il termine si può semplificare con $ C(t) $

Ora si cerca la soluzione di $ (t-4t^2)a'(t) + (1-2t)a(t) = 1 $

+ $ (t-4t^2)\rho'(t) + (1-2t)\rho(t) = 0 $
  $  \frac{\rho'(t)}{\rho(t)} =\frac{-1+2t}{t-4t^2} = \frac{-1+2t}{t(1-4t)}$
  $  \frac{k}{t}+ \frac{r}{(1-4t)} =  \frac{k(1-4t)+rt}{t(1-4t)} $
  $  \frac{k -4kt+rt}{t(1-4t)} $

  Si associano i valori di $k$ e $r$ all'equazione $\frac{-1+2t}{t-4t^2}$
  $ \begin{cases} k=-1 \\ -4k+r = 2 \end{cases}  
    \begin{cases} k=-1 \\ r = -2 \end{cases} $  
  da cui :  $  \frac{-1}{t} - \frac{2}{1-4t} $
  $ \log \rho(t) = -\log(t)+ \frac{1}{2}\log(1-4t) $
  $ \log \rho(t) = \log\ \frac{1}{t}+ \log\sqrt{(1-4t)} $
  $ \log \rho(t) = \log\ \frac{\sqrt{(1-4t)}}{t} $
  $ \rightarrow \rho(t) =  \frac{\sqrt{(1-4t)}}{t} $

+ $( \frac{a(t)}{\frac{\sqrt{(1-4t)}}{t}})' =  \frac{1}{\frac{\sqrt{(1-4t)}}{t} (t-4t^2)}  $
  $ =\frac{1}{\sqrt{(1-4t)}(1-4t)} =\frac{C(t)}{\rho(t)A(t)} $
  $ t  \frac{a(t)}{\sqrt(1-4t)} = \int_o^t \frac{1}{\sqrt{(1-4t)}(1-4t)} dx = \int_o^t \frac{1}{(1-4t)^{3/2}} dx$
  Sostituzione
  $ 1-4x = y $
  $ 1-y = 4x\rightarrow x =  \frac{1-y}{4} \rightarrow dx =  -\frac{1}{4}dy$  
  $ \int _{x=0}^{x=t} -  \frac{1}{4y^{3/2}} dy$
  $ -\frac{1}{4} \int y^{-3/2}dy$
  $ -\frac{1}{4}  |\frac{y^{-3/2+1}}{-3/2+1} |_{x=0}^{x=t}$
  $ -\frac{1}{4}  |2y^{-1/2} |_{x=0}^{x=t}$
  $ -\frac{1}{4}  |2(1-4x)^{-1/2}|_{0}^{t} $

  > riguardare i passaggi

  Quindi:
  $  t\frac{a(t)}{\sqrt(1-4t)} = -\frac{1}{4}(-2\frac{1}{\sqrt{1-4t}}-2) $
  $  =\frac{1}{2}( \frac{1}{\sqrt{1-4t}}-1) = \frac{1}{2} \frac{1-\sqrt{1-4t}}{\sqrt{1-4t}}$
  $ a(t) = \frac{1}{2} \frac{1-\sqrt{1-4t}}{\sqrt{1-4t}}  \frac{\sqrt{1-4t}}{t}$

Abbiamo così:
$$ a(t) =  \frac{1-\sqrt{1-4t}}{2t}$$
