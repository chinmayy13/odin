# Word by word narration script: pump selection task

Apps on camera: Visual Studio Code (Jupyter notebook), PowerPoint, Microsoft Word.
Spoken lines are in quotes after SAY. Lines after DO are actions, never spoken. Lines after PAUSE are silent beats.
Adjust "left" to "right" wherever your Dock sits.

Keep this script on paper or a phone, never on the recorded display. Read it once aloud before recording.

---

## Voice and pointer rules (from guide.pdf)

1. After every click, count "one" in your head, then speak or move (p. 79, and the checklist item "Teaching Pointer" on p. 58).
2. Say what, where and why for every meaningful step (p. 66). Put the pointer on whatever you name.
3. Avoid "this" or "here" alone. Name the control and where it is. (p. 71)
4. Say every scroll, and say where you stopped. (review lessons, Review A)
5. Announce every keyboard shortcut before you press it. (p. 72)
6. Speak slowly, under 220 words a minute. Aim for about 120 to 130. (review lessons, AutoQC)
7. Never leave the pointer still for more than 20 seconds, and never be silent more than 45 seconds. When a cell is loading, keep talking and move the pointer over what it will show. (pp. 57, 58, 79)
8. Keep each typing burst to 30 seconds or less. (p. 79)
9. Never say: Project Odin, Studio, Mercor, personal information, TaskRecorder (except silent start and stop), or the name of any AI tool.
10. Never read the Goal aloud. Introduction under 20 seconds. (p. 51)
11. Prepared inputs: at first use, say what the file contains, why it exists and that it is free of royalties and copyright. Do not name how it was made. (pp. 83, 97 to 98)
12. Window rule: one clear window at a time, ordinary Fill, never Full Screen. Keep the menu bar, clock and Dock visible. (p. 77)

---

## Before you press Start (silent, off camera)

1. Working folder "Pump Task Working Folder" is on the Desktop with helper.py, input 1 pump curves.csv, input 2 piping data.json, pump selection.ipynb, data sheet template.docx and starter deck.pptx. Keep the original zip as a clean backup of the starter notebook.
2. Run the notebook once in a temporary copy of the folder, so the first cell on camera loads quickly. Then reopen the clean pump selection.ipynb with no outputs.
3. VS Code: Copilot and any chat panel closed, inline suggestions off, no signed in account visible, folder path free of real names. Kernel already selected.
4. PowerPoint has starter deck.pptx open. Word has data sheet template.docx open. Both minimized.
5. Dock on the left or right, seconds on the clock, wallpaper changed, Accessibility Inspector icon with a dot and its window closed, Insightful minimized, notifications off, Finder closed, Mac plugged in.
6. A Word document containing only the approved Goal is open behind TaskRecorder. TaskRecorder shows the Goal and the three apps, and its window is enlarged so every line shows.
7. Run a one minute audio test. Confirm the volume bar rises into green.

---

## 0. Introduction (under 20 seconds)

DO: Click Start Recording in TaskRecorder, then minimize it at once. Leave the Word Goal document visible.

SAY (exactly, nothing more):
"I will be beginning my task soon. Here is the workflow I have in mind."

PAUSE: about 4 seconds, no speech, Goal document still visible.
DO: Click the yellow minimize button at the top left corner of the Word window to hide the Goal document.

---

## 1. Open the notebook (about 1 minute)

DO: Click the Visual Studio Code icon in the Dock.

SAY:
"I will click the Visual Studio Code icon in the Dock on the left edge of the screen. I need the notebook window, because all the pump calculations happen in it."

PAUSE: count one.
DO: Move the pointer slowly over the notebook title, then the first heading.

SAY:
"The notebook is called pump selection. It has nine steps, each with its own heading and one ready to run code cell below it. Each cell has a Run arrow at its left edge, so I can work through the analysis with the mouse and keep typing to a minimum."

DO: Point to the title at the top, then scroll down slowly.

SAY:
"I will scroll down with the mouse wheel to the heading Step 1, Load the data, because the first job is to look at what the plant and the manufacturers have given me."

---

## 2. Step 1: Load the data (about 2 minutes)

DO: Click the Run arrow at the left edge of the setup cell, then the Run arrow at the left edge of the Step 1 cell.

SAY:
"The grey cell above the heading loads the helper functions, so I will click its Run arrow first. Now I will click the Run arrow at the left edge of the Step 1 cell, to read the pump curve table and the piping data sheet."

PAUSE: count one. While it runs, keep moving the pointer over the output area and talk.

SAY:
"The cell is running. While it loads, the output will show the first eleven rows of the pump curves, and then the key facts from the piping data."

