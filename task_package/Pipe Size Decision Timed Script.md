# Pipe Size Decision: Timed Script

Oct 17, 2026


## Read this first

This script has 19:00 of speaking and doing, built for a video of about 32:18. Your earlier videos ran about 1.6 times the script time, and you will now speak slower with a pause after every click, so it is planned for about 1.7 times. That keeps a wide margin above the 15:00 minimum and below the 45:59 cap. It follows the same layout as your droplet script, and it avoids every mistake listed in your Review Lessons file. The table below shows where.

| Mistake or advice from your reviews | How this script avoids it |
|---|---|
| Critical: scrolling was never narrated. Say where you scroll to. | Every scroll is its own action with its own spoken line, 12 of them: I am scrolling down with the mouse wheel until I reach [heading]. Nothing scrolls in silence. |
| What and Why were fine, Where was missing. Say which part of the screen you click, every time. | Every click names the control and its place: the Dock along the left edge, the menu bar along the top, the yellow button in the top left corner, the Run arrow at the left edge of the cell, the Explorer sidebar on the left, the ribbon across the top, the Save button at the bottom right. |
| It felt rushed. Too many things in one task. | The task is deliberately small: 7 parts, 587 typed characters, three genuine apps, and most steps are pointer clicks and speaking. Lines are short, one action each. Pause one second after every click and one second between sentences. |
| Do not say that no personal information shows. Do not narrate opening TaskRecorder and Stop Recording. | Both removed. The last SAY line is the closing statement. You then silently click the TaskRecorder icon and Stop Recording. |
| Mouse idle for more than 90 seconds. Keep the pointer moving with purpose. | The pointer only moves to name something, never to look busy. It is never still for more than 20 seconds, and the Writer Guidelines limit is 45. Every typing burst is one line of at most 30 seconds, and the pointer goes back to the code right after it. |
| Vague words such as here and this. Name the action, the control, its location and the reason. | Each line gives the action, the exact control, its location and the reason, using real names. |
| Review B: pause 1 second after every click. | Every click in the DO lines is followed by the pointer resting on the next thing you name. Count one in your head after each click before you speak. |
| Review B: the Task Description in TaskRecorder was cut off. | Before you press record, drag the TaskRecorder window larger until every line of the Task Description is visible. |
| Review B: video.mp4 was submitted as screen_recording.mp4. | After recording, upload the file named video.mp4 from the recording folder, exactly as it is. |
| AutoQC: some narration was faster than 220 words a minute. | Short lines, one action each, and the plan assumes a slow pace of about 1.7 times the script time. |
| AutoQC: recording showed 12 of 15 core parts, because the text promised more than the video showed. | The Goal coverage table below lists every promise in the approved Goal and the step that shows it. Nothing is promised that is not shown. |


## Goal coverage: every promise in the approved text, and where it is shown

| Promised in the approved Goal and checks | Shown in step |
|---|---|
| Visual Studio Code opens a Jupyter notebook | 2.1, 2.2 |
| Load a CSV catalog of candidate pipe sizes with their costs | 2.3, 3.1 |
| Calculate velocity, Reynolds number, friction factor, pressure drop, pump power and yearly total cost | 2.2, 3.3 |
| Screen out sizes that break the velocity limit and pick the lowest cost size that remains | 3.4, 3.5 |
| Check that every flow is turbulent by its Reynolds number | 3.3, 4.2 |
| Check that the chosen size is inside the velocity limit | 3.5, 4.1 |
| Recalculate the pressure drop for one size in a separate cell and confirm it matches | 4.2 |
| Confirm the lowest point on the chart matches the table | 4.1 |
| PowerPoint: one-slide cost versus pipe size chart | 5.1 to 5.4 |
| Microsoft Word: one-page line sizing datasheet | 1.2 to 1.5, 6.1 to 6.4 |
| Numbers on the slide and in the datasheet match the notebook | 5.4, 6.2, 7.1 |


## The five rules while recording

- Pointer. After every click and every typing burst, move the pointer onto the thing you are about to name and keep it there while you explain it. Drag across code to highlight it. Never wiggle.
- Narration. Say: I'm [action] on [exact control, and where it is on the screen], because [reason]. Say the real name, never just here, this or that. One sentence per action. Speak slowly and leave one second after every click.
- Scrolling. Say it every time: I am scrolling down with the mouse wheel until I reach [the heading or part you stop at]. Keep the pointer on the page while you scroll, and name what you find when you stop.
- Typing. Say what you will type and why, type one line in silence, then explain it with the pointer. A burst of 25 seconds is the target, stop at 30.
- Audio. Quiet room, door closed, notifications off, same distance from the microphone, do not touch the desk while speaking, and never mutter. If you lose your place, stop talking, find it, then say the next line.

## Timing and checkpoints

The clock in the menu bar shows seconds. Write down the time when you press Start Recording, and check it at each checkpoint below. Do not use a stopwatch on the recorded screen. The times are estimates from the word count of each SAY line, the number of actions and the typing.

