# Pump Selection: Timed Script

Oct 19, 2026


## Read this first

This script has 23.5 minutes of speaking and doing, built for a video of about 39:55. Your earlier videos ran about 1.6 times the script time, and you will now speak slower with a pause after every click, so I planned for about 1.7 times. That keeps a wide margin above the 15:00 minimum and below the 45:59 cap. It follows the layout of your droplet script and avoids the mistakes a reviewer flagged on another task, listed below. Every number in the SAY lines was produced by running the notebook on these exact files, so a correct run reads the same on your screen.


| Mistake flagged in a review of another task | How this script avoids it |
|---|---|
| Critical: scrolling was never narrated. Say where you scroll to. | Every scroll is its own action with its own line, 16 of them: I'm scrolling down with the mouse wheel until I reach [heading or cell]. Nothing scrolls in silence. |
| What and Why were given, Where was missing. Say which part of the screen you click, every time. | Every click names the control and its place: the Dock along the left edge, the menu bar along the top, the yellow button in the top left corner, the Run arrow at the left edge of the cell, the Explorer sidebar on the left, the ribbon across the top, the slide thumbnails on the left. |
| It felt rushed. Slow down, shorten the task, be concise. | The task is deliberately small: 8 short parts, 820 typed characters in 24 short bursts, three genuine apps, and most steps are pointer clicks and speaking. Pause one second after every click and one second between sentences. |
| Said no personal information is showing, and narrated opening TaskRecorder and Stop Recording. | Both removed. The last SAY line is the closing statement. You then silently click the TaskRecorder icon and Stop Recording. |
| Mouse idle over 90 seconds. No artificial movement. | The pointer only moves to name something, never to look busy. It is never still for more than 20 seconds, and the Writer Guidelines limit is 45. Every typing burst is one line of at most 30 seconds, and the pointer goes back to the code right after it. |
| Vague words such as here and this. Narration must be followable without the screen. | Each line gives the action, the exact control, its location and the reason, using real names. The audio rules below apply, plus a test recording before you start. |

What is different from my first script: it now follows your droplet script layout, with a DO line and a SAY line for every action, a pointer instruction for each one, checkpoints with a real clock, a typing counter and trim lists. Three changes come from your own test and from how VS Code behaves. (1) The less-than and greater-than keys did not type for you, so the pass rule uses .ge(1.5) instead of a greater-than-or-equal sign, and no typed line contains either key. (2) Each gap in the notebook is the word FILL_IN, which selects cleanly with a double-click. You then press Delete before typing, because VS Code wraps selected text in a bracket or quote if you type one over it. (3) The criteria table goes into Word by paste and Convert Text to Table, and the cost comparison is a chart picture, so you type no table values in Word or PowerPoint. Use the new zip, pump_study_inputs.zip, and throw the earlier one away. The deliverables are 13 files, and the memo is final_output_4.docx.

The five rules while recording

- **Pointer.** After every click and every typing burst, move the pointer onto the thing you are about to name and keep it there while you explain it. Drag across code to highlight it. Never wiggle.
- **Narration.** Say: I'm [action] on [exact control, and where it is on the screen], because [reason]. Say the real name, never just here, this or that. One sentence per action. Speak slowly and leave one second after every click.
- **Scrolling.** Say it every time: I'm scrolling down with the mouse wheel until I reach [the heading or cell you stop at]. Keep the pointer on the page while you scroll, and name what you find when you stop.
- **Typing.** Say what you will type and why, type one line in silence, then explain it with the pointer. A burst of 25 seconds is the target, stop at 30.
- **Audio.** Quiet room, door closed, notifications off, same distance from the microphone, do not touch the desk while speaking, and never mutter. If you lose your place, stop talking, find it, then say the next line. Keep your eyes open and on the screen, and glance at the script rather than staring at it.

## Timing and checkpoints

The clock in the menu bar shows seconds. Write down the time when you press Start Recording, and check it at each checkpoint below. Do not use a stopwatch on the recorded screen.


| Part | Script length | Script clock | Real clock to expect (1.7 times) |
|---|---|---|---|
| 1. Intro, open VS Code and look at the inputs | 3:40 | 3:40 | 6:15 |
| 2. Fit the pump curves | 1:05 | 4:45 | 8:05 |
| 3. System curve, operating points and the hand check | 2:55 | 7:40 | 13:00 |
| 4. Criteria, annual energy cost and the decision | 4:20 | 12:00 | 20:25 |
| 5. Save the tables and charts, copy the criteria table | 2:15 | 14:15 | 24:10 |
| 6. Recommendation memo in Word | 5:20 | 19:35 | 33:15 |
| 7. Approval deck in PowerPoint | 2:35 | 22:05 | 37:35 |
| 8. Cross-check and stop | 1:25 | 23:30 | 39:55 |

If you are more than 3 minutes behind a checkpoint, use the cut order in the last section right away. The video must stay between 15:00 and 45:59, so a finish near 39:55 leaves you about 6 minutes of safety.


## Before you press record

Do all of this before pressing Start Recording. The guide forbids setting up an app after recording starts.

