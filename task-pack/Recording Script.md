# Recording script: Heat exchanger E-101 fouling check

Everything in this script follows the Writer Guidelines (guide.pdf, updated 8 Oct 2026), your Review Lessons file, and the current task page (epilogue rule, 15:00 to 50:59 length, 45 AutoQC checks). Numbers in the script come from running the prepared files, so they only match if you use the files in `Working Files.zip` unchanged.

**How to read it**

- Lines starting with **DO** are actions. Every click, drag or typing action carries a silent one-second pause afterwards. Count "one" in your head before you speak or move.
- Lines in a quote block starting with **SAY** are the words to speak. Speak slowly, about 120 to 140 words a minute. Say numbers the way they are written out in words.
- Where the script says "type", the exact text is in the Typing Sheet at the end.
- Never say: "here" or "this" on their own, anything about personal information, TaskRecorder, how the files were made, or any AI tool. Do not read the Goal aloud.
- Expected recording time: about 30 to 35 minutes including the epilogue. The limit is 50:59.

---

## Part 0. Important note on the input files

The guide says AI-generated inputs must come from Gemini only, prepared before recording, and disclosed in Final Notes as exactly "AI-generated before recording". The files in this pack were written with a different assistant (Claude), so do not describe them as Gemini-made or tick "AI-generated file" for them on that basis. Before you record, do one of these:

1. Regenerate the same files with Gemini, using the prompts from my earlier message, then re-run the notebook once. The numbers in this script will then change, so re-read each result aloud from your own output. Or
2. Ask Loki in your domain Loki channel whether files prepared with another assistant are acceptable for this approved idea, and follow the answer exactly.

Do not guess. The approved idea text says the files are AI-generated before recording.

---

## Part 1. Setup checklist (before you press Start Recording)

Do all of this on the Recorder user account. Keep Studio, Slack, the guide and this script on another device or your regular profile, never on the recorded screen.

**Files**

- [ ] Unzip `Working Files.zip`. Put the folder **Task Files** on the Desktop. It holds `exchanger_data.csv`, `fouling_analysis.ipynb`, `Maintenance Memo Template.docx`, `Briefing Template.pptx`.
- [ ] Put `Opening Note.docx` somewhere else (for example Documents). It holds only the Goal paragraph.
- [ ] Keep an untouched copy of `Deliverables inputs only.zip` for after recording.

**Desktop and tools (guide, Technical Setup and Workflow Checklist)**

- [ ] Dock on the left or right edge, visible, not auto-hidden.
- [ ] Menu bar clock shows seconds.
- [ ] Wallpaper changed (and enter resolution, light or dark mode, Dock position and "wallpaper changed" in Studio).
- [ ] Mouse cursor size and colour at default.
- [ ] Accessibility Inspector running, window closed with the red button, a dot under its Dock icon.
- [ ] Insightful running and minimized. Notifications off (Focus on). Mac plugged in. Finder windows closed.
- [ ] Display resolution matches what you entered in Studio. Microphone selected, test sentence turns the bar green, wired or built-in mic stays connected for the whole recording.

**Apps (all launched, logged in, minimized, one ordinary window each, never Full Screen)**

- [ ] Visual Studio Code: folder Task Files open, `fouling_analysis.ipynb` open, kernel (Python 3) already selected, Python and Jupyter extensions installed, GitHub Copilot and the chat panel turned off, no personal account avatar visible. Run every cell once as a warm-up in a temporary copy, then restore the original notebook so the placeholders `TYPE_HERE` are back.
- [ ] Microsoft Word: `Maintenance Memo Template.docx` open and minimized. `Opening Note.docx` open and visible. Both windows are the same app, so the minimized memo thumbnail in the Dock is the one to click later.
- [ ] PowerPoint: `Briefing Template.pptx` open and minimized.
- [ ] No Terminal, Preview, TextEdit, Notes, Safari or Chrome opened at any point.

