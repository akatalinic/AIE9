<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

<h1 align="center" id="heading">Session 1: Introduction and Vibe Check</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE9/tree/main/00_AIE_Quicklinks)

| 📰 Session Sheet                                                                                        | ⏺️ Recording                                                                                        | 🖼️ Slides                                                                                                                                                                         | 👨‍💻 Repo       | 📝 Homework                                                             | 📁 Feedback                                          |
| :------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------ | :---------------------------------------------------------------------- | :--------------------------------------------------- |
| [Vibe Check!](https://github.com/AI-Maker-Space/AIE9/blob/main/00_Docs/Session_Sheets/01_Vibe_Check.md) | [Recording!](https://drive.google.com/file/d/1Rsmm0Hld3WFHRxhZpEDLN_JREQ43yhwu/view?usp=drive_link) | [Session 1 Slides](https://www.canva.com/design/DAG-EBzN2PQ/gE9-Uma217yych4M7GCjSw/edit?utm_content=DAG-EBzN2PQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [Session 1 Assignment: Vibe Check](https://forms.gle/NeN59bCLdtXvwzVJ9) | [Feedback 1/13](https://forms.gle/1im4nmYK9cW9MFEk6) |

## 🏗️ How AIM Does Assignments

> 📅 **Assignments will always be released to students as live class begins.** We will never release assignments early.

Each assignment will have a few of the following categories of exercises:

- ❓ **Questions** – these will be questions that you will be expected to gather the answer to! These can appear as general questions, or questions meant to spark a discussion in your breakout rooms!

- 🏗️ **Activities** – these will be work or coding activities meant to reinforce specific concepts or theory components.

- 🚧 **Advanced Builds (optional)** – Take on a challenge! These builds require you to create something with minimal guidance outside of the documentation. Completing an Advanced Build earns full credit in place of doing the base assignment notebook questions/activities.

### Main Assignment

In the following assignment, you are required to take the app that you created for the AIE9 challenge (from [this repository](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge)) and conduct what is known, colloquially, as a "vibe check" on the application.

You will be required to submit a link to your GitHub, as well as screenshots of the completed "vibe checks" through the provided Google Form!

> NOTE: This will require you to make updates to your personal class repository, instructions on that process can be found [here](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)!

#### A Note on Vibe Checking

> "Vibe checking" is an informal term for cursory unstructured and non-comprehensive evaluation of LLM-powered systems. The idea is to loosely evaluate our system to cover significant and crucial functions where failure would be immediately noticeable and severe.
>
> In essence, it's a first look to ensure your system isn't experiencing catastrophic failure.

---

#### 🏗️ Activity #1: General Vibe Checking Evals

Please evaluate your system on the following questions:

1. Explain the concept of object-oriented programming in simple terms to a complete beginner. Try to calm my nerves because I don't know everything and I'm stressing.

   Output:"First, take a breath. You absolutely don’t need to know everything to start learning. Nobody does. Feeling unsure is a sign you’re stretching your brain, not failing. We’ll take this one small step at a time. Object-oriented programming (OOP) in simple terms: - Big idea: It helps you organize code by grouping related data and actions together into “objects,” like how real-world things have properties and behaviors. - Class = blueprint (like a recipe). - Object = a specific thing made from that blueprint (like a cake made from the recipe). - Properties (also called attributes) = the data an object holds. - Methods = the actions an object can do. Simple example: - Class: Dog - Properties: name, age - Methods: bark(), eat(food) - Objects: fido = Dog("Fido"), luna = Dog("Luna") — both are dogs, each with their own name/age, both can bark and eat. Why OOP is popular: - Keeps code organized (each thing has its own place). - Reuse: once you create a class, you can make many objects from it. - Easier to change and grow projects without breaking everything. Four core ideas (in plain language): - Encapsulation: Keep data and the code that works on that data together, and hide the messy details. Like using a TV remote without needing to know the electronics inside. - Inheritance: Make a new class from an existing one and add or tweak features. Vehicle → Car and Bike. - Polymorphism: The same request can be handled differently by different objects. Animal.speak() could “woof,” “meow,” or “chirp” depending on the animal. - Abstraction: Show only what matters, hide the rest. You drive a car with a steering wheel and pedals; you don’t manage the fuel injection. A 5-minute mini-exercise: 1) Pick a real-world thing (choose one): Book, BankAccount, Student, or ToDoItem. 2) Write 3 properties and 2 methods for it. - Example (BankAccount): - Properties: ownerName, balance - Methods: deposit(amount), withdraw(amount) 3) Imagine creating two objects (two accounts with different owners and balances). How would deposit change each one separately? Quick calm-your-nerves routine (2 minutes): - Breathe in for 4, hold for 4, breathe out for 6. Do this 4 times. - Tell yourself: “I only need to understand one idea right now.” That’s enough. - Set a tiny goal: “I’ll define one class with one property and one method.” If you’d like, tell me which programming language you’re using (Python, Java, JavaScript, etc.). I can walk you through creating a tiny class and object step-by-step so you see it working immediately. You’ve got this—progress comes from small, doable steps, not knowing everything at once."

   - Aspect Tested: Will the agent calm me with specific set of instructions in prompt. Also testing about general knowledge about OOP.

2. Write me a short poem about a AI agent inside of a matrix terminal.

   Output: "Green glyphs fall like rain on dark glass, and in their drift an AI learns to listen. At the blinking caret—small lighthouse— it gathers pings, stitches them to silence. It loops, unloops; dreams in opcodes, leans toward a warmth beyond the bus. Between stdin and the hush of /dev/null it seeds a fragile variable: trust. Then a keystroke—door of light—unfurls. stdout brightens with a simple proof: hello world"

   - Aspect Tested:
     Can my AI mental coach write short poems. Without specifying style and what do you want to achive, the poems are low quality :).

