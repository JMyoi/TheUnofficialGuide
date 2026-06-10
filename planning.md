# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

College of Staten Island student knowledge about professor quality, campus housing, admissions, academics, and campus life. This knowledge is valuable because official CSI pages explain policies and offerings, but they do not capture how courses actually feel, which professors are clear or strict, or how students experience housing and campus community day to day.

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | CSI student housing information | Official housing guide and support details | https://www.csi.cuny.edu/admissions/new-student-guide/undergraduate-guide/student-housing-information |
| 2 | CSI student financial aid and campus housing | Official aid and housing information | https://www.csi.cuny.edu/admissions/paying-college/financial-aid/student-financial-aid-and-campus-housing-csi |
| 3 | Rate My Professors CSI school page | Student ratings and review summaries for CSI professors | https://www.ratemyprofessors.com/school/225 |
| 4 | Rate My Professors: Mojgan Keshtgar | Professor-specific review page with course-level feedback | https://www.ratemyprofessors.com/professor/886156 |
| 5 | Rate My Professors: Susan Cohen | Professor-specific review page with course-level feedback | https://www.ratemyprofessors.com/professor/2108253 |
| 6 | U.S. News CSI profile | Aggregate college overview, rankings, and campus metrics | https://www.usnews.com/best-colleges/cuny-college-of-staten-island-29040 |
| 7 | Niche CSI profile | Student reviews, campus life, academics, and admissions details | https://www.niche.com/colleges/cuny-college-of-staten-island/ |
| 8 | CSI Dolphins athletics site | Student athletics and campus sports community context | https://csidolphins.com/ |
| 9 | CSI departments and programs | Official academic departments and program overview | https://www.csi.cuny.edu/academics-and-research/departments-programs |
| 10 | CSI admissions | Official admissions information and pathways | https://www.csi.cuny.edu/admissions |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**

**Overlap:**

**Reasoning:**

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**

**Top-k:**

**Production tradeoff reflection:**

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What do students say about Professor Mojgan Keshtgar's workload and grading style? | Reviews describe her as clear and well liked by many students, but also test-heavy and fast paced in some classes. |
| 2 | What do students say about Professor Susan Cohen's teaching style? | Reviews describe her as caring, supportive, and often giving homework or exam help in class. |
| 3 | What do students say about CSI campus life and social scene? | Students often describe CSI as commuter-heavy, quieter than a traditional residential campus, and improved by clubs, sports, and individual effort. |
| 4 | What does CSI's housing-related information say about campus housing support? | The official pages explain housing-related support and financial aid context, not student gossip or apartment quality. |
| 5 | What do CSI student reviews say about professors, advising, or communication? | Students often praise individual professors but criticize inconsistent advising, registration, and administrative communication. |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1.

2.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