**TaskRecorder (do not show it on camera except Start and Stop)**

- [ ] Signed in with the assigned OTA account. All three permissions green.
- [ ] Task Description: clear the old text, then paste the Goal (see "Goal text" at the end). Check what Studio shows in the Prompt/Description field; if it says to paste more than the Goal, follow that and paste the same text into Metadata.rtf Request.
- [ ] Used Apps: exactly `Visual Studio Code`, `Microsoft Word`, `PowerPoint`, matching Studio.
- [ ] Drag the window larger until the whole description is visible.
- [ ] Correct display selected.

**Final look**

- [ ] The only visible window is `Opening Note.docx`, with TaskRecorder in front of it.
- [ ] Metadata.rtf, Studio, Slack, Insightful and the guide are closed or minimized.

---

## Part 2. Start sequence (under 20 seconds of speech)

**DO** In TaskRecorder, click **Start Recording**. Say nothing. Click the yellow minimize button on the TaskRecorder window.

**DO** The opening note shows the Goal. Leave it on screen for about four seconds.

> **SAY (exactly this sentence, nothing else):** "I will be beginning my task soon. Here is the workflow I have in mind."

**DO** Wait about four seconds, then click the yellow minimize button on the opening note window. Do not narrate any of this.

---

## Part 3. The work

### Scene 1. Open the notebook and read the helpers (Visual Studio Code, about 3 minutes)

**DO** Click the Visual Studio Code icon (or minimized thumbnail) in the Dock.

> **SAY:** "I'll start in Visual Studio Code, so I'm clicking its icon in the Dock on the edge of the screen."

**DO** The notebook is open. Move the pointer over the Explorer panel on the left.

> **SAY:** "The window opens on the notebook called fouling underscore analysis. In the Explorer panel on the left, the folder Task Files lists the data file, exchanger underscore data dot csv. The data file, the starter notebook and the two document templates are prepared inputs, free of royalties and copyright."

> **SAY:** "I'm a process engineer checking heat exchanger E-101. Over time, deposits build up on the tubes and slow the heat transfer, so the overall heat transfer coefficient, called U, falls. My goal is to find the day U drops twenty percent below its clean value, because that is when the supervisor should schedule a cleaning."

**DO** Scroll down with the mouse wheel to the first code cell. Rest the pointer on the code.

> **SAY:** "I'm scrolling down with the mouse wheel to the first code cell, which holds the imports and three helper functions."

> **SAY:** "The first function, duty underscore kW, multiplies flow, specific heat and temperature change to give the heat duty in kilowatts. The second, lmtd underscore counter, calculates the log-mean temperature difference for counter-current flow, and it handles the case where both end differences are equal, which would otherwise divide zero by zero. The third, overall underscore U, divides the duty by the area times that temperature difference. The exchanger area is forty-two square metres."

**DO** Click the **Run arrow** (Execute Cell) at the left edge of the first code cell.

> **SAY:** "I'll click the Run arrow at the left edge of the first code cell to load the libraries and define the functions. A green check mark appears beside the cell, so it ran without errors."

### Scene 2. Load and inspect the data (about 2 minutes)

**DO** Scroll down with the mouse wheel to the heading **Step 1**. Click the Run arrow of the first code cell under it (the one that reads the CSV).

> **SAY:** "I'm scrolling down to the heading Step 1. In the first cell under it, I'll click the Run arrow to load the CSV and add a day column, which converts each timestamp into days since the start."

> **SAY:** "The table below shows the first five hourly readings: hot and cold flow, specific heat, and the inlet and outlet temperatures. The hot stream enters at about one hundred twenty degrees Celsius and the cold stream at about twenty-three."

**DO** Click the Run arrow of the next cell (the summary table). Move the pointer down the output to the `hot_flow_kg_s` row, then the `cold_flow_kg_s` row.

> **SAY:** "In the next cell I'll click the Run arrow to summarize every column by minimum, mean and maximum."