DO: Point to the table, row by row.

SAY:
"The table is called input 1 pump curves. It holds the manufacturer curves for three candidate pumps: head in metres, efficiency, and the NPSH the pump requires, at flows from zero up to two hundred cubic metres per hour. I prepared it before recording to compare the pumps, and it is free of royalties and copyright."

DO: Move the pointer to the printed lines below the table.

SAY:
"Below it, the cell prints the piping facts from input 2, the piping data file, which I also prepared before recording and which is also free of royalties and copyright. The plant needs at least one hundred and ten cubic metres per hour. The static head is eighteen metres, the suction lift is five metres, and the pipe has an inner diameter of zero point one five four metres."

SAY:
"I note the suction lift. The pump sits above the water level, which means NPSH will matter later, because low pressure at the pump inlet can cause cavitation."

DO: Point to the last printed line.

SAY:
"The last line lists three pumps: Pump A, Pump B and Pump C."

---

## 3. Step 2: Head loss at 120 cubic metres per hour (about 2 minutes)

DO: Scroll down.

SAY:
"I will scroll down with the mouse wheel until I reach the heading Step 2, Head loss at one hundred and twenty cubic metres per hour. I am stopping when the heading is at the top of the window."

DO: Click the Run arrow at the left edge of the Step 2 cell.

SAY:
"I will click the Run arrow at the left edge of this cell, to calculate the pipe flow state and the head loss at the middle of the flow range. I picked one hundred and twenty because it sits just above the required flow."

PAUSE: count one. Keep pointer over the output.

SAY:
"The output gives a velocity of one point seven nine metres per second, a Reynolds number of about three hundred and forty three thousand, and a friction factor of zero point zero one six seven. The Reynolds number is high, so the flow is fully turbulent, and the Colebrook equation is the right way to get the friction factor."

DO: Trace the next two output lines with the pointer.

SAY:
"Friction loss in the pipe is two point three nine metres, and the fittings add one point seven one metres. The system head at this flow comes to twenty seven point one one metres. That number includes the eighteen metres of static head and five metres across the heat exchanger. I will keep it in mind, because the next step checks it independently."

---

## 4. Step 3: Hand check (about 2 minutes)

DO: Scroll down.

SAY:
"I will scroll down to the heading Step 3, Hand check. I am stopping when the heading is at the top of the window."

DO: Trace the code lines with the pointer, top to bottom.

SAY:
"I never trust a single calculation, so this cell repeats it from scratch, with a different friction factor equation. Line by line: it computes the pipe area from the diameter, the velocity from the flow, and the Reynolds number from the water properties."

SAY:
"Then it uses the Swamee-Jain equation, which is explicit, instead of the iterative Colebrook equation. It adds the pipe and fittings loss to eighteen metres of static head and five metres across the heat exchanger."

DO: Click the Run arrow at the left edge of the Step 3 cell.

SAY:
"I will click the Run arrow at the left edge of the Step 3 cell."

PAUSE: count one.

SAY:
"The hand check gives a friction factor of zero point zero one six eight and a head of twenty seven point one two metres. The difference from the helper is under two hundredths of a metre. That agrees well, so the head loss function is correct and I can build on it."

---

## 5. Steps 4 and 5: System curve and pump curves (about 3 minutes)

DO: Scroll down.

SAY:
"I will scroll down to the heading Step 4, System curve. I am stopping when the heading is at the top of the window."

DO: Click the Run arrow at the left edge of the Step 4 cell.

SAY:
"I will click the Run arrow at the left edge of this cell, to plot how much head the piping demands at each flow."

PAUSE: count one. Keep pointer on the chart.

SAY:
"The black curve rises with flow. At low flow it is mostly the eighteen metres of static head. At higher flow, friction and the heat exchanger take more, so the curve climbs. The dashed grey line marks the required flow of one hundred and ten cubic metres per hour."

DO: Scroll down.

SAY:
"I will scroll down to Step 5, Pump curves and operating points. I am stopping when the heading is at the top of the window."

DO: Click the Run arrow at the left edge of the Step 5 cell.

SAY:
"I will click the Run arrow at the left edge of this cell. It fits each pump's head curve, finds where it crosses the system curve, and saves the chart as a picture file for my briefing."

PAUSE: count one.

DO: Move the pointer to each marker in turn.

SAY:
"The operating point is where the pump head equals the system head, because that is the only flow where the pump can actually run in this piping. The orange square is Pump A. The green dot is Pump B. The purple dot is Pump C."

