You can update LLMDetect benchmark and trained model into huggingface, and provide the download & usage guidelines here.

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