> **SAY:** "I'm moving the pointer down to the hot underscore flow row. The mean hot flow is about eleven point nine kilograms per second, but the minimum is only point zero two three. The cold flow shows the same pattern, with a mean near nine and a minimum of point zero two. Flows that close to zero mean some hours were a shutdown, and those hours would give meaningless coefficients."

### Scene 3. Remove shutdown hours (about 1.5 minutes)

**DO** Scroll down to the cell that starts with `FLOW_MIN = TYPE_HERE`.

> **SAY:** "I'm scrolling down to the next cell, which needs one decision from me: the minimum flow for the exchanger to count as running. Normal flow is about twelve and nine kilograms per second, and the shutdown readings are below point one. I'll choose one kilogram per second, roughly ten percent of normal flow, so every shutdown hour is removed but no real operating hour is lost."

**DO** Double-click the placeholder `TYPE_HERE` on the `FLOW_MIN` line so it is selected. Type `1.0`.

> **SAY:** "I'm double-clicking the placeholder TYPE underscore HERE on the first line to select it, and typing one point zero."

**DO** Click the Run arrow of the cell.

> **SAY:** "I'll click the Run arrow. The output says six shutdown hours were removed and seven hundred fourteen of seven hundred twenty readings were kept. Six hours matches a single shutdown window on the eleventh of September, so the filter did what I intended."

### Scene 4. Duty, temperature difference and U (about 1.5 minutes)

**DO** Scroll down to the heading **Step 2**. Click the Run arrow of the cell under it. Move the pointer along the first output row.

> **SAY:** "I'm scrolling down to the heading Step 2. The cell under that heading adds four columns: the hot-side duty from the hot stream's flow, specific heat and temperature drop; the cold-side duty from the cold stream; the log-mean temperature difference; and U. U uses the average of the two duties, because each side carries some measurement error. I'll click the Run arrow."

> **SAY:** "In the output, the first hour shows a hot duty of about one thousand two hundred forty-two kilowatts, a cold duty of about one thousand two hundred forty-nine, a log-mean temperature difference of about fifty-nine kelvin, and U of about five hundred two watts per square metre kelvin. A coefficient near five hundred is what I would expect for a clean exchanger."

### Scene 5. Energy balance check (about 2.5 minutes)

**DO** Scroll down to the heading **Step 3** and the cell that starts with `TOL = TYPE_HERE`.

> **SAY:** "I'm scrolling down to the heading Step 3, the energy balance check. In a healthy exchanger, the heat the hot side loses equals the heat the cold side gains. If they disagree, a meter or a temperature sensor is probably wrong. Process data usually agrees within a few percent, so I'll set the tolerance at five percent, written as zero point zero five."

**DO** Double-click the placeholder after `TOL =`. Type `0.05`. Click the Run arrow.

> **SAY:** "I'm double-clicking the placeholder after TOL and typing zero point zero five. Now I'll click the Run arrow."

**DO** Move the pointer over the printed lines, then along the four rows of the table.

> **SAY:** "Four readings are outside tolerance and seven hundred ten are kept. The largest mismatch among the kept readings is two point nine percent, comfortably inside five."

> **SAY:** "The table lists the four flagged hours: the fifth, thirteenth, nineteenth and twenty-seventh of September, with mismatches between about six and eight percent. The hot and cold duties are off in both directions, which points to a drifting outlet temperature sensor rather than a real process change. Because U uses the average duty, each of these would bias U by roughly three to four percent, so I'm leaving them out of the trend instead of letting them distort it."

### Scene 6. Fouling limit, trend and chart (about 4 minutes)

**DO** Scroll down to the heading **Step 4** and the first cell, which has two placeholders.

> **SAY:** "I'm scrolling down to Step 4. The first cell under it needs two values. The clean condition comes from the first three days, which is seventy-two hourly readings, enough to average out noise while the tubes are still close to clean. So BASELINE underscore DAYS is three. The fouling limit is twenty percent below clean, a common rule of thumb for scheduling a cleaning, so LIMIT underscore DROP is zero point two zero."

