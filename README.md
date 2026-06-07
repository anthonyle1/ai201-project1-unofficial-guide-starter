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

**Chunk size:** 1000

**Overlap:** 200

**Why these choices fit your documents:**
Chunk size varies depending on the type of document. Since we are working with both shorter reddit posts and comments with complete thoughts and longer blog-style posts, it would be better to chunk these differently to help our program to ensure context within a chunk is best-fit.

**Final chunk count:** 510

**Sample Chunks**
```
================================================================================
QUERY: What are some of the differences between living on and off campus at UF?
================================================================================

Rank #1
Source: documents\reddit\should_freshmen_live_on_or_off_campus.json
Chunk Position: should_freshmen_live_on_or_off_campus_reddit_comment_14
Distance: 0.5996

Chunk:
Post Title: Should freshmen live on or off campus?
Comment by [deleted]

hey, there’s pros and cons to both. you can reach out to the off campus life office to learn about it! the directors do one on one meetings to answer all of your questions and go through options with u
--------------------------------------------------------------------------------

Rank #2
Source: documents\reddit\should_freshmen_live_on_or_off_campus.json
Chunk Position: should_freshmen_live_on_or_off_campus_reddit_comment_4
Distance: 0.6507

Chunk:
Post Title: Should freshmen live on or off campus?
Comment by TraderGIJoe

Search on this sub. 

There are new students like transfers who have had trouble making friends isolated off campus.

Get the full college experience, if possible!
--------------------------------------------------------------------------------

Rank #3
Source: documents\reddit\should_freshmen_live_on_or_off_campus.json
Chunk Position: should_freshmen_live_on_or_off_campus_reddit_post_0
Distance: 0.6546

Chunk:
Title: Should freshmen live on or off campus?
Author: jjjjn240

I want to get an idea on whether it’s better to live on or off campus as a freshman, both socially and economically.
--------------------------------------------------------------------------------

Rank #4
Source: documents\reddit\should_freshmen_live_on_or_off_campus.json
Chunk Position: should_freshmen_live_on_or_off_campus_reddit_comment_16
Distance: 0.6573

Chunk:
Post Title: Should freshmen live on or off campus?
Comment by Little-Pace2622

As a freshman living off-campus, I feel like the whole “being on-campus is better for socialization” can be supplemented if you’re heavily involved with the student orgs! While it is harder to involve myself with other freshman since I’m off-campus, I still prefer the ability to have my own room and kitchen over being in the dorms.
--------------------------------------------------------------------------------

================================================================================
QUERY: What are the negatives of living at Jennings Hall?
================================================================================

Rank #1
Source: https://residencehalls.alligator.org
Chunk Position: residencehalls_alligator_org_webpage_11
Distance: 0.9143

Chunk:
of a communal study place. It was a fun place to do work.âIf youâre looking for the communal dorm experience, definitely be in Jennings,âIt was absolutely perfect, and I would choose it all over again.âI think it has a nice common space that people get to hang out in,âI never had any problems with bugs, rodents or anything,âIt's further from food and things to do,âYou either have to convert your beds into these weird bunk beds that aren't actually bunk beds or sleep so close to each other that you could hold hands every night,âs housing website.
Washers and dryers are located at the bottom floor of the building.
Jennings Hall construc
--------------------------------------------------------------------------------
```
---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**
all-MiniLM-L6-v2

**Production tradeoff reflection:**
Increasing the top-k can provide more context to the LLMs, as you provide more chunks for the LLMs at the cost of increasing the number of tokens used. The LLM we use allow for different context lengths, which helps inform how much of the "top-k" we can use or even increasing the chunk size to help better give context to LLM queries. Additionally, the type of LLM we use have other constraints, such as what written languages are supported (English, Spanish, Chinese, etc.). Providing more context could also bring more accurate content for domain-specific text.

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
I used the following from the project the specification: "Answer the question using only the information in the provided documents. If the documents don't contain enough information to answer, say 'I don't have enough information on that" After, I added on the question and related chunks to the prompt before prompting the LLM.

```python
def build_prompt(question):
    return f"""
        Answer the question using only the information in the provided documents. If the documents don't contain enough information to answer, say 'I don't have enough information on that. Additionally, cite the source(s) used to help generate the response.
        
        {question}

        Answer:
        """
```

