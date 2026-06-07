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

---

On-campus and Off-Campus Housing at the University of Florida. 

Thousands of students at the University of Florida need somewhere to live that fits their individual needs, such as cost, apartment amenties, location, and proximity to the Gainesville campus. The University of Florida offers plenty of on-campus options to live, but some students may prefer off-campus versions. Additionally, quality of individual apartment complexes may vary significantly and information is typically spread through word of mouth, instead of official channels for both on-campus dormitories and off-campus apartments do not want to diminish their reputations. The Unofficial Guide aims to help students decide between on-campus and off-campus options based on anecdotal data from students.

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | The Alligator: "A look inside UF Residence Halls" | Individual reviews for all of the on-campus housing options from the Alligator, an independent student newspaper. | https://residencehalls.alligator.org/|
| 2 | Reddit r/ufl: "What off campus housing is the best at UF? " | Reddit forum with student-responses about off-campus housing options and their respective opinions from living there. | https://www.reddit.com/r/ufl/comments/1jkdc8f/what_off_campus_housing_is_the_best_at_uf/ |
| 3 | Reddit r/ufl: "Should freshmen live on or off campus?"  | Student perspectives debating to live on or off campus for both economical and social perspectives | https://www.reddit.com/r/ufl/comments/1q3vwbj/should_freshmen_live_on_or_off_campus/ |
| 4 | SwampRentals: "What are the pros and cons of living in apartments in Gainesville vs the dorms on campus?" | Article from UF-specific student apartment locator/finder explaining differences between living on campaus and off campus. | https://www.swamprentals.com/help-finding-apartments/off-campus-vs-dorm |
| 5 | RateMyDorm | Ranking of on-campus housing options from 110 different student reviews on RateMyDorm's website, only shares 1 per unit | https://www.ratemydorm.com/ranking-dorms/university-of-florida |
| 6 | Reddit r/ufl "Any off-campus recommendations?" | Reddit forum thread highlighing off-campus apartment recommendations. | https://www.reddit.com/r/ufl/comments/154pr4g/any_offcampus_recommendations/ |
| 7 | Reddit r/ufl " Is off campus first year that bad as people say? " | Reddit thread discussing life off-campus for first-year students.| https://www.reddit.com/r/ufl/comments/1ie69mb/is_off_campus_first_year_that_bad_as_people_say/ |
| 8 | Reddit r/ufl "What are some good off-campus housing options?" | Reddit forum listing popular off-campus housing options | https://www.reddit.com/r/ufl/comments/189gg0/what_are_some_good_offcampus_housing_options/ |
| 9 | Reddit r/ufl "Dorm Reviews for UF 2024 (Or Anyone Else)" | Reddit forum reviewing most (since this is an older post) of the housing options that are on campus. | https://www.reddit.com/r/ufl/comments/fbgqnq/dorm_reviews_for_uf_2024_or_anyone_else/ |
| 10 |Reddit r/ufl "Landlords/Apartments to Avoid" | Reddit forum listing "bad" apartments to avoid. Some comments debate some of the listed apartments. | https://www.reddit.com/r/ufl/comments/ll5qbp/landlordsapartments_to_avoid/ |

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
