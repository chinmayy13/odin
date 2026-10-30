# ⚡Odin Reviewer Handbook

LAST UPDATED: Oct 28, 2026

## Confidentiality

**All Odin project information and materials are confidential.** This includes the project name, client identity, nature of the work and your involvement, along with this handbook, task materials, recordings, screenshots and review feedback.

Use project materials only for authorized project work. Share them only through approved project channels with people authorized to access them. Do not post, publish, sell or share them externally, including in videos, on social media or websites, or in external group chats. Do not confirm or deny guesses about the project or client, even if someone appears to know the details already.

# How the Odin Reviewer Handbook is structured

Use the tabs below to find each part of the workflow.

| **Section** | **Goal** |
|---|---|
| **<u>01. Start Here</u>** | This page introduces the project and role. |
| **<u>02. Changelog</u>** | Updates to this guidance. Check regularly! |
| **<u>03. Onboarding</u>** | Details on the steps to get onboarded as a reviewer |
| **<u>04. Reviewer Expectations</u>** | General expectations, pay, and role tiers |
| **<u>05. Workflow</u>** | Workflow for how to conduct reviews |
| **<u>06. Reviewer Checklist</u>** | Detailed guidance for how to score each dimension in the review, and a quick reference decision making table |
| **<u>07. FAQ</u>** | Frequently Asked Questions |
| **<u>08. Examples</u>** | Examples of good vs bad tasks |
| **<u>09. Feedback Templates</u>** | Some templates you can use when providing feedback |

# What is Odin?

![](images/p002_1.png)

> *Text shown in the image:* The goal of Project Odin is to produce training data for a frontier AI model. Specifically, this data will capture realistic, professional macOS workflows to show how real users interact with applications, menus, and macOS system behaviors.

# Your Role

The review process is a **partnership** with the top goal being the quality of the task. Our goal as a team is to produce the highest quality tasks with the highest efficiency. These guidelines outline the review process with the mindset that this is a **collaboration between peers**.

Writers and reviewers are partners in the process. The writers work on creating a high quality task based on their expert knowledge in their corresponding field. The reviewers work alongside the writers as a second set of expert eyes to help validate and refine the task.

The reviewer's mission is to:

✅ **Validate** the accuracy and adherence to all project guidelines.

✅ **Elevate** the quality of the task by identifying areas for improvement.

✅ **Facilitate** a smooth and efficient workflow through clear, structured communication.

✅ **Demonstrate** a professional, respectful tone that keeps feedback collaborative and solutions-focused.

There are specific onboarding steps in Section 3, but please review this whole guide before you begin reviewing.