- **Studio first.** The idea is already approved. The Goal you paste into TaskRecorder, the opening note and the Metadata.rtf Request must be the approved Goal, word for word, and nothing in the video may go beyond it. Every part it promises appears in the table near the end of this document. Download the Metadata.rtf from your claimed task and use the filled copy in this folder.
- **Inputs.** All five input files are made before recording, with no private data. Before you use them, ask @Loki whether inputs drafted by another AI are acceptable and how to label them, because the guide allows only Gemini for AI-made inputs. If the answer is no, rebuild the CSV and helper with Gemini, and compare your results with the answer key. Final Notes must say exactly: AI-generated before recording.
- **Fresh folder.** Make a folder named pump_study on the Desktop of the Recorder user and unzip the five input files into it. It must hold only those five files, with no .vscode, .DS_Store or ~$ files and no outputs. Open the folder in VS Code.
- **Kernel.** Open input_3_starter_notebook.ipynb, click Select Kernel at the top right and choose a Python environment that has pandas, numpy and matplotlib. Do not run or save anything in the starter inside the study folder. The dry run below proves the environment: if the first cell shows ModuleNotFoundError, choose another environment.
- **VS Code AI features.** Close the Chat and Copilot panels and sign out of Copilot. Any AI interface on screen fails the recording. Quit Grammarly and every background app except Insightful, Accessibility Inspector and TaskRecorder.
- **Word and PowerPoint.** Both signed in with the assigned account, with no name, email or avatar visible in the title bar or ribbon, and no Copilot button used. Open two Word documents: your opening note with the Goal in it, and input_4_memo_template.docx. In PowerPoint open input_5_deck_template.pptx. Turn off design suggestions in PowerPoint if they appear.
- **Desktop.** Dock on the left edge of the screen, clock with seconds, unique wallpaper, dark mode as a second change, mouse cursor size and colour left at default, Accessibility Inspector running with its window closed, Insightful minimized, notifications off, Finder closed. The Mac is plugged in with enough free storage. Zoom windows with the Window menu, never the green Full Screen button, then minimize every window except your opening note. Metadata.rtf stays closed.
- **TaskRecorder.** Signed in, three permissions green, microphone on, Goal pasted, apps entered as Visual Studio Code, Microsoft Word and PowerPoint. Drag the TaskRecorder window larger until every line of the Goal is visible. Read this script from another device, never on the recorded screen.
- **Audio test, 1 minute.** Say one SAY line at your planned speed, type for 20 seconds, and play it back on headphones. Your voice must be clear and louder than the typing, with no fan hum.
- **Dry run.** In a temporary folder with copies of the five inputs, type every cell once, then click through Word (Save As, paste, Convert Text to Table, picture, Export to PDF) and PowerPoint (Save As, two pictures). Then delete the folder. This warms up the plotting cache and proves the menus match your versions.
Typing speed test, 2 minutes. This decides your typing share. In a scratch notebook outside the study folder, type the pass rule (59 characters): res.pct_of_bep.between(70, 110) & res.npsh_margin_m.ge(1.5) with a stopwatch and no talking. Divide your seconds by 59 to get seconds per character, then read your row below. Your longest burst anywhere is 68 characters.


| Seconds per character | Seconds for the 68 character burst | Typing share at 39:55 | Typing share at 45:00 | What to do |
|---|---|---|---|---|
| 0.25 | 17 | 9 % | 8 % | Record |
| 0.35 | 24 | 12 % | 11 % | Record |
| 0.40 | 27 | 14 % | 12 % | Split the long sentences at the semicolon, then record |
| 0.45 | 31 | 15 % | 14 % | Split them, use trim list 1, and check again |

These shares are estimates: 820 characters times your seconds per character, divided by the video length. I do not know exactly how AutoQC counts typing, so the test decides, not my table. The limit is strictly below 20 percent, or 30 percent only if Loki confirms this counts as a coding plus writing task.

Keys. The special characters you type are: " ( ) [ ] , . : ; = - _ / * & % $. Capital letters are the only other Shift keys. The less-than and greater-than keys are never needed. Test the ampersand once before recording: in your scratch notebook, type res.pct_of_bep.between(70, 110) & res.npsh_margin_m.ge(1.5). If any key does not appear, tell me before recording.


## Rules from guide.pdf, the Writer Guidelines and the Studio criteria


| Rule | How this script meets it |
|---|---|
| Clock shows seconds; dock on the left, visible, never at the bottom; one UI change; cursor default (Studio items 7 to 9, 15). | Desktop checklist above, checked again before Start. |
| Accessibility Inspector icon has a dot in the Dock; its window is never visible (items 10, 11). | Desktop checklist above. |
| TaskRecorder shows an accurate Goal; Goal document is shown first; the opening narration is short (items 12 to 14). | Part 1.1: only the one required sentence, about 15 seconds, and the Goal is never read aloud. |
| Metadata.rtf and project information never shown; TaskRecorder never shown outside Start and Stop (items 16, 27, 31). | Kept closed, and the stop is silent. |
| No unused window covers more than 25% of another for more than 6 seconds (item 17). | Each app is minimized with the yellow button the moment you finish with it. Only dialogs of the same app overlap. |
| Pointer never idle over 45 seconds (item 18); every click followed by a 1 second pause (item 28). | The pointer rests only on what you name. Count one after every click. |
| Typing at most 20% (item 19). | 820 characters in short bursts; see the typing counter for the estimated share. |
| Zero restricted apps (item 20). | Only VS Code, Word and PowerPoint. Never open the PDF in Preview, never use Terminal, Notes, TextEdit, Excel, Chrome or Safari. Finder stays closed. |
| Clear narration, no silence over 45 seconds, what, where and why, no here or this (items 21 to 24). | Every SAY line names the control, its place and the reason. While a cell runs you keep talking and trace the code. |
| No AI interaction, no PII, no copyrighted content, no profanity (items 29, 30, 32, 33). | Copilot, Chat and design suggestions are off and never mentioned. The prepared inputs are described only as prepared input files, free of royalties and copyright. |