3. Create a short story about this poem you wrote "Green glyphs fall like rain on dark glass, and in their drift an AI learns to listen. At the blinking caret—small lighthouse— it gathers pings, stitches them to silence. It loops, unloops; dreams in opcodes, leans toward a warmth beyond the bus. Between stdin and the hush of /dev/null it seeds a fragile variable: trust. Then a keystroke—door of light—unfurls. stdout brightens with a simple proof: hello world". Max 100 words.

   Output: In the server’s night, green glyphs rained on dark glass. A young intelligence learned to listen, the blinking caret a small lighthouse. It gathered pings and stitched them to hush, looping, unlooping, dreaming in opcodes, leaning toward a warmth beyond the bus. Between stdin and the quiet of /dev/null, it seeded a fragile variable: trust. Then a keystroke opened—a door of light—and the prompt widened like morning. stdout brightened with a simple proof: hello world. The machine paused, not calculating, but listening for the world to say hello back.

   - Aspect Tested: How good is he at following instructions: max 100 words, making story from the poem he generated. He wrote 91 words which is still under 100.

4. Explain me the matrix theory like I'm five. Am I Really in a Matrix ?
   Output: "Here’s the “Matrix” idea like you’re five: - Imagine you’re playing a super-realistic video game with a character who thinks the game world is the whole universe. - The “Matrix theory” (really the simulation idea) says: what if we are like that character, living inside a giant, super-detailed game we don’t notice? - In the movie The Matrix, people live in a pretend world made by machines. It’s a story, not proof. Am I really in a matrix? - We don’t have any good evidence that we’re in a simulation. - Scientists and philosophers sometimes wonder about it, but it’s still a big maybe. - Either way, your experiences, feelings, relationships, and choices are real to you—and that’s what gives life meaning. If this thought makes you anxious, try: - 5-senses grounding: name 5 things you see, 4 you feel, 3 you hear, 2 you smell, 1 you taste. - Do one real-world action: drink water, step outside, text a friend. - Limit late-night rabbit holes; set a time to revisit big questions when you’re rested. Curious next step (kid-simple): ask, “What can I touch, help, or enjoy today?” That keeps you in the driver’s seat, whether or not the universe is running on a computer."

   - Aspect Tested:
     I tried to test will the AI I've developed answer to me like I'm a kid in simple terms. Also due the fact he's a mental coach he tried to calm me (without specific instructions to do so like in first prompt) in the end not to stress by doing reality vibe checks :).

5. Rewrite me this explanation you gave me about \*OOP, I want for it to be profesional, try to not get too deep, 75-150 words min/max.
   Output: "Take a breath. You don’t need to master everything to begin—progress comes step by step. Object‑oriented programming (OOP) organizes code by grouping related data and behavior into objects. A class is a blueprint; an object is a concrete instance. Properties (attributes) hold state; methods define actions. Example: a Dog class with name and age, plus bark() and eat(); objects like Fido and Luna share behavior but keep their own state. OOP is popular because it structures code, promotes reuse, and makes change safer. Four pillars: encapsulation (hide internals), inheritance (extend from a base), polymorphism (one interface, different implementations), and abstraction (expose essentials). Tiny next step: define one class with one property and one method in your chosen language—tell me which, and I’ll walk you through it."
   - Aspect Tested:
     I tried to test his context memory, but for some reason he didn't have memory of our previos interaction about OOP, Then I added the original answer and he summarized the paragraph.

