---
id: political-twitter-messages-toernberg2023
title: Political Twitter Messages
author: Petter Törnberg
paperlink: https://arxiv.org/pdf/2304.06588.pdf
date: 14.4.2023
language: en
task:  political affiliation of a Twitter poster
version: 1.0
addedby: chkla
keywords: political affiliation, twitter
---

## Prompt Description

[Briefly describe the purpose of the prompt and the context in which it is intended to be used, especially in the context of artificial annotation with generative models.]

## Prompt Text

“You will be given a set of Twitter posts from different US politicians, sent during the two months preceding the 2020 US presidential election, that is, between September 3rd, 2020, and November 3rd, 2020. Your task is to use your knowledge of US politics to make an educated guess on whether the poster is a Democrat or Republican. Respond either ‘Democrat’ or ‘Republican’. If the message does not have enough information for an educated guess, just make your best guess.” (Törnberg 2023, p. 2)

## Language

- Prompt Language: English
- Dataset Language: English

## NLP Task

- Task: "\[C\]lassifying the political affiliation of a Twitter poster based on the content of a tweet" (Törnberg 2023, p. 1)


## Example Input and Output

- Example 1
  - Input: [Provide an example input for the prompt]
  - Output: [Provide an example output for the given input]
- Example 2
  - Input: [Provide another example input for the prompt]
  - Output: [Provide another example output for the given input]

## Parameters and Constraints

"The API was then given the Twitter messages, selected in random order. The model was run with high and low values for temperature – a parameter that controls the level of randomness or “creativity” in the generated text. Since the responses are stochastic, we ran the model 5 times at a low temperature (0.2), and at a high temperature (1.0) to capture variability in responses. The model was thus run for a total of 5000 times." (Törnberg 2023, p. 2)

## Evaluation Metrics

[List the evaluation metrics used to assess the quality of the generated artificial annotations, such as accuracy, F1 score, or BLEU score.]

## Use Cases

[List any specific use cases or applications for the prompt in artificial annotation, such as data annotation, semi-supervised learning, or active learning.]

## Limitations and Potential Biases

[Briefly discuss any limitations or potential biases associated with the prompt, as well as any steps taken to mitigate them, in the context of artificial annotation with generative models.]

## Related Research and References

[List any relevant research papers, articles, or resources that informed the creation of the prompt or are closely related to it, especially in the area of artificial annotation with generative models. Include proper citations where applicable.]

## Cite

>> Petter Törnberg (2023) "ChatGPT-4 Outperforms Experts and Crowd Workers in Annotating Political Twitter Messages with Zero-Shot Learning" [[Paper]](https://arxiv.org/pdf/2304.06588.pdf)