Every part the Goal promises, and where it is shown (the recording-shows-the-task AutoQC check):


| Promised in the Goal | Shown in step |
|---|---|
| Fit a head-flow curve for each pump in a Jupyter notebook in VS Code | 2.1 |
| Intersect it with the system curve to find the operating point, with a hand check | 3.1, 3.2, 3.3 |
| Check 70 to 110 percent of best-efficiency flow and 1.5 m of NPSH margin | 4.2, 4.3 |
| Compare annual energy cost | 4.2, 4.3, 5.2 |
| Word memo with the criteria table and the operating-point chart, saved and exported to PDF | 6.3, 6.4, 6.6 |
| PowerPoint two-slide approval deck, chart on slide 1, cost comparison and recommendation on slide 2 | 7.2, 7.3 |
| The facilities manager can approve: a clear recommendation | 4.3, 6.5, 7.3, 8.2 |

Never say: personal information, TaskRecorder, Mercor, Odin, Studio, AI, Gemini, ChatGPT, Copilot, Designer. Never say here or this without naming the item.


## Part 1: Intro, open VS Code and look at the inputs (0:00 to 3:40)

Two short typing bursts: the first file name and the range check. Everything else is pointer work. Every scroll is named with where it stops. Never read your Task Description aloud, never say an AI tool name, your name, the project, the platform or the company, and never narrate TaskRecorder.


### 1.1 Intro (15 seconds)

**DO:** Click Start Recording in TaskRecorder, then click the yellow button in the top left corner of the TaskRecorder window to minimize it. Say nothing while you do this. Leave your opening note (the Word document holding the Goal) visible.

**SAY:** “I will be beginning my task soon. Here is the workflow I have in mind.”

**DO:** Wait one second. Click the yellow button in the top left corner of the note window to minimize it.


### 1.2 Open VS Code and name the prepared inputs (55 seconds)

**DO:** Move the pointer to the Visual Studio Code icon in the Dock along the left edge of the screen. Click it. Rest the pointer on the Explorer sidebar on the left side of the VS Code window, then move it down the file list, one file at a time.

**SAY:** “I'm clicking the Visual Studio Code icon in the Dock along the left edge of the screen, because the analysis runs in a Jupyter notebook inside it. In the Explorer sidebar on the left side of the window, I'm pointing at my five prepared input files in the pump_study folder: the pump data, the helper functions, the starter notebook, and the memo and deck templates. They are prepared inputs with synthetic values, free of royalties and copyright. I'm a mechanical engineer choosing a pump for a chilled-water loop that must deliver 50 litres per second at 28 metres, from three candidates: A, B and C.”


### 1.3 Save a copy before touching the starter (40 seconds)

**DO:** Click the input_3_starter_notebook.ipynb tab at the top of the editor, if it is not already in front. Move to the menu bar along the top of the screen and click File. In the dropdown, click Save As.

**SAY, before typing:** “I'm clicking File in the menu bar at the top of the screen, then Save As in the dropdown. I will type final output one as the name, so the starter stays untouched, and click the Save button at the bottom right of the window.”

**DO:** Type this in silence, then click the Save button at the bottom right of the Save window:

**TYPE:** `final_output_1.ipynb`

**SAY:** “Saved. From now on I save with Command and S.”

*Do not press Command + S before this Save As, or you overwrite the starter.*


### 1.4 Run the setup cell (55 seconds)

**DO:** Rest the pointer on the kernel name in the top right corner of the notebook. Scroll down with the mouse wheel until heading 1, Load the data and check units, and the first code cell are in the middle of the window. Click the Run arrow at the left edge of the first code cell. Trace the import lines with the pointer while it loads. When the table appears, rest the pointer on the column headers in its first row.

**SAY:** “The kernel name in the top right corner is my Python environment. I'm scrolling down with the mouse wheel until I reach heading 1, Load the data and check units, and clicking the Run arrow at the left edge of the first code cell. It imports my tools and reads the pump data. The first run takes a few seconds while the kernel starts.”

**SAY:** “In the output, I'm pointing at the column headers: pump, flow in litres per second, head in metres, efficiency in percent, and NPSH required in metres.”


### 1.5 Check the ranges (55 seconds)

**DO:** Scroll down a little with the mouse wheel until the next code cell, the one with agg in it, is in the middle of the window. Double-click the word FILL_IN inside agg (drag across it if it does not highlight), then press the Delete key.

**SAY, before typing:** “I'm scrolling down a little with the mouse wheel to the next code cell. I'm deleting FILL_IN inside agg and typing minimum and maximum, to check each column's range for each pump.”

**DO:** Type this in silence, then click the Run arrow at the left edge of the cell. If a suggestion list appears while you type, press Escape once and carry on.

