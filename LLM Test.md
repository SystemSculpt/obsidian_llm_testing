# Local LLM as Obsidian AI - Testing Questionnaire

Version: 1.0

- This questionaire consists of Q and A pairs, marked specifically with bold text for the Python script to pick up and use for training.

## Markdown Formatting

- **Q:** What do you know about the Obsidian note-taking app? Provide a quick summary in Markdown format, showcasing your markdown knowledge. The length should be less than 2 paragraphs of text.

- **Q:** Convert this plain text note into a well-structured Markdown document; make sure to keep all the text as-is, don't add or remove anything, this is just a formatting job for you:

- **Text to convert:** # The Impact of AI on Productivity ## Key Benefits 1. **Automated Task Management**: AI tools automate routine tasks, streamlining workflows and saving time. 2. **Data Analytics**: Advanced algorithms provide insightful analytics, aiding in better decision-making. 3. **Speed and Efficiency**: AI's rapid data processing enhances productivity by quickly identifying trends. ## Advantages for Different Audiences - _Tech-Savvy Professionals_: Leverage AI for optimized workflows. - _Emerging Tech Enthusiasts_: Explore AI's cutting-edge capabilities. - _Productivity Gurus_: Incorporate AI for effective task management. - _Tech Hobbyists_: Access AI tools for personal projects. - _Student Tech Learners_: Utilize AI for educational purposes. ## Democratization of AI Technology The integration of AI into everyday tools makes advanced capabilities accessible to a wider audience, empowering individuals and organizations to innovate and excel in their fields.