**DO** Double-click the placeholder after `BASELINE_DAYS =`. Type `3`. Double-click the placeholder after `LIMIT_DROP =`. Type `0.20`. Click the Run arrow.

> **SAY:** "I'm double-clicking the first placeholder and typing three, then double-clicking the second placeholder and typing zero point two zero. Now I'll click the Run arrow."

> **SAY:** "Clean U is four hundred ninety-six point one, so the limit is three hundred ninety-six point nine. The current U, averaged over the last twenty-four hours, is four hundred twenty-eight, which is thirteen point seven percent below clean. So the exchanger has not reached the limit yet."

**DO** Scroll down to the next cell (trend and plot). Click its Run arrow. Keep talking and move the pointer along the code while it runs.

> **SAY:** "I'm scrolling to the next cell. It fits a straight line to U against days with polyfit, solves for the day the line reaches the limit, and draws the chart. I'll click the Run arrow."

> **SAY (while it loads):** "While it runs, the code draws each hourly U as a blue dot, the trend as a blue line extended to day forty-five, and the limit as a red dashed line, with a dotted vertical line at the crossing day."

> **SAY:** "The output says the trend is minus two point four seven watts per square metre kelvin per day, and the limit is crossed on day forty-one point nine, which is Monday the twelfth of October, twenty twenty-six."

**DO** Scroll down to the chart. Trace the blue dots, then the trend line, then the red dashed line with the pointer.

> **SAY:** "I'm scrolling down to the chart. The blue dots fall steadily from about five hundred to about four hundred twenty-eight at the end of the data. The blue trend line continues past the data and meets the red dashed limit line where the dotted vertical line drops, near day forty-two. The code also saved the chart as coefficient underscore trend dot png in the Task Files folder, which I'll use in both documents."

**DO** Press Command and S.

> **SAY:** "I'll press Command plus S to save the executed notebook."

**DO** Click the yellow minimize button on the Visual Studio Code window.

### Scene 7. Maintenance memo (Microsoft Word, about 5 minutes)

**DO** Click the minimized Word window thumbnail named **Maintenance Memo Template** in the Dock (hover first to read its name).

> **SAY:** "Now I'll write the memo for the supervisor. I'm clicking the minimized Word window named Maintenance Memo Template, on the Dock near the Trash."

> **SAY:** "The template has a header block addressed to the maintenance supervisor, then four headings: Summary, Key values, Trend chart and Recommendation."

**DO** Click the empty line under **1. Summary**. Type the summary sentence (Typing Sheet, T1). Pause halfway and point at the words you have typed.

> **SAY:** "I'll click the empty line under heading one, Summary, and type a single sentence with the answer, so the supervisor reads the conclusion first."

> **SAY (after typing):** "The sentence states how far fouling has gone and when the limit will be reached."

**DO** Click the right-hand cell beside each label in turn and type the five values (Typing Sheet, T2 to T6).

> **SAY:** "Under heading two, Key values, I'll fill the right-hand column. In the cell beside Clean coefficient I'll type four hundred ninety-six point one W per m2K. Beside Current coefficient, four hundred twenty-eight point zero. Beside Fouling limit, three hundred ninety-six point nine. Beside Predicted day the limit is crossed, Day forty-one point nine. And beside Predicted crossing date, Monday twelve October twenty twenty-six."

**DO** Click the empty line under **3. Trend chart**. Click the **Insert** tab in the ribbon, open the **Pictures** drop-down, choose **Picture from File**. In the file window open the folder **Task Files**, select `coefficient_trend.png`, click **Insert**.

> **SAY:** "I'll click the empty line under heading three, Trend chart, then click the Insert tab in the ribbon, open the Pictures drop-down, and choose Picture from File. In the file window I'll open the Task Files folder, select coefficient underscore trend dot png, and click Insert."

