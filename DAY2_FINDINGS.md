# Day 2 – Prompt Engineering Experiments

## Objective
The goal of Day 2 was to understand how prompt engineering techniques affect the quality, consistency, and reliability of LLM responses.

---

## 1. JSON Output

### Observation
- JSON output works best when the prompt explicitly instructs the model to:
  > "Return ONLY valid JSON."

### Key Learning
- Using clear formatting instructions prevents unnecessary explanations.
- Structured output is easier to parse in applications and APIs.

### Best Practice
- Use `temperature = 0`
- Clearly define the required JSON schema.
- Tell the model not to include Markdown or extra text.

---

## 2. Few-Shot Prompting

### Observation
Providing examples before asking the actual question significantly improves output consistency.

### Comparison

**Zero-Shot Prompting**
- No examples are provided.
- The model may produce inconsistent formatting.

**Few-Shot Prompting**
- Uses example input-output pairs.
- Produces more consistent and predictable responses.

### Best Use Cases
- Text classification
- Data extraction
- Standardized formatting
- AI evaluation tasks

---

## 3. Temperature Experiments

| Temperature | Observation | Best Use |
|--------------|------------|-----------|
| **0.0** | Deterministic and consistent responses | JSON, extraction, classification |
| **0.5** | Balanced creativity and accuracy | General assistants |
| **1.0** | More creative and varied responses | Brainstorming, storytelling |

### Key Learning
For structured tasks, **temperature = 0** gives the most reliable results.

---

## 4. Model Comparison

| Model | Speed | Response Quality | Recommended For |
|--------|-------|------------------|-----------------|
| **Llama 3.3 70B Versatile** | Medium | Excellent explanations | Learning, mentoring, detailed responses |
| **Llama 3.1 8B Instant** | Fast | Good accuracy | Quick responses and lightweight tasks |

### Key Learning
- Larger models provide more detailed explanations.
- Smaller models respond faster and are suitable for simple tasks.

---

## 5. Prompt Reliability

### Effective Prompt Characteristics

A good prompt should:

- Clearly define the AI's role.
- Specify the desired output format.
- Include constraints.
- Avoid ambiguity.
- Provide examples when consistency is required.

Example:

```text
You are an AI Engineering Mentor.

Rules:
- Explain concepts step by step.
- Give practical examples.
- Return ONLY valid JSON when requested.
- End every explanation with one practice exercise.
```

---

## 6. Edge Cases Tested

### Case 1
**Input**

```text
I am Tayyab from Lahore and I want to learn Machine Learning.
```

✅ Successfully extracted all fields.

---

### Case 2

**Input**

```text
I'm from Lahore.
```

✅ Returned only the available information without inventing missing values.

---

### Case 3

**Input**

```text
My name is Tayyab.
```

✅ Extracted the name correctly while leaving missing fields empty or null.

---

## Final Conclusions

During Day 2, I learned that:

- Prompt wording has a significant impact on AI responses.
- Few-Shot Prompting improves consistency over Zero-Shot Prompting.
- Structured prompts are more reliable than vague prompts.
- Temperature should be selected based on the task.
- Explicit output instructions improve response quality.
- Prompt engineering is an iterative process of testing and refinement.

---