| Part | Script length | Script clock | Real clock to expect (1.7 times) |
|---|---|---|---|
| Intro and design basis in Word | 2:20 | 2:20 | 3:58 |
| VS Code setup | 2:00 | 4:20 | 7:22 |
| Load, set the limits, calculate and screen | 5:30 | 9:50 | 16:43 |
| Chart, cross-check and save | 2:40 | 12:30 | 21:15 |
| One slide in PowerPoint | 2:35 | 15:05 | 25:38 |
| Datasheet in Word | 2:55 | 18:00 | 30:36 |
| Cross-check and stop | 1:00 | 19:00 | 32:18 |

If you are more than 3 minutes behind a checkpoint, use the cut order in the typing section right away. If you reach 38:00 and are not in Part 7, go straight to Part 7. The video must stay between 15:00 and 45:59, so a finish near 32:18 leaves a wide safety margin on both sides.


## Before you press record

Do all of this before pressing Start Recording. The guide forbids setting up an app after recording starts.

- Studio first. The idea must already be approved in Studio. The Goal you paste into TaskRecorder, the opening note and the Metadata.rtf Request must be the approved Goal, word for word. All four input files must be made before recording starts, with no private data. Download the Metadata.rtf template from your claimed task and fill it in before recording.
- Fresh folder. Make a folder named pipe_study and unzip the four files from the starter kit into it. It must hold only those four files, with no .vscode, .DS_Store or ~$ files, and no artifact files. Open the folder in VS Code and open input_3_starter_notebook.ipynb, with the Explorer sidebar visible on the left.
- Kernel. In the notebook, click Select Kernel at the top right and choose a Python environment that already has pandas, numpy and matplotlib. Do not run or save anything in the starter in the study folder. Test the environment in the dry run below: if the first cell there shows a ModuleNotFoundError, choose another environment.
- Quit Grammarly and every background app except Insightful, Accessibility Inspector and TaskRecorder. In VS Code, do not sign in to GitHub or Settings Sync, and close the welcome tab and extra panels.
- Word and PowerPoint. Word signed in with the assigned account, no Copilot button on screen. Open exactly two Word documents: your opening note with only the Goal in it, and input_1_datasheet_template.docx. In PowerPoint open input_4_review_slide_template.pptx. The right-click list on the Dock icon shows these open windows, which is how the script opens them.
- Desktop. Dock on the left edge of the screen (if yours is on the right edge, say right instead of left in every line), clock with seconds, unique wallpaper, mouse cursor size and colour left at default, Accessibility Inspector running with its window closed, Insightful minimized, notifications off, Finder closed. The Mac is plugged in with enough free storage. Zoom windows with the Window menu, never the green Full Screen button, then minimize every window except your opening note. Metadata.rtf stays closed.
- TaskRecorder. Signed in, three permissions green, microphone on, Goal pasted, apps entered as Visual Studio Code, PowerPoint, Microsoft Word. Drag the TaskRecorder window larger until every line of the Task Description is visible. Read this script from another device, never on the recorded screen.
- Audio test, 1 minute. Say one SAY line at your planned speed, type for 20 seconds, and play it back on headphones. Your voice must be clear and louder than the typing, with no fan hum.
- Dry run. In a temporary folder with a copy of the starter and the CSV, type every cell once, click through the PowerPoint and Word steps, and practise the file window for the picture so you know where artifact_3.png appears. Then delete the folder. This warms up the plotting cache and proves the environment works.
Typing speed test, 2 minutes. This decides your typing share. In a scratch notebook outside the study folder, type the longest line from step 3.5 (56 characters): table['pass'] = table.velocity_m_s.between(MIN_V, MAX_V) with a stopwatch and no talking. Divide your seconds by 56 to get seconds per character, then read your row below.

| Seconds per character | Seconds for the 56 character line | Typing share at 32:18 | What to do |
|---|---|---|---|
| 0.25 | 14 | 8 % | Record |
| 0.35 | 20 | 11 % | Record |
| 0.40 | 22 | 12 % | Record |
| 0.45 | 25 | 14 % | Use trim list 1, then record |

These shares are estimates: 587 characters times your seconds per character, divided by the video length. The limit is strictly below 20 percent, or 30 percent only if Loki confirms this counts as a coding plus writing task. I do not know exactly how AutoQC counts typing, so the test decides, not my table.

Keys. This script never needs the less-than, greater-than, dollar, slash, percent or hyphen keys when typing. The special characters you type are: ' ( ) , . = [ ] _ and Capital letters. Test them once before recording: type the 56 character line above in your scratch notebook, and type Use 8 inch pipe. in a scratch Word page. If a key does not appear, fix that before recording.


## Part 1: Intro and design basis in Word (0:00 to 2:20)

No typing in this part. Your pointer does the work: rest it on each row as you name it. Every scroll is narrated with where it stops. Never read your Task Description aloud, never say an AI tool name, your name, the project, the platform or the company, and never narrate TaskRecorder.


**1.1 Intro (15 seconds)**

DO: Click Start Recording in TaskRecorder, then click the yellow button in the top left corner of the TaskRecorder window to minimize it. Say nothing while you do this. Leave your opening note visible.

