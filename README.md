# Annotation PromptCards 🏷️: A Way for Structured Prompt Sharing and Reuse in Artificial Annotation with Generative Models

PromptCards are designed to facilitate prompt sharing and reuse in research, providing a structured template for documenting and comparing prompts, especially for artificial annotation using generative models. By using a consistent format, researchers can reuse existing prompts in new contexts and compare results across projects that have employed the same prompts.

Check out ⬇️:
* Annotation PromptCards [![Google Slides](https://img.shields.io/badge/Archive-yellow?logo=google-slides)](https://huggingface.co/spaces/chkla/AnnotationPromptCards)
* Annotation PromptCards [![Google Slides](https://img.shields.io/badge/Playground-green?logo=google-slides)](https://huggingface.co/spaces/chkla/PromptCardsPlayground)

Some studies have highlighted the potential of ChatGPT as a data annotation tool (Huang et al., 2023). For instance, Gilardi et al. (2023) reported that ChatGPT outperforms MTurk in four out of five tasks. This has prompted researchers to ask if we are witnessing the beginning of the end for manual linguistic data annotation (Kuzman et al., 2023).

When training large language models, the concept of "non-determinism" arises. With zero-shot annotations using generative language models like ChatGPT, several factors influence the generative output. Consequently, similar inputs can yield different results. Reiss (2023) demonstrated the ambiguity of prompts and their predictions in an artificial annotation setting in his paper.

This project aims to establish a method for standardizing and sharing prompts, as well as validating the performance of a given prompt for a specific task on a particular dataset. We offer a way to evaluate various annotation prompts for a defined task. AnnotationPromptCards [![Google Slides](https://img.shields.io/badge/Archive-yellow?logo=google-slides)](https://huggingface.co/spaces/chkla/AnnotationPromptCards) serves as an archive of prompts for artificial annotation. Using the [![Google Slides](https://img.shields.io/badge/AInnotator-green?logo=google-slides)](https://huggingface.co/spaces/chkla/PromptCardsPlayground) tool, users can experiment with different prompts on their data.

The project serves as a hub for sharing prompts, enabling users to test existing and new prompts. Our objective is to lower the barriers to using artificial annotators for testing purposes, while simultaneously promoting standardization, reliability and transparency of annotation templates in research and other domains.

We encourage you to contribute your PromptCards to the repository and engage with the community to improve and expand the range of available prompts. Please use the following template:

## 🏷️ PromptCard Template

To create a PromptCard, simply copy the template below and fill in the relevant details. Share your PromptCard with the community by submitting it to the repository.

```markdown
---
Title: [Title of your prompt]
Author: [Your name or organization]
Paper: [Link to the paper]
Date: [Date created or updated]
Language: [Language of the prompt]
Task: [NLP task]
Version: [Version number, e.g., 1.0]
---

## Prompt Description

[Briefly describe the purpose of the prompt and the context in which it is intended to be used, especially in the context of artificial annotation with generative models.]

## Prompt Text

[Insert the complete prompt text here, including any specific instructions or formatting.]

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

[Add the relevant publication]


```

## Literature:
* Reiss (2023) "Testing the Reliability of ChatGPT for Text Annotation and Classification: A Cautionary Remark" [[Paper](https://www.dropbox.com/s/3z7okruhft74o1a/ChatGPT_Reliability_0405.pdf?dl=0)]
* Kuzman et al. (2023) "ChatGPT: Beginning of an End of Manual Linguistic Data Annotation? Use Case of Automatic Genre Identification" [[Paper](https://www.semanticscholar.org/reader/31f44f0f2124c54e47f4df54dec63118232c25da)]
* Gilardi et al. (2023) "ChatGPT Outperforms Crowd-Workers for Text-Annotation Tasks" [[Paper](https://arxiv.org/pdf/2303.15056.pdf)]
* ... and many more!

---

_Made with ❤️ and 🤖_
