---
id: moderation-relevance-en-gilardi2023
title: Content Moderation Relevance
author: Gilardi et al. 2023
date: 11.4.2023
language: en
task: relevance
version: 1.0
addedby: chkla
keywords: content moderation, relevance
---

## Prompt Description

[Briefly describe the purpose of the prompt and the context in which it is intended to be used, especially in the context of artificial annotation with generative models.]

## Prompt Text
For each tweet in the sample, follow these instructions:<br>
1. Carefully read the text of the tweet, paying close attention to details.<br>
2. Carefully read the text of the tweet, paying close attention to details.<br>
<br>
Tweets should be coded as RELEVANT when they directly relate to content moderation, as defined above. This includes tweets that discuss: social media platforms’ content moderation rules and practices, governments’ regulation of online content moderation, and/or mild forms of content moderation like flagging.<br>
<br>
Tweets should be coded as IRRELEVANT if they do not refer to content moderation, as defined above, or if they are themselves examples of moderated content. This would include, for example, a Tweet by Donald Trump that Twitter has labeled as “disputed”, a tweet claiming that something is false, or a tweet containing sensitive content. Such tweets might be subject to content moderation, but are not discussing content moderation. Therefore, they should be coded as irrelevant for our purposes.

## Language

- Prompt Language: [Specify the language of the prompt, e.g., English]
- Dataset Language: [Specify the language of the dataset to which the prompt is applied, e.g., English]

## NLP Task

- Task: [Specify the NLP task in more detail, e.g., sentiment analysis, named entity recognition, summarization]
- Subtask: [If applicable, provide any subtask or variation related to the main NLP task, e.g., binary sentiment classification, multi-class sentiment classification]

## Example Input and Output

- Example 1
  - Input: [Provide an example input for the prompt]
  - Output: [Provide an example output for the given input]
- Example 2
  - Input: [Provide another example input for the prompt]
  - Output: [Provide another example output for the given input]

## Parameters and Constraints

- Parameter 1: [Specify any parameters, such as temperature or token count]
- Parameter 2: [Specify additional parameters or constraints if applicable]

## Evaluation Metrics

[List the evaluation metrics used to assess the quality of the generated artificial annotations, such as accuracy, F1 score, or BLEU score.]

## Use Cases

[List any specific use cases or applications for the prompt in artificial annotation, such as data annotation, semi-supervised learning, or active learning.]

## Limitations and Potential Biases

[Briefly discuss any limitations or potential biases associated with the prompt, as well as any steps taken to mitigate them, in the context of artificial annotation with generative models.]

## Related Research and References

[List any relevant research papers, articles, or resources that informed the creation of the prompt or are closely related to it, especially in the area of artificial annotation with generative models. Include proper citations where applicable.]