**DO** If the picture is large, drag its lower-right corner handle toward the upper left until it is about five inches wide. Point at the status bar at the bottom-left of the window.

> **SAY:** "The picture is too large for a one-page memo, so I'll drag its lower-right corner handle toward the upper left until it is about five inches wide. I'm checking the status bar at the bottom-left of the window: it reads Page 1 of 1, so the memo still fits on a single page."

**DO** Click the empty line under **4. Recommendation**. Type the recommendation (Typing Sheet, T7). Pause halfway.

> **SAY:** "Last, I'll click the empty line under heading four, Recommendation, and type the decision: clean E-101 at the next planned shutdown, no later than Friday the ninth of October. The date keeps a three-day margin, because a linear trend is only an estimate."

**DO** Click **File** in the menu bar, then **Save As**. In the dialog set the name to `Maintenance Memo`, keep the folder **Task Files** and the format **Word Document (.docx)**, click **Save**.

> **SAY:** "I'll save it under a new name so the template stays untouched. I'm clicking File in the menu bar at the top-left, choosing Save As, typing Maintenance Memo in the name field, checking that the folder is Task Files and the format is Word Document, and clicking Save."

**DO** Click the yellow minimize button on the Word window.

### Scene 8. Briefing slides and PDF (PowerPoint, about 5 minutes)

**DO** Click the minimized PowerPoint window in the Dock.

> **SAY:** "Now the briefing. I'm clicking the minimized PowerPoint window in the Dock."

> **SAY:** "The template has two blank slides. In the thumbnail panel on the left, slide one is selected."

**DO** Click the title box at the top of slide 1 (it reads Click to add title). Type the slide 1 title (Typing Sheet, T8).

> **SAY:** "I'll click the title box at the top of slide one, which says Click to add title, and type the headline finding: E-101 will reach its fouling limit on Monday twelfth October."

**DO** Click the **Insert** tab, open **Pictures**, choose **Picture from File**, select `coefficient_trend.png` in **Task Files**, click **Insert**. Drag the picture below the title and use a corner handle to size it so the whole chart is visible.

> **SAY:** "Next I'll click the Insert tab, open the Pictures drop-down, choose Picture from File, select coefficient underscore trend dot png in Task Files, and click Insert. I'll drag the picture below the title and use its corner handle to size it so the whole chart is visible."

**DO** Click the slide 2 thumbnail in the left panel. Click its title box. Type the slide 2 title (T9).

> **SAY:** "I'll click the slide two thumbnail on the left, then its title box, and type: Recommendation, clean E-101 by Friday ninth October."

**DO** Click the large text box under the title. Type bullet 1 (T10). Press Return. Type bullet 2 (T11).

> **SAY:** "Now I'll click the large text box under the title and type the first bullet, the recommended action. I'll press Return for a second bullet, which states the risk. Weekly rechecks matter because fouling rarely follows a perfectly straight line."

**DO** Click **File**, **Save As**, name `Fouling Briefing`, folder **Task Files**, format **PowerPoint Presentation (.pptx)**, click **Save**. Then click **File**, **Export**, choose **PDF** in the File Format drop-down, keep the name `Fouling Briefing`, click **Export**.

> **SAY:** "I'll save the deck first: File in the menu bar, Save As, the name Fouling Briefing, the folder Task Files, the PowerPoint Presentation format, and Save. Then File, Export. In the File Format drop-down I'll choose PDF, keep the name Fouling Briefing, and click Export."

**DO** Click the yellow minimize button on the PowerPoint window.

### Scene 9. Verify by hand and across files (about 5 minutes)

**DO** Click the Visual Studio Code thumbnail in the Dock. Scroll to the heading **Step 5** and the cell with `ROW = TYPE_HERE`.

