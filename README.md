# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->
My domain I chose is "Everything Computer Science" for CUNY College of Staten Island. This will give students useful information about the Computer science department and major at CSI. Students can for example ask about courses offered, the different programs and specializations, Research, The faculty, etc.
---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | CS Home page|Computer science at College of staten island official home page | https://www.cs.csi.cuny.edu/index.html |
| 2 | CS Faculty|CS Faculty all prof and staff info|https://www.cs.csi.cuny.edu/people.html |
| 3 |CSI CS page|CSI official CS page |https://www.csi.cuny.edu/academics-and-research/departments-programs/computer-science |
| 4 |Graduate page|CS graduate program page |https://www.cs.csi.cuny.edu/graduate.html |
| 5 | CS Undergrad page|CS undergrad information page |https://www.cs.csi.cuny.edu/undergraduate.html |
| 6 | CS Roadmap| Computer science Sample Road map carrer map |https://www.csi.cuny.edu/sites/default/files/pdf/academciadvisement/PathwaysAcadPlans/ComputerScienceBS_DegreeMap.pdf|
| 7 | Course Catalog|Computer Science Course Catalog |https://csi-undergraduate.catalog.cuny.edu/departments/CSC-CSI/courses |
| 8 | Course Catalog V2| More course catalog|https://www.cs.csi.cuny.edu/courses.html |
| 9 |Mandatory Core CS course|CSC 126|https://csi-undergraduate.catalog.cuny.edu/courses/0626561/general-aoYks |
| 10 | Mandatory Core CS course|CSC 211|https://csi-undergraduate.catalog.cuny.edu/courses/0626631/general-aoYks |
| 11 |Mandatory Core CS course |CSC 326 |https://csi-undergraduate.catalog.cuny.edu/courses/0626831/general-aoYks |
| 12 | Mandatory Core CS course|CSC 382 | https://csi-undergraduate.catalog.cuny.edu/courses/0626991/general-aoYks|

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**

**Overlap:**

**Why these choices fit your documents:**

**Final chunk count:**

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
