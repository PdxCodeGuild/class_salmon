
# Capstone Proposal

The Capstone is a web application that touches on every major technology we covered: Python, HTML, CSS, JavaScript, and Django. Below are the criteria for your proposal. It's difficult to be certain how long each feature will take to develop. Therefore you should plan out multiple 'milestones' for your project. That way, if you reach milestone 2 but not 3, you still have something worthwhile to present and be proud of. It also gives you the opportunity to plan out what you'd like to work on after the class is finished. I can help you sculpt out an idea, and I'll tell you very plainly whether a goal is attainable given our time constraints. I highly recommend doing some sketches of pages. This document is for you as much as it is for me. By planning thoroughly and precisely, the implementation will be much easier. Please do not change your idea after we start working on our capstones, it wastes your time and your end result won't be as good. Your proposal is due by the time we start our capstones (3-4 weeks before the end of the course).

- Your proposal must set specific and attainable goals
- Your proposal must cover all major topics we've covered
- Your proposal must include the sections below
- Your proposal must be in a markdown `.md` file [more info](https://help.github.com/articles/basic-writing-and-formatting-syntax/)

## Name
Give your project a cool name. If you can't think of one, Matthew recommends going to [translate.google.com](https://translate.google.com/), picking a random language, and typing in some words relating to your project. Or there's [behindthename.com](https://www.behindthename.com/).

## Project Overview
What are the major features of your web application? What problem is it attempting to solve? What libraries or frameworks will you use?

## Features
Walk through the application from the user's perspective. Think about features in terms of **user stories**.

### User stories
User stories are high-level descriptions of features for your application from a user's standpoint.

User stories follow this template:
"As a _____ (user), I want _____ (feature) because _____ (reason)."

From these user stories, you can break down *features* into actionable *tasks*. Your user stories will make up your **product backlog**.

#### Examples
"As a **teacher**, I want **a dashboard of students' last month/week/day's scores** because **I want to be able to track my students' progress**."

**Tasks:**
- Store students' scores in model/db table 
- Filter scores by dates
- Display scores in charts

"As a **moderator**, I want **to delete flagged posts** because **it's my job to keep the forums safe**."

**Tasks:**
- Allow posts to be flagged
- Give mods permissions to delete flagged posts

#### Questions to ask yourself about functionalities
What will the user see on each page? What can they input and click and see? How will their actions correspond to events on the back-end?

## Data Model

What data will you need to store as part of your application? These should be specific nouns, collections of information that serve a collective purpose. Examples might be 'User', 'Book', 'ImageSet'. These are *schemas* for your data models (database tables).

## Schedule

Here you'll want to come up with some (very rough) estimates of the timeframe for each section, as well as milestones. State specifically which steps you'll take in the implementation. This section should also include work you're planning to do after the capstone is finished.

### Agiles/Scrum Methodology and Workflow
We're going to be following a modified [Agile/Scrum](https://linchpinseo.com/the-agile-method/) workflow. Most software development teams follow Agile/Scrum methodology, so we're going to as well. The difference is that rather than working on a team, you'll be working as a team of one with me as your *Scrum Master*. 

#### Iterative Development
Agile development is **iterative development**. The goal is to set short sprints (1-4 week intervals), where at the end of each sprint you have a **minimal viable product**, or **MVP**. This means you have a functioning, *end-to-end* application at the end of each iteration.

So, rather than spend a huge amount of time building up the infrastructure for your application (i.e. setting up the wheels and frame for a car) and not have a complete, shippable product until the very end of the process, you build MVPs each sprint (i.e. start off with a scooter, then bike, then motorcycle, until eventually you have a car). 

![MVP diagram](./Making-sense-of-MVP-.jpg)

This way, you can fall back to a shippable, completed product at any phase. Also, if your requirements change (as they often do) midway through development, your product can much more easily adapt to changing needs since you haven't locked yourself in with an extensive infrastructure.

#### Setting up MVP
You want each of your milestones to result in a minimal viable product. For each milestone, take a few features off of your **product backlog** (the set of user stories you have defined). 

Generally, you want to rank your product backlog in terms of:

- Essential features
- Really-great-to-haves
- Nice-to-haves

Structure your milestones first to cover essential features. Then, think about adding the great-to-haves and nice-to-haves in terms of how much they'd improve your application and how difficult it would be to implement them.

Each MVP must be a completed *end-to-end product*. What this means is you need a functioning back-end connected to a functioning front-end. Get all your models, views/templates, and controller/views connected.

These MVPs are what you should strive to work on. Build up your application, feature by feature, until you're at a working state. Then commit and push your working MVP before you start on the next version. Rinse and repeat until you're ready to ship!