> **SAY:** "To verify, I'll go back to Visual Studio Code and check one reading by hand. I'm clicking its thumbnail in the Dock, then scrolling down to the last two cells, Step 5."

**DO** Double-click the placeholder after `ROW =`. Type `400`. Click the Run arrow. Move the pointer down the output.

> **SAY:** "I'll double-click the placeholder after ROW and type four hundred. Row four hundred is the reading for the seventeenth of September at sixteen hundred, a normal operating hour with a good energy balance. I'll click the Run arrow."

> **SAY:** "The output lists the raw flow and temperatures, plus the notebook's answers: a hot duty of about one thousand one hundred forty-three point five kilowatts, a log-mean temperature difference of fifty-nine point five kelvin, and U of four hundred fifty-eight."

**DO** In the last cell, replace each of the three placeholders: `dt1` (T12), `dt2` (T13), `q_by_hand` (T14). Type each separately. Click the Run arrow.

> **SAY:** "In the last cell I'll type the hand calculation from the raw numbers. The first temperature difference is hot in minus cold out: one hundred twenty point four minus fifty-six point two nine. The second is hot out minus cold in: eighty point eight nine minus twenty-five point eight. And the duty is hot flow times specific heat times the hot temperature drop: eleven point eight five seven times two point four four one, times the quantity one hundred twenty point four minus eighty point eight nine. I'll click the Run arrow."

> **SAY:** "By hand I get one thousand one hundred forty-three point five kilowatts and a log-mean temperature difference of fifty-nine point four nine kelvin, identical to the notebook. U comes out four hundred fifty-seven point seven against four hundred fifty-eight point zero, a difference of under a tenth of a percent, because the notebook uses the average of both duties. So the calculation chain checks out."

**DO** Press Command and S. Move the pointer down the Explorer panel on the left.

> **SAY:** "I'll press Command plus S to save the notebook again. In the Explorer panel on the left, the new files have appeared: coefficient underscore trend dot png, Maintenance Memo dot docx, Fouling Briefing dot pptx and Fouling Briefing dot pdf. So every output was saved."

**DO** Click the yellow minimize button on Visual Studio Code. Click the minimized **Maintenance Memo** Word window in the Dock. Point at the table values.

> **SAY:** "Now I'll confirm the documents match the notebook. I'm clicking the Word window named Maintenance Memo in the Dock. In the Key values table, the clean coefficient four hundred ninety-six point one, the current coefficient four hundred twenty-eight, the limit three hundred ninety-six point nine, day forty-one point nine and Monday twelve October all match the notebook output."

**DO** Click the yellow minimize button on Word. Click the PowerPoint window in the Dock. Show slide 1, then click the slide 2 thumbnail.

> **SAY:** "Last, I'll click PowerPoint in the Dock. The slide one title gives the same Monday twelfth of October crossing, and on slide two the cleaning date, Friday the ninth of October, is three days earlier, matching the memo. The same chart appears in the notebook, the memo and the slide."

**DO** Leave PowerPoint on slide 2, open. Everything is saved.

---

## Part 4. Epilogue (target 3:30, maximum 4:00)

Start immediately after Scene 9, with all outputs saved and before bringing TaskRecorder back. Your mouse can stay still. About 420 words at a calm pace, which is roughly three and a half minutes.

> **SAY:** "The work is finished and saved, so I'll summarize how it went."

> **SAY (completion and outcome):** "I verified the result in three ways. The energy balance check showed every kept reading agreeing within three percent. I recalculated one reading by hand and matched the notebook's duty and temperature difference exactly, with U within a tenth of a percent. And I confirmed the same numbers appear in the notebook, the memo and the slides. The outcome is that E-101 is thirteen point seven percent below its clean coefficient today, and the straight-line trend reaches the twenty percent limit on Monday the twelfth of October, so I recommended cleaning by Friday the ninth. The main limitation is that the prediction extends thirty days of data about twelve days forward with a straight line, so the date is an estimate, not a guarantee."

