# Metodo simbolico

$ A = \{ \epsilon,01,001,10\} $
$ B = \{ 110,1101,0,1 \} $

$ \alpha \in A \qquad |\alpha| =$ lunghezza di $ \alpha $  

$ a(t) =  \sum_{\alpha \in A}^{}t^{|\alpha|} $

$ a(t) = t^0 + t^2 +t^3+t^2 = 1+2t^2+t^3 \qquad a_n = (1,0,2,1,0,0,0,...)$

$ b(t)= t^3+t^4+t+t = 2t+t^3+t^4 \qquad b_n = (0,2,0,1,1,0,0,0,...)$

Prendendo A come un insieme di alberi
$ \alpha \in A \qquad |\alpha| =$ numero di nodi interni all albero $ \alpha $  

$ a(t) = t + t^3 +t^2+t^2+t^3 $

Per ogni insieme se è possibile associare una misura allora si può trovare una
funzione generatrice.

Se A è un insieme di strutture combinatorie, ovvero oggetti ai quali posso
associare una misura, (dato $\alpha \in A$ si può trovare la sua misura)
$ a(t) =  \sum_{\alpha \in A}^{}t^{|\alpha|} =  \sum_{n\geq0}^{}a_nt^{n} $
con $a_n$ = numero di oggetti della classe che hanno misura n
Metodo simbolico.

Dato $ A \cup B = \{ \epsilon,01,001,10,110,1101,0,1\} $
$ C(t) = 1+t^2+t^3+t^2+t^3+...= a(t)+b(t) $
Gli insiemi devono essere disgiunti
$ C =  A \cup B \qquad c(t) = a(t)+b(t)$

## Prodotto cartesiano 
$ A \cdot B =
\{110,1101,0,1,01110,011101,010,011,001110,0011101,$
$0010,0011,10110,101101,100,101\} $  
$C(t) = t^3+t^4+t+t+t^5+t^6+t^3+t^3+t^6+t^7+t^4+t^4+t^5+t^6+t^3+t^3=$
$= 2t+5t^3+3t^4+2t^5+3t^6+t^7$

che è il prodotto di $ a(t) \cdot b(t) $
$ C = A \times B = \{ \gamma =(\alpha,\beta) : \alpha \in A , \beta \in B .
|\gamma| = |\alpha| + |\beta| \}$

$ C(t) =  \sum_{\gamma \in C}^{}t^{|\gamma|} =  \sum_{\alpha \in A , \beta
  \in B}^{}t^{|\alpha|+|\beta|} =  \sum_{n\geq0}^{}C_nt^n$

---
$ B =  $ insieme di stringhe binarie
Si cerca un equazione simbolica associata alla lunghezza di $ b\in B \qquad
|b|$ lunghezza

$ B = \epsilon \cup \{0,1\} \times B $ equazione simbolica
$ b(t) = 1+2t \cdot b(t) $
$ b(t) =  \frac{1}{1-2t} =  G(2^n) $
