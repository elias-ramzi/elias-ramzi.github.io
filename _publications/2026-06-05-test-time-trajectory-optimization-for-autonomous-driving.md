---
title: "Test-Time Trajectory Optimization for Autonomous Driving"
collection: publications
permalink: /publication/2026-06-05-test-time-trajectory-optimization-for-autonomous-driving
excerpt: "End-to-end planners for autonomous driving typically generate a set of candidate trajectories, score each one, and return the highest-scoring candidate. However, the scorer is applied only after the proposals are generated and cannot influence the set of trajectories: a weak set of candidates limits planning performance regardless of the scorer&apos;s quality. We instead treat the scorer as a learned trajectory-level reward function and search for trajectories that maximize it. Our method, TOAD, runs the Cross-Entropy Method at test time, warm-started from the planner&apos;s proposals. It requires no retraining and is plug-and-play for existing planners. Across six base planners, TOAD improves results on NAVSIM-v1 (94.7 PDMS), NAVSIM-v2 (56.3 EPDMS), and the closed-loop HUGSIM benchmark. The code will be made publicly available via the project page: https://valeoai.github.io/TOAD/."
date: 2026-06-05
venue: 'arXiv preprint'
paperurl: 'https://arxiv.org/pdf/2606.07170'
citation: 'Yihong Xu, Éloi Zablocki, Yuan Yin, <b>Elias Ramzi</b>, Ellington Kirby, Alexandre Boulch, Matthieu Cord: Test-Time Trajectory Optimization for Autonomous Driving. arXiv preprint (2026).'
---