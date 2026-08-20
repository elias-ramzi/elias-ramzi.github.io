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

News

======

* Pictura is accepted at an ECCV 2026 workshop: a GPU-accelerated simulator that renders every agent's egocentric view, and the first large-scale driving self-play policy trained directly from perspective images; [[paper]](https://arxiv.org/abs/2607.26005) [[project page]](https://valeoai.github.io/Pictura/) [[code]](https://github.com/valeoai/Pictura/).
* TOAD is online: test-time trajectory optimization that improves existing end-to-end planners without retraining; [[paper]](https://arxiv.org/abs/2606.07170).
* Franca, on scalable visual representation learning, is accepted at CVPR 2026; [[paper]](https://arxiv.org/abs/2507.14137).
* DRIV-EX, on counterfactual explanations for driving LLMs, is accepted at ACL Findings 2026, congrats Amaia; [[paper]](https://arxiv.org/abs/2603.00696).
* My thesis was awarded the Prix de Thèse by [AFRIF](http://afrif.irisa.fr/?page_id=54) 🎉
* We have released a tech report and fully open-sourced code and weights for VaViM & VaVAM. This project builds a world model composed of a next frame predictor (VaVIM) and an action model (VaVAM); [[paper]](https://arxiv.org/abs/2502.15672) [[code]](https://github.com/valeoai/VideoActionModel).
* LLM-wrapper, which allows black-box fine-tuning of VLMs, has been accepted at ICLR 2025, congrats Amaia; [[paper]](https://arxiv.org/abs/2409.11919) [[code]](https://github.com/valeoai/LLM_wrapper).
* SupRank is accepted at TPAMI, it is the first of its kind hierarchical landmark retrieval dataset; [[paper]](https://arxiv.org/abs/2309.08250) [[code]](https://github.com/elias-ramzi/SupRank) [[dataset]](https://github.com/cvdfoundation/google-landmark).

Publications

======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