**How source attribution is surfaced in the response:**
The sources used for each chunk are saved when retrieving the chunks alongside the source text. Afterward, the related texts fill the "retrived from:" section on the Gradle UI.
Additionally, the prompt includes "Additionally, cite the source(s) used to help generate the response", which tells the Groq client/LLM to ensure facts are cited with relevant sources found in the metadata of each chunk. 

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What are some cons of living on-campus? | Limited parking, not guaranteed for freshman students, limited cooking ability | On-campus dorm living has several drawbacks, including limited privacy and shared living spaces. Housing is not always guaranteed, so students may need a backup plan. It can also be more expensive, with additional concerns like parking difficulties and limited cooking options compared to off-campus housing, where students may have more flexibility and amenities like private kitchens. | Relevant | Accurate |
| 2 | What are some pros of living on campus? | Proximity to classes and club events, ability to connect with people more easily; often ideal for freshman students | Living on campus offers convenience and a strong college experience, including easy access to classes and campus events, proximity to athletics and tailgates, and built-in campus security. It also supports social connection and a more traditional college environment. Source: Swamp Rentals Off-Campus vs Dorm | Relevant | Accurate |
| 3 | Can you list all of the available on-campus dorms? | List all available dorms on campus | Not enough provided data to list all dorms. Only partial list available (e.g., Yulee and Keys). | Partially relevant | Partially accurate |
| 4 | Can you list some off-campus apartment complexes? | List of available apartment complexes in Gainesville, FL | 1. Canopy<br>2. The Woodlands<br>3. University Club<br>4. University Common<br>5. College Park<br>6. Off Campus Life Website | Partially relevant | Accurate |
| 5 | What are some of the benefits of living at Murphree Hall? | Proximity to Midtown, gym access, aesthetic/architecture, community feel, etc. | Murphree Hall offers several benefits, including quieter living conditions due to thick walls, strong community engagement through events and shared spaces like lounges, and a convenient location with scenic surroundings. It also provides relatively spacious rooms, less crowded communal bathrooms, good air conditioning, cleanliness, and close access to the gym. | Relevant | Partially accurate |

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
Can you list all of the available on campus dorms?

**What the system returned:**
I don't have enough information on that. The provided documents only mention a few specific dorms, such as Yulee Hall and Keys, but do not provide a comprehensive list of all available on-campus dorms at the University of Florida.

**Root cause (tied to a specific pipeline stage):**
Questions was fairly specific. Poor chunking so data that includes all of the relevant dorms on campus are split between individual pages. There isn't anywhere in the data that had all of the possible dorms on campus in one area. The output also exists in part to the guardrails written into the prompt given to the Groq client. 

**What you would change to fix it:**

I would add another document which listed all of the relevant dorms on campus in a more central chunk. Then I would add the chunk to the ChromaDB vector database. Other options include increasing the chunk size and increase the amount of chunks retrived then given to the LLM.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
The spec provided a lot of things to look for in the output of each milestone! It provided insights to how to do the project, in regards to how chunks look like, how to ask questions, and what to look for when verifying my code. I used it to ensure I was on the right track between milestones. 

**One way your implementation diverged from the spec, and why:**
Creating seperate chunking methods for JSON and HTML files. I ended up doing this to ensure comments's content, which are typically very short, are containted with each other and do not interfere with others. 

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

- *What I gave the AI:* I asked AI to generate the chunking functions based on the structure of how I formatted the data in my ingestion functions. 
- *What it produced:* Chunking functions which provided a fixed-size approach to chunking data. 
- *What I changed or overrode:* I changed the chunk size from 500 to 1,000 after testing and adjusted metadata to not be a random uuid() and be a better name based on the source for later debugging. I also edited the prompt to additionally account for reddit comments, which are typically short. I edited the prompt to account to differentiate, but also unite the metadata titles of the reddit posts and individual comments. 

**Instance 2**

- *What I gave the AI:* I asked AI to help connect my functions from retriever.py to app.py (the Gradle UI).
- *What it produced:* AI wrote the connection between retriever.py functions and the LLM hosted on the Groq client. Afterward, the results after querying Groq and other relevant data was inputted to the Gradle UI from the project spec.
- *What I changed or overrode:* I changed the way sources are generated in the code to better attribute the individual resources by creating a set in retriever.py, as initally the code provided the whole query instead of individual sources. I also made changes to the prompt to help ensure relevant data from the knowledge base is used. Additionally, I made some changes to the Gradle UI to better display information for the video demo. 