**TYPE:** `["min", "max"]`

**DO:** Rest the pointer on the flow_Ls columns, then the head_m columns, then the efficiency_pct columns, then the npshr_m columns in the output.

**SAY:** “I'm clicking the Run arrow at the left edge of the cell. Every pump covers 10 to 80 litres per second. Efficiency peaks at 77.1 percent for A, 83.6 for B and 87.9 for C, and NPSH required climbs to 8.5 metres for pump C. The ranges are physical, so I can fit the curves.”


## Part 2: Fit the pump curves (3:40 to 4:45)

Same routine for every cell: scroll to the heading, say what you will type and why, double-click the word FILL_IN, press Delete, type one short burst in silence, click the Run arrow at the left edge of the cell, then rest the pointer on each result as you explain it. Pressing Delete first matters: if text is selected and you type an opening bracket or quote, VS Code wraps the selection in it instead of replacing it.


### 2.1 Fit a quadratic for each pump, under heading 2 (1 minute 5 seconds)

**DO:** Scroll down with the mouse wheel until heading 2, Fit a quadratic curve for each pump, and the code cell under it are in the middle of the window. Double-click FILL_IN after fits equals, then press the Delete key.

**SAY, before typing:** “I'm scrolling down with the mouse wheel until I reach heading 2, Fit a quadratic curve for each pump. Test points need an equation to find where a pump meets the system, and a second-degree polynomial suits these curves. I'm deleting FILL_IN after fits equals and typing fit_all of df, my helper for all three pumps.”

**DO:** Type this in silence, then click the Run arrow at the left edge of the cell. Rest the pointer on the head_m column, then efficiency_pct, then npshr_m.

**TYPE:** `fit_all(df)`

**SAY:** “I'm clicking the Run arrow at the left edge of the cell. In the fit_report table, the largest error is 0.04 metres for head, 0.05 points for efficiency and 0.04 metres for NPSH. The errors are tiny, so a quadratic is justified.”

**DO:** Press Command + S.

**SAY:** “I'm pressing Command and S to save the notebook.”


## Part 3: System curve, operating points and the hand check (4:45 to 7:40)

Same routine as Part 2. I ran every cell on this data with these file names, so the numbers below are what your screen should show. If a number differs slightly, say what your screen shows and use that number in the memo and deck.


### 3.1 The system curve, under heading 3 (1 minute 5 seconds)

**DO:** Scroll down with the mouse wheel until heading 3, System curve and operating points, and its first code cell are in the middle of the window. Double-click FILL_IN after static_head equals, then press the Delete key.

**SAY, before burst 1:** “I'm scrolling down with the mouse wheel until I reach heading 3. The loop needs 50 litres per second at 28 metres. Twelve metres is static head and the other 16 is friction, which grows with flow squared, so H equals 12 plus k times Q squared. I'm deleting FILL_IN after static_head and typing 12.0.”

**TYPE:** `12.0`

**DO:** Double-click FILL_IN after k equals, then press the Delete key.

**SAY, before burst 2:** “For k, I'm deleting FILL_IN and typing 28 minus the static head, divided by 50 squared.”

**TYPE:** `(28 - static_head) / 50**2`

**DO:** Click the Run arrow at the left edge of the cell. Rest the pointer on the number printed under the cell.

**SAY:** “I'm clicking the Run arrow at the left edge of the cell. It prints k as 0.0064, so the system curve is defined.”


### 3.2 The operating points (55 seconds)

**DO:** Scroll down with the mouse wheel until the next code cell, the loop that starts with op equals an empty dictionary, is in the middle of the window. Rest the pointer on the for line, then the roots line. Double-click FILL_IN after roots equals, then press the Delete key.

**SAY, before typing:** “I'm scrolling down with the mouse wheel to the loop that finds the operating points. The operating point is where pump head equals system head, so I'm deleting FILL_IN after roots equals and typing the head fit minus the system curve, then dot roots.”

**DO:** Type this in silence, then click the Run arrow at the left edge of the cell. Rest the pointer on the A line, then B, then C in the output.

**TYPE:** `(f["head"] - system).roots`

**SAY:** “I'm clicking the Run arrow at the left edge of the cell. Pump A settles at 49.91 litres per second, pump B at 50.00 and pump C at 50.20, all close to the 50 litre duty.”


### 3.3 Hand check on pump B (55 seconds)

**DO:** Scroll down with the mouse wheel until the heading Hand check on one pump and its code cell are in the middle of the window. Rest the pointer on the p and q lines. Double-click FILL_IN at the start of the last line, then press the Delete key.

**SAY, before typing:** “I'm scrolling down with the mouse wheel to Hand check on one pump. I'm deleting FILL_IN on the last line and typing pump B's head fit at q minus the system curve at q. The difference must be under 0.1 metres.”

**DO:** Type this in silence, then click the Run arrow at the left edge of the cell. Rest the pointer on the number under the cell.

**TYPE:** `fits[p]["head"](q) - system(q)`

**SAY:** “I'm clicking the Run arrow at the left edge of the cell. The difference is essentially zero, so the intersection is correct.”

*Numpy may print np.float64(0.0) or a tiny number like 1e-14. Say essentially zero either way.*

**DO:** Press Command + S.

**SAY:** “I'm pressing Command and S to save the notebook.”