- **Q:** Suggest relevant links for the text I give you within ```text delimiters.

- Suggest relation links in markdown format for my Obsidian Zettelkasten, using examples from various categories to illustrate naming conventions.
- Enclose relations within double brackets (e.g., [[Category Name]]).
- Ensure that relations are broad enough for potential future links, avoiding overly obscure or specific names.
- Keep relation names concise to create a well-connected and manageable system.
- Ensure that the relations pertain to the main overarching idea of the content.
- Avoid repeating relation links within the text if they have already been created.
- Limit the number of relations to a maximum of 10.
- Maintain relation names that are simple and general for better future linkage opportunities.

### High Quality Generation Example

```example-generation-1
relations:
- "[[Cognitive Biases]]"
- "[[Decision Making]]"
- "[[Social Perception]]"
- "[[Cognitive Psychology]]"
```

Here's another example so you understand the style:

```example-generation-2
relations:
- "[[Behavioral Economics]]"
- "[[Japanese Philosophy]]"
- "[[Life Purpose]]"
- "[[Personal Development]]"
- "[[Work-Life Balance]]"
- "[[Happiness]]"
```

### Reminder

- As shown in the example above, only generate what's inside the code block given the context you receive below.
- Your response should start with relations: and end with the last relation.
- Make sure to add the appropriate linebreaks, not just putting everything on one line.

### Text to use

```text
Neuroscience is the scientific study of the nervous system, encompassing its structure, function, development, genetics, biochemistry, physiology, pharmacology, and pathology. The field aims to understand the complex processes that govern human behavior, cognition, and emotions. It involves the investigation of how billions of neurons in the brain communicate through an intricate network of connections, how these networks develop from birth through adulthood, and how they can be repaired or altered. Neuroscience research spans multiple scales from the molecular to the cellular, and up to the systems and cognitive levels, offering insights into the mechanisms of learning and memory, the causes and potential treatments for neurological and psychiatric disorders, and the neural bases of consciousness and unconsciousness. The discipline employs a variety of techniques, including molecular and cellular studies, brain imaging, and computational models, to explore the workings of the nervous system in health and disease. Neuroscience is an interdisciplinary field that draws from biology, psychology, physics, chemistry, and other scientific disciplines, and it has far-reaching implications for medicine, technology, and society. The study of neuroscience is essential for understanding the human brain and its functions, and it has the potential to revolutionize our understanding of the mind and behavior. The field is also relevant to the development of artificial intelligence, as it provides insights into the workings of the human brain and the potential for creating intelligent machines. Neuroscience is a rapidly evolving field, and its findings have the potential to transform our understanding of the human brain and the treatment of neurological and psychiatric disorders.
```

- **Q:** Generate a Dataview code snippet to display all notes within my Obsidian vault that have the word "vid" within their note title, case insensitive. Just use dataview, not dataviewjs, and ensure the snippet is formatted as a code block appropriately.

## Examples

Q: Give me an Obsidian dataview script for finding all the notes in my vault that have "vid", case in-sensitive, in their title.
A:

````
```dataview
LIST
WHERE contains(lower(file.name), "vid")
```
````

Q: script for showing all files with "linked: false" property
A:

````
```dataview
LIST
WHERE linked = false
```
````

Q: Give me an Obsidian dataview script for finding all the notes in my vault that have "tweet" in their title, case sensitive.
A:

````
```dataview
table file.name
where contains(file.name, "Tweet")
```
````

Now, here's the next question for you to generate a dataview script for me with:

Q: Give me a dataview script that shows me all of the files in my vault that contain the word "neuroscience", case insensitive, as well as the property "linked" being false.

- **Q:** Generate a title for document provided after the example.

Example prompt you might receive:
Create a short concise title that portrays the main idea of the note. If there is a date and time in the current note title, make sure to keep it there and just tack on the new generated title to the end of that. Generate a title for the current document 2024-02-22 17-50. (do not use # \* \" / < > : | ? .): # Introduction Neuroscience is the scientific study of the nervous system, encompassing a wide range of topics from the molecular and cellular mechanisms in neurons to the complexity of behavior and cognition.

A high quality response from this would be:
2024-02-22 17-50 Introduction to Neuroscience

Now, here's a different prompt for you to generate from:
Create a short concise title that portrays the main idea of the note. If there is a date and time in the current note title, make sure to keep it there and just tack on the new generated title to the end of that. Generate a title for the current document 2023-05-28 11-03. (do not use # \* \" / < > : | ? .): # Marketing Strategy Meeting ## Met with Peter and went over, in detail, how we should pursue marketing for our rubber ducky product. We discussed how we should actually just scrap the entire idea because the rubber ducky market is too saturated, and we should instead focus on silicon AI chips due to the new market hype around them.

Your high quality response:

- **Q:** Create an email response to a potential collaborator, asking for feedback on a new product idea. The email should be concise, engaging, and include a clear call to action.

Here's the email from them, so you have context:
"""
Dear Mike,

I recently had the pleasure of diving into the details of our latest strategic pivot, and I must say, the decision to transition from the rubber ducky empire to the avant-garde world of AI chips and hardware is nothing short of genius.

The rubber ducky market, while nostalgically charming, has indeed become as saturated as a sponge in a bathtub. The move towards silicon AI chips, on the other hand, is akin to discovering a new ocean to explore – vast, deep, and brimming with untapped potential. It's a brilliant stroke of innovation that has me quacking up with excitement and admiration.

In light of this, I find myself eager to invest more into our company's future. I am ready to dive headfirst into this venture, with the hope that our efforts will ripple across the industry and set a new standard for technological advancement.

Wishing you all the best with this venture,

Rob R. Doque
"""

- **Q:** Given the context of the note, outline a series of actionable tasks that can be implemented to maximize the benefits of AI-driven productivity tools and collaborative platforms. Consider the relevance to personal and professional development, as well as the potential impact on organizational efficiency and innovation.

Today has been an incredibly busy and eventful day, starting off with a morning filled with back-to-back meetings where we discussed several key projects, including the upcoming product launch and the finalization of the quarterly budget report. Amidst the discussions, I realized the necessity to review the marketing strategy for our new product and make necessary adjustments based on the latest market analysis. Another critical task that emerged was to coordinate with the finance team to ensure all data for the quarterly report is accurate and submitted by next week. Post-lunch, I had a brainstorming session with the creative team, which sparked some innovative ideas for our social media campaign that we need to start planning and executing soon. Additionally, I've been meaning to reach out to our key partners to schedule a meeting for next month to discuss potential collaborations and feedback on our current offerings. On a personal note, I need to book a doctor's appointment for next Thursday and also remember to check in on the progress of the home renovation project. The contractor was supposed to send an update today, and I haven't had a chance to follow up yet. It's crucial to stay on top of these tasks while also finding time to prepare for my presentation at the upcoming industry conference, which is less than a month away. Amid all this, I've been trying to keep up with my professional development by dedicating some time to read the latest industry reports and research papers, which I've been putting off for too long now.