> **SAY (approach):** "My approach was to clean the data first, because shutdown hours and faulty sensor readings would corrupt everything after them. I checked the energy balance before trusting U, since U depends on the duty, and then compared a simple trend with a rule-of-thumb limit. A simple trend like that is easy for a maintenance supervisor to follow and challenge."

> **SAY (challenges):** "The hardest part was deciding what to exclude. Removing the six shutdown hours was clear-cut. The four readings with six to eight percent imbalance needed judgment. I excluded them because a drifting sensor can bias U by several percent, and I reported them rather than deleting them silently. I also kept every threshold as a visible value in its cell, so a reviewer can see my decisions and change them."

> **SAY (quality):** "The result is good enough for planning. The scatter around the trend line is only about two watts per square metre kelvin, small next to the roughly hundred-unit drop from clean to the limit. The weaknesses are that fouling is rarely perfectly linear, the model ignores changes in flow and fluid properties, and the three-day margin is a judgment, not a calculated bound."

> **SAY (reflection):** "With more time I would fit the fouling resistance instead of U, because it is the physically meaningful quantity. I would give the crossing date as a range using confidence intervals, and I would automate the weekly recheck I recommended."

> **SAY (insight):** "One thing a less experienced engineer might overlook is that the log-mean temperature difference is undefined when the two end differences are equal, and that near-zero flow hours silently produce nonsense coefficients that can drag a trend line toward an early cleaning. Both are easy to miss unless you look at the raw data first."

**DO** After the last word, bring TaskRecorder to the front and click **Stop Recording** in silence. Say nothing about stopping or about TaskRecorder.

---

## Part 5. Typing sheet (exact text)

Type at a natural pace. Keep each burst under 25 to 30 seconds. Read each string from a second device.

| # | Where | Type exactly |
|---|---|---|
| Cell FLOW_MIN | notebook | `1.0` |
| Cell TOL | notebook | `0.05` |
| Cell BASELINE_DAYS | notebook | `3` |
| Cell LIMIT_DROP | notebook | `0.20` |
| Cell ROW | notebook | `400` |
| Cell dt1 | notebook | `120.4 - 56.29` |
| Cell dt2 | notebook | `80.89 - 25.8` |
| Cell q_by_hand | notebook | `11.857 * 2.441 * (120.4 - 80.89)` |
| T1 | Word, Summary | E-101 is 13.7 percent below its clean coefficient, and the 20 percent fouling limit is predicted to be crossed on Monday 12 October 2026. |
| T2 | Word, table row 1 | 496.1 W/m2K |
| T3 | Word, table row 2 | 428.0 W/m2K |
| T4 | Word, table row 3 | 396.9 W/m2K |
| T5 | Word, table row 4 | Day 41.9 |
| T6 | Word, table row 5 | Monday 12 October 2026 |
| T7 | Word, Recommendation | Clean E-101 at the next planned shutdown, no later than Friday 9 October 2026, which keeps a three-day margin because the linear trend is only an estimate. |
| T8 | PowerPoint slide 1 title | E-101 will reach its fouling limit on Monday 12 October |
| T9 | PowerPoint slide 2 title | Recommendation: clean E-101 by Friday 9 October |
| T10 | PowerPoint slide 2 bullet 1 | Clean E-101 at the next planned shutdown, no later than Friday 9 October. |
| T11 | PowerPoint slide 2 bullet 2 | Risk: the linear trend is an estimate, so recheck the coefficient weekly until then. |

Typing totals about three and a half minutes of a 30 to 35 minute video, well under the 20 percent limit. If you type slowly, shorten T10 and T11 first.

---

## Part 6. How each guide rule is covered