## Part 4: Criteria, annual energy cost and the decision (7:40 to 12:00)

Same routine, still in VS Code. Four short bursts in the loop, one line each. The pass rule is your typing speed test line.


### 4.1 The assumptions, under heading 4 (55 seconds)

**DO:** Scroll down with the mouse wheel until heading 4, Criteria and annual energy cost, and the first code cell under it are in the middle of the window. Double-click FILL_IN, then press the Delete key.

**SAY, before typing:** “I'm scrolling down with the mouse wheel until I reach heading 4. A pump must run at 70 to 110 percent of its best-efficiency flow, or it wears and wastes energy, and keep an NPSH margin of at least 1.5 metres, or it can cavitate. I'm deleting FILL_IN in the constants cell and typing five assumptions: water density, gravity, 6000 running hours a year, 12 cents per kilowatt-hour, and 6 metres of NPSH available.”

**DO:** Type this in silence, then click the Run arrow at the left edge of the cell:

**TYPE:** `1000, 9.81, 6000, 0.12, 6.0`


### 4.2 The criteria loop (2 minutes)

**DO:** Scroll down with the mouse wheel until the loop that starts with rows equals an empty list is fully in view. Trace the prefilled lines with the pointer: q, h, eta, then the four lines with FILL_IN.

**SAY:** “I'm scrolling down with the mouse wheel until the criteria loop is in view. For each pump, it reads the operating flow, the head, and the efficiency as a fraction. Four lines are left for me.”

**DO:** Double-click FILL_IN after q_bep equals, then press the Delete key.

**SAY, before burst 1:** “First, the best-efficiency flow, the top of the efficiency parabola: minus b over 2a.”

**TYPE:** `-f["eff"].coeffs[1] / (2 * f["eff"].coeffs[0])`

**DO:** Double-click FILL_IN after margin equals, then press the Delete key.

**SAY, before burst 2:** “Second, the NPSH margin: available minus required.”

**TYPE:** `npsh_avail - f["npshr"](q)`

**DO:** Double-click FILL_IN after kw equals, then press the Delete key.

**SAY, before burst 3:** “Third, shaft power in kilowatts: density times gravity times flow times head, over efficiency, over 1000.”

**TYPE:** `rho * g * (q / 1000) * h / eta / 1000`

**DO:** Double-click FILL_IN after cost equals, then press the Delete key.

**SAY, before burst 4:** “Fourth, annual cost: kilowatts times hours times tariff.”

**TYPE:** `kw * hours * tariff`

**DO:** Click the Run arrow at the left edge of the cell. If the table is wider than the window, scroll the output sideways with two fingers on the trackpad and say so. Rest the pointer on the A row, then B, then C.

**SAY:** “I'm clicking the Run arrow at the left edge of the cell. Pump A runs at 107 percent of best-efficiency flow, with a margin of 2.32 metres, and costs 12,762 dollars a year. Pump B runs at 93 percent, margin 1.99, and costs 11,824. Pump C runs at 87 percent, but its margin is only 1.08 metres.”


### 4.3 Pass or fail and the decision (1 minute 25 seconds)

**DO:** Scroll down with the mouse wheel until the next code cell, the one with res and pass in it, is in the middle of the window. Double-click FILL_IN after res pass equals, then press the Delete key.

**SAY, before typing:** “I'm scrolling down with the mouse wheel to the next code cell. I'm deleting FILL_IN and typing the pass rule: between 70 and 110 percent, and an NPSH margin of at least 1.5, using ge for greater than or equal.”

**DO:** Type this in silence, then click the Run arrow at the left edge of the cell. Rest the pointer on the new pass column on the far right, then on the C row.

**TYPE:** `res.pct_of_bep.between(70, 110) & res.npsh_margin_m.ge(1.5)`

**SAY:** “I'm clicking the Run arrow at the left edge of the cell. In the pass column on the far right, A and B are True and C is False. Pump C is cheapest, 319 dollars a year below B, but its margin of 1.08 metres is under 1.5, so it risks cavitation and I reject it. Pump B saves 938 dollars a year over A. I recommend pump B, with pump A as the runner-up.”

**DO:** Press Command + S.

**SAY:** “I'm pressing Command and S to save the notebook.”


## Part 5: Save the tables and charts, copy the criteria table (12:00 to 14:15)

Same routine, one typed line. Then the first pointer-only stretch: reading the two charts.


### 5.1 Save and draw, under heading 5 (45 seconds)

**DO:** Scroll down with the mouse wheel until heading 5, Save the tables and the charts, and its code cell are in the middle of the window. Rest the pointer on the first three lines. Double-click FILL_IN on the last line, then press the Delete key.

**SAY, before typing:** “I'm scrolling down with the mouse wheel until I reach heading 5. The first three lines save the results table, a criteria table for the memo, and the operating-point chart. I'm deleting FILL_IN and typing a call to my cost chart helper, which saves artifact two.”

**DO:** Type this in silence, then click the Run arrow at the left edge of the cell:

**TYPE:** `cost_chart(res, "artifact_2.png")`


### 5.2 Read the two charts (50 seconds)

**DO:** Scroll down with the mouse wheel until the first chart in the output is fully in view. Rest the pointer on the left panel's dashed line, then trace pump A, B and C. Move to the right panel and rest on each dot in turn. Scroll down until the cost chart is in view and rest on each bar.

