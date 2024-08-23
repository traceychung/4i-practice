# 4insite Backend Take-home Assignment
_Employees and Assets to meet our client's Scope of Work_

## Description
At 4insite, our software helps manage and empower a workforce of thousands around the world.

To be a successful team, we need to seamlessly add new employees into our system.

We also need to make critical assets available to our team, like vacuums, lifts, and floor scrubbers.

## Requirements
Your task is to use this simple frontend as a jumping-off point for the creation of a Django and Postgres backend to handle these feature.

Picture this code as the first draft of the "create" portion of the UI, built to `POST` new items to the backend. The junior dev working on this will eventually be building out tables to display all of each kind, with buttons per row that will enable updating or deleting items one at a time.

### MVP
To pass this examination, meet these goals with clean, well written code and supporting evidence (see [Submission](#submission) below).
- Python/Django + PostgreSQL backend, built from scratch
- Stick to the core Python and Django packages
  - if you want to add extra requirements, please document them and your reason for using them
- API to recieve all CRUD operations for two models: Employee and Asset
  - create single new items of a type
  - read all of a type, or one by `id`
  - update or delete one by `id`
  - response with appropriate data and HTTP status code for successful operations
  - error handling with correct HTTP status code for malformed requests
  - no auth required
- Models to store all properties of these two different kinds of objects
  - must use appropriate data types per property
  - **all properties** in current frontend code are required, **except** for the `input:checkbox` props
  - stretch items do not need to be accounted for unless they are fully implemented
- No frontend updates are necessary, focus on crafting your backend code
- A short `README` for your teammates to review.
  - this is a closed-source project and your team knows all the `env` reqs
  - just the facts, please

---
**Stretch goals**

Think of these as the next sprint. Not due today, or even required at all, these are upcoming enhancements that the Product team has outlined.
- Assets can be marked as functional or non-functional, with a brief description of damage if non-functional
- Employees can have a list of specific Assets they are approved to use
- Employees can have a list of certifications they hold by "Asset name"
- An Asset that requires certification cannot be assigned to an Employee who lacks that certification
- Employees and Assets can be bulk deleted

**Super stretch**

Really, what are you trying to prove? Have fun with this if you want, but don't let this cut into your personal life…
- The junior dev building the frontend is out sick — help them build the UI tables to display all Employees and Assets
- Add update and delete functionality per row in those tables — what does that look like, and how to handle bulk actions?
- Connect this enhanced, functional frontend to your backend
- Deploy your application to Heroku, Render, Vercel, or whatever platform you prefer
---

### Submission
Reach the **MVP** goals and submit a link to your public repository on GitHub, Bitbucket, or GitLab.
Additionally, submit screen recordings or screenshots of your backend API working in **Postman, Insomnia,** or your prefered API platform.
This evidence should include all forms of relevant CRUD operations functioning, including examples of error responses. If you achieve any of the "Stretch" goals, try to demonstrate those as well.

For **video** evidence, we don't need any fancy edits, and narration is optional. Just run the requests in Postman in a logical order and show the responses. Try to keep it under 5 minutes — the shorter the better, as long as it's legible.

Embed all of these screenshots or recordings into your `README`. Remember, YouTube is a great, free way to host and embed videos. Email submissions of evidence are also acceptable — send those to the inbox of your contact at 4insite.

**Good luck,** you got this.