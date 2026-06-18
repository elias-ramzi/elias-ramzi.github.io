---
title: "ITEM: Improving Training and Evaluation of Message-Passing based GNNs for top-k recommendation"
collection: publications
permalink: /publication/2024-07-03-item-improving-training-and-evaluation-of-message-passing
excerpt: "Graph Neural Networks (GNNs), especially message-passing-based models, have become prominent in top-k recommendation tasks, outperforming matrix factorization models due to their ability to efficiently aggregate information from a broader context. Although GNNs are evaluated with ranking-based metrics, e.g NDCG@k and Recall@k, they remain largely trained with proxy losses, e.g the BPR loss. In this work we explore the use of ranking loss functions to directly optimize the evaluation metrics, an area not extensively investigated in the GNN community for collaborative filtering. We take advantage of smooth approximations of the rank to facilitate end-to-end training of GNNs and propose a Personalized PageRank-based negative sampling strategy tailored for ranking loss functions. Moreover, we extend the evaluation of GNN models for top-k recommendation tasks with an inductive user-centric protocol, providing a more accurate reflection of real-world applications. Our proposed method significantly outperforms the standard BPR loss and more advanced losses across four datasets and four recent GNN architectures while also exhibiting faster training. Demonstrating the potential of ranking loss functions in improving GNN training for collaborative filtering tasks."
date: 2024-07-03
venue: 'TMLR'
paperurl: 'https://arxiv.org/pdf/2407.07912'
citation: 'Yannis Karmim, <b>Elias Ramzi</b>, Raphaël Fournier-S &apos;Niehotta, Nicolas Thome: ITEM: Improving Training and Evaluation of Message-Passing based GNNs for top-k recommendation. TMLR (2024).'
---