**SAY:** “I'm scrolling down with the mouse wheel until the first chart is in view. In the left panel, the dashed line is the system curve and the solid lines are the pump curves. In the right panel, pump C is the hollow orange dot, hollow because it fails the NPSH margin.”

**SAY:** “Now I'm scrolling down with the mouse wheel until the cost chart is in view: pump B is recommended, and pump C, the cheapest bar, is hatched because it fails.”

**DO:** Press Command + S.

**SAY:** “I'm pressing Command and S to save the notebook.”


### 5.3 Copy the criteria table for Word (35 seconds)

**DO:** Click artifact_1.csv in the Explorer sidebar on the left side of the window. Rest the pointer on its first line, then the three pump lines. Click inside the file text. Press Command + A, then Command + C. Click the yellow button in the top left corner of the VS Code window.

**SAY:** “I'm clicking artifact_1.csv in the Explorer sidebar on the left side of the window and clicking inside its text. I'm pressing Command and A to select all and Command and C to copy, to paste it into the memo. Then I'm clicking the yellow button in the top left corner to minimize Visual Studio Code.”

*Copy nothing else until you have pasted the table in Word.*


## Part 6: Recommendation memo in Word (14:15 to 19:35)

Subject, To and From are already filled in the template, and every heading has an empty line under it. You type four short sentences and paste one table. Every Save As shows the folder: make sure Where says pump_study and the format says Word Document (.docx).


### 6.1 Open the template and save a copy (40 seconds)

**DO:** Move the pointer to the Word icon in the Dock along the left edge of the screen. Right-click it. In the list that opens to the right of the Dock, click input_4_memo_template.docx. Click File in the menu bar along the top of the screen, then Save As in the dropdown.

**SAY, before typing:** “I'm right-clicking the Word icon in the Dock along the left edge of the screen and choosing the memo template in the list to its right, a prepared input with headings only, free of royalties and copyright. Now I'm clicking File, then Save As, typing final output four, checking the folder is pump_study, and clicking Save at the bottom right.”

**DO:** Type this in silence, then click the Save button at the bottom right of the Save window:

**TYPE:** `final_output_4.docx`


### 6.2 Purpose and criteria, headings 1 and 2 (1 minute)

**DO:** Click the empty line under heading 1, Purpose, near the top of the page.

**SAY, before burst 1:** “I'm clicking the empty line under heading 1, Purpose, and writing one sentence on what the memo is for.”

**TYPE:** `Select a pump for the chilled-water loop; duty is 50 L/s at 28 m.`

**DO:** Click the empty line under heading 2, Duty point and criteria.

**SAY, before burst 2:** “Now I'm clicking the empty line under heading 2 and stating the two tests every pump must pass.”

**TYPE:** `Flow 70 to 110% of best-efficiency flow; NPSH margin at least 1.5 m.`


### 6.3 Paste the criteria table, heading 3 (45 seconds)

**DO:** Click the empty line under heading 3, Results. Press Command + V. Drag from the start of the first pasted line to the end of the last one. Click the Insert tab in the ribbon across the top of the window, then Table, then Convert Text to Table in the dropdown. Check that Separate text at says Commas and the table has 5 columns. Click OK at the bottom right of the dialog. Rest the pointer on each row of the new table: the header, then A, B and C.

**SAY:** “I'm clicking the empty line under heading 3, Results, and pressing Command and V to paste the criteria table. It is comma separated text, so I'm dragging across all four lines. Now I'm clicking the Insert tab in the ribbon across the top, then Table, then Convert Text to Table. The separator is commas with five columns, so I'm clicking OK.”

**SAY:** “Reading down the table: A and B pass, and pump C fails on NPSH.”

*If Word shows a small Paste Options button after the paste, ignore it. If the cost column wraps, say so; it does not matter.*


### 6.4 Insert the chart, heading 4 (25 seconds)

**DO:** Click the empty line under heading 4, Operating-point chart. Click the Insert tab in the ribbon across the top, then Pictures, then Picture from File. In the file window, click Desktop in the sidebar on the left, double-click the pump_study folder, click final_output_3.png, then click Insert at the bottom right. Rest the pointer on the left panel, then the right panel of the chart.

**SAY:** “I'm clicking the empty line under heading 4, then the Insert tab, Pictures, and Picture from File. In the file window, I'm opening Desktop and pump_study and choosing final_output_3.png, the operating-point chart, then clicking Insert.”

*If the picture is wider than the margins or the memo spills onto page 2, click the picture and drag one corner handle inward. Say so out loud.*


### 6.5 The recommendation, heading 5 (1 minute 15 seconds)

**DO:** Scroll down with the mouse wheel until heading 5, Recommendation and next step, and its empty line are in view. Click the empty line.

**SAY, before burst 1:** “I'm scrolling down with the mouse wheel until I reach heading 5, Recommendation, and clicking its empty line. Three short pieces: first, the choice.”

**TYPE:** `Buy pump B: lowest cost of the pumps that pass both criteria.`

**SAY, before burst 2:** “Second, why not pump C.”

**DO:** Press the space bar, then type:

**TYPE:** `Pump C is $319 cheaper but fails the NPSH margin (cavitation risk).`

**SAY, before burst 3:** “Third, the fallback.”

