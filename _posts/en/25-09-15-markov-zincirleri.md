---
title: "Markov Chains"
date: 2025-09-15 18:00:00 +0300
categories: [artificial intelligence, mathematics, probability]
tags: [nlp, mathematics, artificial intelligence, math, science, markov chains, chain, statistics, probability, llm]
authors: yusuf-said
image:
  path: /assets/img/2025-09-15-markov-zincirleri/cover.webp
description: The history of Markov Chains and their significance today
toc: true
math: true
mermaid: false
comments: true
pin: false
lang: en
---

In this article, we will examine Markov Chains
## 1. What Are Markov Chains? Their Origin and Structure

**Markov Chains** are named after the Russian mathematician **Andrey Markov**. These chains are a probability model based on mathematics and statistics with a stochastic structure. Markov chains are used to predict the probabilities of future states based on the current state. The fundamental assumption is that the future depends only on the current state; the past has no direct effect. This property is called **memorylessness** and forms the basis of Markov chains.

<figure>
    <img src="/assets/img/2025-09-15-markov-zincirleri/2.webp" width="600" alt="">
</figure>

Its foundations date back to the early 20th century and were addressed by Andrey Markov. The discovery process began when Pavel Nekrasov grounded the Law of Large Numbers on a religious basis, claiming that everything happened in a certain order and was independent. Markov, however, argued that this was not the case, that events were not completely independent, but rather connected to the current situation and linked to each other in a random manner. To prove this, he examined the distribution of letters and words in Alexander Pushkin's poem “Eugene Onegin.” First, he prepared the first twenty thousand words of the poem as his data, dividing the letters into **vowels (V)** and **consonants (C)**. As a result of this separation, he determined that 43% of the text consisted of vowels and 57% of consonants. He then counted the pairs of letters that came together in different combinations (CC, CV, VC, VV) and calculated the transition probabilities based on these numbers. For example, the probability of a vowel following another vowel is 13%, while the probability of a consonant following is 87%. Similarly, the probability of a vowel following a consonant is approximately 67%, while the probability of another consonant following is 33%.

These ratios were organized into a **transition matrix**, thus establishing a two-state probability model, known today as a **Markov chain**. Using this chain, Markov demonstrated that a randomly started sequence of letters would, in the long run, converge to the general distribution in the text (43% vowels, 57% consonants). This structure proved that, as Nekrasov said, everything can converge not through order but through a combination of randomness and dependent states.

In the next section, we wanted to explain the basic mathematical representation. Of course, our goal here is not to focus on mathematical proofs or representations but only to provide a philosophical and intuitive explanation.

## 2. Mathematical Foundations of Markov Chains

### 2.1. Definition
A **Markov chain** is a discrete-time stochastic process:

$$
\{X_n\}_{n \ge 0},\quad X_n \in S
$$

Here:
- $S$ = set of states (finite or countable).
- $X_n$ = state of the system at time $n$.

**Markov property (memorylessness):**
$$
P(X_{n+1}=j \mid X_n=i, X_{n-1},\dots,X_0) = P(X_{n+1}=j \mid X_n=i)
$$

In other words, the future depends only on the present; the past has no effect.

---

### 2.2. Transition Probabilities
Transitions are defined by a **transition matrix** $P$:
$$
P = [p_{ij}],\qquad p_{ij} = P(X_{n+1}=j \mid X_n=i)
$$

Conditions:
$$
p_{ij} \ge 0,\qquad \sum_j p_{ij} = 1
$$

**Example (2-state system):**
$$
P=\begin{bmatrix}
0.8 & 0.2\\
0.4 & 0.6
\end{bmatrix}
$$

- If it is sunny today: tomorrow is 80% sunny, 20% rainy.  
- If it is rainy today: tomorrow is 40% sunny, 60% rainy.

---

### 2.3. Initial Distribution
Initial probability distribution:
$$
\boldsymbol{\pi}^{(0)}=[\pi^{(0)}_1,\pi^{(0)}_2,\dots,\pi^{(0)}_m],\qquad \sum_i \pi^{(0)}_i=1
$$

Distribution after $n$ steps:
$$
\boldsymbol{\pi}^{(n)}=\boldsymbol{\pi}^{(0)}P^n
$$

---

### 2.4. Stationary Distribution
Markov Chains reach a steady-state distribution after a certain number of iterations. This distribution $\boldsymbol{\pi}$ is the **stationary (equilibrium)** distribution.
If the following equation is solved, a general distribution and stable value are obtained:
$$
\boldsymbol{\pi}=\boldsymbol{\pi}P,\qquad \sum_i \pi_i=1
$$

**Example:**
Solution for the above $P$:
$$
\boldsymbol{\pi}=\begin{bmatrix}\frac{2}{3} & \frac{1}{3}\end{bmatrix}
$$
Therefore, in the long term, approximately 67% of days will be sunny and 33% will be rainy.

## 3. Applications of Markov Chains
### 3.1 Physics and Subatomic Particles:
<figure>
    <img src="/assets/img/2025-09-15-markov-zincirleri/1.webp" alt="" width="600">
