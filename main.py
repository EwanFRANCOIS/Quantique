# Importation des outils nécessaires
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# On créer un circuit avec 2 qubitq et 2 bits classique (pour stocker la mesure) -> (premier nombre est le nombre de qubit et le deuxième nombre est le nombre de bits
circuit = QuantumCircuit(2, 2)

# On applique les portes
circuit.h(0)    # Porte Hadamard sur le qubit 0 (il devient 50% 0 et 50% 1)
circuit.cx(0, 1) # Porte CNOT : contrôle = qubit 0, cible = qubit 1 (Intrication !)

# On mesure les qubits
circuit.measure([0, 1], [0, 1]) # Mesure du qubit en premier et du bit en deuxième

# On créer et on dessine le circuit
print("Voici le circuit : ")
circuit.draw(output='mpl') # Dessine le circuit dans le terminal avec des elements de text

# On lance la simulation
simulation = AerSimulator()
lancement = simulation.run(circuit, shots = 1024)
resultat = lancement.result()

# On affiche les résultats
compteur = resultat.get_counts()
print("\nRésultats (comptage sur 1000 essais): ")
print(compteur)
plt.draw()
plt.show()