# Project Odin Reviewer Checklist

## Workflow
1. Claim from the Review queue (max 2 at a time). Finish in one sitting, because claims auto-release after 3 hours of inactivity.
2. Check the Goal against the Task Description and metadata.
3. Watch at 1.5x with live captions on (Chrome Live Caption).
4. Check every AutoQC flag, major and minor. Confirm the real ones and dismiss the false ones.
5. Check deliverables, score the checklist, write feedback, and send the Slack DM.

If you find a critical issue, spend about 10 more minutes looking for other critical issues, then send back with everything listed. You don't need to finish the full review.

## Desktop setup (a miss on any of these is a send-back)
- [ ] The menu bar clock shows seconds.
- [ ] The Dock is on the left or right. A bottom Dock is banned, and the Dock must be visible at the start and end.
- [ ] Accessibility Inspector is running (dot under its icon) with its window hidden.
- [ ] At least one UI element is changed from default (wallpaper, dark mode, icon size, resolution). Dock position doesn't count. Cursor size and color must stay default.
- [ ] TaskRecorder is pre-filled with the correct Goal and apps, shown only at start and stop.
- [ ] The Goal document is shown at the start. The intro should be under 20 seconds, with the script "I will be beginning my task soon. Here is the workflow I have in mind."

## Narration (the #1 reason for send-backs)
- [ ] Each action covers what, where, and why. Pass if at least 70% of actions have 2 of the 3.
- [ ] Eyes-closed test passes. Watch for "this", "that", and "here".
- [ ] Silences are 45 seconds or less (46-60 is an edge case, over 60 fails).
- [ ] Audio is clear, with background noise under about 30%.
- [ ] Shortcuts are narrated with their keystrokes.
- [ ] The pace is not rushed. Pauses after clicks of 1 second or more are expected, but don't send back solely because pauses are under 1 second (the threshold is under review).

## Recording content
- [ ] **Length:** 15:00 to 54:59 total for reviewer acceptance. Don't reject for 51:00 to 54:59.
- [ ] **Typing:** 20% or less (about 30% for coding and content/writing).
- [ ] **Mouse idle:** 45 seconds or less, except in the epilogue.
- [ ] **Windows:** no unused window covers more than 25% of another for over 6 seconds (6-30 seconds is an edge case, over 30 fails).
- [ ] **Metadata.rtf:** not shown being filled out.
- [ ] **Language:** English only.
- [ ] **Complexity:** a non-expert couldn't do the task. A single-app task is fine, so don't ask for extra apps just to reach a count. A complexity send-back is for Review 1 only. On a resubmission, approve and note your concern in Internal Notes, unless you raised it in R1 and it wasn't fixed.

## Compliance
- [ ] **AI:** no prompting, chatting, AI Mode, or Google "Ask anything". Google AI Overview with no follow-up is an edge case. AI-powered tools doing real task work (e.g. Photoshop subject select) means request edits. Escalate unclear passive features.
- [ ] **PII:** no personal emails, real names with other identifying info, phone numbers, addresses, or account details. Fake names, example.com, and mercor.expert are fine.
- [ ] **Copyright:** CC0 or public domain only for what ends up in the deliverable. A visible watermark means reject unless it's CC0. Don't recommend websites unless you're 100% sure of their license.
- [ ] **Restricted apps:** check every app that appears on screen, even briefly. Use the live list at https://odin-mercor1.vercel.app/validated-apps, since older tables are historical. An unlisted app is not a failure by itself. If a restricted app is the only issue, don't approve or reject. Add an Internal Note, log the task ID in the tracking sheet, unclaim it, and contact an EPM.
- [ ] **Project references:** Mercor, Odin, and Studio on screen are tolerated in small amounts and shouldn't lead to rejection alone.
- [ ] **Profanity:** none in narration or typing.

## Metadata.rtf and deliverables
- [ ] The Goal, TaskRecorder description, and Request section all match.
- [ ] Topology uses only LOOKUP, CREATE, and MODIFY, in chronological order. Apps can repeat.
- [ ] Fix metadata errors yourself and re-upload. Never send back for metadata alone.
- [ ] If the recording differs from the listed app or description and the task is otherwise fine, note it in Internal Notes and approve.
- [ ] All 4 files are present: MP4, deliverables.zip, the TaskRecorder zip, and Metadata.rtf.
- [ ] deliverables.zip contains input N, artifact N, and final output N files. Research-only websites are not inputs. Rename files yourself if they're slightly off.
- [ ] Don't list a browser if it's only used to open web apps. List the web apps instead.

## Decision rules
- Scores 3-5 mean approve. Scores 1-2 mean Needs Edits.
- Send back if any critical issue fails, or if more than 3 major issues fail.
- **Critical issues:** narration fails, restricted app, PII, video doesn't match the Goal, desktop setup missed, task too simple (R1 only).
- **Fix and approve** for metadata errors, small naming problems, a slightly long intro, or overlap of 6-30 seconds as the only issue. Add a growth note.
- **Reject** only for an invalid task idea or when the recording does a different task than approved.
- **Epilogue** (4:00 max) applies only to ideas approved at or after Oct 19, 2026 6PM PT. Don't send back solely for a missing one on an exempt task.

## Feedback
- Reviewer Comments start with `MM/DD @ HH:MM TIMEZONE, Review #, NAME`, with the newest at the top.
- Give 1-2 personalized sentences with timestamps, and send the same text as a Slack DM using the templates.
- Use Internal Notes for edge-case reasoning and minor issues.

## Your metrics
- Defect rate under 10%.
- Pass rate 30% or higher (20-30% is a warning).
- AHT under 45 minutes (from Oct 19).
- About 15 hours per week.
- Move back to writer on 3 or more defects in your last 10 audited reviews.

## Where the doc contradicts itself
The Oct 20 changelog doesn't fully match the checklist table. It lists typing failing at over 25%/35%, an intro of 21-30 seconds as an edge case and over 30 as a fail, and says missing epilogues never fail a task. The checklist table says 21-60 seconds for the intro and still scores the epilogue. The changelog is newer, so lean on it, but confirm in #odin-reviewers-hub before failing a task on those items.