SAY, only this: "I will be beginning my task soon. Here is the workflow I have in mind."

DO: Wait one second. Click the yellow button in the top left corner of the note window to minimize it.


**1.2 Open the datasheet template (25 seconds)**

DO: Move the pointer to the Word icon in the Dock along the left edge of the screen. Right-click it. In the list that opens to the right of the Dock, click input_1_datasheet_template.docx.

SAY: "I'm right-clicking the Word icon in the Dock along the left edge of the screen. In the list that opens to its right, I'm clicking input_1_datasheet_template.docx, a prepared input file, free of royalties and copyright. It is the line sizing datasheet for the cooling water line. Its top section holds the design basis I need before I touch any data."


**1.3 Line and fluid (40 seconds)**

DO: Rest the pointer on the title at the top of the page, then on heading 1, Design basis. Move the pointer down the left column of the first table, resting on line number, service, design flow, line length, fluid and pipe in turn.

SAY: "At the top of the page, I'm pointing at the title, then at heading 1, Design basis. In the first table, I'm moving down the left column. The line is CW one oh one, a cooling water supply. The design flow is 150 cubic metres per hour, through 250 metres of line including fittings. The fluid is water, with a density of 996 and a viscosity of 0.8 milli Pascal seconds. The pipe is commercial steel with a roughness of 0.045 millimetres."


**1.4 Economics (35 seconds)**

DO: Move the pointer down to the next three rows and rest on each: pump efficiency, electricity price, pipe cost basis.

SAY: "Now I'm pointing at the next three rows. Pump efficiency is 70 percent. Electricity costs 12 cents per kilowatt hour, with 8,000 running hours a year. The pipe cost is spread over 10 years at 8 percent, a capital recovery factor of 0.149. These rows turn pressure drop into a yearly pumping cost and the pipe price into a yearly cost, so every size can be compared on one number."


**1.5 The velocity limits, then minimize (40 seconds)**

DO: Rest the pointer on the last row of the first table, Plant velocity limits. Scroll down with the mouse wheel until heading 2, Selection, is near the top of the window. Rest the pointer on the grey prompts. Click the yellow button in the top left corner of the Word window.

SAY: "The last row decides this task. The plant velocity limits are a minimum of 1.0 and a maximum of 2.0 metres per second for cooling water lines. Now I'm scrolling down with the mouse wheel until I reach heading 2, Selection. I'm pointing at the grey prompts, which are blank on purpose. I will fill them at the end, once the notebook has given me the answer. Now I'm clicking the yellow button in the top left corner of the window to minimize Word."


## Part 2: VS Code setup (2:20 to 4:20)

One short typing burst, the file name. The rest is pointer work.


**2.1 Bring VS Code forward and save a copy (40 seconds)**

DO: Click the Visual Studio Code icon in the Dock along the left edge of the screen. Move to the menu bar along the top of the screen and click File. In the dropdown, click Save As.

SAY: "I'm clicking the Visual Studio Code icon in the Dock along the left edge of the screen. Now I'm clicking File in the menu bar at the top of the screen, then Save As in the dropdown. I will type artifact one as the name, because the starter must stay untouched, and click the Save button at the bottom right of the window."

DO: Type this in silence, then click the Save button at the bottom right of the Save window:

```
artifact_1.ipynb
```
SAY: "Saved. From now on I save with Command and S."

Do not press Command + S before this Save As, or you overwrite the starter.


**2.2 Run the setup cell (50 seconds)**

DO: Point at the kernel name in the top right corner of the notebook. Click the Run arrow at the left edge of the first code cell. Scroll down slowly inside the cell with the mouse wheel, resting the pointer on size_table, then plot_costs, then colebrook_check.

SAY: "In the top right corner of the notebook, the kernel name is my Python environment. I'm clicking the Run arrow at the left edge of the first code cell to load the helper functions. A green tick under the arrow means it has finished. I'm scrolling down slowly with the mouse wheel and pointing at size_table, which calculates velocity, Reynolds number, friction factor, pressure drop, pump power and yearly cost for each size. Then plot_costs, which draws the chart, and colebrook_check, which I will use to verify the pressure drop. This starter is a prepared input file, free of royalties and copyright. The decisions are mine, and I will type them."


**2.3 Look at the catalog (40 seconds)**

DO: Click input_2_pipe_catalog.csv in the Explorer sidebar on the left side of the VS Code window. Rest the pointer on the column headers in the first row. Rest it on the 8 row. Click the artifact_1.ipynb tab at the top of the editor.

SAY: "I'm clicking input_2_pipe_catalog.csv in the Explorer sidebar on the left side of the window. It is a synthetic catalog prepared for this exercise, free of royalties and copyright. In the first row, I'm pointing at the headers: nominal size in inches, inside diameter in millimetres, roughness in millimetres and installed cost per metre. Each row is one candidate pipe. I'm pointing at the 8 row: 202.7 millimetres inside and 330 dollars per metre installed. Now I'm clicking the artifact_1 tab at the top of the editor to return to the notebook."


## Part 3: Load, set the limits, calculate and screen (4:20 to 9:50)

