# 🧙‍♀️✨ Hamiltonian Graph with Super Clusters ✨🧙‍♀️

In network theory, a **Hamiltonian graph** is one that contains a Hamiltonian cycle, visiting each vertex exactly once
and returning to the starting vertex. Super clusters are densely connected subgraphs within the larger network.

## 🔮 Definitions

1. **Hamiltonian Graph**:

- <p>A graph <code>G</code> is Hamiltonian if there exists a cycle <code>C</code> in <code>G</code> that visits every
    vertex exactly once [1].</p>

2. **Clusters (Super Clusters)**:

- <p>Subsets of vertices within a graph that are more densely connected internally [2].</p>

## 🌌 Mathematical Representation

To represent a Hamiltonian graph with super clusters mathematically:

### 🕸️ Vertices and Clusters

- <p><strong>Cluster <code>C_A</code></strong>: <code>{A_1, A_2, A_3, A_4}</code></p>
- <p><strong>Cluster <code>C_B</code></strong>: <code>{B_1, B_2, B_3, B_4}</code></p>

### 🔗 Edges Within Clusters

- <p>For cluster <code>C_A</code>: <code>E_A = { (A_i, A_j) | ∀ i ≠ j, 1 ≤ i, j ≤ 4 }</code> [3]</p>
- <p>For cluster <code>C_B</code>: <code>E_B = { (B_i, B_j) | ∀ i ≠ j, 1 ≤ i, j ≤ 4 }</code> [3]</p>

### 🔄 Inter-Cluster Edges

- <p><code>E_{AB} = { (A_i, B_i) | 1 ≤ i ≤ 4 }</code> [4]</p>

### 🌟 Hamiltonian Cycle

<p>A Hamiltonian cycle <code>C</code> can be described as:</p>
<p><code>A_1 → A_2 → A_3 → A_4 → B_1 → B_2 → B_3 → B_4 → A_1</code></p>

### 📝 Short Formula

<p><code>G = (V, E)</code></p>
<p>where</p>
<p><code>V = C_A ∪ C_B</code></p>
<p><code>E = E_A ∪ E_B ∪ E_{AB}</code></p>
<p><code>C: A_1 → A_2 → A_3 → A_4 → B_1 → B_2 → B_3 → B_4 → A_1</code></p>

## 📚 References

1. [Hamiltonian Path](https://en.wikipedia.org/wiki/Hamiltonian_path)
2. [Community Structure](https://en.wikipedia.org/wiki/Community_structure)
3. [Complete Graph](https://en.wikipedia.org/wiki/Complete_graph)
4. [Graph Theory](<https://en.wikipedia.org/wiki/Graph_theory>