SAY:
"Pump A and Pump B sit almost on top of each other at about one hundred and nineteen cubic metres per hour. Pump C runs much further to the right, at about one hundred and fifty. All three clear the required one hundred and ten, so flow alone does not decide the choice."

---

## 6. Steps 6, 7 and 8: Tables, NPSH and cost (about 4 minutes)

DO: Scroll down.

SAY:
"I will scroll down to Step 6, Operating point table. I am stopping when the heading is at the top of the window."

DO: Click the Run arrow at the left edge of the Step 6 cell.

SAY:
"I will click the Run arrow at the left edge of this cell, to list each operating point in numbers."

PAUSE: count one.

DO: Move the pointer across the column labelled percent of BEP flow.

SAY:
"BEP means best efficiency point, where the pump wastes the least energy. A good selection runs between seventy and one hundred and twenty percent of that flow. Pump A is at one hundred and thirteen percent, Pump B is at one hundred and one, and Pump C is at ninety one. All three are inside the window, and Pump B is right on the best point."

DO: Move the pointer across the Efficiency column, then the Power column.

SAY:
"Efficiency is zero point seven two nine for A, zero point seven eight for B, and zero point seven nine four for C. Shaft power is eleven point eight five kilowatts for A, eleven point two six for B, and sixteen point three eight for C. Pump C draws about five kilowatts more."

DO: Scroll down.

SAY:
"I will scroll down to Step 7, NPSH check. I am stopping when the heading is at the top of the window."

DO: Click the Run arrow at the left edge of the Step 7 cell.

SAY:
"I will click the Run arrow at the left edge of this cell. NPSH available is the pressure margin at the pump inlet above vapour pressure. NPSH required is what each pump needs. If available is too close to required, bubbles form and damage the impeller."

PAUSE: count one.

DO: Point to the black curve, then each coloured curve, then the table below.

SAY:
"The black curve is NPSH available. It falls as flow increases, because suction friction grows. The coloured curves are what each pump requires, and they rise with flow."

DO: Move the pointer along the table rows.

SAY:
"The table gives the margin. Pump A has available four point two eight metres against required three point eight seven, a margin of only zero point four one metres and a ratio of one point one one. My rule is a margin of at least one metre and a ratio of at least one point three. Pump A fails that rule. Pump B has a margin of two point zero one and a ratio of one point eight nine. Pump C has one point five one and one point six three. Both pass."

DO: Scroll down.

SAY:
"I will scroll down to Step 8, Energy and five year cost. I am stopping when the heading is at the top of the window."

DO: Click the Run arrow at the left edge of the first Step 8 cell.

SAY:
"I will click the Run arrow at the left edge of the first cell, to turn power into running cost."

PAUSE: count one.

DO: Move the pointer across the last column.

SAY:
"The plant runs eight thousand hours a year at twelve cents per kilowatt hour. Energy cost is about eleven thousand four hundred dollars for A, ten thousand eight hundred for B, and fifteen thousand seven hundred for C. Adding the purchase price and five years of energy gives sixty one thousand seven hundred dollars for A, sixty thousand two hundred for B, and eighty seven thousand five hundred for C."

SAY:
"Pump A is the cheapest to buy, but it does not win over five years, and it fails the NPSH check anyway."

DO: Scroll down slightly to the second Step 8 cell.

SAY:
"I will scroll down a little to the sensitivity cell. It tests whether the ranking depends on the electricity price."

DO: Double click the number zero point one two on the line that starts with rate test. Type 0.18.

SAY (before typing):
"I will double click the number zero point one two on the first line, to select it, and type zero point one eight, a fifty percent higher electricity price."

DO: Type "0.18". Then click the Run arrow at the left edge of the cell.

SAY:
"Now I will click the Run arrow at the left edge of this cell."

PAUSE: count one.

SAY:
"At eighteen cents the ranking is Pump B, then Pump A, then Pump C. It did not change, so the decision is not sensitive to the power price."

---

## 7. Step 9: Decision (about 1.5 minutes)

DO: Scroll down.

SAY:
"I will scroll down to the final heading, Step 9, Decision. I am stopping when the heading is at the top of the window."

DO: Click the Run arrow at the left edge of the Step 9 cell.

SAY:
"I will click the Run arrow at the left edge of this cell. It applies my three pass rules, picks the cheapest pump that passes, saves a comparison table as a picture, and prints the values I need for the data sheet."

PAUSE: count one.

DO: Point to the pass table, then the line Recommended pump.

SAY:
"Pump A passes the flow and best efficiency rules, but fails NPSH. Pumps B and C pass all three. Between them, Pump B has the lowest five year cost, so the notebook recommends Pump B."