Routine for every cell: scroll to the heading, click inside the empty code cell under it, say what you will type and why, type one burst in silence, click the Run arrow at the left edge of the cell, then rest the pointer on each result as you explain it. Enter between lines is not a shortcut, so you do not announce it. Where a step lists several lines, each line is its own burst. If a suggestion list appears while you type, press Escape once, then carry on. VS Code indents for you, so never type leading spaces. VS Code closes brackets and quotes for you, and typing the closing one types over it. If a double bracket ever appears, press Delete once.


**3.1 Load the catalog, under heading 1 (55 seconds)**

DO: Scroll down with the mouse wheel until heading 1, Load the catalog, and the empty cell under it are in the middle of the window. Click inside the empty cell.

SAY, before typing: "I'm scrolling down with the mouse wheel to heading 1, Load the catalog, and clicking inside the empty code cell under it. I will type two lines: the first reads the CSV into a table called catalog, the second shows it, so I can confirm all seven sizes loaded."

```
catalog = load_catalog()
catalog
```
DO: Click the Run arrow at the left edge of the cell. Rest the pointer on the first row of the output under the cell, then on the last.

SAY: "I'm clicking the Run arrow at the left edge of the cell. In the output under it, I'm pointing at the first row, 3 inch, and the last row, 12 inch. All seven sizes are there, and the numbers match the file."


**3.2 Set the velocity limits, under heading 2 (80 seconds)**

DO: Scroll down with the mouse wheel until heading 2, Set the velocity limits, and the parameters cell under it are in the middle of the window. Rest the pointer on the flow line, then the length line, then the efficiency, price, hours and capital recovery lines in turn.

SAY: "I'm scrolling down with the mouse wheel to heading 2, Set the velocity limits. In the cell under it, I'm pointing at the design inputs, and they match the datasheet. Flow is 150 cubic metres per hour. Line length is 250 metres. Water density is 996 and viscosity is 0.0008 Pascal seconds. Pump efficiency is 0.70. Electricity is 0.12 dollars per kilowatt hour, for 8,000 hours a year. The capital recovery factor is 0.149."

DO: Rest the pointer on the MIN_V line, then the MAX_V line.

SAY, before typing: "The two limits at the bottom are still None. The datasheet says the minimum is 1.0 and the maximum is 2.0 metres per second, so I will type those. A pipe that runs too fast wears out and is noisy, and one that runs too slow lets sediment settle."

DO: Double-click the word None on the MIN_V line to select it. Type this in silence:

```
1.0
```
DO: Double-click the word None on the MAX_V line to select it. Type this in silence:

```
2.0
```
DO: Click the Run arrow at the left edge of the cell.

SAY: "I'm clicking the Run arrow at the left edge of the cell. The minimum is 1.0 and the maximum is 2.0 metres per second, as the datasheet says."


**3.3 Calculate every size, under heading 3 (65 seconds)**

DO: Scroll down with the mouse wheel until heading 3, Calculate every pipe size, and the empty cell under it are in the middle of the window. Click inside the empty cell.

SAY, before typing: "I'm scrolling down with the mouse wheel to heading 3 and clicking inside the empty code cell under it. I will type two lines: the first builds the results table for all sizes using my inputs, the second shows it."

```
table = size_table(catalog, params)
table
```
DO: Click the Run arrow at the left edge of the cell. Scroll the output down with the mouse wheel until all seven rows are visible. If columns are cut off, scroll the output sideways with two fingers on the trackpad. Rest the pointer on the velocity_m_s column, then friction, then reynolds, then dp_kpa, then pump_kw, then total_usd.

SAY: "I'm clicking the Run arrow at the left edge of the cell. I'm scrolling the output down with the mouse wheel until all seven rows are visible. In the velocity column, the 3 inch pipe runs at 8.74 metres per second, and the 12 inch at only 0.58. In the friction column, the friction factor is about 0.016 to 0.018 in every size. In the Reynolds column, every number is above 4,000, so the flow is turbulent in every size and the friction equation is valid. In the pressure drop column, the 3 inch pipe loses 2,185 kilopascals and needs 130 kilowatts, which is not workable. The 8 inch pipe loses 16.7 kilopascals and needs 1 kilowatt. The last column is yearly total cost, pumping energy plus pipe cost."


**3.4 The cheapest size on paper, under heading 4 (40 seconds)**

DO: Scroll down with the mouse wheel until heading 4, Screen by velocity and pick the size, and its first empty cell are in the middle of the window. Click inside the empty cell.

SAY, before typing: "I'm scrolling down with the mouse wheel to heading 4 and clicking inside the first empty code cell under it. I will type one line that shows the single cheapest row, before I apply any limit."

```
table.nsmallest(1, 'total_usd')
```
DO: Click the Run arrow at the left edge of the cell. Rest the pointer on the nps_in value, then the velocity_m_s value, then the total_usd value.

SAY: "I'm clicking the Run arrow at the left edge of the cell. The cheapest size on paper is the 6 inch pipe, at 11,809 dollars a year. But its velocity is 2.23 metres per second, above the 2.0 limit. So the cheapest size cannot be my answer."


