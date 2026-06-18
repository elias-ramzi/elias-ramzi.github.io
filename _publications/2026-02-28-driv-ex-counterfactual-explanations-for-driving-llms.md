---
title: "DRIV-EX: Counterfactual Explanations for Driving LLMs"
collection: publications
permalink: /publication/2026-02-28-driv-ex-counterfactual-explanations-for-driving-llms
excerpt: "Large language models (LLMs) are increasingly used as reasoning engines in autonomous driving, yet their decision-making remains opaque. We propose to study their decision process through counterfactual explanations, which identify the minimal semantic changes to a scene description required to alter a driving plan. We introduce DRIV-EX, a method that leverages gradient-based optimization on continuous embeddings to identify the input shifts required to flip the model&apos;s decision. Crucially, to avoid the incoherent text typical of unconstrained continuous optimization, DRIV-EX uses these optimized embeddings solely as a semantic guide: they are used to bias a controlled decoding process that re-generates the original scene description. This approach effectively steers the generation toward the counterfactual target while guaranteeing the linguistic fluency, domain validity, and proximity to the original input, essential for interpretability. Evaluated using the LC-LLM planner on a textual transcription of the highD dataset, DRIV-EX generates valid, fluent counterfactuals more reliably than existing baselines. It successfully exposes latent biases and provides concrete insights to improve the robustness of LLM-based driving agents. The code is available at &quot;https://github.com/Amaia-CARDIEL/DRIV_EX&quot; ."
date: 2026-02-28
venue: 'ACL findings'
paperurl: 'https://arxiv.org/pdf/2603.00696'
citation: 'Amaia Cardiel, Éloi Zablocki, <b>Elias Ramzi</b>, Eric Gaussier: DRIV-EX: Counterfactual Explanations for Driving LLMs. ACL findings (2026).'
---
