# Funzioni generatrici

Abbiamo trovato le funzioni per i confronti del quicksort e una funzione analoga per gli scambi.

La ricorrenza di fibonacci è detta lineare perché i coef. sono costanti.

$ F_{n+2} = F_{n+1}+F_n $ con $ F_0=0 , F_1 = 1 $

Definiamo in generale sequenza di reali:
$$ (a_n)_{n \in N} \qquad a_n \in R $$    

Ad esempio:
$ (C_n)_n = (0,2,5, \frac{26}{3}, \frac{77}{6}...) $ con $ C_n \in Q $
Abbiamo trovato $ C_n $ per le soluzioni della lezione passata.

Indichiamo con $ G $ l'operatore funzione generatrice.

$ G_n^t(a_n) =  \sum_{n\geq 0}^{}a_nt^n = a_0+a_1t+a_2t^2+...$

Non essendoci una differenza sostanziale tra le sequenze e la sommatoria di espressioni esponenziali, associamo le sequenze ad una funzione che chiameremo appunto funzione generatrice.
Facciamo questa associazione perché le funzioni generatrici sono più facili da studiare.
Se non si sono ambiguità si scriverà soltanto $ G(a_n) $
t è un segnaposto e di solito non ha significato. Indica solo la posizione del
valore della sommatoria. $ t^2 $ indica il secondo posto.

## Proprietà di $ G $

### Linearità
  $ (a_n)_n , (b_n)_n $ sono due sequenze
  L'insieme di due sequenze è un gruppo commutativo rispetto alla somma.
  $$ G(\alpha a_n+ \beta b_n) = \alpha G  (a_n) + \beta G (b_n) \quad  \alpha, \beta  \in R$$

  Dimostrazione :
  $ G(\alpha a_n+ \beta b_n) =  \sum_{n\geq 0}^{} (\alpha a_n +\beta b_n) t^n$
  $ \qquad \qquad \qquad =  \alpha \underbrace{\sum_{}^{} a_n t^n}_\text{ G(a)} + \beta  \sum_{}^{}b_n t^n$  

  il prima sommatoria corrisponde a $ G (a_n) $

### Spostamento
  $ G(a_{n+1}) =  \frac{G(a_n)-a_0}{t} $

  $ =  \sum_{}^{}a_{n+1}t^n = a_1 + a_2t + ..$
  $ =  \frac{a_0+a_1t+a_2t^2+...}{t} $  

  Lo spostamento si vedrà che potrà essere generalizzata anche per altre posizioni.

### Derivazione
  $ G(na_n)      k = tDG(a_n) $
  $ \quad \qquad =  \sum_{n\geq 0}^{}na_nt^n = 0 +a_1t+2a_1t^2+3a_2t^3+...$

  > $N.B. $ Per fibonacci G è
    $ G(F_n) = t+t^2+2t^3+3t^4+... $
    $ nG(F_n) = t+2t^2+6t^3+12t^4+25t^5... $

  $ D  G(a_n)= 0 +a_1 + 2a_2t+3a_3t^2+...$

  Si moltiplica l espressione per t
  $ tD  G(a_n)= 0 +a_1t + 2a_2t^2+3a_3t^3+...$

  Abbiamo così la relazione

### Convoluzione
  $ G ( \sum_{k=0}^{n} a_kb_{n-k}) =  G(a_n) G(b_n) $
  Permette di trasformare prodotti di funzioni generatrici note in altre funzioni generatrici.

  $ G(b_n) =  \sum_{}^{} b_nt^n $ e si sviluppa come  $G(a_n)$
  Il prodotto:
  $  G(a_n) G(b_n) = (a_0+a_1t+a_2t^2+...)(b_0+b_1t+b_2t^2+...) $     
  $ a_0b_0 $ è il termine noto perché non ha t
  si ha $t^1$ solo per le moltiplicazioni con $ a_0 , b_0$ con i primi t di $a_1$ e $b_1$
  Il procedimento per $ t^2 $ è analogo

  $ a_0b_0 +  (a_0b_1+a_1b_0)t+(a_0b_2+a_1b_1+a_2b_0)t^2+...$

  in generale potremo scrivere questa somma con la sommatoria :

  $  \sum_{k=0}^{n}a_kb_{n-k} $  

  Ad esempio :
  $  (a_n) =  \frac{1}{n} ,  (b_n) = 1$
  $  \sum_{k=0}^{n} \frac{1}{k} = H_n $
  Facendo la convoluzione si ha la ricorrenza dei numeri armonici.
  Per :
  $  (a_n) =  n ,  (b_n) = 1$
  $  \sum_{k=0}^{n} n =$  Formula di Gauss

### Composizione
  $\sum_{n\geq 0}^{}a_n( G(b_k))^n =  G(a_n) \circ  G(b_n)$
  Praticamente se si mette al posto di t una altra sequenza.
  $ G_n^t(a_n) =  \sum_{n\geq 0}^{}a_nt^n$
  Troviamo la composizione di due funzioni.

  Per esempio:

  $\sum_{}^{}2^na_nt^n =  \sum_{}^{} a_n(2t)^n$
  $ =  G(a_n) \circ G(2t)  $
  In questo caso 2t è la funzione generatrice (per quanto semplice) :
  $ 2t \rightarrow (0,2,0,0,0,0,...) $   

### Principio di identità
  $a_n = b_n \quad \forall n \quad \iff \quad G(a_n)= G(b_n)$
  C'è una equivalenza tra funzioni generatrici e sequenze.

### Metodo del rapporto
  Sequenza definita da una relazione di ricorrenza
  Sequenza nota $(a_n = 1 \quad \forall n)$
  $  G(1) =   \sum_{}^{}t^n$
  In questo metodo si va a valutare il rapporto tra due termini
  della sequenza.
  $  \frac{a_{n+1}}{a_n} = 1 \rightarrow a_{n+1} = a_n $
  Dato che vale per ogni $n$ allora si può trasformare in un uguaglianza tra
  funzioni generatrici.
  $  G(a_{n+1}) = G(a_n) $
  $  \frac{G(a_n)-1}{t} =  G(a_n) $

  $ (1-t) G(a_n) = 1 \rightarrow  G(1) =  \frac{1}{1-t} $
  la funzione generatrice della sequanza 1 può essere generata da $ \frac{1}{1-t} $