**3.5 Screen and pick, same heading (80 seconds)**

DO: Click inside the second empty cell under heading 4.

SAY, before typing: "In the second empty cell, I will type three lines. Line one marks each size Pass if its velocity is between the two limits. Line two keeps only the passing sizes and takes the cheapest. Line three shows it."

```
table['pass'] = table.velocity_m_s.between(MIN_V, MAX_V)
```
DO: Press Enter.

SAY, before typing: "Line two keeps the rows marked Pass and takes the one with the lowest total cost."

```
best = table[table['pass']].nsmallest(1, 'total_usd')
```
DO: Press Enter.

SAY, before typing: "Line three shows the answer."

```
best
```
DO: Click the Run arrow at the left edge of the cell. Rest the pointer on the nps_in value, then the velocity_m_s value, then the total_usd value, then the pass value.

SAY: "I'm clicking the Run arrow at the left edge of the cell. The size that remains is the 8 inch pipe. Its velocity is 1.29 metres per second, inside the limits, and the pass column says True. Its total cost is 13,249 dollars a year. It costs about 1,440 dollars a year more than the 6 inch pipe, and I judge that worth paying to stay inside the plant standard."


## Part 4: Chart, cross-check and save (9:50 to 12:30)

Three short cells, then the files appear in the Explorer.


**4.1 The chart, under heading 5 (55 seconds)**

DO: Scroll down with the mouse wheel until heading 5, Chart yearly total cost, and the empty cell under it are in the middle of the window. Click inside the empty cell.

SAY, before typing: "I'm scrolling down with the mouse wheel to heading 5 and clicking inside the empty code cell under it. I will type one line that draws the chart and saves it as artifact three."

```
plot_costs(table)
```
DO: Click the Run arrow at the left edge of the cell. Rest the pointer on the green bar, then the 6 inch gray bar, then the 3 inch bar, then the legend in the upper right corner of the chart.

SAY: "I'm clicking the Run arrow at the left edge of the cell. The green bar is the 8 inch pipe, the only size inside the limits. The lowest bar overall is the gray 6 inch pipe at 11,809, which matches the table, but it is outside the limits. The 3 inch bar is cut off at the top, and its label says it is off scale. The legend in the upper right corner explains the colours."


**4.2 Cross-check the pressure drop, under heading 6 (60 seconds)**

DO: Scroll down with the mouse wheel until heading 6, Cross-check the pressure drop, and the empty cell under it are in the middle of the window. Click inside the empty cell.

SAY, before typing: "I'm scrolling down with the mouse wheel to heading 6 and clicking inside the empty code cell under it. I will type one line that recalculates the pressure drop of the chosen size with a different friction equation, the iterative Colebrook method, to prove the table is reliable."

```
colebrook_check(catalog, best, params)
```
DO: Click the Run arrow at the left edge of the cell. Rest the pointer on the table pressure drop line, then the Colebrook line, then the difference line, then the flow regime line.

SAY: "I'm clicking the Run arrow at the left edge of the cell. The table pressure drop is 16.7 kilopascals, and the Colebrook pressure drop is 16.7 as well. The difference is minus 0.21 percent, well inside 1 percent. The flow regime is turbulent, with a Reynolds number of 325,847. So the table is reliable."


**4.3 Save the table and the notebook, under heading 7 (50 seconds)**

DO: Scroll down with the mouse wheel until heading 7, Save the results table, and the empty cell under it are in the middle of the window. Click inside the empty cell.

SAY, before typing: "I'm scrolling down with the mouse wheel to heading 7 and clicking inside the empty code cell under it. I will type one line that saves the results table as artifact two."

```
table.to_csv('artifact_2.csv', index=False)
```
DO: Click the Run arrow at the left edge of the cell. Press Command + S. Rest the pointer on artifact_2.csv, then artifact_3.png in the Explorer sidebar on the left. Click the yellow button in the top left corner of the VS Code window.

SAY: "I'm clicking the Run arrow at the left edge of the cell. Now I'm pressing Command and S to save the notebook with its results. In the Explorer sidebar on the left, two new files appeared: artifact_2.csv, the results table, and artifact_3.png, the chart. Now I'm clicking the yellow button in the top left corner of the window to minimize Visual Studio Code."


## Part 5: One slide in PowerPoint (12:30 to 15:05)

The title and headings are already in the template. You insert one picture with the mouse and type three short texts.


**5.1 Open the template and save a copy (40 seconds)**

DO: Move the pointer to the PowerPoint icon in the Dock along the left edge of the screen. Right-click it. In the list that opens to the right, click input_4_review_slide_template.pptx. Click File in the menu bar along the top of the screen, then Save As in the dropdown.

SAY, before typing: "I'm right-clicking the PowerPoint icon in the Dock along the left edge of the screen and choosing the slide template, a prepared input file, free of royalties and copyright. Now I'm clicking File in the menu bar at the top of the screen, then Save As. I will type final output one as the name, and click the Save button at the bottom right of the window."

DO: Type this in silence, then click the Save button at the bottom right of the Save window:

```
final_output_1.pptx
```