</figure>

Markov chains are used to simulate how subatomic particles behave and the probabilities of jumping from one orbital to another within a set of probabilities. They are also used to determine scattering and energy states within the nucleus.
 For example, 
during World War II, John von Neumann, together with Stanislaw Ulam, developed the **Monte Carlo method** and used it to model neutron transport and chain reactions as part of the Manhattan Project. During this process, it was discovered that neutrons did not move independently, but that each step depended on the previous state, and therefore the process had to be modeled using **Markov chains**. Von Neumann and Stanislaw Ulam simulated these chains on the **ENIAC** and discovered the Monte Carlo method. In the years that followed, these studies were further developed, leading to the discovery of MCMC, which is a combination of Monte Carlo and Markov Chains.

### 3.2 NLP (Natural Language Processing)

<figure>
    <img src="https://media.geeksforgeeks.org/wp-content/uploads/20230503183646/Markov-Chains-in-NLP.webp" alt="Düşünme zinciri basamakları" width="600">
    <figcaption> Markov Chains in NLP(picture 1)</figcaption>
</figure>

Markov Chains form the basis of NLP. In early NLP models, they were used for probability calculations, such as predicting which word would follow another or for simple text generation. However, because Markov Chains have short memory, n-grams (an advanced form of Markov Chains) and the Transformer architecture have replaced Markov Chains today.

### 3.3 Google Searches and PageRank

PageRank is an algorithm developed in 1996 to determine the importance of web pages and forms the basis of Google's search algorithm.

Consider an imaginary random user browsing websites. This user enters any page and selects one of the links on that page to move to another page. These transitions are based solely on the link structure of the websites. The resulting transitions and websites are modeled on a **graph structure**. Each node on the graph is added to the Markov chain as a **state**. When this state is repeated many times, the chain reaches a **stationary-stable state** over time. This obtained state led to the emergence of the **PageRank algorithm**, which forms the basis of search engines such as Google today.
### 3.4 Bioinformatics and Modeling Biological Structures

Markov chains are widely used in bioinformatics to model statistical relationships in DNA, RNA, and protein sequences. They play an important role in gene prediction, motif search in sequences, identification of protein families, splice site detection, and phylogenetic analysis. Furthermore, hidden Markov models (HMMs) [“Markov chains specialized to capture hidden connections and relationships”] are one of the fundamental methods, particularly in genome annotation and protein sequence classification.
### 3.5 Artificial Intelligence
We mentioned that Markov Chains are used in NLP. They are also used in various areas of artificial intelligence. For example, they are used in Reinforcement Learning (Markov Decision Process, Partially Observable MDP), Image Processing (Markov Random Fields), Time Series (Markov Switch Models), and Bayesian Methods.
## 4. Weaknesses of Markov Chains

* **Memorylessness**: Markov Chains only calculate the present time, making probability calculations impossible in situations where the past is important.
* **Limited Explanatory Power**: Markov chains cannot explain the why and how of events. They only allow us to predict the outcome of events. This prevents us from getting to the root of problems in medicine and engineering and explaining them.
* **Large probability spaces**: We need a lot of computing power and data to calculate large probabilities. More data and more computing power means more situations. 
* **Insufficiency of Hidden States**: Normal Markov Chains are used to directly observe events. This leads to missing the relevant connections between some events and failing to evaluate hidden links. For this, **Hidden Markov Chains**, an enhanced version of Markov Chains, are used. For example, in speech recognition systems, it is not only the connections between words that are important, but also how the words are pronounced and in what tone of voice. We do not capture these with normal Markov chains. Instead, we use hidden Markov chains.
* **Stability**: Since Markov chains reach a stable distribution after a certain point, they may be insufficient for modeling long-term user behavior.

## 5. Advanced and Specialized Models of Markov Chains

### Monte Carlo Markov Chains (MCMC)
We mentioned MCMCs earlier. The properties of MCMCs enable the modeling and calculation of relationships that are difficult to capture and model directly, thereby revealing probabilities. They were developed in 1953 alongside the Metropolis algorithm. They are used to model the behavior of subatomic particles.

### Hidden Markov Model (HMM)
**Hidden Markov Models (HMM)** are probabilistic models that involve unobservable (hidden) states and the observations that arise from these states. It is based on a Markov chain, where each hidden state depends only on the previous state. However, these hidden states cannot be directly observed. Their effect is seen indirectly through observable outputs. It is used in areas such as speech recognition, bioinformatics, and finance.

### Table Containing Markov Chains