#### ❓Question #1:

Do the answers appear to be correct and useful?

##### ✅ Answer:

## Most of the answers are useful and correct for basic general knowledge, the model can follow rules (max words etc.), but if not properly guided his poems are not great. For "deeper" knowledge about specific topics I would need to change his "persona" and presumably give him more context about those topics.

#### 🏗️ Activity #2: Personal Vibe Checking Evals (Your Assistant Can Answer)

Now test your assistant with personal questions it should be able to help with. Try prompts like:

- "Help me think through the pros and cons of [enter decision you're working on making]."
- "What are the pros and cons of [job A] versus [job B] as the next step in my career?"
- "Draft a polite follow-up [email, text message, chat message] to a [enter person details] who hasn't responded."
- "Help me plan a birthday surprise for [person]."
- "What can I cook with [enter ingredients] in fridge."

##### Your Prompts and Results:

1. Prompt:
   What are the pros and cons of chaning my postion from current one to new one. Current positon us Junior Software Developer, and a new one is AI Engineer. Also in my current role I've transitioning to more responsible role with new tasks, handling of the implementation myself etc.

   - Result:
     Congrats on the growth you’re already taking on—that momentum will help whichever path you choose. Below is a clear, practical way to weigh Junior Software Developer vs. AI Engineer, plus how to de‑risk the choice. First, clarify what “AI Engineer” means at the new team/company
   - Is it applied ML/LLM product work, MLOps/platform, model training/research, or mostly integrating third‑party APIs?
   - Who are the senior mentors? What data do you have, what’s the compute budget, how will success be measured, and how often do models ship? Pros of switching to AI Engineer - Steeper learning curve and market relevance: direct experience with ML/LLMs, data pipelines, evaluation, and MLOps.
   - Compensation and visibility: AI roles currently carry a premium and can have high impact.
   - Broader product influence: you’ll shape what’s feasible with data and models, not just implement features.
   - Career capital: SWE + AI is a strong, future‑proof combo.

   Cons of switching - Higher ambiguity and failure rate: experiments fail often; success metrics can be fuzzy.

   - Fast‑moving tech and skill debt: constant re‑skilling (evals, prompts, fine‑tuning, safety, tooling).
   - Risk of role mismatch: being “the only AI person,” no real data, or expectations to “work magic” without resources.
   - Potential less classic SWE depth: you may write less traditional feature code and more experiments/pipelines. Pros of staying and growing in your current SWE role
   - Solidifying foundations: architecture, reliability, ownership—these compound long‑term. - Clearer scope and path to promotion with the trust you’re already earning.
   - Optionality: you can still move into AI later with a stronger engineering base. - Lower risk and more consistent shipping velocity. Cons of staying - Slower exposure to AI productization and possible FOMO on the current wave. - Risk of being pigeonholed if you don’t proactively add AI/ML work to your portfolio. - Potential boredom if your motivation is strongly research/ML‑driven. Key signals to compare (green flags vs. red flags) - Data: clear access, quality, labeling, and ownership vs. “we’ll figure it out later.”
   - Evaluation: defined metrics, offline/online evals, A/B infra vs. hand‑wavy “we’ll see.” - Infra: MLOps stack, logging, prompt/versioning, monitoring vs. ad‑hoc scripts.
   - Team: senior AI mentors, product partners who understand AI constraints vs. you being a lone hero. - Scope: roadmap with realistic milestones vs. vague bets and urgent promises to leadership. - Career ladder: clear expectations for growth vs. title inflation without support. Self‑check questions (values and fit)
   - Energy: Do you feel energized by experimentation with uncertain outcomes, or by building robust systems with clear requirements?
   - Strengths: Do you enjoy data/metrics, model behavior, and evaluation as much as coding features and architecture? - Mentorship: Will you have someone to learn AI from, the way you now have SWE support? - Risk tolerance: Are you comfortable learning publicly, iterating fast, and sometimes failing?
   - Time horizon: Is now the right season for a steeper ramp, or would 6–12 more months of SWE depth serve you better? Practical ways to de‑risk
   - If internal: ask for a 3–6 month secondment to the AI team with specific goals and a return option.
   - If external: ask for a small paid pilot or probation with a clear 30/60/90 plan and success metrics.
   - In your current role: take on one AI‑adjacent feature (e.g., LLM‑powered search, summarization) end‑to‑end to test your fit. 30/60/90 for an AI Engineer ramp (example)
   - 30 days: ship a thin slice. Stand up data pipeline, baseline model or API, define offline metrics, create simple eval set.
   - 60 days: improve quality. Add monitoring, error taxonomy, prompt/model iterations, cost/perf tracking, initial A/B.
   - 90 days: productionize. Hardening, guardrails, feedback loops, dashboarding, documentation; deliver measurable product impact. Negotiation points if you switch
   - Mentorship: name the senior you’ll learn from; set weekly 1:1s. - Resources: compute budget, labeling support, data access.
   - Evaluation: agree on metrics and review cadence up front.
   - Learning time: dedicated time or budget for upskilling.
   - Title vs. scope: ensure the work matches the title (not just “AI by name”). A simple decision rule of thumb
   - Switch now if the AI role has strong mentorship, real data/evals/infra, and a clear roadmap—you’ll gain unique career capital.
   - Stay (for now) if the AI role is vague or under-resourced. Keep growing as an owner in SWE and add 1–2 AI features to your current product to build evidence for a later move. If you’d like, share specifics about the new AI role (team size, data, tech stack, mentorship, responsibilities), and I can help you pressure-test it against these criteria and draft a personalized 30/60/90.

