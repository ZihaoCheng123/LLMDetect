# Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement

This repository contains the data of the paper Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measuremen. See the paper for additional details:

Cheng, Z., Zhou, L., Jiang, F., Wang, B., & Li, H. (2024). Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement. [Link](https://arxiv.org/abs/2410.14259)

You can also view the dataset on Hugging Face. [Link](https://huggingface.co/datasets/czhcuhk/LLMDetect)

You can download the PLM-based models on Hugging Face. [Link](https://huggingface.co/czhcuhk/LLMDect)

This is a comprehensive benchmark for LLM-Generated Text Detection. 

- LLMDetect
  - HNDC
    - train.json
    - val.json
    - test.json
  - DetectEval
    - Cross-context
      - cross-time
      - cross-prompt
      - cross-source
      - cross-cultural
      - cross-domain
    - Multi-intensity
      - Variable-Length-Extension
      - Multi-Staged-Polish

label "PR" is LLM Involvement Ratio in our task, and we use "human","draft","revise","continue" to label the text source.

If the label "human" equals 1, indicating it is Human-Author.

If the label "draft" equals 1, indicating it is LLM-Creator.

If the label "revise" equals 1, indicating it is LLM-Polisher.

If the label "continue" equals 1, indicating it is LLM-Extender.

## Citation

```bibtex
@inproceedings{cheng2025beyond,
  title={Beyond binary: Towards fine-grained llm-generated text detection via role recognition and involvement measurement},
  author={Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
  booktitle={Proceedings of the ACM on Web Conference 2025},
  pages={2677--2688},
  year={2025}
}