You can also read the [Writer Handbook](https://docs.google.com/document/d/1tOxjGqxhA6T49kXw9hrhwpEsk8ERaFOsB6gqZcrLAHg/edit?usp=sharing) for more details on how tasks are written.

# 🖊️ Changelog of Reviewer Guidelines

This list is updated whenever something in this guide changes. **Please review it regularly** to ensure you implement recent changes!

|   |   |
|---|---|
| **Date** | **Details of changes** |
| Oct 28, 2026 | 🟩 New format for Reviewer Handbook. Consolidated all reviewer documents into this single source of truth. |
| Oct 27, 2026 | 🟩 [October 27 quality alignment](https://docs.google.com/spreadsheets/d/17i84NYjpjP4FErjdSH2xrllHd4PhZnY5DosSvJzk-oc/edit#gid=0): intro length, silence duration and click pacing removed from reviewer scoring. Intro and silence remain in AutoQC but never block approval. Minor non-English content on screen is acceptable; narration must be fully in English.<br>🟩 Reviewers can write tasks when review queue is clear. Do not track time while writing. Pay is a flat rate $100 + $2/minute for each RFD task. |
| Oct 26, 2026 | 🟩 Poor window management can cause sendback; same-app dialogue box is still an exception<br>🟩 Bottom dock alone should not trigger a send-back as long as at least one UI element has been changed |
| Oct 25, 2026 | 🟩 New 3 band checklist (1=ideal, 2=tolerable, 3=fail). Send back with anything marked 3.<br>🟩 Historical intro timing guidance, superseded October 27: intro length is now advisory only and never blocks approval.<br>🟩 Missing epilogue not a sendback reason<br>🟩 If Metadata.rtf has an issue, fix rather than sendback<br>🟩 Updated Quick review eligibility, checklist, timing<br>🟩 Maximum of 4 reviews per task<br>🟩 Claim timing: finish reviews within about an hour; use Extend Review Claim if needed. Tasks held over 2 hours may be released.<br>🟩 Onboarding pay and hour limits for reviewers follow your individual invitation. |
| Oct 22, 2026 | 🟩 Reviewer guidelines FULLY UPDATED with new details - please read through the entire document and pay close attention to your role’s respective checklists |
| Oct 20, 2026 | 🟩 Reviewer and QC checklist are now aligned<br>🟩Reviewer Checklist: every item now states its fail point in option 4. \[Automated\] items are scored on the same 1–4 ranges as manual items.<br>🟩 Studio, Airtable, Mercor and Project Odin being mentioned (item 17) is now OK in the recording and no longer blocks approval.<br>🟩 Metadata.rtf (item 1): fails when it is under 70% similar to the TaskRecorder Goal or Studio.<br>🟩 Window overlap (item 2): 6–30 s = option 2; over 30 s with no clear effort to fix within time = option 4.<br>🟩 What / Where / Why (item 3): fails when under 70% of actions have at least 2 of the 3 Ws. An action is anything that changes the state of the document.<br>🟩 Eyes Closed (item 4): 4 or more ambiguous references is edge case. A 2+ minute stretch narrated mostly with "here" and "this" fails.<br>🟩 Historical intro-length scoring (former item 8), superseded October 27: removed from reviewer scoring; AutoQC findings are never blocking.<br>🟩 Metadata.rtf shown (item 9): up to 10 s is edge case; over 10 s fails.<br>🟩 Typing (item 10): fails over 25% (over 35% for Coding / Content & Writing).<br>🟩 Historical silence scoring (former item 11), superseded October 27: removed from reviewer scoring; AutoQC findings are never blocking.<br>🟩 Background noise (item 12): 30–40% of narration = option 2; option 3 = N/A; over 40% fails (option 4).<br>🟩 Profanity (item 18): minor on-screen profanity not typed by the writer = option 2 and does not block approval; profanity said or typed by the writer, or more than minor on-screen profanity, fails (option 4).<br>🟩 Domain expertise (item 23): fails when a non-expert could do more than 10% of the actions.<br>🟩 Pace (item 24): 10–15% of the video above 220 WPM is edge case; over 15% fails.<br>🟩Missing epilogues DO NOT FAIL tasks regardless of approval date |
| Oct 19, 2026 | 🟩 Clarified that CC0, public domain, copyright, royalty free issues only apply to information that ends up in the deliverable.zip. Browsing websites with logos doesn’t violate our terms.<br>🟩Clarified that while ideally project information is hidden (e.g., references to Mercor, Project Odin, Studio Instructions), they will be tolerated in small quantities and should not lead to task rejection on its own.<br>🟩 Historical announcement — epilogue-length disposition superseded. Epilogue narration requirements: All task ideas originally approved at or after Oct 19, 2026 6PM PT must include an epilogue narration (target: 3-4 mins; maximum: 4:00; longer epilogues may be sent back) which serves as a brief reflection of the work. See [here](https://docs.google.com/document/d/1tOxjGqxhA6T49kXw9hrhwpEsk8ERaFOsB6gqZcrLAHg/edit?tab=t.nvo0dh78tkt4) for more details Current reviewer rule: over 4:00 is band 2 (nonfailing) and does not require a send-back on its own.<br>🟩Reviewer acceptance is up to 54:59 total, including intro and epilogue. Writer recording guidance remains no more than 50:59; the higher acceptance limit is not a writer target. |
| Oct 17, 2026 | 🟩 Historical, superseded reviewer-writing arrangement: Clarified Insightful and pay for reviewers who write tasks (Getting Started). Promoted reviewers keep Insightful running and stay hourly while writing; directly hired reviewers do not run Insightful while writing. These historical terms are superseded. Under the October 27 arrangement, reviewers may write when no review work is available, with Insightful off; see [Pay & time](#onboarding-steps). |
| Oct 16, 2026 | App-policy update (effective 2026-10-16 18:08 PDT): Historical restriction entries below, including the blanket TextEdit ban, are [superseded by the canonical three-category app list. TextEdit may be](https://odin-mercor1.vercel.app/validated-apps) used for metadata.rtf; separate opening-Goal instructions remain unchanged. In-flight work is protected and now-allowed app rejections may be reconsidered subject to other quality checks. |
| Oct 14, 2026 | 🟩 Added the following apps to the restricted app list - all tasks submitted before 10/14 5PM PST should be approved if their only failure mode was a restricted app on this list:<br>1. anatomyapp<br>2. Autodesk FBX Review<br>3. Defold<br>4. drawBook<br>5. FL Studio / FruitLoops Studio<br>6. GameMaker<br>7. JASP<br>8. KiCad<br>9. LTspice<br>10. Milanote<br>11. MohrPlotter<br>12. OpenVSP<br>13. Penpot<br>14. qemu-system-aarch64<br>15. Sticky Notepad<br>16. Substance 3D Stager<br>17. TextExpander 18. VMD |
| Oct 14, 2026 | 🟩 Added “If the Reviewer raised the complexity issue in R1 and the writer didn’t fix it, then R2 can send back.”<br>🟩 Added DM templates |
| Oct 13, 2026 | 🟩 Added “The goal is to leave 1-2 sentences of feedback”<br>🟩 Added New Reviewer info: Run Insightful and Device Requirements |
| Oct 12, 2026 | 🟩 TextEdit is now fully restricted, including for filling out Metadata.rtf: the restricted app list entry “FOR METADATA.RTF ONLY - TextEdit.app” was changed to “TextEdit.app” (Odin Production Full Workflow world). |
| Oct 12, 2026 | 🟩 Full Facelift |
| Oct 11, 2026 | 🟩 Added the following apps to the restricted app list (Odin Production Full Workflow world):<br>1. Adobe Express<br>3. Google Gemini<br>4. Google Play<br>5. Kali Linux<br>6. Screenshot<br>7. Splice<br>8. Steam<br>9. Trading View<br>10. WPS Office |
| Oct 10, 2026 | 🟩 Added the following apps to the restricted app list (Odin Production Full Workflow world):<br>1. Adobe Acrobat<br>2. Adobe After Effects<br>3. Adobe Illustrator<br>4. Adobe InDesign<br>5. Adobe Premiere Pro<br>6. Antigravity IDE<br>7. App Store.app<br>8. Apple Music Classical<br>9. Cisco Packet Tracer<br>10. CleanMyMac X<br>11. Complete Anatomy 12. Dictionary.app 13. Font Book.app 14. Games.app 15. GoodNotes 16. GraphPad Prism 17. Linear 18. Magnet 19. Maps.app 20. Mendeley 21. Microsoft Intune 22. Microsoft Store 23. Microsoft Support 24. Music.app 25. News.app 26. NVivo 27. Paprika Recipe Manager 28. Parallels Desktop 29. PDFgear 30. Podcasts.app 31. Shazam 32. Siri.app 33. SnapGene 34. Spotify 35. Substance 3D Painter 36. TradingView 37. UCSF Chimera 38. Wolfram Mathematica |
| Oct 4, 2026 | 🟩 Added the following apps to the restricted app list (Odin Production Core world):<br>1. Apple Compressor<br>2. Apple Motion<br>3. Final Cut Pro<br>4. iMovie<br>5. Keynote<br>6. Logic Pro<br>7. MainStage 8. Pages |

# Reviewer Onboarding

🎯 **After this phase, you will:**

**•** Understand the steps to get onboarded as a Reviewer

**•** Have access to all of the tools you’ll need

## Onboarding Steps

Here is a quick reference guide for how to complete onboarding.

| **Step** | **Goal** |
|---|---|
| [**1 · Insightful**](#insightful) | Download the Insightful timer and know how and when to use it |
| [**2 · Okta**](#okta) | Access the Okta dashboard |
| [**3 · Reviewer Handbook**](#reviewer-handbook) | Read this guide to understand the review process |
| [**4 · Quiz**](#reviewer-assessment) | Complete reviewer training. Pass the quiz on the Odin Dashboard unless you qualify for the promoted-writer assessment exemption described below. |
| [**5 · Access Studio**](#studio) | How to access and navigate Studio |

## Insightful

Insightful is used for all of our time tracking, and is how you get paid.

- Once your contract is active, download the Workpuls desktop app from the [Insightful download page](https://app.insightful.io/#/token/download). Full details on Insightful installation and use can be found [here](https://talent.docs.mercor.com/how-to/use-insightful).
- Sign in using Continue with SSO and your @mercor.expert email.
- Insightful has separate Task and Reviewer timers for reviewers. Begin using the Reviewer timer as soon as it appears when reviewing. Do not log writing time on the Task timer.

    ![](images/p011_1.png)

    > *Text shown in the image:* Insightful app window. ‹ PROJECTS (back link) · Odin · 34:37 h/week · Search tasks · Today (Recent Time) · task “Glowstone-Odin - Task” (priority Low) with a running timer 05:23:14 and a red stop button (highlighted with a red box). Bottom: Last sync Today at 01:16 PM · [Open Dashboard].

**⚠ Unauthorized Time**

You may only track time when you are actively working. Excess idle time, or time spent on non-project work, is considered fraudulent and will be deducted. You may be offboarded from the project if this occurs- only track time while working on Odin.

Track time only for eligible activities. See the table below.

| ✅**Ok to Track** | ❌ **Do not track** |
|---|---|
| Reviewer onboarding and completing the reviewer training and quiz. | Sitting idle or waiting for new tasks or meeting attendees without an authorized, paid duty. |
| Reading the review guidelines and required project updates within your allowed hours. | Sitting idle watching Slack in case something is posted. |
| Required reviewer training and approved project meetings. | Working for a non-Odin project. |
| Approved reviewer office hours or review-related support - **max 2 hrs weekly**, on the “Admin” timer. | Optional office hours or other optional calls. |
| Reviewing and re-reviewing assigned tasks, including evidence checks and file corrections. | Breaks, social media, unrelated websites, personal tasks |
| Writing complete feedback in the writer-facing Studio field and sending the required writer DM. | Resolving non-blocking personal technical issues or waiting for access to project tooling. |
| Actively participating in necessary review-related Slack discussions. | Chit-chatting with other experts in Slack. |
| Other explicitly approved reviewer duties. | Waiting for Maven or another AI tool to return an answer. |

# Okta

The Okta Dashboard is accessed by logging in to your account at [work.mercor.com](http://work.mercor.com), using your personal email and password.

- Click ‘Home’ on the left toolbar, then ‘Contracts’. Find and click your Odin contract.
- Scroll to ‘Tools & Integrations’, find Okta, and click the Dashboard link.

    ![](images/p012_1.png)

    > *Text shown in the image:* Tools & integrations — “Platforms connected to your contract”. Okta (Active) — SSO access to client tools; Docs · [Dashboard] (highlighted with a red box) · Reset password. CLIENT TOOLS: Google Workspace (Provisioned) · Slack (Provisioned).

- When prompted to add a verification method, use the Passkey option, and set one up for your account by following the steps.
    - You will be taken to the Okta dashboard where you can access your Slack app, Studio, and your Google Workspace Mail, which will display your mercor.expert account.

        ![](images/p013_1.png)

        > *Text shown in the image:* Dashboard (side menu): My Apps · Work · Add section · Notifications · Add apps · Last sign in: a few seconds ago. My Apps → Work: Google Workspace Mail · Slack Enterprise · Google Workspace Drive · Google Workspace Calendar · **Studio** (tooltip “Studio”) · Google Workspace Sites

    - To access project documentation, you **must** be logged in to a browser using your mercor.expert account.
    - Once you have logged in to Okta, you can do this by setting up a new Google profile, pasting in your mercor.expert email address, and clicking next- it will log in with the SSO.

💡**Okta issues**

For access issues not covered in this guide, please email support@mercor.com.

# Reviewer Handbook

This guide is your single source of truth for the reviewing process. Please ensure you review it in full before you begin reviewing!

💡**No Mac required**

Reviewers do not need to have a Mac to complete reviews on Project Odin. If you wish to write tasks as well, you will need a Mac.

# Reviewer Assessment

To become a reviewer, complete the training and pass the assessment on the Odin Vercel Dashboard. Promoted writers with first-pass approvals on four of their last five tasks are exempt from the assessment.

The reviewer assessment includes:

- 2 mock reviews
    - Watching a short task
    - Completing a review checklist
    - Writing your feedback
- Narration check
    - Watch a 40-second task snippet with no audio
    - Type out a transcript of what good narration would sound like in the snippet
- You can only take the assessment once, and the results will determine if you become a reviewer or not.
- If you do become a reviewer, your starting tier will be decided based on your score on the quiz. See more information in [Roles & Pay](#onboarding-steps).
- If you do not pass the assessment and do not have your role automatically returned to “writer” after an hour, or simply do not wish to be a reviewer, fill in the [Pay & Role Request Form](https://forms.gle/g3YJjsAecgMKYEuV6) to return to the Writer role.

# Studio

When you have passed the quiz, you should get reviewer access to Studio within 30 minutes.

Inside Studio, you will see the Reviewer Dashboards available on the left side, and the worlds available in the top right drop down menu.

![](images/p015_1.png)

> *Text shown in the image:* Studio — Review queue — “Filtered tasks in Odin Production Full Workflow”. World selector “Odin Production Full Workflow” (highlighted with a red box) and [Create Task]. Left menu (Annotator): Project Guide · Announcements · Tasks · Dashboards (highlighted) → Available to claim · My tasks · My re-reviews · Review queue · My current reviewed tasks · My reviewed tasks · Ideas awaiting review · My idea reviews · Quick review queue · My current quick reviews · Leaderboard · Prioritized Review Queue. Note: “the Get next task button at the top of the task list is for probation audits only. To take a task from this queue, open it and press its Claim button.” “Tasks awaiting review that you can claim.” Table (Filter · Columns · Group · Page 1 of 1 · 77 tasks – Showing 1–77 of 77 · 100 rows): columns Task Name · Task Status · Created By · Updated By · Needs Attention From · Created At · Updated At; the Task Status “Ready for Review” cells are highlighted with a red box.

💡**No review tasks?**

Review tasks are claimed quickly! If you open the dashboard and there are no tasks available, refresh the page, or check the other dashboards. Once you are off probation, you can review in **Review Queue, Quick Review Queue**, and **Ideas Awaiting Review**.

# Reviewer Role

🎯 **After this phase, you will:**

**•** Know the expectations for reviewers

**•** Understand the different reviewer tiers

**•** Know the pay associated with the role

# Reviewer Expectations

Reviewers are always expected to communicate with the writers using collaborative, respectful language.

- An important part of your role as a reviewer is to help the writers **to improve**- not to simply point out what they’ve done wrong.
- As a reviewer, you are **setting the tone**. Approach every interaction as a collaborative discussion, not a top-down correction.

Good feedback is essential on this project. Follow these general guidelines:

| **Item** | **What it means** |
|---|---|
| **Start with the positive** | Acknowledge what the writer did well |
| **Be specific** | Clearly explain each issue with the task. Include a timestamp and specific example. |
| **Provide clear, actionable feedback** | Suggest a path to improvement |

When providing feedback, we ask our reviewers to follow a [specific template](#odin-reviewer-feedback-templates) to allow for as much alignment as possible and to improve clarity. There are additional message templates in the <u>Feedback Templates</u> section.

💡**Good Communication**

Clear, respectful communication is the foundation of our workflow. It improves our work, our team morale, and our overall project speed! Early in the project, Reviewers are essential to help **calibrate/motivate** writers, and this interaction can set the whole tone for their experience.

Reviewers are expected to maintain good efficiency standards. All reviewers should aim for:

- &lt;45 minutes per review, on average, while ensuring quality remains high.
- At least 15 hours of work per week, to ensure tasks continue to turn over.
- A review pass rate of 30% or higher- that is, that at least 30% of your reviews result in approvals.
    - You are responsible for ensuring only high quality tasks are approved, and also for helping to coach writers to improve so this rate can be achieved.
- A reviewer defect rate &lt;10%.

💡**Reviewer Defect Rate**

A defect is recorded against you when an auditor **reverses** your review decision at the QC audit stage. For example, if you approve a task and the auditor decides it Needs Edits, that review counts as a **defect**.

Defect rate = (# of defects + 1) ÷ (audited reviews + 10), expressed as a percentage. Example: You have one audited review, which is a defect.

(1 + 1) ÷ (1 + 10) = 2/11, or about 18%.

# Pay Policy

Your contract will determine your base rate.

For eligible hourly-paid tasks, time tracked within your stage allowance or weekly limit is paid. Idle or off-project time, and hours above your limit, are not paid.

**Payment schedule**

- Hourly pay is sent every Wednesday for the previous week (Friday 11:30 am PT - Friday 11:29 am PT following week).
- Tier bonuses are normally paid the Wednesday after the corresponding hourly pay, but may arrive earlier, including with the hourly payment. Tier bonuses are the amount paid above the base hourly rate in your contract.
- First payout: Verification may add 3-5 business days.
- Possible delays: Bank holidays, processing schedules, and bank cutoffs may delay settlements.

**Payment providers**

- **Stripe:** The primary payment platform for ongoing contributors. After accepting a job offer, follow the [instructions](https://talent.docs.mercor.com/how-to/payments#setting-up-stripe) to create your payout account.
- **Wise:** Generally used for one-time payments, contributors who have not completed Stripe onboarding, or contributors whose bank accounts are in countries Stripe does not support. You don't need a Mercor account to receive payment through Wise. Follow the [instructions](https://talent.docs.mercor.com/how-to/payments#setting-up-wise) to set up Wise.

# Roles & Pay

Reviewers are divided into three tiers, each with different pay rates and hours: Probation, Standard, and Trusted. Tiers are reviewed once a day at 00:00 India time, and reviewers will be moved into the appropriate tier and notified of the change. Each tier applies to the whole India-time day (11:30am PT - 11:29am PT.

|   |   |
|---|---|
| **⚠️Probation** |   |
| **Summary** | **Details** |
| **Base Pay:** The hourly rate in your contract **Bonus Pay:** None<br>**Total Pay:** The hourly rate in your contract **Available Hours:** 6 hours **Hours roll over:** Never | ◦ If you passed your Reviewer training/quiz with a mid-range score, you begin in this tier.<br>◦ You will complete 2 reviews, which will be audited.<br>&emsp;◦ If both pass, you move to the Standard Tier.<br>&emsp;◦ If either fails, you complete a further 2 audited reviews.<br>&emsp;◦ If either of those fail, you return to being a Writer. |

✅**Standard**

| **Summary** | **Details** |
|---|---|
| **Base Pay:** $55/hour **Bonus Pay:** None **Total Pay:** $55/hour **Available Hours:** 80 hours **Hours roll over:** Weekly | ◦ If you passed your Reviewer training/quiz with a high score, you begin in this tier.<br>◦ You may also move up from Probation to this tier if your first reviews pass audit.<br>◦ This is the standard reviewer tier, but you may move to the Trusted tier if your work is high quality. |

|   |   |
|---|---|
| 🎯**Trusted** |   |
| **Summary** | **Details** |
| **Base Pay:** $55/hour **Bonus Pay:** +$20/hour **Total Pay:** $75/hour **Available Hours:** 80 hours **Hours roll over:** Weekly | ◦ You may move up from Standard to this tier if you are a high quality, efficient reviewer.<br>◦ Reviewers are eligible for this tier with:<br>&emsp;◦ 10+ reviews<br>&emsp;◦ AHT &lt;45 min on your last 10 reviews<br>&emsp;◦ Lifetime defect rate under 10% |

*Effective October 22, 2026 at 3:00 p.m. Pacific (PDT). Hours worked around the cutoff use the rate applicable when the work was done.*

Reviewers are also able to write when there is no review queue.

- Use the Reviewer timer when reviewing. Begin using the Reviewer timer as soon as it appears; Do not log time on the Task timer.
- When there are no tasks in the review queue, you can also write!
- All reviewers are paid $100 + $2/minute for each task that reaches RFD. Do not log time on Insightful when writing.

# Review Workflow

🎯 **After this phase, you will:**

**•** Understand how the review types differ

**•** Know how to claim tasks for review and the rules

**•** Understand the full workflow for each review type

# Orienting with Studio

You will conduct all reviews inside Studio, which you can access via [Okta](#okta). When you click the Studio tile, it will open this page.

Key components:

- **Dashboards:** Dropdown menu on the left side where you can access the different Reviewer Dashboards.
- **World:** Dropdown on the top right corner. You will have access to two worlds.
    - Odin Production Core world- Original world. Very few tasks left to review.
    - Odin Production Full Workflow world- New world. Most tasks will be found here.
- **Main task section:** Once you have clicked a dashboard, the tasks will appear in the middle of the page.

    ![](images/p021_1.png)

    > *Text shown in the image:* Studio — Review queue — “Filtered tasks in Odin Production Full Workflow”, with the worlds dropdown open (search “Search worlds…”: Odin Production Core · ✓ Odin Production Full Workflow) and the selector highlighted with a red box. Left menu: Dashboards (highlighted) and Review queue (highlighted). Table (8 tasks – Showing 1–8 of 8): Task Name · Task Status (Ready for Review; one “Idea Needs Review”) · Created By · Updated By · Needs Attention From · Created At · Updated At, with the first two columns highlighted with a red box.

## General Review Guidelines

Project Odin has 3 different types of reviews. The general process for each of these reviews is the same.

| **Review Type** | **What it is** | **Where to find it** |
|---|---|---|
| Idea | Reviews initial ideas before the writer starts recording. | Review Queue |
| Full | Tasks that require all 17 dimensions to be reviewed. | Prioritized Review Queue |
| Quick | Shorter reviews that only have 5 dimensions to check. | Quick Review Queue |

💡**On probation? Full or Quick Reviews only!**

If you are on probation as a reviewer, please only perform Full or Quick Reviews until you reach Standard Reviewer status.

# Claiming Reviews

Reviewers are expected to complete reviews in the same sitting in which they are claimed.

- Always aim to complete a review within 1 hour of claiming it. AHT should remain &lt;45 minutes overall.
- Do not claim more than 2 reviews at a time.
- Tasks held in review for >2 hours are at risk of being released back to the queue.
- If you need more time, you can extend it by ticking the ‘Extend review claim’ box.
    - This should be used sparingly- we monitor how often reviewers use it.
- If you need to step away and cannot finish a review, you should release it.
- To claim a review in any of the workflows, click an available task, scroll to the bottom, and click the ‘claim’ button in the left tab.

    ![](images/p022_2.png)

    > *Text shown in the image:* REVIEW DECISION — “No transitions available.”

    ![](images/p022_1.png)

    > *Text shown in the image:* REVIEW DECISION — green button [Claim idea review].

- If you get to the bottom and it says ‘No transitions available’, this just means someone else has already claimed it.

**⚠ Do not hold on to reviews**

Reviews should be completed in the same sitting they are claimed. Do not claim tasks in order to reserve them for later. The ‘Extend review claim’ box should only be used if you are waiting for technical guidance/support, never to save a review for another time.

# Idea review

Idea reviews are found in the main Review or Ideas awaiting review dashboards.

- Idea checks are mostly automated. Distinct ideas are approved automatically so the writer can start recording.
- Ideas the model can't verify or that the writer has escalated appear as Idea Needs Review in the review queue.
- Once you have claimed the idea review, read through the goal, starting point, suggested apps, and reviews and checks.
- You will see the report with details from the automated check in the ‘Idea Check Report’ section.

    ![](images/p023_1.png)

    > *Text shown in the image:* IDEA CHECK RESULT — “While your idea shows Checking Idea, the check is running. It usually takes about a minute, so refresh the page to see the result. If it is still checking after a few hours, it is re-run automatically within a day.” Idea check report — **Sent back: needs changes.** “The proposed documentation work is understandable, but the deployment goal and app list conflict with the described steps and deliverable.” Feedback: • “Will you deploy and configure the solution during this task, or is the intended work to design and document its workflow?” • “The steps name Microsoft Viso, but the app list names only Microsoft Word. Will you use both apps?” “Similarity check runs once the idea is clear.” “Disagree? Use **Escalate to human** and add a note.” IDEA CHECK DETAILS (REVIEWERS) — Idea check details (reviewers): **Sent back: needs changes.** “Similarity check runs once the idea is clear.” “Check version e0d9b662912a”. REVIEW DECISION — [Claim idea review].

- On the right side of the page, you can add your Feedback to support your decision in the feedback section.
- You can then click ‘Approve idea’, ‘Reject idea’ or ‘Send back to writer’ if you believe it just needs some minor edits.
- Reject ideas only if you are convinced they are entirely outside project guidelines and will need to be completely redone.

    ![](images/p024_1.png)

    > *Text shown in the image:* Needs edits reason — “Select every reason this task needs edits. Pick the specific reason under the group that matches the problem. Do not send back for complexity, narration speed, missing Why alone or mouse inactivity alone. Mouse findings belong in delivery callouts. Extended pauses here means a retained narration-silence issue, not pointer inactivity.” Re-record: No Deliverable · No/Incomplete Setup · Extended Pause(s) or Too Much Typing · Narration/Audio Issues · Poor Window Management · Restricted App Open/Used · Task Length is below threshold. Files / metadata: Observable PII/Paywalled Content · AI Used in Setup or Task. Clarification: Other (Explain in Reviewer Comments). Feedback* — “Goes to the WRITER. When you send a task back it returns to the writer, not the reviewer. In 1-2 sentences, tell the writer exactly what to fix, with timestamps and the exact element. Probation auditors: write this for the writer; put any notes about the reviewer in the audit sheet, not here.” Review History — “No previous review rounds yet.” Buttons: [Approve idea] · [Reject idea] · [Send back to writer] · [Save].

# Full review

When conducting full reviews, check several dashboards. Always check in this order:

- My re-reviews- Tasks that have come back to you for another review.
- Prioritized Review Queue- Higher priority tasks.
- Review Queue- The normal review queue.

On the right side of the page, inside the task, you’ll score 17 dimensions as either 1 (ideal), 2 (acceptable), or 3 (failing). Please see <u>Reviewer Checklist</u> for more details on how to score each dimension.

- Make sure you open and review all of the input files.

    ![](images/p025_1.png)

    > *Text shown in the image:* Review tab — REVIEW FEEDBACK. Review checklist — “Score every item against the Reviewer Checklist:” (link to the Reviewer Checklist document). 1 = Ideal state · 2 = Within acceptable tolerance · 3 = Failing tolerance. “One item at band 3 sends the task back, except Metadata.rtf (item 1), which you fix yourself. Items at band 2 are feedback only. Writers never see bands: in your feedback, point at the ideal state. Select ‘I understand’ to proceed.” [I understand]. **1. Metadata.rtf matches the TaskRecorder Goal (apps, workflow)** — “This item should NOT send a task back; if Metadata.rtf is wrong, fix it yourself, re-upload it, and DM the writer (and the reviewer, if you are auditing). AutoQC checks the file name, leftover template text, numbered steps, Topology tags, and that the Request is at least 70% similar to the TaskRecorder Goal. It does not compare apps, so check those yourself.” Dropdown: “1 = The Request matches the TaskRecorder Description word for word, and the apps …”. **2. No window covers >25% of another for >6 s** — “Popups, menus and dialogs inside a window or app are fine while in use, but a window can’t cover another window, including another window of the same app (for example two Chrome windows or two Word documents). For any call, note the timestamp and the two windows involved. AutoQC flags only overlap over 30 s, so check 6-30 s and any cover over the content being worked on yourself.” Dropdown: “1 = No window covers >25% of another for >6 s, and nothing covers the content bei…”. **3. Narration says what and where for each action, and why when useful** — “Eyes-closed test: with your eyes closed, could you follow which actions are being performed? An action is anything that selects something or changes the state of the app. Example with all three: “I’ll click the blue Export button in the top right to save the chart as a PDF.” Vague words like “here” or “this” only fail when there’s a 2+ minute stretch of them. AutoQC flags only under 70% with 2 of the 3 Ws, so it can pass narration with what and why but no where: check where yourself.” Dropdown: “1 = ≥70% of actions have what, where and why”. **[Retired] 4. [Automated but PLEASE manually check] Eyes closed test: Viewer clearly understands what actions are being performed in the video with eyes closed (no ‘click here’, ‘change this’)** — “Automated check. Look at the AutoQC card and any writer dispute, check the recording, and score on the ranges below.”

As with all review types, you can select whether to approve, send for edits, or reject a task at the bottom on the right side, with these buttons:

![](images/p026_1.png)

> *Text shown in the image:* Decision buttons: [Send for Edits] (orange) · [Reject] (red) · [Approve ▾] (green). Part of the feedback text above the buttons is visible (cropped).

💡**When to reject**

You should rarely reject tasks- this will discard them. Reject should be used only when **explicitly** instructed; in the vast majority of cases, you will send it for edits instead. Tasks can only be reviewed 4 times. After the 4th review, if it is not approved, reject it instead of sending it back.

# Quick review

Some tasks will be routed to the Quick review queue. Quick review is a more focused review process that targets the main areas that AutoQC misses.

These tasks only have 5 dimensions that need to be reviewed:

![](images/p027_1.png)

> *Text shown in the image:* REVIEW FEEDBACK — **1. Metadata.rtf matches the task** — “Open Metadata.rtf and compare it with the TaskRecorder Goal and the recording. Pass if it matches, or if you fixed it yourself. This item never makes a task Needs edits on its own: if Metadata.rtf is wrong, fix it, re-upload it, and DM the writer.” [Pass] [Needs edits]. **2. Window management** — “Skim the recording. Needs edits if a window covers more than 25% of another for over 30 seconds (including two windows of the same app), or if any window covers the content being worked on. Popups, menus and dialogs inside a window or app are fine while in use; side by side or split screen is fine.” [Pass] [Needs edits]. **3. Narration says what and where** — “Listen to 2-3 minutes. Eyes-closed test: can you follow what the writer is doing and where on screen from the narration alone? Needs edits if under 70% of actions have what and where. Why is optional.” [Pass] [Needs edits]. **4. Recording shows the task** — “Skim the recording and compare it with the task. A major action is a step in the task’s numbered description, or a step that creates part of the deliverable. Needs edits if 1+ major action stated in the task is missing from the video.” [Pass] [Needs edits]. **5. Recording is free of Major PII, on screen and in the audio** — “The video PII review table covers the screen only. Check the audio yourself. Major PII, flagged or not, means rejecting the task.” [Pass] [Needs edits].

These operate on a simpler tagging system instead of scoring from 1-3.

- Check each dimension carefully and select ‘Pass’ or ‘Needs edits’, based on the guidance in the <u>Reviewer Checklist</u> section.
- Also review the [AutoQC checks](#autoqc-coverage-for-reference) on every task, and any disputes written by the writers.
- If you notice other issues that would warrant sending the task back, please send it for edits, even if they are outside the 5 dimensions checked.
- These should be faster- ideally 30-40 minutes or less.

# Completing your review

After every dimension has been given a score of 1-3 (or scored ‘Pass’ or ‘Needs edits’ in Quick Reviews), you can move on to the rest of the review.

- Select an overall quality score using the toggle, from 1 to 5.
- Be aware that on this scale, 1 is the worst score, and 5 is the highest!

    ![](images/p028_1.png)

    > *Text shown in the image:* OVERALL QUALITY SCORE — 1–2 = NEEDS EDITS, 3–5 = APPROVE. Scale bar 1 to 5: **1 Poor** — many items at band 3, task likely not salvageable · **2 Needs revisions** — one or a few items at band 3 · **3 Lower quality, but likely useful** — several items at band 2, none at band 3 · **4 Good, writer needs some tips** — a couple of items at band 2 · **5 Excellent** — all or nearly all items at band 1. Groups: NEEDS EDITS (1–2) and APPROVE (3–5). “**Outcome:** 3, 4 or 5 approves the task. 1 or 2 sends it back.”

    ![](images/p029_1.png)

    > *Text shown in the image:* Writer’s Quality Score* — “Rate the work as submitted:” 5 = Excellent: all or nearly all items at band 1 · 4 = Good, writer needs some tips: a couple of items at band 2 · 3 = Lower quality, but likely useful: several items at band 2, none at band 3 · 2 = Needs revisions: one or a few items at band 3 · 1 = Poor: many items at band 3, task likely not salvageable. Slider Poor ↔ Excellent set to 2. Needs edits reason — “Select every reason this task needs edits. Pick the specific reason under the group that matches the problem. Do not send back for complexity, narration speed, missing Why alone or mouse inactivity alone. Mouse findings belong in delivery callouts. Extended pauses here means a retained narration-silence issue, not pointer inactivity.” Re-record: No Deliverable · No/Incomplete Setup · Extended Pause(s) or Too Much Typing · Narration/Audio Issues · Poor Window Management · Restricted App Open/Used · Task Length is below threshold. Files / metadata: Observable PII/Paywalled Content · AI Used in Setup or Task. Clarification: Other (Explain in Reviewer Comments). (the “Other (Explain in Reviewer Comments)” option is selected) Feedback* — “Goes to the WRITER. When you send a task back it returns to the writer, not the reviewer. In 1-2 sentences, tell the writer exactly what to fix, with timestamps and the exact element. Probation auditors: write this for the writer; put any notes about the reviewer in the audit sheet, not here.”

- If sending for edits, select a reason from those given, or select ‘Other’ and explain.
- Always leave a detailed review in the writer-facing ‘Feedback’ section.
    - Review the [communication expectations](#reviewer-expectations), and make use of the <u>Feedback Templates</u> to ensure good feedback is provided.
    - Always ensure you include timestamps and examples in the feedback.
- Add Internal Notes: These are notes that the writers will not see. They are for QC and EPMs only.
    - Pro tip: If you find yourself making a judgment call on an edge case, explain your reasoning for approving the task in the Internal Notes.

💡**Good feedback is crucial!**

As a reviewer, part of your role is to ensure the writers receive constructive, detailed feedback, with timestamps and examples, to help them improve.

Your role is not only to ensure tasks are high quality- helping to calibrate the writers is also very important.

Always add the feedback directly in the task, AND send a message to the writer via DM on Slack.

# Review Efficiency

There are several things you can do to improve your efficiency and speed up the review process, while maintaining quality.

Quick tips:

| **Try:** | **But remember:** |
|---|---|
| ✅ Watch the recording in 1.5x or 2x speed. | Check in 1x to make sure narration is paced well. |
| ✅ Use AutoQC as a quick check for quality. | Make sure key issues are addressed. |
| ✅ Focus your time on what AutoQC misses. | Good narration is crucial- make sure it is checked. |
| ✅ Cut time if you know early on the task needs to be sent back. | Do a quick check of the rest of the task so you can flag other major issues. |
| ✅ Always fix minor issues yourself. | This saves time overall if it doesn’t need another review. |

Keep in mind what AutoQC is good at, and focus your attention elsewhere.

![](images/p031_1.png)

> *Text shown in the image:* **Who checks what.** *AutoQC is good at* (Open every flag and confirm it. If it passes, trust it unless something looked off.): Recording length · Typing % · Mouse idle and silences · Window overlap timing · Click pauses.<br>*You need to check* (AutoQC misses these often. This is where your watch time goes.): **Narration: what, where, why** (tagged “#1 ISSUE”) · Restricted apps, even if not listed · PII and sensitive info · Video matches the Goal · Stacked windows, trial-and-error

Other ways to save time:

- Start loading the video as soon as you claim the task. Do the Goal and metadata check while it buffers.
- Use AutoQC flag timestamps to go straight to the moment in question.
- Keep feedback short. One line per issue with a timestamp and the fix.
- Pay attention to narration! Watch for vague words like "this", "that", "here".
- If it is a re-review, check what the previous reviewer’s comments were, and focus on these areas first.

💡**Live captions in Chrome**

To assist with your review of the video, try using live captions! Click the three dots in the top right of the browser, and select Settings. On the left sidebar, click Accessibility, then Turn on Live Captions, and make sure to select English.

💡**Narration**

Narration is by far the most common quality issue. It is the top reason writers get sent back, and the top issue QC finds in tasks reviewers approved. Give it most of your attention.

Does it explain **what** is happening, **where** on screen, and **why**? Would it pass the eyes-closed test (could you follow along without seeing the screen)?

# Reviewer Checklist

🎯 **After this phase, you will:**

**•** Understand the 1/2/3 quality scale for reviewing

**•** Understand all the different items to score for each task

**•** Have access to the Quick Reference review decisions table

# Reviewer Checklist

Below is the Project Odin Reviewer checklist that will be used to verify the quality of tasks on Project Odin. When reviewing a task, you will be selecting which tolerance criteria have been met for each checklist item, which is on the following scale:

- 1 = Ideal state
- 2 = Within acceptable tolerance
- 3 = Failing tolerance

    ![](images/p033_1.png)

    > *Text shown in the image:* SCORING SCALE — BINARY ROWS: 1 = YES, 3 = NO. Scale bar: **1 Ideal state** · **2 Within acceptable tolerance** · **3 Failing tolerance**. Groups: WITHIN TOLERANCE (1–2) and FAIL (3).

Some checklist items have binary tolerance criteria: they either fulfilled it (1 = Yes) or they failed to meet it (3 = No). Other checklist items have a range which is described within each checklist item.

**⚠ Any score of 3 = Send back**

A single item in this checklist which scores a 3 will require the task to be sent back. The only exception is item 1 (Metadata.rtf matches the TaskRecorder Goal)- because you can, and should, correct the Metadata.rtf file yourself.

## Metadata.rtf

The first checklist item relates to the Metadata.rtf file. Here’s what it is, and how to handle it.

- Open the file in any text editor and keep it in .rtf format. Fix any errors yourself and re-upload it.
- **Request:** the Goal section of the approved idea, exactly as approved. Nothing else.
- **Task Description:** a numbered, step-by-step outline of how the writer will complete the task.
- **Topology:** the apps in the order used, each tagged LOOKUP (reading or finding, no changes), CREATE (making something new) or MODIFY (changing something that exists). Apps can repeat. Example: Safari (LOOKUP) → Excel (CREATE) → GraphPad Prism (CREATE)

    ![](images/p034_1.png)

    > *Text shown in the image:* Metadata.rtf Upload* — The filled-in Metadata.rtf for this recording.<br>File: Metadata.rtf (46.7 KB) with a download icon (highlighted)

|   |   |   |   |   |
|---|---|---|---|---|
| **Checklist item** | **1 = Ideal state** | **2 = Within acceptable tolerance** | **3 = Failing tolerance** | **Notes** |
| 1. Metadata.rtf matches the TaskRecorder Goal (apps, workflow). | The metadata.rtf Request matches the TaskRecorder Description word for word, and the apps in the Task Description and TOPOLOGY fields match the TaskRecorder apps. | The Request wording differs but keeps every key idea, and the apps match. | Key ideas differ, or the apps do not match. | If this scores a 3, it does not send the task back- you should **correct this issue yourself in the Metadata.rtf.** |
| 2. The content being worked on remains visible. | No window covers >25% of another for >6 s, and no window covers any part of the content being worked on. | A window covers >25% of another for 6-30 s, and no window covers any part of the content being worked on. | A window covers >25% of another for >30 s, or a window covers any part of the content being worked on. | Minor window overlap alone is not an error and does not require edits or a re-record. Two tabs belonging to one window of the same app are not separate windows. For any call, note the timestamp and the two windows involved. |
| 3. Narration says what and where for each action, and why when useful. | ≥70% of actions have all 3 Ws (what, where, why). | ≥70% of actions have what and where (why optional). | Under 70% of actions have what and where. Missing where fails. (A narration with what and why, but no where, now fails.) | Eyes-closed test: with your eyes closed, could you follow which actions are being performed? An action is anything that selects something or changes the state of the app. Example with all three: “I'll click the blue Export button in the top right to save the chart as a PDF.” |
| 4. Screen recording shows the workflow described in the task. | All major actions stated in the task are in the video. | N/A | The video is missing 1+ major action stated in the task. | A major action is a step in the task's numbered description, or a step that creates part of the deliverable. |
| 5. The menu bar clock shows seconds at the start and end of the video. | Yes | N/A | No | Check the first and last few seconds; it doesn't need to be visible in between. |
| 6. The Goal document (task description) is shown at the start of the recording, then promptly minimized. | Yes | N/A | No | The Goal document can’t be shown in Notes.app or TextEdit; Preview and other apps are fine. |
| 7. Typing takes up 25% of the video or less (35% or less for Coding / Content & Writing tasks). | ≤25% of the video (≤35% for Coding / Content & Writing) | N/A | >25% of the video (>35% for Coding / Content & Writing) | Use the AutoQC typing % and task type; do not estimate by hand. |
| 8. The narration can be understood on first listen. Background noise, mumbling, speaking too fast, a strong accent or broken English only matter when they get in the way of understanding the video. Loud typing is fine if the narration stays clear. | You can follow everything the writer says without replaying. | N/A | You have to replay or guess to understand what is happening in the video, because of noise, mumbling, pace or unclear speech. | Tip: turn on Chrome Live Caption (Chrome Settings > Accessibility > Live Caption) and play the video. **If the captions pick up what the writer is saying, that is a good sign it is clear.** Many auditors have found this helpful. Judge clarity at 1x speed. |
| 9. The recording is free of disallowed AI use. | No AI used. | Only allowed AI: reading Google AI Overview with no follow-ups, autocomplete, or SWE/ML code that is part of the task. | Any prompting or chatting with AI, AI Mode, Google “Ask anything”, or an AI feature doing real task work (for example Photoshop subject select). | Escalate unclear cases, such as passive enhancement features. Apply Privacy rules in the [Writer Handbook](https://docs.google.com/document/d/1tOxjGqxhA6T49kXw9hrhwpEsk8ERaFOsB6gqZcrLAHg/edit?usp=sharing), or the [LLM section](#llm-use) in this document. |
| 10. The recording is free of personal information (PII), both on screen and in the audio. | Yes | N/A | No | Apply Privacy rules in the [Writer](https://docs.google.com/document/d/1tOxjGqxhA6T49kXw9hrhwpEsk8ERaFOsB6gqZcrLAHg/edit?usp=sharing)<br>[Handbook](https://docs.google.com/document/d/1tOxjGqxhA6T49kXw9hrhwpEsk8ERaFOsB6gqZcrLAHg/edit?usp=sharing), or the [PII section](#personally-identifiable-information-pii) in this document. |
| 11. Deliverable assets meet licensing requirements. | Yes | N/A | No | Apply licensing rules in the [Writer Handbook](https://docs.google.com/document/d/1tOxjGqxhA6T49kXw9hrhwpEsk8ERaFOsB6gqZcrLAHg/edit?usp=sharing) or [brief details](#licensed-content-and-copyrights) in this guide. Merely browsing a website with a trademarked logo does not fail. |
| 12. The narration and everything on screen are free of profanity. | Yes | Minor profanity on screen, not said or typed by the writer | Profanity said or typed by the writer, or major on-screen profanity | Minor: a mild word on a webpage or file the writer did not create. Major: slurs, explicit content, or anything prominent on screen. |
| 13. Narration must be fully in English, and deliverables must be in English. | Yes | N/A | No, or cannot verify | Minor amounts of non-English content on screen are acceptable. |
| 14. Recording includes an epilogue narration of 4:00 or less before recording stops: a narrated summary of how the task was verified, the approach, challenges, quality and reflections. | 4:00 or less, with real detail. | Over 4:00, or lacks detail (nonfailing). | N/A | A missing epilogue never sends a task back: use the unscored “Missing epilogue — does not block approval” response instead of a band. Ideas first approved before Oct 19, 2026, 6pm PT don’t need an epilogue, even after later revision. |

# Quick Reference Guide

Below is a quick reference table for when to approve, fix and approve, send back, or reject a task.

| **Issue** | **Action** | **How** |
|---|---|---|
| Any Metadata.rtf error (Request, topology, apps, mismatch with Goal or TaskRecorder) | FIX + APPROVE | Fix, re-upload, explain in Studio feedback + Slack DM. Never send back for metadata alone. |
| TaskRecorder description missing or mismatched, and it’s the only error | FIX + APPROVE | Once metadata.rtf matches the Studio goal: Internal Note + Edge Case checkbox. |
| Non-restricted app unlisted, or listed but unused | FIX + APPROVE | Fix editable files; if the field is locked, add an Internal Note. A materially different workflow still needs edits. |
| Deliverable file name slightly off | FIX + APPROVE | Rename it yourself. |
| Brief glimpse of the names Mercor or Odin | APPROVE | No note needed. |
| Intro length is above the ideal 20s, silence above 45s, or rushed clicks | APPROVE | Provide feedback. |
| One typing segment over 45s, typing at exactly 25%/35% | APPROVE | Provide feedback. |
| Dock not visible, Dock is at bottom but with a UI change, TaskRecorder window visible | APPROVE | Provide feedback. UI change can be wallpaper (not the macOS default), light/dark mode, Dock size, colours, resolution, icon size, theme. Cursor size and colour must stay default. |
| Minor overlap, content still visible | APPROVE | Score item 2 by its thresholds. |
| Mouse inactivity | APPROVE | Timestamped Internal Note. |
| Epilogue missing / over 4:00 or thin | APPROVE | Use the unscored “missing” response / band 2 + growth note. |
| Video is 50:59–54:59, single-app task, low task complexity | APPROVE | No deduction for these alone. |
| TaskRecorder window not shown at the start | APPROVE | Possibly a recorder bug. Review as normal and add an Internal Note. |
| Any active checklist item at band 3 (2, 3, 4, 5, 6, 8, 10, 12–16) | SEND BACK | Send-back template, with timestamps. |
| Confirmed there is an app-use violation. Check the [Writer Handbook](https://docs.google.com/document/d/1tOxjGqxhA6T49kXw9hrhwpEsk8ERaFOsB6gqZcrLAHg/edit?usp=sharing) for the source of truth list. | SEND BACK | Name the app, the prohibited use and timestamps. |
| Workflow or deliverable materially different from the approved idea | SEND BACK | Fixing the metadata can’t repair this. |
| Resubmitted with no changes | SEND BACK | Point to the original note. |
| Accessibility Inspector not running / no UI element changed | SEND BACK | At least one UI element needs to be changed, and Accessibility Inspector must be running. |
| Studio, Insightful or Odin Slack on screen | SEND BACK | Project materials cannot be shown on the recording. |
| Missing or unreadable files, video outside 15:00–54:59 | SEND BACK | Send back with suggestions. |
| Concept can’t be fixed within the approved scope | REJECT | If unsure, send back instead. |
| Still needs writer changes after review #4 | REJECT | Tasks have a maximum of 4 reviews. If it can’t be approved on review 4, it should be rejected. |
| Unclear AI feature, licensing or PII | ESCALATE | #odin-reviewers-hub for advice if you aren’t sure. |

# Additional review rules and guidance

Below are some additional things to keep in mind while reviewing.

# Check for good narration

**Use What, Where, and Why**

For each meaningful step, the writer should say **what** they are doing, identify the control and **where** it is on screen, and explain the **purpose or result** when it is not obvious.

The cursor should be on the correct place on the screen while they are narrating the navigation, to ensure they match.

| **Element** | **Purpose** |
|---|---|
| **What** | The action being taken |
| **Where** | The exact app, control, file, value, or interface location |
| **Why** | The purpose or what happens after the action, when it is not obvious |

💡**Listen for ‘there’ and ‘that’**

Too many instances of ‘here’ or ‘there’ or ‘this’ or ‘that’ may indicate writers have not narrated the what/where/why successfully. See the <u>Examples</u> tab for good narration examples.

Also ensure the audio is generally good quality, with low background noise, that each step is narrated, and it is well-paced rather than moved through too quickly.

## Manage Windows Clearly

Writers must manage their windows properly, with one clear active window, or having them arranged with the needed windows side by side. Other task apps may remain open, but minimize them when not needed for the current step.

💡**Window management**

App windows must be open in only a single layer on-screen with minimal overlap, otherwise Accessibility Inspector can't accurately communicate to TaskRecorder which UI elements the cursor is passing over or selecting. In-app dialogues, pop-ups, menus, and toolbars will always be an exception to this for practical reasons.

## Personally Identifiable Information (PII)

You can check quickly for PII by scrubbing to each app/window change and looking for any of the below issues.

| ✅ **Ok to include** | ❌ **Not ok to include** |
|---|---|
| Your @mercor.expert email and account name | Other real account or identification numbers |
| Public figures or public profiles | MAC addresses, or a Mac serial number + an IPv6 address |
| Mentioning Mercor or Project Odin aloud | Showing any Project Odin tools or documents |
| Obviously fake names, emails, and phone numbers (John Smith, [JohnSmith@example.com](mailto:JohnSmith@example.com), 123-456-7890) | Personal emails, home addresses or phone numbers of real people |
| Your first name | Personal photos or biometrics |

There are several places PII can slip in, and recordings which include them will need to be re-done. Pay particular attention to:

- **App profile corners.** The writer’s name or photo in the top-right account area of PowerPoint, Word, Google Docs, Sheets or Slides, or the browser's profile button.
    - An initial in the corner of Chrome, with no personal photo, is ok.

        ![](images/p044_1.png)

        > *Text shown in the image:* Google account menu fragment: a pink “Work” profile chip with an “H” avatar and a three-dot menu; below it a Gemini sparkle icon and a pink circular “H” avatar.

        &lt;-- This is ok!

- **Usernames in paths.** The writer’s name in the Finder sidebar, a window title, a save or export dialog (/Users/yourname/...), or the Terminal prompt.
- **Logged-in accounts.** A personal email or profile photo in Chrome, Gmail, Google Drive or any web app.
- **Autofill and history.** The writer’s name or email in search suggestions, recent-file lists, or notification previews.

Also ensure no Project Odin tools or documents ever show on screen. This includes:

- The Project Odin Writer Guidelines or other project-administration documents.
- Mercor Studio at any point, including the Studio icon, a Studio URL, or any task, instruction or review page.
- Insightful (Workpuls) at any point; it should only run in the background.
- Odin Slack, including the workspace or any Odin Slack URL.

# Licensed Content and Copyrights

Any images, videos or other downloaded content which are used for the task must be CC0 or Public Domain. Royalty-free on its own is not enough.

For SWE/ML/DS tasks, public GitHub repositories are fine. Prefer these licenses:

- [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.en), [PDDL](https://opendatacommons.org/licenses/pddl/), [ODC-by](https://opendatacommons.org/licenses/by/), [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0), [BSD](https://choosealicense.com/licenses/0bsd/), [MIT](https://choosealicense.com/licenses/mit/), Public Domain

Recordings should not contain:

- A visible creator watermark (except Gemini- this watermark is allowed)
- A copyright symbol or ownership notice
- Unverified or unclear licensing
- Paywalled or otherwise restricted material
- Private repositories

# LLM Use

- Writers may use Gemini generated content for tasks, but it must be created **before the recording**.
- Writers should not discuss on the recording how the file was generated, or use Gemini to create additional content during recording.
- Writers should also make it clear in their submission how the files were generated if LLM was used.

**Detailed LLM use cases**

|   |   |   |
|---|---|---|
| **Use Case** | **Status** | **Rule** |
| Standard Google Search results | Allowed | Use search results normally |
| Opening a static link shown in Google AI Overview, including under Show more | Allowed | Do not interact with the AI Overview |
| Selecting Ask anything in Google AI Overview | Not allowed | This begins an AI interaction |
| Using AI Mode, Gemini, ChatGPT, Claude, or another conversational assistant | Not allowed | Do not prompt, chat, ask follow-up questions, generate, or summarize |
| Using AI to generate task content during recording | Not allowed | Task content must be created manually through the recorded professional workflow |
| Using an AI-powered feature for substantive task work | Not allowed | The feature cannot make meaningful task decisions or create the deliverable |
| Using ordinary built-in functionality that is not presented as AI | May be allowed | It must involve no prompting, conversation, generation, or summarization |
| Running software that contains an AI or ML component | Conditionally allowed | It must be part of normal software validation and cannot act as an assistant that completes the task |

**When an AI feature is built in**

There may be cases where part of the workflow has a feature which uses AI/ML to perform part of the task work- for example, Photoshop subject identification may have AI tooling.

How to handle:

- If the feature is not presented as AI, involves no prompting/generative AI, and only performs incidental quality cleanup rather than substantive task work, it may be acceptable.
- For SWE tasks, writers may use code that includes an AI/ML component (such as building foundation models). Running the code may be acceptable only if it is part of normal SWE validation and not being used as an external assistant to complete the task.

# App use

Unlisted apps and apps without prior approval are fine unless they are banned or restricted according to the list and rules in the [Writer Handbook](https://docs.google.com/document/d/1tOxjGqxhA6T49kXw9hrhwpEsk8ERaFOsB6gqZcrLAHg/edit?usp=sharing).

- Insightful (Workpuls) and Splashtop Streamer must stay in the background.
- Every listed app must contribute meaningfully to the deliverable. Copying text from one app into another doesn’t count.
- List web apps themselves (e.g., Google Docs), not the browser they run in. List the browser only when it’s used as an app in its own right.
- Don’t list the notes app used during setup unless it’s used in the task.

# Deliverables

You should open all of the files for each task and check everything is there. Websites visited only for research aren’t inputs. Don’t fail a task for leaving them out.

|   |   |   |
|---|---|---|
| **Deliverable file type** | **What it is** | **Naming convention** |
| **Inputs** | Any original starting files they prepared in advance. | ‘input 1’, ‘input 2’, etc. |
| **Intermediate Artifacts** | Any files downloaded during recording, intermediate deliverables, or work-in-progress artifacts created during the task. | ‘artifact 1’, ‘artifact 2’, etc. |
| **Final outputs** | The final product they produced. | ‘final output 1’, ‘final output 2’, etc. |

# AutoQC coverage (for reference)

AutoQC checks do not replace the current reviewer guidance or manual checklist. A green result is not a band 1 on its own.

Always review the AutoQC, and any disputes, when performing your review.

- **Item 1:** Checks the file name, template text left in, unnumbered Task Description steps, a Topology step with no LOOKUP/CREATE/MODIFY tag, or a Request under 70% similar to the TaskRecorder Goal. It does not compare apps.
- **Item 2:** Checks if a window covers about 25% or more of another for over 30 s. It does not check 6-30 s, or any cover over the window being worked in.
- **Item 3:** AutoQC checks for two of What, Where and Why on actions that change the document. It can pass narration with What and Why but not Where. Check Where coverage yourself.
- **Item 4:** AutoQC checks whether the recording matches the described task. Independently verify that every major action promised in the task appears in the recording.
- **Item 5:** Checks if the menu-bar clock does not show seconds.
- **Item 6:** advice only when no document stating the task is shown at the start.
- **Item 7:** intro length: retained in AutoQC for advisory feedback only. Never blocks approval and is not scored in the reviewer checklist.
- **Item 8:** Checks if there is typing over 25% of the video (35% for Coding and Content & Writing).
- **Item 9:** Checks silence duration: retained in AutoQC for advisory feedback only. Never blocks approval and is not scored in the reviewer checklist.
- **Item 10:** background-noise checks- but these do not replace the first-listen clarity test. Ensure the audio is clear.

    AutoQC also checks: That all files uploaded and readable, video length is 15:00-54:59, deliverable file names, final output saved during the recording, Dock visible at start and end, Accessibility Inspector running with its window hidden, TaskRecorder description and Used Apps, at least one UI element changed, mouse idle, banned apps, background-only apps (Insightful, Splashtop) in front for 10 s or more, limited-use apps over 20% of the video, and work on an unrecorded screen.

# Reviewer FAQ

## Probation

**How do probation audits work, and how many reviews can I complete?**

Reviews are audited in pairs. If both reviews in the first pair pass, you pass probation. If either review in the first pair fails, complete a second pair of audited reviews. Both reviews in the second pair must pass; if either fails, you fail probation. You may complete at most four reviews while awaiting audit feedback.

A clean review reaches the correct decision for the right reasons, catches the major issues and gives the writer clear instructions for any required fixes.

**Does “Approved (Probation)” mean I am personally on probation?**

That task label does not establish your personal reviewer status. Use your assessment outcome and the auditor’s confirmation. The current onboarding guide asks you to allow up to 48 hours before reporting that probation feedback has not arrived; this is a reporting guideline, not a guaranteed turnaround.

**My probation audit is delayed.**

The target is 48 hours, but audits can take longer. If your audit has been waiting for days or appears not to have reached the queue, tag @Maven in [#odin-reviewers-hub](https://mercor.enterprise.slack.com/archives/C0CA0DBEFU3) with the task links, submission dates and available results. Ask Maven to escalate the delayed or missing audit to an EPM. Keep follow-up in the same thread.

Stay within your approved allowance and the four-review probation limit while awaiting the result. The audit target is not a guaranteed completion time.

**What happens if I don't pass probation?**

If you don’t pass probation then you will be offered a writer contract to remain on the project.

**Are screening scores shared?**

Screening scores are not shared in order to keep the answers confidential. You can get feedback from your first few reviews on probation or through reaching out to your review lead / EPM.

## Payments

**What if I’m missing a payment or my payment is wrong?**

Keep your contract, applicable offer, dates, tracked hours and task/review links. For an expected payment or bonus still missing after two pay cycles, use the [Pay & Role Request Form](https://forms.gle/g3YJjsAecgMKYEuV6) with your @mercor.expert account; the stated response time is 2 business days.

To dispute hours that were removed, see [Disputes](https://talent.docs.mercor.com/policies/time-tracking-pay#disputes).

**Where can I see my pay?**

The Odin dashboard’s My pay page includes the reviewer quiz bonus and the October 23 payouts, with bonus status and a link to the original announcement. Use your invitation and the applicable offer to confirm eligibility; a dashboard entry does not replace those terms. The bonus may take up to two days to appear under normal circumstances. Please only submit a dispute form after this window, to give it time to display.

My pay shows hours and base pay recorded for each pay week, or an estimate if processing is incomplete. Bonuses show Paid, Processing or Not yet issued, with the original announcement linked. Processing remains until you receive the payment. Report missing or incorrect amounts through the payment query form above, not Slack comments or DMs.

**When will I get paid?**

Hourly pay is sent every Wednesday for the previous Saturday–Friday workweek, measured in India time.

Tier bonuses are normally paid the Wednesday after the corresponding hourly payment, although they may arrive earlier or with that payment. A tier bonus is the amount above the base hourly rate in your contract. Separately announced incentives follow their own payout terms.

It may take up to a week after the bonus earning period has **ended** for announced incentives to reflect in your account.

Complete the payout setup instructions provided with your offer. [Stripe](https://talent.docs.mercor.com/how-to/payments#setting-up-stripe) is the primary payment provider for ongoing contributors. [Wise](https://talent.docs.mercor.com/how-to/payments#setting-up-wise) is generally used for one-time payments, contributors who have not completed [Stripe](https://talent.docs.mercor.com/how-to/payments#setting-up-stripe) onboarding, or bank accounts in countries [Stripe](https://talent.docs.mercor.com/how-to/payments#setting-up-stripe) does not support.

First-payout verification may add 3–5 business days. Bank holidays, processing schedules and bank cutoffs may also delay settlement.

## Queues and claims

**Which review queue should I use?**

Clear My re-reviews first, then work from the top of the Prioritized Review Queue. If both are empty, you may use the regular Review Queue. Only independent reviewers who are not on probation should take idea reviews; these are found under Needs Review in Full Workflow.

**Where is the Claim button?**

Open the task and scroll to the bottom of the left-hand panel. Scrolling the middle video panel will not reveal it.

**Why can’t I claim this task?**

Open the task and check its current status and claim availability. A queue entry does not guarantee that it is still available; another reviewer may have claimed it. Refresh and check your active claims. If the problem persists across eligible tasks, tag @Maven in [#odin-reviewers-hub](https://mercor.enterprise.slack.com/archives/C0CA0DBEFU3) with the task links, statuses and a screenshot, and ask for EPM escalation.

**Is 45 minutes a hard limit for each review?**

No. It is an average handling-time target. Complete the checks required for the assigned review path and track eligible time actually worked. Claim-extension and release instructions are separate; follow <u>Workflow</u> if you need longer to finish.

**Is a re-review reserved for me?**

Do not assume that a task you reviewed previously will return to you or be reserved for you. Check My re-reviews and the task’s current claim availability, then follow the published queue priority. A previous review does not guarantee that you can claim the next review.

**Can I write tasks when review queues are empty or re-reviews go elsewhere?**

Yes, when nothing is available to review, you may create and submit your own tasks without additional permission. A re-review going to someone else does not qualify if other review work is available. Check the queues and prioritize reviewing when work becomes available. Use the Reviewer timer while reviewing, as required from October 27, 2026 at 11:59 p.m. Pacific. Do not log writing time on the Reviewer timer.

You will be paid $100 + $2/minute for each task you write that reaches RFD. <u>Current claim timing and Quick Review access</u>

## Decisions and feedback

<u>Current checklist and exceptions</u>

<u>Feedback templates</u>

**My review matched the final decision. Why did I fail the audit?**

Auditors check your reasoning and feedback as well as the final decision. A review can fail if it misses a major issue, bases the decision on incorrect reasoning, or does not tell the writer what to fix. For required fixes, identify the issue, include a timestamp where relevant, and explain the change needed. Minor misses alone do not fail an audit, and extra feedback on nonblocking issues is allowed. Keep the complete feedback in the writer-facing Studio field so the writer and auditor can review it.

**Why are my review fields or decision buttons unavailable?**

Check the task, world, current status and whether your claim is still active. Preserve your review notes. Tag @Maven in [#odin-reviewers-hub](https://mercor.enterprise.slack.com/archives/C0CA0DBEFU3) with the exact error, task link and screenshot, and ask for EPM escalation if the problem remains unresolved. An unavailable button alone does not identify the cause.

**How do checklist bands differ from Writer Quality Score?**

Checklist 1 is ideal, 2 is within tolerance and 3 requires edits unless an explicit exception applies. For a full review, Writer Quality Scores 3–5 are approvable and 1–2 mean edits. A quality score of 3 is therefore different from checklist band 3. On re-review, score the current evidence rather than retaining ratings for corrected issues.

**What narration is acceptable?**

At least 70% of actions must explain what and where; why is optional for the acceptable band. Assess clarity separately at normal playback. An AutoQC pass can miss missing Where coverage. See <u>Standards</u> for the action definition and full criteria.

**Is mouse inactivity a reason to send back?**

Mouse inactivity alone is not a scored failure or a reason to reject, send back or require re-recording. Record useful timestamps and context in Internal Notes. The closing epilogue may be still. Separate typing and narration requirements continue to apply.

**How much feedback should I write?**

Write enough specific, timestamped feedback for the writer to fix every required issue. One or two sentences is not a hard limit. Separate required changes from growth notes. Save the full feedback in the writer-facing Studio field and send the writer a Slack DM. Both are required; keep the outcome, required fixes and timestamps consistent.

**Do intro length, silence duration or click pacing require edits?**

No, not on their own. These are no longer scored in the reviewer checklist. Intro-length and silence-duration findings remain in AutoQC but never block approval. Keep feedback advisory: the writer targets remain an intro under 20 seconds, silent gaps of 45 seconds or less and deliberate clicks with a pause of about 1 second. Assess narration coverage and first-listen clarity under the remaining checklist items.

**Does an epilogue longer than four minutes require edits?**

No. An epilogue over 4:00 or lacking detail is band 2 (nonfailing). Give improvement feedback where useful; do not send back or require re-recording for that alone. A missing epilogue uses the unscored “Missing epilogue — does not block approval” response.

## Files you cannot open

**What if I cannot open a deliverable on my computer?**

The files still need to be opened and checked against the recording. Seek help from a reviewer with a compatible setup who can verify that format; do not skip the file check.

## Copy/paste

**Is copy/paste allowed to reduce typing?**

Yes, alongside small typed additions and explanations that demonstrate the writer’s analysis. For example, a pre-made table can be filled in and explained as the problem is solved. Pasting alone should not replace the analysis.

## Task statuses

**What does RFD mean?**

Ready for Delivery: the task has passed every required check and is final for delivery. RFD - Minor is a different status and is not final approval; see the next question.

**What do RFD – Minor and "Under Quality Review" mean?**

Both are quality re-review statuses for tasks that were sent back: RFD - Minor for minor issues and Under Quality Review for larger ones. Neither is final approval, and neither waives any requirement. The re-review checks every requirement again. If the task passes, it moves to Ready for Delivery; if not, it is sent back for fixes or archived. Mouse-inactivity findings are recorded as delivery callouts, not reasons to send back on their own.

## Review limits

**What happens to tasks already at or beyond four reviews when the cap takes effect?**

The four-review cap takes effect October 27, 2026 at 11:59 p.m. Pacific.

Tasks already at or beyond the cap may receive one final review if the writer submits the final revision by that cutoff. A final revision submitted by the cutoff remains eligible for that review even if it is still waiting in the queue after the deadline; approval does not need to happen before the cutoff.

If that final review still requires changes from the writer, reject the task rather than sending it back again.

## Account sync or onboarding problems

**Can Maven in Slack tell me my Odin role?**

No. The Maven that responds in Odin Slack channels does not have live access to Studio and cannot see your Mercor dashboard, so it cannot confirm your current role. Ask an EPM to check your role on Studio.

To see the role you should have, go to [work.mercor.com](https://work.mercor.com) → Home → Contracts and check what it says for Odin.

Check the hour allowance shown in Insightful and ask an EPM to check your role on Studio. Use the [Pay & Role Request Form](https://forms.gle/g3YJjsAecgMKYEuV6) to report discrepancies between your expected role, hour cap or Studio access. Describe your Odin contract, Insightful allowance, the Studio role confirmed by the EPM and any blocked step. Any reported hour-cap discrepancy must also be escalated to an EPM.

**My reviewer role, hour cap or access is still wrong.**

Follow the checks above: check your Odin contract and Insightful hour allowance, and ask an EPM to check your role on Studio. Use the [Pay & Role Request Form](https://forms.gle/g3YJjsAecgMKYEuV6) to report a discrepancy in your expected role, hour cap or Studio access, and describe what is preventing you from working. Any reported hour-cap discrepancy must also be escalated to an EPM. Follow your confirmed work permissions and allowance while awaiting an update. Submitting the form does not itself change your role, grant access or increase your hours.

**The assessment glitched or the next part is locked. What should I do?**

There are no assessment retakes. Complete all parts of your assigned assessment; continuing to the next assigned part is not a retake. A blocked or missing next step does not by itself mean you failed. Reporting a technical issue does not authorize a retake or change your result. The team is looking into these assessment issues and is taking note of the technical issues raised.

**What if Insightful is not tracking correctly?**

For ordinary hourly work, pause while accurate tracking is broken. Tag @Maven in [#odin-reviewers-hub](https://mercor.enterprise.slack.com/archives/C0CA0DBEFU3) with the exact error, affected time and a redacted screenshot, and ask for EPM escalation if unresolved. A broken timer is different from an exhausted allowance.

## Wrong review decision

**What if a task received the wrong decision?**

If a task received the wrong review decision, post in [#odin-reviewers-hub](https://mercor.enterprise.slack.com/archives/C0CA0DBEFU3) and tag @Maven. Include the task URL, current decision, requested decision and reason. Ask Maven to escalate to an EPM if the decision needs to be corrected.

If the correction requires a send-back, include specific writer-facing feedback and relevant timestamps. If the task is reassigned to you, add that feedback before sending it back. Attach corrected files when requesting a file replacement.

# Reviewer setup & access

**Where do I start as a new reviewer?**

Start with this guide, and complete the reviewer onboarding in the [Odin dashboard](https://odin-mercor1.vercel.app/). Choose the correct route for a new hire or promoted writer. The live onboarding session is optional. Sessions run on weekdays only and alternate between 10:00 am PT and 4:00 am PT. Join from the link for your date:

- [Friday, Oct 30 — 10:00 am PT](https://meet.google.com/hes-pdnc-xug)
- [Monday, Nov 2 — 4:00 am PT](https://meet.google.com/wnf-hvsy-vng)
- [Tuesday, Nov 3 — 10:00 am PT](https://meet.google.com/hes-pdnc-xug)
- [Wednesday, Nov 4 — 4:00 am PT](https://meet.google.com/wnf-hvsy-vng)
- [Thursday, Nov 5 — 10:00 am PT](https://meet.google.com/hes-pdnc-xug)
- [Friday, Nov 6 — 4:00 am PT](https://meet.google.com/wnf-hvsy-vng)
- [Monday, Nov 9 — 10:00 am PT](https://meet.google.com/hes-pdnc-xug)
- [Tuesday, Nov 10 — 4:00 am PT](https://meet.google.com/wnf-hvsy-vng)
- [Wednesday, Nov 11 — 10:00 am PT](https://meet.google.com/hes-pdnc-xug)
- [Thursday, Nov 12 — 4:00 am PT](https://meet.google.com/wnf-hvsy-vng)
- [Friday, Nov 13 — 10:00 am PT](https://meet.google.com/hes-pdnc-xug)

**What do I need to complete before reviewing?**

Complete the required training and all parts of your assigned assessment. Promoted writers with first-pass approvals on four of their last five tasks are exempt from the assessment. The assessment includes two mock reviews and a narration check, assessed together. Follow your confirmed assessment outcome and work permissions. A role offer, task label or hour balance does not by itself establish that you may review independently.

**Do I need a Mac to review tasks?**

Reviews run in Studio through your browser on Mac or Windows. Recording tasks requires a physical Mac (Apple silicon or Intel) running macOS 15 or newer. Reviewers may write when no review work is available under the arrangement in [Role & Pay](#onboarding-steps); an approved switch to Writer is not required for that arrangement.

**I passed the quiz but cannot see the reviewer queue. What should I do?**

The team is looking into provisioning issues affecting reviewers who have passed the assessment but cannot yet see the reviewer queue.

**Why do the guidelines or onboarding links say “Access denied”?**

Open them in a browser signed in to Google with your @mercor.expert account. A personal Google account can trigger organization or permission restrictions.

**Can I retake a quiz or see the individual answers?**

There are no assessment retakes, and individual answers are not shared.

**Are promoted writers exempt from the assessment?**

Promoted writers with first-pass approvals on four of their last five tasks are exempt. Being offered a reviewer role alone does not establish that you meet this exemption.

**What happens after a final failed assessment?**

Stop reviewing. If you want to request a switch to Writer, use the [Pay & Role Request Form](https://forms.gle/g3YJjsAecgMKYEuV6) . Writer work requires confirmation of the role, terms and access, along with a supported Mac. To leave the project, ask Maven in [work.mercor.com](https://work.mercor.com) > Maven and ask to be offboarded from Odin.

## Incorrect caps or access

**What should I do when the initial hour cap blocks me?**

Check your Odin contract in [work.mercor.com](https://work.mercor.com) → Home → Contracts and the hour allowance shown in Insightful. Report an hour-cap discrepancy using the [Pay & Role Request Form](https://forms.gle/g3YJjsAecgMKYEuV6) and escalate it to an EPM.

# Example Tasks

🎯 **After this phase, you will:**

**•** Understand what a bad task looks like, and why

**•** Understand what a good task looks like, and why

## What makes a good vs. a bad task

|   |   |
|---|---|
| ✅ **Good task** | ❌ **Bad task** |
| Completes the approved goal and workflow, produces the required deliverables and verifies the result. Complexity and professional-level sophistication are not scored. | Has repetitive steps that add nothing to the workflow. |
| Has no set-up issues (menubar is visible with the seconds, accessibility inspector has a dot underneath it and TaskRecorder is prefilled with the goal and the task apps) | Set-up is incomplete/absent |
| Task length is within the 15 minute and 54:59 minute threshold | Task length is either lower than the 15 minute threshold or over the 54:59 minute threshold |
| Does not contain any PII | Contains disallowed identifying information, such as private contact or account details. Apply the privacy guidance’s exceptions for names and public information. |
| App use complies with the current categories, use limits and applicable in-flight protections. | App use violates a current requirement and is not covered by an applicable in-flight protection. |
| AI is not used during the recording. Inputs may be prepared with AI before recording if that preparation is disclosed. | The writer uses AI during their recording/ interacts with AI prompts such as ‘Ask me anything’. |
| Has all the 4 files including the Metadata.rtf file, video.mp4 file, recording\_TIMESTAMP.zip and the deliverables.zip | Is missing one or all the files required to review the task. |
| The deliverables.zip contains all the files including the input file, artifacts and final outputs. | The deliverables.zip is missing the final output |
| Bottom Dock is acceptable when at least one UI element has been changed | Bottom Dock with no UI element changed; the issue is missing UI diversity, not Dock position. |
| Has at least one UI element changed apart from the position of the dock, such as the wallpaper, resolution, the mode or the color of the icons. | No UI change apart from the position of the dock. |
| Working windows remain readable and unnecessary overlaps are minimized. | An unused window covers more than 25% of another for over 30 seconds |
| The cursor naturally guides the viewer. The closing epilogue may be still. | The cursor sits still for long stretches outside the epilogue (a timestamped callout, not a send-back on its own). |
| Typing is ≤25% for a non-coding and non-Content & Writing task and ≤35% for a Coding / Content & Writing task | Typing is >25% for a non-coding and non-Content & Writing task and >35% for a Coding / Content & Writing task |
| At least 70% of actions say what is done and where it is on screen; why is added when useful. Narration can be followed on first listen. Silence duration is advisory and never blocks approval. | Fewer than 70% of actions explain what is done and where it is on screen. Vague words such as ‘this’ and ‘here’ do not identify the element or its location. |
| Mercor Studio and Insightful stay off screen. Mentions of Mercor or Project Odin are fine. | Mercor Studio or Insightful is visible on screen. |

# ❌Bad Example❌

Use the Bad Example to study Project Odin quality guideline violations.

1. Data Science and Analytics

Task Description

As a data scientist who is compiling information to help guide decision making for the upcoming state election in Victoria, I have been tasked with presenting specific demographic data to decision makers. As part of this I need to prefer data for age demogramphics for a regional town area (Ararat, VIC) against overall state averages to be used in a future presentation.

I will use Firefox to obtain the data for the publicly available census 2026 data that can be commercial planning, market research, and strategy and download as a CSV file. I will then load the data into Google Sheets to analyse the data and create a plot of the data in a comparison format between the community and state. I will then print the data to pdf to be used as required, and open it in preview to show that the print worked. Apps Used

Firefox

Google Sheets

Video: [Full task recording](https://drive.google.com/file/d/1urN8CdMfuahC6cgA50YVVosaWDYKd6_d/view?usp=sharing) (16:41)

![](images/p059_1.png)

> *Text shown in the image:* Example frame from a recording: Firefox “New Tab” page with the TaskRecorder window open in front (Status: Recording… · Stop Recording). Task Description: “Obtain demographics data for the LGA of Ararat in Western Victoria. Find the age demographics data within this informaiton and create a table of this in Google Sheets. Then compare this table against the census data online to show the table has been correctly produced”. Used Apps: Google Sheets · Firefox.

|   |   |   |   |
|---|---|---|---|
| **Checklist item** | **1 = Ideal state** | **2 = Within acceptable tolerance** | **3 = Failing tolerance** |
| 1. Metadata.rtf matches the TaskRecorder Goal (apps, workflow) | Yes |   |   |
| 2. No unused window covers >25% of another for >6 s | Not scored in this example |   |   |
| 3. Narration says what and where for each action, and why when useful | Not scored in this example |   |   |
| 4. Screen recording shows the workflow described in the task | Not scored in this example |   |   |
| 5. The menu bar clock shows seconds at the start and end of the video | Yes |   |   |
| 6. The Goal document is shown at the start of the recording |   |   | No |
| 8. Typing takes up 25% of the video or less (35% for Coding / Content & Writing) | Yes, about 20% of the task |   |   |
| 10. The narration can be understood on first listen | Yes, no background noise |   |   |
| 12. The recording is free of disallowed AI use | Yes |   |   |
| 13. The recording is free of PII, on screen and in the audio | Yes |   |   |
| 14. Deliverable assets meet licensing requirements | Yes |   |   |
| 15. The narration and everything on screen are free of profanity | Yes |   |   |
| 16. Narration and deliverables are in English; minor non-English content on screen is acceptable | Yes |   |   |
| 17. Epilogue narration (over 4:00 is nonfailing) | Not scored in this example |   |   |

Verdict: send back. Item 6 (Goal document not shown) is at band 3. Click pacing is no longer scored and does not support this send-back. The original example also recorded app-use and submission-confirmation concerns. Assess app-use concerns under the current rules and applicable in-flight protections; an old restricted label alone does not establish a failure. “Not scored in this example” means the original example did not record a score for that item.

# 🏅Golden Examples🏅

Use the Golden Examples to study professional workflow and narration standards.

- [Finance](#golden-examples)
- Design
- Audio & Music
- Animation & VFX
- Software & AI/ML Engineering

[**1. Finance**](https://drive.google.com/file/d/1TOANq_bwgQ_Qyti7PL2R86mR1xAgctUP/view?usp=sharing)

Task Description

I am an Account Receivable personnel at a company in the UK and have been tasked with adding a new vendor to our ERP system and creating a Purchase Order (PO) tracking workflow for our Accounting team to manage POs better. I will begin by adding missing information onto a sample PO on the Pages app, then transfer the vendor details, and PO line items onto our ERP system on Microsoft Dynamics 365 Business Central, and finally create a PO tracking workflow on Monday.com. I will verify the flow is complete by running the same at the end of its creation and check if the status updates as per the trigger, and deliver the final PO raised on Microsoft Dynamics 365 Business Central and the PO workflow from Monday.com to my team. Apps Used

Monday.com

Microsoft Dynamics 365 Business Central

Pages

Video: [Full task recording](https://drive.google.com/file/d/1TOANq_bwgQ_Qyti7PL2R86mR1xAgctUP/view?usp=sharing) (44:19)

![](images/p063_1.png)

> *Text shown in the image:* Screenshot of Firefox with the monday.com “PO Tracker” board (groups “PO Pending” and “PO Payment Received”, columns PO number, Person, Status, PO raised, Due date).

[**2. Design**](https://drive.google.com/file/d/10HcP0usXgrPBP4AdVLBUNdjpONvHc_Iq/view?usp=sharing)

Task Description

I am a Content Creator preparing aspects of a new podcast. Using OBS Studio, I will setup different scenes for different aspects of the podcast such as pre-show and screen-share, which will involve the import of some images. The final deliverables will be the export of the scenes created in OBS.

Apps Used

OBS Studio

Video: [Full task recording](https://drive.google.com/file/d/10HcP0usXgrPBP4AdVLBUNdjpONvHc_Iq/view?usp=sharing) (24:44)

![](images/p064_1.png)

> *Text shown in the image:* Screenshot of OBS Studio (Scenes: Logo 1, Pre-Show, Screen Capture, Post Show) previewing a “we will begin shortly” Word Retreat slide.

[**3. Audio & Music**](https://drive.google.com/file/d/18aeXVN8jy6rAIQPv_BMUByg53KDnnSrq/view?usp=sharing)

Task Description

I am a film score composer and I’m working on the underlying theme for a heroic end credit sequence. I will use Logic Pro in the second phase (P2) of the execution to compose a string accompaniment for the piano top melody created in phase one (PI). I will also establish a chordal sequence (I - vi - IV - V) to define the passage. The final deliverable will be a stereo export of the complete Logic Pro session.

Apps Used

Logic Pro

Video: [Full task recording](https://drive.google.com/file/d/18aeXVN8jy6rAIQPv_BMUByg53KDnnSrq/view?usp=sharing) (22:58)

![](images/p065_1.png)

> *Text shown in the image:* Screenshot of Logic Pro Piano Roll (Hero – Piano Roll) with MIDI notes, Time Quantize, Strength, Swing, Scale Quantize and Velocity controls.

[**4. Animation & VFX**](https://drive.google.com/file/d/1wVBfJCTIAPJHJ6w3hoVHnZxSk-ujKYLA/view?usp=drive_link)

Task Description

You are a 3D Modeler tasked with cleaning up the textures of a photogrammetry model for use in Unreal Engine. Use Adobe Substance 3D Painter to bake the provided high poly model onto the provided low poly model, apply the provided photogrammetry diffuse texture, clean up artifacts on the texture, add a powdery finish to the popcorn and add red and white striped packaging textures to the popcorn box. Export the texture maps appropriate for use in Unreal Engine.

Apps Used

Substance 3D Painter

Video: [Full task recording](https://drive.google.com/file/d/1wVBfJCTIAPJHJ6w3hoVHnZxSk-ujKYLA/view?usp=drive_link) (40:59)

![](images/p066_1.png)

> *Text shown in the image:* Screenshot of Adobe Substance 3D Painter (Untitled) with a 3D popcorn bucket, texture set list, layers and Properties – Fill panel.

[**5. Software & AI/ML Engineering**](https://drive.google.com/file/d/14Fgj-2mtxKmCXIMiGnUT57EElc5rnjec/view?usp=drive_link)

Task Description

As an iOS app developer I want to create a distinctive visual identity for a simple Music Player app. Use SF Symbols as independent visual components, and compose them as separate layers in Icon Composer. Build & refine the multi-layered icon in Icon Composer and integrate the resulting icon into a SwiftUI Music Player app in Xcode. Deliver the layered icon and Xcode project; verify that the app builds successfully and the icon is correctly integrated. Apps Used

Device Hub

Xcode

SF Symbols

Icon Composer

Video: [Full task recording](https://drive.google.com/file/d/14Fgj-2mtxKmCXIMiGnUT57EElc5rnjec/view?usp=drive_link) (28:37)

![](images/p067_1.png)

> *Text shown in the image:* Screenshot of Icon Composer with a yellow background, a blue music-play icon, layer tree (Group / play.00) with a context menu, and the Fill/Layer inspector on the right.

# Feedback Templates

🎯 **After this phase, you will:**

**•** Have a catalogue of templates to use to help communicate with writers!

# Templates

In the following tabs, you will find templates for DM communication with writers. Here’s a list of what you will find.

## General Feedback

- Detailed templates for general writer feedback

## Setup and TaskRecorder

- Metadata.rtf corrected by reviewer
- Menu bar clock shows seconds
- Dock visibility at start and end: advisory feedback, not a standalone failure
- Bottom Dock is nonblocking with at least 1 UI change
- Accessibility Inspector running (dot under Dock icon)
- Accessibility Inspector window hidden
- TaskRecorder window minimized: advisory feedback, not a standalone failure
- TaskRecorder description and apps: file fix; preserve original and corrected descriptions in Internal Notes, no rerecord for this alone
- Task description document shown at start
- Intro length: advisory feedback only; never blocks approval
- At least 1 UI element changed
- English narration and deliverables; minor non-English content on screen is acceptable

## Content and compliance

- Free of disallowed AI use: ordinary incidental enhancement may be acceptable; substantive AI task tools are not automatically allowed. Follow the detailed AI guidance and escalate unclear cases.
- Free of PII (screen and audio)
- Project references alone are allowed; Mercor Studio, Insightful and Odin Slack on screen require edits. Assess personal information separately.
- Deliverable assets meet licensing requirements: apply documented exceptions
- Profanity: apply the minor on-screen exception; assess explicit content separately
- Current banned-app, limited-use and app-specific rules followed
- Task complexity and professional-level sophistication are not scored
- Task checklist and PII confirmation completed truthfully

## Performance

- Narration must be understandable on first listen; speed alone has no words-per-minute failure threshold
- Silence duration: advisory feedback only; never blocks approval
- Narration audio clear (loud typing OK if narration stays clear)
- Typing 25% or less (35% or less for Coding / Content & Writing); equality does not fail
- Click pacing: advisory feedback only; not scored

## AutoQC

- Disputes (agree)
- Disputes (disagree)
- Not run

## Files

- All four task files uploaded
- Task Recorder zip contents complete, screenshots present
- video.mp4 opens
- Deliverables named correctly
- Metadata.rtf matches the task (apps, request, workflow)

## Recording

- Video: writer target 15:00-50:59; reviewer acceptance 15:00-54:59
- Keep the content being worked on visible; minor overlap alone is not an error
- Mouse inactivity: qualitative delivery callouts only, not graded; the closing epilogue may be still
- Narration: What and Where, with Why where useful
- Recording shows the writer doing what the task description says

# Odin Reviewer Feedback Templates

**Header line for every review:**

MM/DD @ HH:MM TIMEZONE, Review #\_\_\_, REVIEWER NAME

Writing rules for every snippet:

- Give a timestamp (MM:SS) for anything seen in the video.
- Say what was wrong, why the client needs it, and what to do next time.
- Use the current status names: Needs Edits and Rejected (not "Needs Revision").
- Point to the Writer Guidelines section by name when it helps.

**Approved (all items at 1)**

Use when every current manual item and AutoQC requirement passes. Delete any line that does not apply to this task.

MM/DD @ HH:MM TIMEZONE, Review #\_\_\_, REVIEWER NAME

Comments: Task approved. Clear narration identifies the action, specific element and screen location, with Why where useful. Setup, Goal document, Metadata.rtf, app-use rules, privacy, licensing, profanity, English, window management and typing checked against the applicable checklist. Video length, screenshot count, original recording ZIP, video.mp4 and deliverables.zip verified. The task is complete with its required final deliverable. Reviewer: delete any statement you did not verify; use only the checks required for the review path.

**Approved with growth notes (no blocking failure)**

Use when the task passes, but one or more items are within tolerance. Paste the matching snippets under Areas to grow. Do not include band numbers in writer-facing feedback. MM/DD @ HH:MM TIMEZONE, Review #\_\_\_, REVIEWER NAME

Hi \_\_\_,

I've approved task \_\_\_. You did a strong job on \_\_\_.

Areas to grow for your next tasks:

\- \[paste snippet\]

\- \[paste snippet\]

None of these blocked approval this time, but items at the edge of tolerance can fail on a future task. The Workflow Checklist in the Writer Guidelines covers each one. Keep up the great work!

**Needs Edits (a current blocking item fails)**

Use when at least one current blocking item fails but can be fixed within the approved idea. Split required writer fixes into recording and file fixes. Reviewers correct and verify Metadata.rtf themselves; a fixable metadata issue alone does not require a writer send-back or rerecord. MM/DD @ HH:MM TIMEZONE, Review #\_\_\_, REVIEWER NAME

Hi \_\_\_,

I've completed my review of task \_\_\_. You did a good job on \_\_\_, but the items below need to be fixed before I can approve it.

Requires a re-record:

\- \[paste snippet\]

File fixes (the reviewer handles fixable Metadata.rtf errors):

\- \[paste snippet\]

Growth notes (did not block approval):

\- \[paste snippet\]

Please run full AutoQC again after changes before resubmitting, and use the Workflow Checklist in the Writer Handbook. Address every required fix together. Approval depends on the completed review; the next submission is not guaranteed approval. For a brief video with further details, see [here](https://www.loom.com/share/5c1438d9ec6b4d10aa3c332195c3658a).

**Rejected (Invalid Task Idea)**

Rejected is for a task whose concept cannot be fixed within the approved scope. A correctable app-use violation, a recording that does not match the approved workflow, or several failures together does not automatically make the task Rejected. If the task can be corrected within the approved idea, use Needs Edits. If you are unsure whether the task description is valid, explain the issue in writer-facing Studio feedback and Send for Edits instead. Apply the separate review-attempt cap and transition policy. Pick only a reason that makes the task concept unfixable and delete the others.

MM/DD @ HH:MM TIMEZONE, Review #\_\_\_, REVIEWER NAME

Hi \_\_\_,

I've completed my review of task \_\_\_. Unfortunately, this task cannot be approved or fixed through edits, for the reason below. Please do not resubmit this rejected task. - Unfixable app-policy conflict: The approved task cannot be completed without \_\_\_, which is prohibited by the current app policy: \_\_\_. Check the canonical app list, app-specific conditions and in-flight protections. If the violation can be corrected within the approved idea, use Needs Edits instead. Unlisted apps and missing prior app approval do not fail by themselves.

\- Task concept: The approved workflow doesn't seem like it can be completed without \[excessive typing /exceeding the allotted timeframe\], so no re-record of this idea would meet the requirements.

\- Do not select task complexity or lack of professional-level sophistication as a rejection reason. These restrictions are retired; assess whether the approved task and its required deliverables are complete.

\- Unfixable task concept: \_\_\_ cannot be corrected within the approved idea because \_\_\_. A recording that differs from the approved idea is not, by itself, an unfixable concept; use Needs Edits when a compliant recording of the approved workflow is possible.

For your next task, propose an idea in Studio and follow the current Task Ideation and app-use guidance in the Writer Guidelines. For a brief video with further details, see [here](https://www.loom.com/share/0294daa93bc448eda40f4f23645785cc). I look forward to your next submission.

# Setup and TaskRecorder

**Metadata.rtf corrected by reviewer:**

**file fix; do not send back for metadata alone**

Metadata.rtf - I corrected Metadata.rtf to match the actual task and verified the separately uploaded corrected file. No writer action is needed for this metadata correction. Reviewer: use this message only after making and verifying the correction. Preserve the original recording ZIP; retain both the original and corrected task descriptions in Internal Notes. Attach corrected Metadata.rtf separately. Do not send back or require a rerecord for fixable metadata alone. Every delivery uses a new folder; do not add files to an already-delivered folder.

**Menu bar clock shows seconds**

Clock seconds - The menu bar clock does not show seconds at \[the start / the end\] of the recording. Go to System Settings > Menu Bar > Clock Options and turn on "Display the time with seconds," then re-record. For a brief video with further details, see [here](https://www.loom.com/share/6b4e4737f1d745048a60b1a937927964). Reviewer: check the first and last few seconds; visibility between those points is not required.

**Dock visibility at start and end: advisory feedback, not a standalone failure** Dock visibility - For future recordings, keep the Dock visible at the beginning and end. Reviewer: this retired checklist item is advisory only; missing Dock visibility alone is not a send-back reason. Assess required recording data separately.

**Dock position and UI diversity**

Dock position - A bottom Dock alone must not trigger a send-back when at least one UI element has been changed. **Do not request re-recording solely to move the Dock in that case.**

**Accessibility Inspector running (dot under Dock icon)**

Accessibility Inspector - Accessibility Inspector wasn't running during the recording (no dot under its Dock icon). TaskRecorder needs it running for the whole recording to capture the required data. Open it from Xcode > Open Developer Tool, close only its window with the red button, and confirm the dot stays under its icon. For a brief video with further details, see [here](https://www.loom.com/share/6b4e4737f1d745048a60b1a937927964).

**Accessibility Inspector window hidden**

Accessibility Inspector window - The Accessibility Inspector window was visible at MM:SS. Close its window with the red button before recording (don't minimize or quit the app) so it keeps running in the background. For a brief video with further details, see [here](https://www.loom.com/share/6b4e4737f1d745048a60b1a937927964).

**TaskRecorder window minimized: advisory feedback, not a standalone failure**

TaskRecorder window - For future recordings, minimize the TaskRecorder window after starting and reopen it when ready to stop. Reviewer: this retired checklist item is advisory only; the window appearing during the task does not fail the task on its own. Assess any separate current checklist issue under its own rule.

**TaskRecorder description and apps: file fix; preserve original and corrected descriptions in Internal Notes, no rerecord for this alone**

TaskRecorder fields - The TaskRecorder Task Description/Used Apps did not match the recording: \_\_\_. Reviewer: retain both the original and corrected descriptions in Internal Notes, correct Metadata.rtf and any editable Studio fields to match the actual recording and deliverables, and verify the separately attached corrected file. Preserve the original recording ZIP. This mismatch alone does not require a rerecord. For future recordings, check the Goal and app list before clicking Start Recording. For a brief video with further details, see [here](https://www.loom.com/share/efdd9afbedde42889ff81333b39d822b).

**Task description document shown at start**

Opening Task Description Document - The Goal document wasn't shown at the start of the recording. After starting, minimize TaskRecorder so the Goal document is visible, say the intro sentence, then minimize the document. Use Word, Google Docs or another allowed app (not Notes or TextEdit), and show only the Goal, not the Approval ID. For a brief video with further details, see [here](https://www.loom.com/share/6b4e4737f1d745048a60b1a937927964).

**Intro length: advisory feedback only; never blocks approval** Intro length - Your intro ran about \_\_ seconds. For future tasks, say only “I will be beginning my task soon. Here is the workflow I have in mind,” minimize the Goal document, and begin. Aim for under 20 seconds. Reviewer note: this is advisory feedback only. Intro duration never blocks approval or requires a rerecord on its own, including when AutoQC flags it.

**At least 1 UI element changed**

UI diversity - The desktop uses the default Mac setup. Please change at least one UI element before recording, such as the wallpaper, light/dark mode, Dock size or resolution, and enter it in Studio's Machine and Display fields. For a brief video with further details, see [here](https://www.loom.com/share/efdd9afbedde42889ff81333b39d822b).

**English narration and deliverables; minor non-English content on screen is acceptable**

Language - At MM:SS, \[the narration was not fully in English / the deliverable \_\_\_ was not in English / there was more than a minor amount of non-English content on screen\]. Keep narration fully in English and deliverables in English. Reviewer: minor amounts of non-English content on screen are acceptable; do not request edits for that alone.

# Content and compliance

**Free of disallowed AI use: ordinary incidental enhancement may be acceptable; substantive AI task tools are not automatically allowed. Follow the detailed AI guidance and escalate unclear cases.**

AI use - \[Tool/feature\] was used to \[prompt / generate / summarize\] at MM:SS. No AI interaction is allowed during recording, including Google AI Overview's "Ask anything" and AI Mode. Inputs may be prepared with Gemini before recording, with "AI-generated before recording" selected in Studio.

**Free of PII (screen and audio)**

PII - \_\_\_ was \[shown on screen / said aloud\] at MM:SS. Please re-record without private personally identifiable information, including names, emails, phone numbers, addresses, account details, biometrics and MAC addresses. TaskRecorder 2.4.4 requires no sign-in. For task-app logins, use your mercor.expert account or a new anonymized account as the current app guidance requires. For a brief video with further details, see [here](https://www.loom.com/share/2051a4ea76a5467db3684f5bb6e4a07b).

**Project screens: Mercor Studio, Insightful or Odin Slack**

Project screens - \[Mercor Studio / Insightful / Odin Slack\] was visible at MM:SS. Please re-record without it and close or hide project materials before recording. A separate Recorder macOS profile is optional. Reviewer: Mercor/Odin mentions alone are allowed; assess actual PII under the detailed privacy guidance.

**Deliverable assets meet licensing requirements: apply documented exceptions**

Copyright - \_\_\_ included in deliverables.zip at MM:SS does not meet the applicable licensing requirement: \_\_\_. Apply the asset-licensing requirement to material included in deliverables.zip. Browsing a website with a trademarked logo is acceptable. Apply the public-repository licensing exceptions in the PII and Copyright Issues guidance. For assets subject to the CC0/public-domain rule, verify the source terms; a search filter alone is not enough. Gemini-generated inputs prepared before recording are allowed. Escalate unclear licensing before deciding. For a brief video with further details, see [here](https://www.loom.com/share/2051a4ea76a5467db3684f5bb6e4a07b).

**Profanity: apply the minor on-screen exception; assess explicit content separately**

Profanity - Minor on-screen profanity not typed by the writer is within tolerance. Profanity said or typed by the writer, or more than minor on-screen profanity, fails. For a failure: \[Profanity was said / profanity was typed / more than minor on-screen profanity was shown\] at MM:SS; please re-record without it. Assess explicit content separately: if explicit content was shown at MM:SS, re-record without it.

**Current banned-app, limited-use and app-specific rules followed** App-policy issue - \_\_\_ was used at MM:SS in a way prohibited by the current banned-app, limited-use or app-specific guidance: \_\_\_. Check the canonical app list and in-flight protections. Unlisted apps and missing prior app approval do not fail by themselves. For a brief video with further details, see [here](https://www.loom.com/share/0294daa93bc448eda40f4f23645785cc).

**Task complexity and professional-level sophistication are not scored** Reviewer note - Do not request more complex work or reject a task for lacking professional-level sophistication. Those restrictions are retired. Assess whether the recording completes the approved task and required deliverables.

**Task checklist and PII confirmation completed truthfully**

Submission checklist - The checklist/PII confirmation was marked complete, but \_\_\_ (MM:SS) does not meet that item. Please open the checklist and PII guidelines and verify each item against your recording before checking the box. For a brief video with further details, see [here](https://www.loom.com/share/2b5433fd66384455ab013ebfa93719f0).

# Performance

**Narration understood on first listen**

Growth note: clear but rushed narration

Narration clarity - At MM:SS, \_\_\_. Keep your narration clear enough that the listener can follow the action on first listen. For a brief video with further details, see [here](https://www.loom.com/share/cfa11eb4802840b2bf5948164cce725f). Reviewer: pace alone is not a failure; assess whether noise, mumbling, pace or unclear speech prevents understanding. Failure: narration cannot be understood on first listen

Narration clarity - At MM:SS, \[noise / mumbling / pace / unclear speech\] makes the action difficult to understand without replaying or guessing. Please re-record so the narration clearly explains the action and its location. For a brief video with further details, see [here](https://www.loom.com/share/cfa11eb4802840b2bf5948164cce725f). Loud typing is fine if narration remains clear. Do not apply a words-per-minute cutoff.

**Silence duration: advisory feedback only; never blocks approval** Growth note only — do not score silence duration or require a rerecord for it. Narration gap - There was a \_\_-second silent gap at MM:SS. For future tasks, keep narrating while you work, even during typing or repeated steps, so no gap goes over 45 seconds.

**Audio clarity**

Use the first-listen clarity check

Audio quality - Background noise obscured the narration at MM:SS. For future tasks, record in a quieter space or use headphones with a dedicated microphone. For a brief video with further details, see [here](https://www.loom.com/share/efdd9afbedde42889ff81333b39d822b). Reviewer: use a growth note only if the video remains understandable on first listen.

Failure: unclear narration

Audio quality - Background noise made the narration unclear at MM:SS. Please re-record in a quieter space or use headphones with a dedicated microphone. Check the microphone level in TaskRecorder first, and do not switch audio devices during recording. For a brief video with further details, see [here](https://www.loom.com/share/efdd9afbedde42889ff81333b39d822b).

**Typing 25% or less (35% or less for Coding / Content & Writing); equality does not fail**

Typing - Typing took up about \_\_% of your \_\_-minute recording, over the limit of 25% (35% for Coding / Content & Writing). Exactly 25% or 35%, respectively, does not fail this item. Please re-record with a mouse-driven workflow that meets the total-typing limit. For future recordings, aim to keep each continuous typing segment to 45 seconds or less; exceeding that target alone is not a reviewer failure. If the idea cannot be completed within the total-typing limit, revise the task idea.

**Click pacing: advisory feedback only; not scored**

Growth note: occasional rushed clicks

Click pacing - A few clicks were rushed (MM:SS, MM:SS). For future tasks, pause about one second after each click so the result is captured.

Growth note: repeated rushed clicks

Click pacing - Clicks lacked a pause in several places (MM:SS, MM:SS, MM:SS). For future tasks, click, wait about a second, then continue. Missing click pauses alone do not justify send-back.

Growth note: rushed clicks throughout; not a standalone failure

Click pacing - Clicks lacked a pause throughout the recording (for example, MM:SS and MM:SS). For future tasks, pause about one second after each click so the result is captured. Missing click pauses alone do not justify send-back.

# AutoQC snippets

AutoQC ratings are separate from the three-band manual checklist. Ratings 1 and 2 need no snippet, though a short line for 2 shows the writer their dispute was read. For current blocking checks, ratings 3 (disputed, I disagree) and 4 (failed / not run) use the fail snippet; for a 3, start with the dispute line. Verify the evidence and the current rule. Intro-length and silence-duration AutoQC findings are always advisory and never block approval, regardless of the displayed rating; do not use a fail or rerecord snippet for those findings. Mouse inactivity is a timestamped delivery callout in Internal Notes, not a manual band. Window management follows the current manual checklist. Apply the total-typing limits. A continuous typing segment over the 45-second writer target does not fail by itself.

**Dispute lines:**

AutoQC dispute (agreed) - I reviewed your dispute on the \_\_\_ check and agree with you; it did not count against this task.

AutoQC dispute (not agreed) - I reviewed your dispute on the \_\_\_ check but confirmed the issue at MM:SS, so it still needs to be fixed:

**Not run:**

AutoQC not run - The \_\_\_ AutoQC wasn't run before submission. Please run both AutoQCs (Files & Recording and Narration) and resolve any blocking findings before resubmitting. For a brief video with further details, see [here](https://www.loom.com/share/5c1438d9ec6b4d10aa3c332195c3658a).

# Files and deliverables

(file fixes unless the recording itself is bad)

**All four task files uploaded**

Missing files - \_\_\_ is missing from Studio. Each task needs four uploads: video.mp4, deliverables.zip, the TaskRecorder recording\_TIMESTAMP.zip, and Metadata.rtf in its own field (not inside deliverables.zip). For a brief video with further details, see [here](https://www.loom.com/share/3268bc3d525a49aeb214cad408ae8f56).

**Task Recorder zip contents complete, screenshots present**

Recording archive - The TaskRecorder zip is \[missing files / has only \_\_ screenshots for a \_\_-second video, below 0.5 per second\]. This data is required by the client, so the task needs to be re-recorded. Before your next recording, quit unused apps and large browser tabs, keep enough free storage, and run a short test. Don't rename, unzip or edit the original archive. For a brief video with further details, see [here](https://www.loom.com/share/118e7ce2e7b44f799f4c092d28f0388a).

**video.mp4 opens**

Video file - video.mp4 \[won't open / ends early at MM:SS / is corrupted\]. Please check the beginning, middle and end in QuickTime before uploading. If the file is corrupted, the task needs to be re-recorded. For a brief video with further details, see [here](https://www.loom.com/share/118e7ce2e7b44f799f4c092d28f0388a).

**Deliverables named correctly**

Deliverable naming - Please name the zip "deliverables.zip" and label files inside it as input 1, artifact 1, final output 1, etc., keeping the correct extensions. Every input, intermediate artifact and final output needs to be in the zip. For a brief video with further details, see [here](https://www.loom.com/share/118e7ce2e7b44f799f4c092d28f0388a).

**Metadata.rtf matches the task (apps, request, workflow)**

Metadata.rtf - The \[Topology / Request / Task Description\] section does not match the recording: \_\_\_. For a brief video with further details, see [here](https://www.loom.com/share/b506e514af6143febfff1396f97d8668). Reviewer: retain the original and corrected task descriptions in Internal Notes, correct Metadata.rtf to accurately describe the recording and deliverables, and verify the separately uploaded corrected file. Topology should list each app visit in order as LOOKUP, CREATE or MODIFY. Preserve the original recording ZIP. Fixable metadata alone does not require a send-back or rerecord. Every delivery uses a new folder; do not add to an already-delivered folder.

# Recording

**Video: writer target 15:00-50:59; reviewer acceptance 15:00-54:59** Video length - Your video is \_\_:\_\_ long, outside the reviewer acceptance range of 15:00-54:59 including the intro and epilogue. Please adjust the workflow duration and re-record, planning for the writer target of 15:00-50:59. Do not request a re-record solely because a video exceeds 50:59 but is no longer than 54:59.

**Keep the content being worked on visible; minor overlap alone is not an error**

Window management - \[App 1\] obscured the content being worked on in \[App 2\] at MM:SS. Minor window overlap alone is not an error and does not require edits or a re-record. Please use one Fill window or place task windows side by side, and minimize windows you aren't using. Avoid Full Screen and small floating windows. Pop-ups within the same app are fine while in use.

**Mouse inactivity: qualitative delivery callouts only, not graded; the closing epilogue may be still**

Delivery callout: the cursor was inactive at MM:SS. Describe the observed duration and context without assigning a grade. Use the cursor naturally as a teaching pointer, without artificial movement. The closing epilogue may be still; an epilogue over 4:00 is nonfailing. The separate typing requirements still apply.

**Narration: What and Where, with Why where useful**

Narration - The narration needs to be clear enough that a listener could follow the task without seeing the screen. At MM:SS, MM:SS and MM:SS, \_\_\_. Name the action, specific element and screen location; avoid vague words like “here” and “this.” Add Why for important or non-obvious decisions. Reviewer: apply the current checklist for narration coverage and clarity. Silence duration never blocks approval; do not put bands or tolerance thresholds in the writer’s message. For a brief video with further details, see [here](https://www.loom.com/share/cfa11eb4802840b2bf5948164cce725f), and for golden examples, see [here](https://docs.google.com/document/d/1tOxjGqxhA6T49kXw9hrhwpEsk8ERaFOsB6gqZcrLAHg/edit?tab=t.4g0zgulqxcil#heading=h.h7xm13ec91ub)

**Recording shows the writer doing what the task description says** Workflow match - The recording doesn't complete the approved Goal: \_\_\_ \[was skipped / was replaced with \_\_\_\] at MM:SS. Please record the workflow as approved. If your plan changes materially, submit a change request in Studio before recording. For a brief video with further details, see [here](https://www.loom.com/share/354d3ef8fd4e4c869dfebc8f1093839f).
