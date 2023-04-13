---
id: topic-detection-gilardi2023
title: Topic Detection
author: Fabrizio Gilardi, Meysam Alizadeh and Maël Kubli
paperlink: https://arxiv.org/abs/2303.15056 
date: 27.3.2023
language: en
task: topic detection
version: 1.0
addedby: chkla
keywords: content moderation, topic detection
---

## Prompt Description

[Briefly describe the purpose of the prompt and the context in which it is intended to be used, especially in the context of artificial annotation with generative models.]

## Prompt Text

Tweets about content moderation may also discuss other related topics, such as:<br>
1. Section 230, which is a law in the United States that protects websites and other online platforms from being held legally responsible for the content posted by their users (SECTION 230).<br>
2. The decision by many social media platforms, such as Twitter and Facebook, to suspend Donald Trump’s account (TRUMP BAN).
3. Requests directed to Twitter’s support account or help center (TWITTER SUPPORT).<br>
4. Social media platforms’ policies and practices, such as community guidelines or terms of service (PLATFORM POLICIES).
5. Complaints about platform’s policy and practices in deplatforming and content moderation or suggestions to suspend particular accounts, or complaints about accounts being suspended or reported (COMPLAINTS).<br>
6. If a text is not about the SECTION 230, COMPLAINTS, TRUMP BAN, TWIT- TER SUPPORT, and PLATFORM POLICIES, then it should be classified in OTHER class (OTHER).<br>
<br>
For each tweet in the sample, follow these instructions:<br>
1. Carefully read the text of the tweet, paying close attention to details.<br>
2. Please classify the following text according to topic (defined by function of the text, author’s purpose and form of the text). You can choose from the following classes: SECTION 230, TRUMP BAN, COMPLAINTS, TWITTER SUPPORT, PLATFORM POLICIES, and OTHER<br>

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

## Cite

>> Fabrizio Gilardi, Meysam Alizadeh, Maël Kubli (2023) "ChatGPT Outperforms Crowd-Workers for Text-Annotation Tasks" [[Paper]](https://arxiv.org/abs/2303.15056)