DO: Point to the data sheet values block, line by line.

SAY:
"Below it is the block of data sheet values for Pump B: operating flow one hundred nineteen point six cubic metres per hour, head twenty seven point one metres, efficiency zero point seven eight, one hundred and one percent of best efficiency flow, shaft power eleven point two six kilowatts, NPSH margin two point zero one metres, and a five year cost of sixty thousand two hundred and forty seven dollars. I will copy these into the data sheet at the end."

DO: Press Command+S to save the notebook.

SAY:
"I will press Command plus S to save the notebook with its results, so the calculations are kept."

---

## 8. PowerPoint briefing (about 4 minutes)

DO: Click the PowerPoint icon in the Dock.

SAY:
"Now I will click the PowerPoint icon in the Dock. The plant manager needs a short briefing, not a notebook, so I will build three slides from my results."

PAUSE: count one.

DO: Point to slide 1 in the thumbnail panel on the left, then the text on its right side.

SAY:
"The starter deck already has three titled slides. Slide 1 is Duty point and candidate pumps. Its text box on the right states the required flow, the system head, and the three candidates. It needs the chart."

DO: Click the Insert tab, then Pictures, then Picture from File.

SAY:
"I will click the Insert tab in the ribbon at the top, then Pictures, then Picture from File, to add the chart I saved from the notebook."

PAUSE: count one after each click.

DO: In the file dialog, click the folder Pump Task Working Folder, then the file system and pump curves dot png, then Insert.

SAY:
"In the dialog I will open the Pump Task Working Folder and click the file system and pump curves dot png, then the blue Insert button at the bottom right."

PAUSE: count one.

DO: Drag the picture to the left side under the title and drag a corner handle to resize it so it does not cover the text box.

SAY:
"The picture landed in the middle. I will drag it to the left, under the title, and then drag the bottom right corner handle to make it smaller, so it does not cover the text box on the right."

DO: Click slide 2 in the thumbnail panel.

SAY:
"I will click slide 2 in the panel on the left. It is Comparison and checks, and its text states my three pass rules. It needs the comparison table."

DO: Insert tab, Pictures, Picture from File, choose comparison table dot png, Insert.

SAY:
"Again I will click Insert, Pictures, Picture from File, then pick comparison table dot png, and click Insert."

DO: Drag it to sit under the title and resize if needed.

SAY:
"I will drag the table picture to sit just under the title, and widen it with the corner handle until all the columns are readable."

DO: Click slide 3 in the thumbnail panel, then click inside the empty content box.

SAY:
"Slide 3 is the recommendation. I will click inside the empty content box under the title, to type three short points."

DO: Type bullet 1. Pause 2 seconds. Type bullet 2. Pause. Type bullet 3.

SAY (before each burst, short):
"First point, the choice and its operating point."
TYPE: Recommended: Pump B at 119.6 m3/h and 27.1 m head.
"Second point, why it passes."
TYPE: Passes the flow, best efficiency and NPSH checks, with a 2.01 m margin.
"Third point, the cost comparison and why the others lose."
TYPE: Lowest five year cost: 60,247 USD. Pump A fails NPSH. Pump C costs 87,504 USD.

DO: Press Command+S, type the name Pump briefing, click Save.

SAY:
"I will press Command plus S to save, name the file Pump briefing, and click the blue Save button."

DO: Click File in the menu bar at the top, then Export, set File Format to PDF, click Export.

SAY:
"The plant manager will read this on any device, so I will export a PDF. I will click File in the menu bar at the top, choose Export, set the File Format dropdown to PDF, and click the Export button."

PAUSE: count one.

SAY:
"The PDF is saved next to the notebook, in the same working folder."

---

## 9. Word pump data sheet (about 3 minutes)

DO: Click the Word icon in the Dock.

SAY:
"Now I will click the Word icon in the Dock. Procurement needs a single page data sheet, so I will complete the template for the selected pump."

PAUSE: count one.

DO: Point to table 1, then table 2, table 3, then the empty recommendation area.

SAY:
"Table 1, Service and duty, is already filled in. Table 2, Selected pump, has blank value cells. Table 3 lists the selection checks and needs a result for each. At the bottom is the recommendation, also blank."

DO: Click File, then Save As, name Pump data sheet, click Save.

SAY:
"First I will protect the template. I will click File in the menu bar, choose Save As, name the file Pump data sheet, and click the Save button."

DO: Click the first blank cell, next to Pump model.

