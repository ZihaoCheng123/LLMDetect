This is a comprehensive benchmark for LLM-assisted Text Detection.

The Source of this benchmark is news from New York Times and the Guardian before 2019.

- LLMDetect
  - HNDC
    - train.json
    - dev.json
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

label "PR" in the is LLM Involvement Ratio in our task, and we use "human","draft","revise","continue" to label the text source.

If the label "human" equals 1, indicating it is Human-Author.

If the label "draft" equals 1, indicating it is LLM-Creator.

If the label "revise" equals 1, indicating it is LLM-Polisher.

If the label "continue" equals 1, indicating it is LLM-Extender.
