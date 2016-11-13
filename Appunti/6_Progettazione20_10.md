# G Operatore funzione generatrice

 $G(a_n) =  \sum_{n\geq0}^{} a_nt^n$

# Proprietà

Linearità : $  G(\alpha a_n+\beta b_n) = \alpha  G(a_n) + \beta  G(b_n) $
Spostamento : $  G(a_{n+1}) =  \frac{ G(a_{n})-a_0}{ t}$

Questa proprietà può essere generalizzata:

$  G(a_{n+p}) = a_p+a_{p+1}t+a_{p+2}t^2+...$
$  G(a_{n}) = a_0+a_{1}t+a_{2}t^2+...+a_{p-1}t^{p-1}+a_{p}t^p+a_{p+1}t^{p+1}+...$
In generale quindi:
$  G(a_{n+p}) =  \frac{ G(a_{n})-a_0-a_1t-a_2t^2-...-a_{p-1}t^{p-1}}{t^p} $

Derivazione :  $G(na_{n}) = t  D G(a_{n})$
Convoluzione : $ G ( \sum_{k=0}^{n} a_kb_{n-k}) =  G(a_n) G(b_n) $
Composizione : $\sum_{n\geq 0}^{}a_n( G(b_k))^n =  G(a_n) \circ  G(b_n)$

Si riprende la proprietà di convoluzione.
$  G(a_{n}) *  G(b_{n}) = (a_{0}+a_{1}t+a_{2}t^2+...)(b_{0}+b_{1}t+b_{2}t^2+...) $
$ = a_0b_0 +  (a_0b_1+a_1b_0)t+(a_0b_2+a_1b_1+a_2b_0)t^2+...$

Quindi: $  \sum_{k=0}^{n}a_kb_{n-k} $

Inversa di una sequenza rispetto ad $ a_n $
$(a_{0}+a_{1}t+a_{2}t^2+...)(b_{0}+b_{1}t+b_{2}t^2+...) = 1$
Quindi $a_0b_0 = 1$
$(a_0b_1+a_1b_0) = 0 $
$ (a_0b_2+a_1b_1+a_2b_0) = 0 $ etc.

La prima equazione ci impone una condizione:
$ b_0 =  \frac{1}{a_0} $  
è necessario quindi che $ a_0 \neq 0 $
$(a_0b_1+a_1b_0) = 0  \Rightarrow b_1 = - \frac{a_1b_0}{a_0}= - \frac{a_1}{a_0^2}$
questa operazione si può fare anche per il secondo passo in $ (a_0b_2+a_1b_1+a_2b_0) = 0 $ per $ b_2 $ :
$ b_2 = \frac{-a_1b_1-a_2b_0}{a_0} =  \frac{a_1^2 -a_0a_2}{a_0^3}$

Data $ a_n $ con $ a_0 \neq 0 $  esiste sempre l'inversa di  $G(a_{n})$ ovvero $  G(a_{n}) G(b_{n}) = 1 $
Prendendo : $  G(a_{n}) = 1-t \Rightarrow a_n=(1,-1,0,0,0,...)$
Usando i sistemi sviluppati in precendenza si avrà:
$  G^{-1}(a_{n}) = 1+t^1+t^2+...  $
Quindi la sequenza inversa è $ b_n = (1,1,1,1,...) $

Principio di identità: $a_n = b_n \quad \forall n \quad \Longleftrightarrow \quad G(a_n)= G(b_n)$
### Metodo del rapporto:
$ a_n $ data in modo esplicito
voglio trovare $  G(a_{n}) $
valuto il rapporto $  \frac{a_{n+1}}{a_n} $
trasformo la sequenza esplicita in una relazione di ricorrenza

$ a_n = (1,1,1,1,...) $
$  G(a_{n}) =  \sum_{n\geq0}^{}t^n $
si valuta $  \frac{a_{n+1}}{a_n}  = 1$ che sarà in questo caso 1
quindi si può dire che : $ a_{n+1} = a_n \qquad \forall n\geq0$

e $  G(a_{n+1}) =  G(a_{n}) $

e $   \frac{G(a_{n})-1}{t} =  G(a_{n}) \Rightarrow  G(a_{n})=  \frac{1}{1-t}$

Quindi riprendendo i ragionamenti sull inversa  $  G(1) =  \frac{1}{1-t}$

$ (1-t) G(b_{n})^{-1} = 1 $  

chiamando $ b_n = (1,-1,0,0,0,...) $

$  G(b_{n})^{-1} =  \frac{1}{1-t}$ come avevamo visto in precendenza.

---
$ (a_n) = (0,1,2,3,...) $  
$ a_n = n $
$  G(n) =  \sum_{}^{}nt^n $  si può usare il metodo del rapporto, ma è più facile usare la proprietà di Derivazione.
$  G(n) =  G({n*1}) = t D G(1) = t D  \frac{1}{1-t} = t  \frac{1}{(1-t)^2} = \frac{t}{(1-t)^2} = 0+t+2t^2+3t^3+...$

In generale $ a_0 =(a_0) $

Si può fare lo stesso ragionamento con $  G({n^2}) $ e usando la derivata di un rapporto:
$  G({n^2}) = t + 4t^2 + 9t^3+...=  G({n*n})= t DG(n) = t D  \frac{t}{(1-t)^2} = t  \frac{(1-t)^2 2t(1-t)}{(1-t)^4} = $
$ =  \frac{t(1-t+2t)}{(1-t)^3} =  \frac{t(t+1)}{(1-t)^3} $  

Per $ a_n = 2n+ \frac{1}{3}n^2 $ si possono usare i risultati trovati:
$  G(a_{n})= 2G(n)+\frac{1}{3}G(n^2) $