SAY:
"Now I will click the empty cell next to Pump model in Table 2 and type the values, reading them from my notebook results. I am using the Tab key to move down a cell."

DO: Type with Tab between cells, in bursts of 25 seconds or less: Pump B, 119.6, 27.1, 0.780, 101%.
Pause 3 seconds and point to the cells just filled.

SAY:
"Pump model, operating flow, head, efficiency and the percent of best efficiency flow are in."

DO: Type: 11.26, 4.27, 2.26, 2.01, 10,809, 60,247.
Point to the cells.

SAY:
"Shaft power, NPSH available, NPSH required, the margin, the yearly energy cost and the five year cost are in. These match the notebook block."

DO: Click the first Result cell in Table 3. Type Pass, Tab, Pass, Tab, Pass, Tab, Pass.

SAY:
"Next I will click the first Result cell in Table 3. All four checks pass for Pump B, so I will type Pass, using the Tab key between cells."

DO: Click below the Recommendation heading. Type the sentence in two bursts.

SAY:
"Last, I will click under the Recommendation heading, and type the decision for procurement."
TYPE burst 1: Purchase Pump B.
TYPE burst 2: It meets the flow requirement, operates at 101% of its best efficiency flow, has a 2.01 m NPSH margin and the lowest five year cost of the pumps that pass every check.

DO: Scroll to the top, trace the whole sheet with the pointer, then press Command+S.

SAY:
"I will scroll to the top and read down the sheet to check every value against the notebook. Duty is correct, the pump values match, all four checks say Pass, and the recommendation is clear. I will press Command plus S to save the data sheet."

---

## 10. Wrap-up (about 1 minute)

DO: Click the Visual Studio Code icon in the Dock, then point at the Step 9 output.

SAY:
"Finally, I will click the Visual Studio Code icon in the Dock and look at the Step 9 output once more, to confirm the numbers in the slides and the data sheet match. They do: Pump B, one hundred nineteen point six cubic metres per hour, a margin of two point zero one metres, and sixty thousand two hundred and forty seven dollars over five years."

SAY:
"The work is complete. The notebook, the two chart pictures, the PowerPoint and its PDF, and the Word data sheet are all saved in the working folder."

DO: Stop speaking. Bring TaskRecorder forward from the Dock and click Stop Recording. Say nothing about it.
Wait for Idle: Stopping, Archiving, Idle.

---

## If something goes wrong on camera

- A cell shows an error: "That cell did not run. I will read the message, and the cause is a missing earlier cell. I will click the Run arrow on the setup cell first, then run this cell again." Fix once, confirm the result, carry on.
- A window covers another: "A window opened on top of the notebook. I will minimize it using the yellow button at the top left, so the notebook is clear again."
- Mistyped value: "I typed the wrong digit. I will select the cell, retype the value, and check it against the notebook."
- If errors dominate the take or a result is wrong, stop, wait for Idle and re-record.

---

## Timing and word count

Spoken words in this script are about 2,500. At 120 to 130 words a minute that is about 20 minutes of speech, and real video with clicks, loading and pauses usually runs longer. Expect a final video between 25 and 35 minutes, inside the 15:00 to 45:00 limit. Typing totals roughly 3 minutes, which is well below 20 percent.

If you run long in practice, the sensitivity cell in Step 8 is the one safe cut, because your Goal does not mention it. Everything else in the script maps to a promise in the Goal (Visual Studio Code calculations, charts, operating points, NPSH check, energy cost, PowerPoint PDF, Word data sheet), so keep it all.

---

## After recording (silent)

1. Wait for Idle. Click Show Recordings and find the newest recording folder and zip.
2. Open video.mp4 in QuickTime. Check start, middle, end, narration audible, length between 15:00 and 45:59.
3. Open the screenshots folder and confirm more than 0.5 screenshots per second (a 25 minute video needs more than 750).
4. Rename your own files for Deliverables.zip, using spaces:
   input 1 pump curves.csv, input 2 piping data.json, input 3 helper.py, input 4 starter notebook.ipynb (from your clean zip copy), input 5 data sheet template.docx, input 6 starter deck.pptx, artifact 1 executed notebook.ipynb, artifact 2 system and pump curves.png, artifact 3 comparison table.png, final output 1 briefing.pdf, final output 2 briefing.pptx, final output 3 pump data sheet.docx.
5. Build the zip: `zip -r -X "Deliverables.zip" Deliverables -x "*.DS_Store"`. Check with `unzip -l "Deliverables.zip"`.
6. Fill Metadata.rtf, then upload the four files to Studio separately: video.mp4, recording zip, Deliverables.zip, Metadata.rtf.