| Model                                                 | Description                                                                                                                                        | Applications                                                             |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Hidden Markov Models (HMM)**                        | Establishes probabilistic relationships between hidden states and observations. The state is not directly observed, only inferred through outputs. | Speech recognition, natural language processing, bioinformatics, finance |
| **Markov Chain Monte Carlo (MCMC)**                   | Generates samples from a target distribution using Markov chains. In the long run, the chain converges to the desired probability distribution.    | Bayesian statistics, machine learning, physical simulations              |
| **Semi-Markov Models**                                | The duration of staying in a state is not limited to geometric/exponential, but can follow other distributions.                                    | Queueing theory, reliability analysis                                    |
| **Markov Random Fields (MRF)**                        | Applies the Markov property on a graph structure instead of a chain. Models dependencies through neighborhood relations.                           | Image processing, computer vision, statistical physics                   |
| **Markov Decision Processes (MDP)**                   | A Markov chain augmented with actions and rewards.                                                                                                 | Reinforcement learning, optimization                                     |
| **Partially Observable MDP (POMDP)**                  | A version of MDP where the state is not fully observable. Enables decision-making under uncertainty.                                               | Robotics, games, autonomous systems                                      |
| **Absorbing Markov Chains**                           | Once entered, some states cannot be exited (absorbed).                                                                                             | Game theory, risk analysis                                               |
| **Ergodic / Irreducible Chains**                      | All states are accessible; in the long run, there is a single stationary distribution.                                                             | Theoretical analysis, statistical modeling                               |
| **Kalman Filter (Linear-Gaussian State Space Model)** | A special case of HMM with linear and Gaussian distributions.                                                                                      | Sensor fusion, robotics, finance                                         |
| **Particle Filters**                                  | Approximate tracking of continuous and complex states using particles.                                                                             | Tracking in nonlinear, non-Gaussian systems                              |

## Closing

Markov Chains remain one of the most compelling statistical methods in use today. From words to atoms, they enable us to understand the structure of humanity and nature and perceive reality in a different dimension.

Thank you for reading!

## References
- Eckhardt, R. (1987). *Stan Ulam, John von Neumann, and the Monte Carlo method*. Los Alamos Science, (15), 131–141. Los Alamos National Laboratory.  
  Access: [PDF](https://mcnp.lanl.gov/pdf_files/Article_1987_LAS_Eckhardt_131--141.pdf)

- Johoblogs. (2021, Şubat 24). *All you need to know about Markov chains*. Medium.  
  Access: [https://johoblogs.medium.com/all-you-need-to-know-about-markov-chains-d96e77988a63](https://johoblogs.medium.com/all-you-need-to-know-about-markov-chains-d96e77988a63)

- Math LibreTexts. (2022). *Markov chains and Google’s PageRank algorithm*. In *Understanding Linear Algebra (Austin)*.  
  Access: [https://math.libretexts.org/Bookshelves/Linear_Algebra/Understanding_Linear_Algebra_(Austin)/04%3A_Eigenvalues_and_eigenvectors/4.05%3A_Markov_chains_and_Google's_PageRank_algorithm](https://math.libretexts.org/Bookshelves/Linear_Algebra/Understanding_Linear_Algebra_(Austin)/04%3A_Eigenvalues_and_eigenvectors/4.05%3A_Markov_chains_and_Google's_PageRank_algorithm)

- Page, L., Brin, S., Motwani, R., & Winograd, T. (1999). *The PageRank citation ranking: Bringing order to the web*. Stanford InfoLab Technical Report.  
  Access: [https://web.archive.org/web/20250331133043/http://infolab.stanford.edu/~backrub/google.html](https://web.archive.org/web/20250331133043/http://infolab.stanford.edu/~backrub/google.html)
- StackExchange. (2015). *Markov Chains vs HMM*. Cross Validated (StackExchange).  
  Access: [https://stats.stackexchange.com/questions/148023/markov-chains-vs-hmm](https://stats.stackexchange.com/questions/148023/markov-chains-vs-hmm)

- Wikipedia contributors. (2025). *Monte Carlo method*. In *Wikipedia*.  
  Access: [https://en.wikipedia.org/wiki/Monte_Carlo_method](https://en.wikipedia.org/wiki/Monte_Carlo_method)

- Wikipedia contributors. (2025). *Hidden Markov model*. In *Wikipedia*.  
  Access: [https://en.wikipedia.org/wiki/Hidden_Markov_model](https://en.wikipedia.org/wiki/Hidden_Markov_model)

- Wikipedia contributors. (2025). *PageRank*. In *Wikipedia*.  
  Access: [https://tr.wikipedia.org/wiki/PageRank](https://tr.wikipedia.org/wiki/PageRank)

- Veritasium. (2025, Temmuz 29). *The Strange Math That Predicts (Almost) Anything – Markov Chains* [Video]. YouTube.  
  Access: [https://www.youtube.com/watch?v=KZeIEiBrT_w](https://www.youtube.com/watch?v=KZeIEiBrT_w)

- Görsel 1: GeeksforGeeks. (2023). *Markov Chains in NLP* [Görsel].  
  Access: [https://media.geeksforgeeks.org/wp-content/uploads/20230503183646/Markov-Chains-in-NLP.webp](https://media.geeksforgeeks.org/wp-content/uploads/20230503183646/Markov-Chains-in-NLP.webp)
**Images not cited in the references were generated by artificial intelligence.**