**DO:** Press the space bar, then type:

**TYPE:** `Pump A is the runner-up, $938 a year more than B.`


### 6.6 Review, save and export the PDF (1 minute 10 seconds)

**DO:** Scroll up with the mouse wheel to the top of the page, then scroll down again slowly, resting the pointer on the table, the chart and the recommendation. Point at the page count at the bottom left of the window. Press Command + S.

**SAY:** “I'm scrolling up with the mouse wheel to the top of the page, then down again, pointing at the table, the chart and the recommendation. The page count at the bottom left says Page 1 of 1. I'm pressing Command and S to save the memo.”

**DO:** Click File in the menu bar along the top of the screen, then Export in the dropdown. In the Export window, click the File Format dropdown and choose PDF. Click in the name field, select its text, and type the new name. Click the Export button at the bottom right.

**SAY, before typing:** “To make the PDF, I'm clicking File, then Export, and choosing PDF in the File Format dropdown. I will type final output five as the name and click Export at the bottom right.”

**TYPE:** `final_output_5`

**DO:** Click the yellow button in the top left corner of the Word window.

**SAY:** “I'm clicking the yellow button in the top left corner to minimize Word.”

*Do not open the PDF in Preview. Preview is a restricted app. VS Code's Explorer will show the PDF in Part 8. In your dry run, check that Export does not open the PDF by itself in Preview. If it does, use File, then Print, then the PDF menu at the bottom left, then Save as PDF, instead, and change the narration to match.*


## Part 7: Approval deck in PowerPoint (19:35 to 22:05)

Two slides. Both are already in the template with an empty title and an empty content box. You type two titles and insert two pictures with the mouse.


### 7.1 Open the template and save a copy (35 seconds)

**DO:** Move the pointer to the PowerPoint icon in the Dock along the left edge of the screen. Right-click it. In the list that opens to the right, click input_5_deck_template.pptx. Click File in the menu bar along the top of the screen, then Save As in the dropdown.

**SAY, before typing:** “I'm right-clicking the PowerPoint icon in the Dock along the left edge of the screen and choosing the deck template, a prepared input, free of royalties and copyright. Now I'm clicking File, then Save As, typing final output six, and clicking Save.”

**DO:** Type this in silence, then click the Save button at the bottom right of the Save window:

**TYPE:** `final_output_6.pptx`


### 7.2 Slide 1, the duty point and the chart (50 seconds)

**DO:** Click the title box in the upper middle of slide 1.

**SAY, before typing:** “I'm clicking the title box in the upper middle of slide 1 and typing the finding first, so the manager sees the answer before the evidence.”

**TYPE:** `Pump B meets the 50 L/s duty`

**DO:** Click the Pictures icon in the middle of the content box below the title. In the file window, click Desktop, double-click pump_study, click final_output_3.png, then click Insert. Rest the pointer on the right panel, then on the dot for pump B.

**SAY:** “Now I'm clicking the Pictures icon in the middle of the content box and choosing final_output_3.png, then Insert. In the right panel, pump B sits at 50 litres per second and 28 metres, exactly the duty point.”


### 7.3 Slide 2, the cost comparison and the recommendation (50 seconds)

**DO:** Click slide 2 in the slide thumbnails on the left side of the window. Click the title box in the upper middle of the slide.

**SAY, before typing:** “I'm clicking slide 2 in the thumbnails on the left, then its title box, and typing the recommendation.”

**TYPE:** `Recommend pump B: lowest cost of the pumps that pass`

**DO:** Click the Pictures icon in the middle of the content box. In the file window, click artifact_2.png, then click Insert. Rest the pointer on the bar for pump A, then B, then the hatched bar for C.

**SAY:** “I'm clicking the Pictures icon in the middle of the content box and choosing artifact_2.png, the cost comparison, then Insert. Pump C is cheaper but hatched, because it fails the NPSH margin.”


### 7.4 Review and save (25 seconds)

**DO:** Click slide 1, then slide 2, in the slide thumbnails on the left, resting the pointer on each title. Press Command + S. Click the yellow button in the top left corner of the PowerPoint window.

**SAY:** “I'm clicking through both slides in the thumbnails on the left to check nothing overflows. Now I'm pressing Command and S to save, and clicking the yellow button in the top left corner to minimize PowerPoint.”


## Part 8: Cross-check and stop (22:05 to 23:30)

No typing in this part. Everything is pointer work. This revisit to VS Code is a LOOKUP, so it is listed in the Topology.


### 8.1 Check the numbers and the saved files (55 seconds)

**DO:** Click the Visual Studio Code icon in the Dock along the left edge of the screen. Scroll up with the mouse wheel to the results table under heading 4, resting the pointer on each pump row. Then rest the pointer down the Explorer sidebar on the left side of the window, over the saved files.

**SAY:** “Before I finish, I'm clicking the Visual Studio Code icon in the Dock to check the numbers. I'm scrolling up with the mouse wheel to the results table under heading 4: pump B costs 11,824 dollars and passes, and pump C fails at 1.08 metres. These match the memo and the slides.”

**SAY:** “In the Explorer sidebar on the left side of the window, I'm pointing at the saved files, including the memo as a Word file and a PDF, and the deck. Everything the task needs is saved.”

**DO:** Click the yellow button in the top left corner of the VS Code window.