**5.2 Insert the chart (55 seconds)**

DO: Rest the pointer on the dashed box on the left, then on the three headings on the right. Click the Insert tab in the ribbon across the top of the window. Click Pictures, then Picture from File. In the file window, click artifact_3.png in the pipe_study folder, then click Insert at the bottom right.

SAY: "The slide has a dashed box on the left for the chart, and three headings on the right: Recommendation, Why, and Rejected sizes. I'm clicking the Insert tab in the ribbon across the top of the window, then Pictures, then Picture from File. In the file window, I'm clicking artifact_3.png, the cost chart, and clicking Insert at the bottom right."

DO: Drag the picture so it covers the dashed box. Click the dashed box border, which is visible at its edge. Press Delete.

SAY: "Now I'm dragging the chart onto the left side of the slide, over the dashed box. The dashed box was only a placeholder, so I'm clicking its border and pressing the Delete key."


**5.3 Type the three short texts (65 seconds)**

DO: Click the grey text under Recommendation on the right side of the slide. Press Command + A.

SAY, before typing: "I'm clicking the grey text under Recommendation and pressing Command and A to select it. I will type the decision first, so the reviewer sees the answer before the evidence."

```
Use 8 inch pipe.
```
DO: Rest the pointer on the new text. Click the grey text under Why. Press Command + A.

SAY, before typing: "Now I'm clicking the grey text under Why and pressing Command and A. I will type the reason."

```
Lowest cost inside the velocity limits.
```
DO: Rest the pointer on the new text. Click the grey text under Rejected sizes. Press Command + A.

SAY, before typing: "Last, I'm clicking the grey text under Rejected sizes and pressing Command and A. I will type the size the buyer will ask about."

```
6 inch is too fast at 2.23.
```
DO: Rest the pointer on the new text.


**5.4 Review and save (25 seconds)**

DO: Trace the pointer over the recommendation, the green bar of the chart, and the rejected sizes text. Press Command + S. Click the yellow button in the top left corner of the PowerPoint window.

SAY: "I'm checking the slide from top to bottom. The recommendation, the green 8 inch bar and the rejected size all agree. Now I'm pressing Command and S to save, and clicking the yellow button in the top left corner of the window to minimize PowerPoint."


## Part 6: Datasheet in Word (15:05 to 18:00)

Everything in the first table is already filled. The grey prompts in the second table and the decision note are text you select with a triple-click and type over. If a prompt does not select, drag across its grey text with the mouse.


**6.1 Open the template and save a copy (45 seconds)**

DO: Move the pointer to the Word icon in the Dock along the left edge of the screen. Right-click it. In the list that opens to the right, click input_1_datasheet_template.docx. Click File in the menu bar along the top of the screen, then Save As in the dropdown.

SAY, before typing: "I'm right-clicking the Word icon in the Dock along the left edge of the screen and choosing the datasheet again. Now I'm clicking File in the menu bar at the top of the screen, then Save As. I will type final output two as the name, so the input stays untouched, and click the Save button at the bottom right of the window."

DO: Type this in silence, then click the Save button at the bottom right of the Save window:

```
final_output_2.docx
```

**6.2 Fill the selection table (85 seconds)**

DO: Scroll down with the mouse wheel until heading 2, Selection, is near the top of the window. Triple-click the grey prompt next to Selected pipe size.

SAY, before typing: "I'm scrolling down with the mouse wheel until I reach heading 2, Selection. I'm triple-clicking the grey prompt next to Selected pipe size, and I will type the answer from the notebook."

```
8 inch
```
DO: Triple-click the grey prompt next to Inside diameter.

SAY, before typing: "Next is Inside diameter, in millimetres, as the label says."

```
202.7
```
DO: Triple-click the grey prompt next to Velocity.

SAY, before typing: "Velocity, in metres per second."

```
1.29
```
DO: Triple-click the grey prompt next to Pressure drop.

SAY, before typing: "Pressure drop, in kilopascals."

```
16.7
```
DO: Triple-click the grey prompt next to Pump power.

SAY, before typing: "Pump power, in kilowatts."

```
1.0
```
DO: Triple-click the grey prompt next to Total yearly cost.

SAY, before typing: "Total yearly cost, in dollars."

```
13,249
```
DO: Triple-click the grey prompt next to Rejected sizes and reason.

SAY, before typing: "And the rejected sizes. The 6 inch pipe is too fast, and the 10 and 12 inch pipes are too slow. The 3, 4 and 5 inch pipes are too fast as well, and the notebook table shows all of them."

```
6 inch too fast at 2.23. 10 and 12 inch too slow.
```
DO: Rest the pointer on each value in turn, from Selected pipe size down to Rejected sizes and reason.

SAY: "Reading the table back, the values match the notebook: 8 inch, 202.7 millimetres, 1.29 metres per second, 16.7 kilopascals, 1 kilowatt and 13,249 dollars a year."


**6.3 Decision note (40 seconds)**

DO: Scroll down with the mouse wheel until heading 3, Decision note, is in the middle of the window. Triple-click the grey prompt under it.

