# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->

My domain I chose is "Everything Computer Science" for CUNY College of Staten Island. This will give students useful information about the Computer science department and major at CSI. Students can for example ask about courses offered, the different programs and specializations, Research, The faculty, etc.

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

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
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

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
