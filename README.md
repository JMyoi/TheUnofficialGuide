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
**Chunk size: 500 characters**

**Overlap: 75 characters**

**Using Langchains RecursiveCharacterTextSplitter**

**Reasoning: I will use recursive character splitting, since the document is of mixed types, and have some structure to it, My sources are Structered and factual, course deccriptions, faculty bios, program requirements, They are not flowing essays, they're short and dnese paragraphs where each part is a complete idea, 500 characters is about 2-5 sentences, enough to captuer a complete fact like a course description, too large might merge unrelated courses, too small will cut descriptions in half.**

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:*sentence-transformers (all-MiniLM-L6-v2) Runs locally — no API key, no rate limits*

**Production tradeoff reflection: for this project the all-MiniLM-L6-v2 runs locally with no API cost or rate limit, ideal for this type of practice development, IF it was a real deployment I would weight stuff like accuracy, OpenAI embedding model producs more high quality embeddings, but it's paid, open AI's embedding produces more context lenght aroudn 8k tokens whereas all-MiniLM-L6-v2 is only 256 token imput limit:**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:You are a helpful assistant for students at CUNY College of Staten Island's Computer Science department.
Answer the question using ONLY the information in the provided document excerpts.
Do not use any outside knowledge.
If the documents don't contain enough information to answer, say exactly: "I don't have enough information on that."
At the end of your answer, list the source files you used on a line starting with "Sources:".
**

**How source attribution is surfaced in the response:The system prompt instructs the model to end every response with a line starting with Sources: listing the filenames it drew from**

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What are some core courses that I will take in the computer science major? | CSC 126, CSC 211, CSC 326, CSC 382 | The documents do not specifically list the core courses for the CS major, but mention graduate core courses (CSC 716, 727, 740, 770) and undergraduate intro course CSC 126. Sources: Undergraduate.txt, CSICSPage.txt, Graduate.txt | Partially relevant | Partially accurate |
| 2 | What are the Computer Science Specializations? | Game Dev, Networking and Security, High Performance Computing, Data Science | BS specializations: Game Development, Networking and Security, High Performance Computing, Data Science. MS specializations: AI and Data Analytics, Cloud Computing and Software Engineering, Cybersecurity and Networks. Sources: CSHomePage.txt, Undergraduate.txt | Relevant | Accurate |
| 3 | What AI related or machine learning courses are offered at CSI? | CSC 412, CSC 245, CSC 480, CSC 735 | I don't have enough information on that. Sources: Graduate.txt, Undergraduate.txt, CSICSPage.txt, CSC211.txt, CSC126.txt | Off-target | Inaccurate |
| 4 | What are the required courses for the Masters of Computer Science at CSI? | CSC 716, CSC 727, CSC 740, CSC 759 | Required core: CSC 716 (Advanced Operating Systems), CSC 727 (Algorithms and Information Structures), CSC 740 or CSC 770, CSC 759 or CSC 799. Plus 6 elective graduate courses for 30 total credits. Sources: Graduate.txt | Relevant | Accurate |
| 5 | Who is the Distinguished professor in the CS department? | Sos Agaian | I don't have enough information on that. Sources: CSICSPage.txt, Undergraduate.txt, CSC126.txt, CSC326.txt, CSHomePage.txt | Off-target | Inaccurate |

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

3, 
**Question that failed:**
What AI related or machine learning courses are offered at CSI?
**What the system returned:**
I don't have enough information on that. Sources: Graduate.txt, Undergraduate.txt, CSICSPage.txt, CSC211.txt, CSC126.txt
**Root cause (tied to a specific pipeline stage):**
A whole list of courses was given as data but I guess since they were in separate chunks, 8 returned chunks was not enough to get courses related to AI. 
**What you would change to fix it:**
Increase K for this quesiont could help.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation: specs helped alot because I had to research adn think about the choices I was going to make architectually and also when it came time to generate code since I already had everyything planned out it was easy and specific as to what I wanted and Claude did a good job at generating it**

**One way your implementation diverged from the spec, and why:When I first tested out the generation it seemed that most of the times it would respond with I don't have enough information so I realized that it did not have enough context so I increased k = 5 to k = 8 and it worked better.**


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

- *What I gave the AI:Asked claude to write the chunking logigc, I gave it the specs and the tools that I was planning ot use to implement the chunking as well as the size and overlap and the folder where the data was held.*
 
- *What it produced: chunk.py which was the code implementation for chunking,* 

- *What I changed or overrode: nothing*

**Instance 2**

- *What I gave the AI:asked claude to write logic for embeding query and semantic search the chromaDB for top k = 5 and prompt construction with Grounded generation and to generate with chunk context using GroqAPI and make a UI*
- *What it produced: the code for the UI and logic for retrieval and generation*
- *What I changed or overrode:nothing*