SAY, before typing: "I'm scrolling down with the mouse wheel to heading 3, Decision note, and triple-clicking the grey prompt under it. I will type the decision for the buyer and the plant manager."

```
Approve 8 inch pipe, the lowest cost inside the limits.
```

**6.4 Review and save (30 seconds)**

DO: Scroll up with the mouse wheel to the top of the page, then scroll down again slowly, resting the pointer on the design basis, the selection table and the decision note. Point at the page count at the bottom left of the window. Press Command + S. Click the yellow button in the top left corner of the Word window.

SAY: "I'm scrolling up with the mouse wheel to the top of the page, then down again slowly, pointing at the design basis, the selection table and the decision note. Nothing overlaps, and the page count at the bottom left says one page. Now I'm pressing Command and S to save, and clicking the yellow button in the top left corner of the window to minimize Word."


## Part 7: Cross-check and stop (18:00 to 19:00)

No typing in this part. Everything is pointer work.


**7.1 Check the numbers against the notebook (40 seconds)**

DO: Click the Visual Studio Code icon in the Dock along the left edge of the screen. Scroll up and down the notebook with the mouse wheel, resting the pointer on each output as you name it. Then click the yellow button in the top left corner of the window.

SAY: "Before I finish, I'm clicking the Visual Studio Code icon in the Dock along the left edge of the screen to check the numbers against the notebook. I'm scrolling up with the mouse wheel to the table: the 3, 4 and 5 inch pipes run above 2.0 metres per second, and the 10 and 12 inch pipes run below 1.0. Now I'm scrolling down to the screening result: 8 inch, 1.29 metres per second, 13,249 dollars a year. Every number matches the slide and the datasheet. I'm clicking the yellow button in the top left corner to minimize Visual Studio Code."


**7.2 Closing and stop (20 seconds)**

SAY: "That completes the task. The notebook with its chart and results table, the one slide cost chart and the one page line sizing datasheet are all saved. The recommendation is the 8 inch pipe, the lowest cost size that stays inside the plant velocity limits."

DO: Say nothing more. Silently click the TaskRecorder icon in the Dock, then click Stop Recording. Do not quit it. Wait for Stopping, then Archiving, then Idle. Never use Command + Shift + 9.

If a number does not match, say what differs and fix it in the right app in the next step. If you have to reopen the slide or the datasheet, add that extra visit to the Topology in Metadata.rtf.


## Typing counter and cut order

Total typed: 587 characters. The longest single burst is one line of 56 characters.

| Block | Characters |
|---|---|
| Notebook, 7 cells and 2 limit values | 319 |
| File names, 3 Save As | 54 |
| Slide text | 82 |
| Word text | 132 |
| Total | 587 |

Trim list 1 (saves 66 characters). Use it if your speed test lands above 0.35 seconds per character. Slide: skip typing the Why and Rejected sizes texts. Click each grey prompt box, press Command + A, press Delete, and say the reasons aloud with the pointer on the chart.

Trim list 2 (saves about 55 more). Word: type only 8 inch in the decision note instead of the sentence, and shorten the rejected sizes entry to 6 inch too fast. Say the rest aloud with the pointer on the notebook table.

The analysis cells and the cross-check stay in both lists, because the code is the real work.

Cut order if you are more than 3 minutes behind a checkpoint (time, not typing):

- Say only the two biggest numbers in each result line.
- In 2.3, skip pointing at the 8 row and only point at the headers.
- In 2.2, skip the scroll through the helper functions and only run the setup cell.
- In 5.4, skip the top to bottom check and only save.
- In 6.4, scroll through the datasheet once at a steady pace without naming every part.
Never cut a Command + S, the cross-check in 4.2, the screening in 3.4 and 3.5, or the check in 7.1. Never cut the scroll or click locations to save time: shorten the reasons instead.


## After recording, and if something goes wrong

After you stop

- Wait for Idle. TaskRecorder must go Stopping, then Archiving, then Idle. Do not quit it or close the lid.
- Check the video length. It must be between 15:00 and 45:59. Then scrub it in 10 minute chunks and look for three things: a stretch over 45 seconds with no pointer movement (typing does not count), a typing burst over 30 seconds, and a stretch where your voice is unclear or silent. Open video.mp4 in QuickTime and check the beginning, middle and end.
- Check the screenshots. Count the PNG files and divide by the video length in seconds. It must be above 0.5.
- Build Deliverables.zip: one folder named Deliverables, flat inside, with 9 files. Rename the underscores to spaces: input 1.docx, input 2.csv, input 3.ipynb, input 4.pptx, artifact 1.ipynb, artifact 2.csv, artifact 3.png, final output 1.pptx, final output 2.docx. Input 1, 3 and 4 must be the untouched originals, and the ones you saved copies of must not be the inputs. No .DS_Store, no ~$ files, no __MACOSX, no .vscode. Use: zip -r -X "Deliverables.zip" Deliverables -x "*.DS_Store" and check it with unzip -l from the folder that holds the zip. Do not use Finder's Compress.
- Use the video.mp4 inside the recording folder exactly as it is. Do not rename it or re-export it. Upload the untouched recording zip.
- Metadata.rtf goes in separately, not inside the zip. Topology, in order: Word (LOOKUP) -> Visual Studio Code (CREATE) -> PowerPoint (CREATE) -> Word (CREATE) -> Visual Studio Code (LOOKUP). Request must equal the Goal exactly. Task Description is a numbered outline of those five visits. Delete the red example section. Compare it with the video, and add any extra app visit you made.
- Studio: upload the zip, the video, the recording zip and the Metadata.rtf. Set the input files option correctly (see below). Final Notes, exactly: AI-generated before recording, only if the inputs were made with Gemini. Run both AutoQC checks. If AutoQC flags something, open your video at the flagged timestamps first, and dispute only if the video clearly contradicts the finding.
- Go through the Workflow Checklist in the Writer Guidelines line by line, then the PII confirmation, then tick the final submit box only after every check has passed.
Three things to settle before you upload