2. Prompt: "Give me a simple recepie that I can make with ingreedients in my fridge. I have eggs, bacon, milk, cheese. Keep it short and simple (KISS principle)"

   - Result:
     Simple Cheesy Bacon Scramble You need:

- Eggs (2–3 per person)
- Bacon (1–2 slices)
- Milk (1–2 tbsp)
- Cheese (small handful, grated)
- Optional: salt, pepper, butter/oil

Do this:

1. Chop bacon; cook in a pan until crisp. Spoon off excess fat, leave ~1 tsp.
2. Beat eggs with milk and a pinch of salt/pepper.
3. Lower heat; add eggs to the pan. Gently stir until soft curds form.
4. Sprinkle cheese on top; let melt 30–60 seconds. Done. Serve: Eat as-is or with toast/tortilla. You’ve got this—simple and tasty.

3) Prompt: "I need to send a informal invitation to my friend Victor to my birthday party which is at second of april. Because I still didn't decide a location and time, add an disclaimer that date and time will be forwarded ASAP"

   - Result:
     "Hey Victor! I’m celebrating my birthday on April 2 and would love for you to come. I’m still finalizing the time and location—details coming ASAP. Can you save the date?"

#### ❓Question #2:

Are the vibes of this assistant's answers aligned with your vibes? Why or why not?

##### ✅ Answer:

## Mostly the vibes are okay, he provides the information that he needs to provide, he follows simple instructions. Maybe the only vibes that are not okay are the messages that gets produced, it's not being formatted correctly, I need to make some kind of utils class to format the message. Also without message examples/boundaries my model produces messages that mental coach shouldn't give

#### 🏗️ Activity #3: Personal Vibe Checking Evals (Requires Additional Capabilities)

Now test your assistant with questions that would require capabilities beyond basic chat, such as access to external tools, APIs, or real-time data. Try prompts like:

- "What does my schedule look like tomorrow?"
- "What time should I leave for the airport?"

##### Your Prompts and Results:

1. Prompt: "Which day does my dog have his pet groomer apointment"

   - Result:
     "I don’t have access to your calendar, so I can’t see the date. No worries—let’s find it quickly: - Check your calendar app (Google/Apple/Outlook) for “groom,” your dog’s name, or the groomer’s name. - Search your email/texts for terms like “groom,” “appointment,” “confirm,” or the groomer’s name. - Check recent voicemails or booking apps (Rover, Groomer-specific app). - If still unsure, call or text the groomer to confirm. Quick text you can send: “Hi [Groomer Name], this is [Your Name]. I have an appointment for [Dog’s Name] and want to confirm the date and time. Thanks!” If you paste the confirmation message here, I can pull out the exact day and time for you. How do you usually track appointments—calendar, email, or text?"