---
Per $ (a_n) = (1,0,1,0,1,0,...) $
$  G(a_{n}) = 1+t^2+t^4+... $
> NB: i dispari sono zero

$ =  \sum_{}^{}t^{2n} =  \sum_{}^{}(t^2)^n $
Si può usare la proprietà di Composizione.
$\sum_{}^{}(t^2)^n $ è della forma  $ \sum_{n\geq 0}^{}a_n( G(b_k))^n $
in cui $ t^2 = 0+0t+t^2+0t^3$
$ (b_k) = (0,0,1,0,1,0,...)$
Quindi:
$ G(a_{n}) =  \sum_{}^{}t^{2n} =  \sum_{}^{}(t^2)^n = G(1)\circ t^2 =  \frac{1}{1-t} \circ t^2 =  \frac{1}{1-t^2}$
---
Per $ a_n = (1,0,0,1,0,0,1,0,0,...)$ analogamente:
$  G(a_{n}) =  \sum_{}^{}t^{3n} =  \frac{1}{1-t^3} $
---
Per $ (a_n) = (1,-1,1,-1,...)$
$  G(a_{n})=  \sum_{}^{}(-1)^n t^n =  \sum_{}^{}(-t)^n $  
Si fa la composizione della funzione con -t
$ =  \frac{1}{1-t} \circ (-t) =  \frac{1}{1+t} $
---
Per $ (a_n) = (0,-1,2,-3,4,-5,6,...) $
$  G(a_{n})=  \sum_{}^{}(-1)^n nt^n =  \sum_{}^{}n(-t)^n =  \frac{t}{(1-t)^2} \circ (-t) =  \frac{-t}{(1+t)^2}$
---
In generale quindi $ a(t) =  G(a_{n}) = a_0+a_1t+a_2t^2+... $
$  G((-1)^na_{n}) =  G(a_{n}) \circ (-t) = a(-t)$
---
$ a_n = 2^n $
$ (a_n) = (1,2,4,8,...) $  
$  G(2^n) =  \sum_{}^{}2^nt^n =  \sum_{}^{}2t^n =  \frac{1}{1-2t}$
In generale
$  G(c^n) =  \frac{1}{1-ct} $
---
$a_n =  \frac{1}{n!}$
Si prova con il metodo del rapporto
$  \frac{a_{n+1}}{a_n} =  \frac{n!}{(n+1)!} =  \frac{1}{n+1} $
$ (n+1)a_{n+1} = a_n $  
Si deve controllare che sia vero per ogni n, è semplice vedere che $ \forall n $

$  G((n+1)a_{n+1}) =  G(a_{n}) $
Si può associare $ b_{n+1} = (n+1)a_{n+1} $  e $ b_n = na_n , b_0 =0 $

$  G(b_{n+1}) =  \frac{ G(b_{n})-b_0}{t} =  \frac{ G(na_{n})-0}{t} $
$ =  \frac{t DG(a_n)}{t} =  G(a_{n}) $  
$ a'(t)= a(t) $ equazione differenziale del primo ordine
$  \frac{a'(t)}{a(t)} = 1 $  
$ \log_n a(t) = t+k $
Dato che $a(0) = a_0 = 1$ allora
$ k = 0 $
quindi $a(t) = e^t$
---
$ a_n =  \frac{1}{n}$ con $ a_0 = 0 $
Si può provare il rapporto
$  \frac{a_{n+1}}{a_n} =  \frac{n}{n+1} \Rightarrow (n+1)a_{n+1} = na_n $
Si verifica che valga per ogni n
$ a_1=0 \quad ?$
> no perché si ha 1 = 0

Si usa il delta di Kronecker $ \delta_{n,k} = 1 $ con $ n=k $ e 0 altrimenti  
$ \delta_{n,0} = (1,0,0,...)$
$ \delta_{n,k} = (0,0,0,...,1,0,0,0,...)$
$  G(\delta_{n,k}) = t^k $
$  G(\delta_{n,0}) = t^0 = 1 $

Quindi $  \frac{a_{n+1}}{a_n} =  \frac{n}{n+1} \Rightarrow (n+1)a_{n+1} = na_n + \delta_{n,0}$
$  G((n+1)(a_{n+1})) = G(na_n+\delta_{n,0})$
$ DG(a_n) =  G(na_{n})+ G(\delta_{n,0}) $
$ DG(a_{n}) = t D  G(a_{n})+1$

$ a'(t) = ta'(t)+1 $
$ (1-t) a'(t) = 1 $
$ a'(t) =  \frac{1}{1-t} $
$ a(t) = -\log_n (1-t)+k $     
$ a(t) = \log_n (1-t)^{-1} $    con k=0
$ = \log_n  \frac{1}{1-t} $

Quindi  $G( \frac{1}{n}) = \log_n  \frac{1}{1-t}$

---
$ a_n=H_n=  \sum_{k=1}^{n} \frac{1}{k}$
Si usa la convoluzione da sinistra verso destra.
si può vedere $  \sum_{k=1}^{n} \frac{1}{k}*1$

Definiamo $ c_k = 0 \quad per \quad k =0  $ e $ 1/k \quad per \quad k>0 $

$ a_n = \sum_{}^{}c_k*1 $
$  G( \sum_{}^{}c_k*1) =  G(c_{n})  G(1) $   

$  G( \sum_{}^{}a_k) =  G( \sum_{}^{}a_k*1) =  G(1)  G(a_{k})=  \frac{1}{1-t} G(a_{k})$

$  G( \sum_{}^{}c_k*1) =  G(c_{n})  G(1) =  \frac{1}{1-t}\log_n  \frac{1}{1-t}$

Chiamata Formula di Eulero

> trovare la funzione generatrice di $  \frac{n(n+1)}{2} $
