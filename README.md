
# PROJET QUANTIQUE PYTHON

Bonjours tout le monde, ici se retrouve le travail que je réalise sur le quantique. Voici tout ce que vous allez retrouver dans ce README et dans ce projet ✨

- Toutes les portes / opérations qui peuvent se retrouver dans un circuit quantique ! 🔨

- Les fichiers contenant les circuits quantique, codé en python 🐍
    (les circuits sont affichés avec la bibliothèque "matplotlib" pour avoir les portes et les circuits en couleurs).

- Des Explications au sujet de l'informatique quantique ou généralement au sujet du quantique en lui même 🎲

---

# Explications Quantique

- **UNE INTRICATION**, c'est quoi ?

  Une **intrication** est un phénomène où deux particules (ou qubits ici) sont liées de telle manière que l'état de l'une dépend **forcément et instantanément** de l'état de l'autre, quelle que soit la distance qui les sépare.

- **UNE SUPERPOSITION**, c'est quoi ?

    La **superposition** permet à une particule (ou un qubit ici) d'exister simultanément dans plusieurs état possibles jusqu'à ce qu'une mesure soit effectuée.

# Portes et opérations circuit

**|H|** -> La porte Hadamard

 *Son travail*
- Elle créer une superposition.

 *Ce qu'elle fait*
- Transforme un état "pur" (|0> ou |1>) en un état où le qubit est à la fois 0 et 1 avec une probabilité égale.

*Le résultat*

$$|0\rangle \xrightarrow{H} \frac{|0\rangle + |1\rangle}{\sqrt{2}}$$

$$|1\rangle \xrightarrow{H} \frac{|0\rangle - |1\rangle}{\sqrt{2}}$$

**La matrice**

$$H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\\ 1 & -1 \end{pmatrix}$$ 

*Exemple clair*

On prend une pièce soit sur pile (0) soit sur face (1).

**La porte Hadamard** va faire tourner la pièce très vite sur une table, tant qu'elle tourne, elle est ni face, ni pile.

**Le résultat**, si le qubit est sur |0> , Hadamard le transforme en état de superposition.

C'est à dire que si on mesure, on aura 50% de chance d'avoir 0 et 50% de chance d'avoir 1.

*Remarque*

2 portes Hadamard s'annulent entre elles.

---

**X -> La porte CNOT**

*Son travail*

Elle agit sur deux qubits

*Son fonctionnement*

Elle agit sur un premier qubit qui est un qubit de "contrôle" et sur un autre qubit qui est un qubit de "cible".

**Contrôle** -> C'est lui qui décide si l'action doit avoir lieu, il ne change pas l'état.

**Cible** -> C'est lui qui subit l'action (l'inversion de l'état) selon l'état du contrôle.

*Règle*

`Si le qubit de contrôle est à |0>, le qubit cible ne change pas.`

`Si le qubit de contrôle est à |1>, le qubit cible inverse son état (|0> devient |1> et inversement).`

**La matrice**

$$CNOT = \begin{pmatrix} 1 & 0 & 0 & 0 \\\ 0 & 1 & 0 & 0 \\\ 0 & 0 & 1 & 0 \\\ 0 & 0 & 0 & 1 \end{pmatrix}$$

**Vue que le CNOT agit sur deux qubits, cela donne $$2^2 = 4$$**

*Remarque*

Si une porte Hadamard est présente avec une porte CNOT (c'est à dire qu'il y a présence d'une superposition), si le qubit de contrôle est en superposition, la porte CNOT va traiter |0> et |1> en même temps.

**Le résultat**

On obtient donc un état où les 2 qubits sont **intriqués**