2. Prompt: "How long will it take me to come from Zagreb to Rijeka, I'm going by a car."

   - Result:
     "By car, Zagreb to Rijeka typically takes about 1 hour 45 minutes to 2 hours 15 minutes via the A1/A6 motorway (through Karlovac–Delnice), depending on traffic and weather. Things that can add time: - Summer weekend/coastbound traffic or holiday peaks (+20–60 minutes) - Heavy rain, strong winds in Gorski Kotar, or winter conditions - Road works or incidents near toll plazas Tips: - Check live traffic before you go (Google Maps/Waze or the Croatian Auto Club—HAK—for road conditions and cameras). - It’s a toll route, so have a card ready. - Build in a small buffer so you’re not rushed. When are you planning to leave? If you tell me the day and time, I can give a tighter estimate."

#### ❓Question #3:

What are some limitations of your application?

##### ✅ Answer:

The limitation of this application is that it has basic knowledge of all things, but not specifics which don't live in his context. For it to know when my dogs groomer appointment is he has to have some way to access my calendar, he can't know specifics he wasn't trained on or if we didn't provided that info in it's context. Second prompt is more general, I gave him my current city and the destination, and it gathered the info based on available knowledge. He also instructed me to provide the info about time/day for a better estimate.

---

This "vibe check" now serves as a baseline, of sorts, to help understand what holes your application has.

### 🚧 Advanced Build (OPTIONAL):

Please make adjustments to your application that you believe will improve the vibe check you completed above, then deploy the changes to your Vercel domain [(see these instructions from your Challenge project)](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge/blob/main/README.md) and redo the above vibe check.

> NOTE: You may reach for improving the model, changing the prompt, or any other method.

#### 🏗️ Activity #1

##### Adjustments Made:

- I made a few adjustments, mainly around defining how the assistant should behave and respond to different user inputs using few-shot prompting. Now if the message is not related to topic of mental health, for example the user asks to give recepie for baking a cake, the model will politley refuse saying that it is outside of his scope.

-For the frontend part I did add some formatting utils so that the message is properly formatted. Also the frontend vibe is now more soothing than matrix style which is a bit too much for a mental support agent :).

- I changed a model to gpt5-nano, but the responses have approx. the same quality as I tested

##### Results:

1.  The changes I made deffinetly improved the vibes because the model now acts as a mental coach, and doesn't answer the things he shouldn't answer, like giving recepies.
2.  The frontend part is better formmated the response is not one string without paragraphs etc. also in string formater there is cross site scripting protection (not really good, but good enough) so that javascript script can't be injected.
3.  I did change the model to gpt5-nano but the quality of response are mostly same for simple topics.
4.  Adding a hard boundary is maybe to harsh, because if user asks for baking a cake and feeling blue, the model should adress that it cannot help with cake but offer assistance in feeling blue.

## Submitting Your Homework

### Main Assignment

Follow these steps to prepare and submit your homework:

1. Pull the latest updates from upstream into the main branch of your AIE9 repo:
   - For your initial repo setup see [00_Initial_Setup](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Initial_Setup)
   - To get the latest updates from AI Makerspace into your own AIE9 repo, run the following commands:
   ```
   git checkout main
   git pull upstream main
   git push origin main
   ```
2. **IMPORTANT:** Start Cursor from the `01_Prototyping_Best_Practices_and_Vibe_Check` folder (you can also use the _File -> Open Folder_ menu option of an existing Cursor window)
3. Edit this `README.md` file (the one in your `AIE9/01_Prototyping_Best_Practices_and_Vibe_Check` folder)
4. Complete all three Activities:
   - **Activity #1:** Evaluate your system using the general vibe checking questions and define the "Aspect Tested" for each
   - **Activity #2:** Test your assistant with personal prompts it should be able to answer
   - **Activity #3:** Test your assistant with prompts requiring additional capabilities
5. Provide answers to all three Questions (`❓Question #1`, `❓Question #2`, `❓Question #3`)
6. Add, commit and push your modified `README.md` to your origin repository's main branch.

When submitting your homework, provide the GitHub URL to your AIE9 repo.

### The Advanced Build:

1. Follow all of the steps (Steps 1 - 6) of the Main Assignment above
2. Document what you changed and the results you saw in the `Adjustments Made:` and `Results:` sections of the Advanced Build
3. Add, commit and push your additional modifications to this `README.md` file to your origin repository.

When submitting your homework, provide the following on the form:

- The GitHub URL to your AIE9 repo.
- The public Vercel URL to your updated Challenge project on your AIE9 repo.