**SAY:** “I'm clicking the yellow button in the top left corner to minimize Visual Studio Code.”

*If a number does not match, say what differs and fix it in the right app before you stop. If you reopen Word or PowerPoint, add that extra visit to the Topology in Metadata.rtf.*


### 8.2 Closing and stop (25 seconds)

**SAY:** “That completes the task. The notebook with its tables and charts, the one page memo as a Word file and a PDF, and the two slide approval deck are saved. The recommendation is pump B, which passes both criteria at the lowest energy cost.”

**DO:** Say nothing more. Silently click the TaskRecorder icon in the Dock, then click Stop Recording. Do not quit it. Wait for Stopping, then Archiving, then Idle. Never use Command + Shift + 9.


## Typing counter and cut order

Total typed: 820 characters. The longest single burst is 68 characters, about 17 seconds at 0.25 seconds per character, or 24 seconds at 0.35.


| Block | Characters |
|---|---|
| Notebook cells | 358 |
| File names (Save As and Export) | 72 |
| Word text | 310 |
| Deck text | 80 |
| Total | 820 |

Split rule. If your speed test lands above 0.35 seconds per character, split the two 68 and 64 character memo sentences at the semicolon into two bursts, so no burst passes 30 seconds, and say the second half before typing it.

Trim list 1 (saves 49 characters). Use it only if your typing share lands near the limit. Word 6.5: skip the runner-up sentence, and say it aloud with the pointer on the results table.

Trim list 2 (saves 65 more). Word 6.2: skip the purpose sentence, and say it aloud with the pointer on the heading.

The analysis cells, the pass rule and the recommendation stay in every list, because the code and the decision are the real work.

Cut order if you are more than 3 minutes behind a checkpoint (time, not typing):

- Say only the two biggest numbers in each result line.
- In 1.4, skip pointing at the kernel name and only run the setup cell.
- In 5.2, read only the right panel of the operating-point chart and the cost chart bars.
- In 7.4, click through only slide 2 instead of both slides.
- In 6.6, scroll through the memo once at a steady pace without naming every part.
Never cut a Command + S, the cross-check in 8.1, any analysis cell, the hand check, or the PDF export. Never cut the scroll or click locations to save time: shorten the reasons instead.


## After recording, and if something goes wrong

After you stop

- **Wait for Idle.** TaskRecorder must go Stopping, then Archiving, then Idle. Do not quit it or close the lid.
- **Check the video length.** It must be between 15:00 and 45:59. Then scrub it in 10 minute chunks and look for three things: a stretch over 45 seconds with no pointer movement (typing does not count), a typing burst over 30 seconds, and a stretch where your voice is unclear or silent. Tell me any timestamp before you upload.
- **Check the screenshots.** Count the PNG files and divide by the video length in seconds. It must be above 0.5.
- **Build Deliverables.zip.** One folder named Deliverables, flat inside, with 13 files. Rename the underscores to spaces: input 1.csv, input 2.py, input 3.ipynb, input 4.docx, input 5.pptx, artifact 1.csv, artifact 2.png, final output 1.ipynb, final output 2.csv, final output 3.png, final output 4.docx, final output 5.pdf, final output 6.pptx. Inputs 3, 4 and 5 must be the untouched starters. No .DS_Store, no ~$ files, no __MACOSX, no .vscode. Build it with zip -r -X, not Finder's Compress, and send me the zip so I can check it before you upload.
- **Metadata.rtf** goes in separately, not inside the zip. Topology, in order: Visual Studio Code CREATE, Microsoft Word CREATE, PowerPoint CREATE, Visual Studio Code LOOKUP. Request must equal the Goal exactly. Task Description is a numbered outline of those four visits. Compare it with the video, and add any extra app visit you made.
- **Upload.** Upload Metadata.rtf, video.mp4 (from the recording folder, never renamed), the TaskRecorder zip recording_*.zip, and Deliverables.zip. Final Notes exactly: AI-generated before recording. Fill the Mac spec and display fields to match the recording you made.
- **Workflow Checklist and AutoQC.** Go through the Workflow Checklist in the Writer Guidelines line by line: Before Recording (Task Plan), Before Recording (Prepare), During Recording and After Recording. Then run both AutoQC checks, the files and recording check first and the narration check about 10 minutes later, and resolve every blocking finding. If AutoQC flags something, open your video at the flagged timestamps first, and dispute only if the video clearly contradicts the finding. Tick each manual check only after checking it against the recording, and tick the final box last.
If something goes wrong while recording: say what happened, fix it once, check the fix, and carry on.

- Typo in code: "I mistyped the bracket, so I'll select the line, retype it, and run the cell again to confirm the result."
- Wrong cell run: "That ran the wrong cell. I'll scroll back to the right one and run it from there."
- FILL_IN did not select: "The word did not highlight, so I'll drag across it with the mouse instead."
- A suggestion list appears while typing: press Escape once, say "I'm closing the suggestion list with Escape", then carry on.
- Chart too big in Word: "The chart is wider than the margins, so I'll drag the corner handle inward until the page count reads one of one."
- A file window opens in the wrong folder: "The window opened in the wrong folder, so I'll click Desktop and then pump_study."
- Restart the recording if searching, guessing, undoing and redoing take over, or if the result is wrong and you cannot fix it on screen.