| Guide or review rule | Where the script handles it |
|---|---|
| Intro only the one sentence, under 20 seconds, Goal document shown then minimized | Part 2 |
| TaskRecorder minimized right after Start, never narrated | Parts 1 and 2 |
| What, where and why for every step; name the control and its location | Every scene |
| Narrate every scroll and say where you stopped | Scenes 1 to 6 |
| Say every keyboard shortcut aloud | Command plus S in Scenes 6 and 9 |
| Pause one second after every click | "How to read it" |
| No silence over 45 seconds; keep talking while cells load | Scene 6 loading line |
| Typing bursts short, under 20 percent total | Typing Sheet |
| Prepared inputs described as free of royalties and copyright, without naming how they were made | Scene 1 |
| No restricted apps, no AI, no personal info, no project references | Setup checklist |
| One ordinary window at a time; minimize unused windows; no Full Screen | Yellow minimize steps in Scenes 6 to 9 |
| Verification and complete saved outputs before stopping | Scene 9 |
| Epilogue 3 to 4 minutes, maximum 4:00, after the work and before TaskRecorder returns | Part 4 |
| Stop silently | Part 4 |

---

## Part 7. After recording

1. Wait for TaskRecorder to move through Stopping, Archiving and Idle. Click **Show Recordings** and find the newest `recording_TIMESTAMP` folder and zip. Do not rename, edit or unzip them.
2. Open `video.mp4` in QuickTime and check the beginning, middle and end: picture clear, narration audible, ends after the epilogue. Check the video is between 15:00 and 50:59. Check the screenshot count is above 0.5 per second of video, and that the folder holds the PNG screenshots, `event.jsonl` and the other `.jsonl` files from the same attempt.
3. Build `Deliverables.zip` with spaces in the names, using the mapping below. Do not include Metadata.rtf.

| Put in Deliverables | From |
|---|---|
| input 1.csv | exchanger_data.csv |
| input 2.ipynb | the untouched starter notebook (from `Deliverables inputs only.zip`) |
| input 3.docx | Maintenance Memo Template.docx |
| input 4.pptx | Briefing Template.pptx |
| input 5.docx | Opening Note.docx |
| final output 1.ipynb | the executed fouling_analysis.ipynb |
| final output 2.png | coefficient_trend.png |
| final output 3.docx | Maintenance Memo.docx |
| final output 4.pptx | Fouling Briefing.pptx |
| final output 5.pdf | Fouling Briefing.pdf |

There are no intermediate artifacts in this workflow. From the folder that holds `Deliverables`, build the zip with:
`zip -r -X "Deliverables.zip" Deliverables -x "*.DS_Store"` then check it with `unzip -l "Deliverables.zip"`. Do not use Finder's Compress.

4. **Upload four files:** `Metadata.rtf` (separately), `video.mp4`, `recording_TIMESTAMP.zip`, `Deliverables.zip`.
5. **Studio fields:** resolution, light or dark mode, Dock position, wallpaper changed, Mac chip, GPU, RAM, storage, input types, and Final Note. If your inputs are covered under Part 0, write exactly `AI-generated before recording`. Do not name an AI tool in Final Notes beyond what Studio requires.
6. Run both AutoQCs, fix or comment on anything flagged, tick each manual check only after checking it against the recording, tick the epilogue box, confirm the checklist and PII boxes, tick the final confirmation, and submit.

---

## Goal text (paste into TaskRecorder, the opening note and the Metadata.rtf Request)

I am a process engineer at a chemical plant, and I need to tell the maintenance supervisor when a shell-and-tube heat exchanger should be taken offline for cleaning. Using 30 days of synthetic hourly temperature and flow readings, I will use Visual Studio Code to run a notebook that calculates heat duty, log-mean temperature difference and the overall heat transfer coefficient, checks that the hot-side and cold-side energy balances agree within 5 percent, plots the coefficient over time against a 20 percent fouling limit, and fits a trend line to estimate the day the limit is crossed. I will then record the key results and the recommended cleaning date in a one-page Microsoft Word memo, and build a two-slide PowerPoint briefing with the chart and the recommendation, exported as a PDF.
