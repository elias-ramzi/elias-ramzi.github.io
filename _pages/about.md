---
permalink: /
title: "Elias Ramzi - AI Research scientist"
excerpt: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% include base_path %}

I am a Research Scientist at valeo.ai, where I work on deep learning for autonomous driving. My research focuses on end-to-end driving — learning to plan directly from sensor data — together with the world models that predict how a scene will unfold and the vision-language models and LLMs used for reasoning and explainability. Recent work includes [VaViM & VaVAM](https://arxiv.org/abs/2502.15672), a video world model and action model for driving. I also co-supervise two PhD students, one on LLMs/VLMs and one on world models and reinforcement learning.

Before joining valeo.ai, I earned a PhD in computer vision at Cnam, supervised by Nicolas Thome (Sorbonne Université), Nicolas Audebert (IGN) and Clément Rambour (Cnam), with Xavier Bitot (Coexya) as industrial advisor. My thesis — awarded the AFRIF Prix de Thèse — focused on ranking-loss optimization and hierarchical learning for image retrieval (ROADMAP, HAPPIER, SupRank).

<!-- A data-driven personal website
====== -->

News

======

* We have released a tech report and fully open-sourced code and weights for VaViM & VaVAM. This project builds a world model composed of a next frame predictor (VaVIM) and an action model (VaVAM);  [[paper]](https://arxiv.org/abs/2502.15672) [[code]](https://github.com/valeoai/VideoActionModel).
* LLM-wrapper, which allows black-box fine-tuning of VLMs, has been accepted at ICLR 2025, congrats Amaia; [[paper]](https://arxiv.org/abs/2409.11919) [[code]](https://github.com/valeoai/LLM_wrapper).
* SupRank is accepted at TPAMI, it is the first of its kind hierarchical landmark retrieval dataset; [[paper]](https://arxiv.org/abs/2309.08250) [[code]](https://github.com/elias-ramzi/SupRank) [[dataset]](https://github.com/cvdfoundation/google-landmark).
<!-- * Our code for GalLop is available online at [GalLop](https://github.com/MarcLafon/gallop) -->
* I started at valeo.ai as a research scientist.
* Our paper for local prompt learning, GalLoP, has been accepted to ECCV 2024; [[paper]](https://arxiv.org/abs/2407.01400) [[code]](https://github.com/MarcLafon/gallop).
* Our paper ITEM on improving the learning and evaluation of Message-Passing GNNs models in the recommendation task has been accepted at TMLR; [[paper]](https://arxiv.org/abs/2407.07912).
* I defended my PhD thesis on the 20th of March. I now officialy hold a PhD 🎉 [[manuscript]](https://elias-ramzi.github.io/files/pdf/manuscrit_these_elias_ramzi_final.pdf).
<!-- * My pre-print submitted to TPAMI is now online; it contains the first of its kind hierarchical landmark retrieval dataset -->
<!-- *  at https://arxiv.org/abs/2309.08250. -->
<!-- * I am going to ICML 2023. I will be presenting HEAT in a poster session. -->
<!-- * I am participating to the Internation Computer Vision Summer School (ICVSS, 2023) this summer in Sicily. -->
<!-- * I have released the first of its kind hierarchical landmark retrieval dataset as a part of a TPAMI submission. -->
<!-- *  It is available at https://github.com/cvdfoundation/google-landmark. -->
<!-- * I am a reviewer for NeurIPS 2023. -->
<!-- * I am going to ORASIS 2023. I will be presenting HAPPIER in a poster session. -->
* Our paper on OOD detection, HEAT, using energy-based models has been accepted to ICML 2023; [[paper]](https://arxiv.org/abs/2305.16966) [[code]](https://github.com/MarcLafon/heatood).
<!-- * I am a reviewer for ICML 2023. -->
<!-- * I served as a sub-reviewer for CVPR 2023. -->
<!-- * I am going to present our ECCV 2022 paper, HAPPIER, to the 25th of October in Tel Aviv. -->
* Our paper on hierarchical image retrieval, HAPPIER, has been accepted to ECCV 2022; [[paper]](https://arxiv.org/abs/2207.04873) [[code]](https://github.com/elias-ramzi/HAPPIER).
<!-- * I will be presenting our ROADMAP paper at RFIAP 2022. -->
* Our paper on ranking metric optimization for image retrieval, ROADMAP, has been accepted to NeurIPS 2021; [[paper]](https://arxiv.org/abs/2110.01445) [[code]](https://github.com/elias-ramzi/ROADMAP).

Publications

======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