- Who made the input files. The guide says AI-generated inputs must be made with Gemini only. The starter files in the kit were drafted by a different AI assistant, so do not tick AI-generated file or write AI-generated before recording unless you recreate them with Gemini. Either recreate the four files yourself or with Gemini from the same content and tick the matching option, or ask Loki whether this is allowed, and tick Manually created file only for files you really wrote.
- Ask Loki whether this counts as a coding plus writing task for the 30 percent typing limit. You do not need it, because the typing share is planned near 10 percent.
- Check that the Studio Apps field and the TaskRecorder apps say exactly the same three names as the Metadata.rtf: Visual Studio Code, PowerPoint, Microsoft Word.
If something goes wrong while recording

| Problem | What to do |
|---|---|
| A cell errors or the output looks wrong | Say what happened, make one deliberate fix, rerun, and say the result is now right. |
| A double bracket or quote appears after you type a line | Press Delete once and say what you fixed. Then run the cell. |
| A suggestion list pops up while you type | Press Escape once, then carry on. Never press Tab or Enter on a suggestion. |
| Kernel stops or imports fail | Click Restart in the notebook toolbar, then run the setup cell and each earlier cell in order. If it costs over 3 minutes, stop and restart the recording. |
| The file window does not show artifact_3.png | Click the pipe_study folder in the sidebar of the file window, say what you are doing, then pick the file. |
| A grey prompt in Word does not select with a triple-click | Drag across its grey text with the mouse, then type. |
| The datasheet runs onto a second page | Delete nothing. Click the page count at the bottom left, say why, and reduce the left and right margins in the Layout tab, then check the page count again. |
| The pointer has been still for about 20 seconds | Move it onto the next thing you will name and say what it is. Do not wiggle it. |
| A typing burst passes 30 seconds | Stop typing, move the pointer to the line, explain it, then continue. |
| You are rushing or mumbling | Stop, breathe, and say the next SAY line slowly. Extra time is fine up to the checkpoints. |
| Silence while a cell runs or a dialog loads | Say what you expect to see when it finishes. |
| You are 3 minutes behind a checkpoint | Use the cut order in the typing section. |
| You clicked or scrolled and did not say where | Say it right away in one plain sentence, for example: I just scrolled down with the mouse wheel to heading 3. Then carry on. Do not go back. |
| A notification, personal name or project name shows on screen | Restart the recording. |
| A big mistake in the first 10 minutes | Stop and restart. It costs less than a rejected take. |


## Appendix: values checked

Every number in the SAY lines comes from the executed notebook in the reference set. Your screen should show the same values.

| NPS (in) | ID (mm) | Velocity (m/s) | dP (kPa) | Pump (kW) | Energy ($/yr) | Pipe ($/yr) | Total ($/yr) | Check |
|---|---|---|---|---|---|---|---|---|
| 3 | 77.9 | 8.74 | 2185.0 | 130.06 | 124,855 | 3,539 | 128,394 | Too fast |
| 4 | 102.3 | 5.07 | 536.9 | 31.96 | 30,682 | 4,842 | 35,524 | Too fast |
| 5 | 128.2 | 3.23 | 169.3 | 10.08 | 9,675 | 6,332 | 16,008 | Too fast |
| 6 | 154.1 | 2.23 | 66.5 | 3.96 | 3,801 | 8,009 | 11,809 | Too fast |
| 8 | 202.7 | 1.29 | 16.7 | 1.00 | 956 | 12,292 | 13,249 | Pass |
| 10 | 254.5 | 0.82 | 5.4 | 0.32 | 308 | 17,508 | 17,815 | Too slow |
| 12 | 303.2 | 0.58 | 2.3 | 0.13 | 129 | 23,840 | 23,969 | Too slow |

Reynolds numbers run from 217,840 to 847,872, so every size is turbulent. The cheapest size on paper is 6 inch at 11,809 dollars a year, but it runs at 2.23 m/s, above the 2.0 limit. The cheapest size inside the limits is 8 inch at 13,249 dollars a year, which is 1,440 dollars a year more. The Colebrook cross-check for 8 inch gives 16.7 kPa against 16.7 kPa in the table, a difference of minus 0.21 percent. Decision: 8 inch.
