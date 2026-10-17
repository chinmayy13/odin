# Recording Script: Line CW-101 Pipe Size Selection

Apps: Visual Studio Code, PowerPoint, Microsoft Word. Target script time about 15 minutes, which becomes about 25 minutes of video.

How to read this script:
- SAY: is spoken out loud, word for word. Speak slowly, under 220 words a minute, with short pauses.
- DO: is what your hand does. Never say the DO lines.
- [1 sec] means stay still for one second after the click before you talk or move.
- Keep the pointer on the item you name. Never let it sit still for more than 20 seconds. If something is loading, keep talking and slide the pointer along what is on screen.
- Never read the Goal. Never mention TaskRecorder, personal information, or how any file was made.

---

## Part 0. Intro (under 20 seconds)

DO: Start recording, minimize the recorder right away. The opening note with only the Goal is on screen behind it.

SAY: I will be beginning my task soon. Here is the workflow I have in mind.

DO: Hold for about 3 seconds, then minimize the opening note. Say nothing else.

---

## Part 1. Look at the project and the input (about 2 minutes)

DO: Click the Visual Studio Code icon in the Dock. [1 sec]

SAY: I'll click the Visual Studio Code icon in the Dock on the edge of the screen to bring up my project folder.

DO: Move the pointer slowly down the Explorer list on the left.

SAY: On the left, the Explorer sidebar lists four files. pipe underscore catalog dot csv, pipe underscore sizing dot ipynb, pipe underscore slide dot pptx, and line underscore datasheet dot docx.

SAY: I am a process engineer, and I need to choose the pipe size for a new cooling water line, line CW one oh one. A smaller pipe costs less to buy but flows faster and costs more to pump. A larger pipe saves pumping energy but costs more to install. So I will compare every size, then check each one against the plant velocity limits.

DO: Click pipe_catalog.csv in the Explorer. [1 sec]

SAY: I'll click pipe underscore catalog dot csv in the Explorer to open it.

DO: Trace along the header row, then down the rows.

SAY: This file is a prepared input, free of royalties and copyright. Each row is one candidate pipe size. The first column is the nominal size in inches, from three up to twelve. The second column is the inside diameter in millimetres. The third is the pipe roughness, zero point zero four five millimetres for commercial steel. The fourth is the installed cost per metre in dollars.

DO: Rest the pointer on the 8 row.

SAY: For example, the eight inch pipe has a two hundred and two point seven millimetre inside diameter and costs three hundred and thirty dollars per metre installed.

---

## Part 2. Run the notebook (about 6 minutes)

DO: Click pipe_sizing.ipynb in the Explorer. [1 sec]

SAY: I'll click pipe underscore sizing dot ipynb in the Explorer to open the notebook.

DO: Point at the markdown note at the top.

SAY: At the top, a note gives the plant standard for cooling water lines. Velocity must stay between one point zero and two point zero metres per second. I'll use that to screen the sizes later.

DO: Point at the kernel name at the top right of the notebook.

SAY: At the top right, the kernel picker shows Python three, so the notebook is ready to run.

DO: Click the Run arrow at the left edge of the first code cell. [1 sec]

SAY: I'll click the Run arrow at the left edge of the first code cell, the one that starts with import math.

DO: While it runs, slide the pointer down the code.

SAY: This cell loads the libraries and defines two helper functions. Friction underscore factor uses the Swamee Jain equation, which gives the friction factor for turbulent flow. Size underscore table loops over each pipe size and calculates velocity, Reynolds number, friction factor, pressure drop, pump power and yearly cost. A check mark appears, so it finished.

DO: Scroll down with the mouse wheel.

SAY: I'm scrolling down with the mouse wheel until the parameters cell is on screen.

DO: Slide the pointer down the parameter lines as you name them.

SAY: These are the design inputs. Flow is one hundred and fifty cubic metres per hour. Line length is two hundred and fifty metres including fittings. Water density is nine ninety six, and viscosity is zero point zero zero zero eight Pascal seconds. Pump efficiency is seventy percent. Electricity costs twelve cents per kilowatt hour, with eight thousand running hours a year. The capital recovery factor is zero point one four nine, which spreads the pipe cost over ten years at eight percent.

DO: Rest the pointer on the MAX_V line.

SAY: Maximum velocity is set to three point zero, a generic starting value. I'll run the notebook with it first to see what that limit gives.

DO: Click the Run arrow of the parameters cell. [1 sec]

SAY: I'll click the Run arrow at the left edge of this parameters cell.

DO: Scroll down with the mouse wheel to the next cell.

SAY: I'm scrolling down to the next code cell. It reads the CSV and builds the results table.

DO: Click its Run arrow. [1 sec]

SAY: I'll click its Run arrow. The table appears below the cell.

DO: Scroll the output with the mouse wheel, slowly, and stop on the full table.

SAY: I'm scrolling down the output until all seven rows are visible. Each row is a pipe size. The three inch pipe runs at eight point seven four metres per second. That gives a pressure drop of over two thousand kilopascals and one hundred and thirty kilowatts of pump power, which is not workable. The eight inch pipe runs at one point two nine metres per second, with sixteen point seven kilopascals and about one kilowatt of pump power.

DO: Trace along the Reynolds column.

SAY: Every Reynolds number is above four thousand, so the flow is turbulent in all sizes, and the friction factor equation is valid.

DO: Trace along the Total column.

SAY: The last column is yearly total cost, pumping energy plus the pipe cost spread over its life. Total cost falls as the pipe gets bigger, then rises again once the pipe cost dominates. The lowest total is the six inch pipe, at about eleven thousand eight hundred and nine dollars a year.

DO: Scroll down with the mouse wheel to the screening cell. Click its Run arrow. [1 sec]

SAY: I'm scrolling down to the screening cell. I'll click its Run arrow. It marks each size Pass, Too fast or Too slow, then picks the cheapest size that passes.

DO: Point at the printed lines under the cell.

SAY: With the limit at three point zero, the six inch pipe passes. But the plant standard for cooling water says the maximum is two point zero. The six inch pipe runs at two point two three, which breaks the standard and risks erosion and noise. So three point zero is the wrong limit, and I need to correct it.

DO: Scroll up with the mouse wheel to the parameters cell.

SAY: I'm scrolling back up with the mouse wheel to the parameters cell.

DO: Double-click the 3.0 value on the MAX_V line. [1 sec]

SAY: I'll double click the three point zero on the MAX underscore V line to select it.

DO: Type 2.0.

SAY: I'll type two point zero, the plant maximum.

DO: Click the Run All button in the notebook toolbar at the top. [1 sec]

SAY: To rerun everything with the new limit, I'll click Run All in the notebook toolbar at the top.

DO: While cells run, keep the pointer moving down the notebook and keep talking.

SAY: The cells run from top to bottom, and the new results fill in below. The screening cell is the one I care about, so I'll scroll down to it with the mouse wheel.

DO: Scroll to the screening output and stop on it.

SAY: Now the selected size is eight inch, with a total of about thirteen thousand two hundred and forty nine dollars a year. In the table, the six inch pipe now shows Too fast. The five, four and three inch pipes are also too fast. The ten and twelve inch pipes are too slow, and they cost more as well.

SAY: The eight inch pipe costs about one thousand four hundred and forty dollars a year more than the six inch pipe. I judge that worth paying to stay inside the plant standard, because a pipe running too fast wears out sooner and is noisy.

DO: Scroll down with the mouse wheel to the chart cell.

SAY: I'm scrolling down to the chart cell. It plots yearly total cost for each size. Green bars pass the velocity limits, gray bars do not.

DO: Trace along the bars with the pointer.

SAY: The green bar at eight inch is the only one inside the limits. The six inch bar is lower, but it is gray. The three inch bar goes off the scale, which the label says. This chart will go on my slide.

DO: Scroll down with the mouse wheel to the last cell. Click its Run arrow. [1 sec]

SAY: I'm scrolling down to the last code cell. I'll click its Run arrow. This is my cross check. It recalculates the pressure drop for the selected size with an iterative Colebrook friction factor, instead of the Swamee Jain shortcut.

DO: Point at the printed result.

SAY: The table gives sixteen point seven kilopascals, and the Colebrook check gives sixteen point seven as well. The difference is about minus zero point two percent, well inside one percent. The flow regime is turbulent. So the table is reliable.

DO: Press Command and S.

SAY: I'll press Command plus S to save the notebook with its results.

DO: Point at the Explorer on the left.

SAY: In the Explorer, two new files appeared. cost underscore chart dot png, and results underscore table dot csv.

---

## Part 3. Build the slide in PowerPoint (about 3 minutes)

DO: Click the PowerPoint icon in the Dock. [1 sec]

SAY: I'll click the PowerPoint icon in the Dock. This one slide is for the shutdown planning review.

DO: Point at the dashed box on the left, then at the three headings on the right.

SAY: The template has a dashed box on the left for the chart, and three headings on the right. Recommendation, Why, and Rejected sizes.

DO: Click the Insert tab in the ribbon at the top. [1 sec]

SAY: I'll click the Insert tab in the ribbon at the top.

DO: Click Pictures, then Picture from File. [1 sec]

SAY: I'll click Pictures, then Picture from File, to add the chart.

DO: In the file dialog, pick cost_chart.png and click Insert. [1 sec]

SAY: In the file window, I'll select cost underscore chart dot png and click the Insert button at the bottom right.

DO: Drag the chart so it covers the dashed box. Click the dashed box border and press Delete if it still shows.

SAY: I'll drag the chart onto the left side so it sits over the dashed box. The dashed box was only a placeholder, so I'll click its border and press the Delete key.

DO: Click the placeholder text under Recommendation. Press Command and A. [1 sec]

SAY: I'll click the text under Recommendation, and press Command plus A to select the placeholder text.

DO: Type: Use 8 inch pipe for line CW-101.

SAY: Now I'll type the recommendation. Use eight inch pipe for line CW one oh one.

DO: Pause, point at it, then click the text under Why. Press Command and A. [1 sec]

SAY: That states the decision. Next, I'll click the text under Why and press Command plus A again.

DO: Type: Velocity is 1.29 m/s, inside the 1.0 to 2.0 m/s plant limit. Total cost is $13,249 per year, the lowest of the sizes that pass.

SAY: I'll type the reasons. Velocity is one point two nine, inside the plant limit. Total cost is thirteen thousand two hundred and forty nine dollars a year, the lowest of the sizes that pass.

DO: Pause, point at it, then click the text under Rejected sizes. Press Command and A. [1 sec]

SAY: Now the text under Rejected sizes. Command plus A to select it.

DO: Type: 6 inch costs less but runs at 2.23 m/s, above the limit. 3, 4 and 5 inch are too fast. 10 and 12 inch are too slow and cost more.

SAY: I'll type why the others were rejected. Six inch costs less but runs at two point two three, above the limit. Three, four and five inch are too fast. Ten and twelve inch are too slow and cost more.

DO: Trace the pointer over the three text boxes and the chart.

SAY: Reading it through, the chart, the decision, and the reasons all agree.

DO: Press Command and S.

SAY: I'll press Command plus S to save the slide.

---

## Part 4. Complete the datasheet in Word (about 3 minutes)

DO: Click the Microsoft Word icon in the Dock. [1 sec]

SAY: I'll click the Word icon in the Dock. This page is the line sizing datasheet for the maintenance planner and the buyer.

DO: Trace down the top five rows, which are already filled.

SAY: The top five rows are already filled with the design basis. Line number, service, design flow, line length, and plant velocity limit. The lower rows are blank, and I will fill them from the notebook.

DO: Click the empty cell next to Selected pipe size. [1 sec]

SAY: I'll click the empty cell next to Selected pipe size.

DO: Type: 8 inch nominal. Press Tab.

SAY: Eight inch nominal. I'll press the Tab key to move to the next row.

DO: Type: 202.7 mm. Press Tab.

SAY: The inside diameter is two hundred and two point seven millimetres. Tab.

DO: Type: 1.29 m/s. Press Tab.

SAY: Velocity, one point two nine metres per second. Tab.

DO: Type: 16.7 kPa. Press Tab.

SAY: Pressure drop, sixteen point seven kilopascals. Tab.

DO: Type: 1.0 kW. Press Tab.

SAY: Pump power, one kilowatt. Tab.

DO: Type: $13,249 per year. Press Tab.

SAY: Total yearly cost, thirteen thousand two hundred and forty nine dollars. Tab.

DO: Type: 6 inch: 2.23 m/s, above limit. 3, 4, 5 inch: too fast. 10, 12 inch: too slow, higher cost.

SAY: In the last row, I'll record the rejected sizes and the reason for each, so the buyer knows they were considered.

DO: Click the empty line under Decision note. [1 sec]

SAY: I'll click the empty line under Decision note.

DO: Type: Approve 8 inch pipe. It is the lowest cost size that meets the plant velocity limits.

SAY: And I'll type the decision. Approve eight inch pipe. It is the lowest cost size that meets the plant velocity limits.

DO: Press Command and S.

SAY: I'll press Command plus S to save the datasheet.

---

## Part 5. Final check and stop (about 30 seconds)

DO: Trace down the datasheet values with the pointer.

SAY: Last check. The datasheet shows eight inch, one point two nine metres per second, sixteen point seven kilopascals, and thirteen thousand two hundred and forty nine dollars a year. Those match the notebook table and the slide.

SAY: The notebook, the slide and the datasheet are all saved, so the task is complete.

DO: Bring the recorder to the front and stop the recording. Do not speak about it.

---

## Typing check

Typing is short bursts: one number in the notebook, three short slide texts, and seven short datasheet entries. Each burst is under 30 seconds, and the total is well under 20 percent of the video.

## If something goes wrong

- A cell takes a long time: keep talking and slide the pointer down the code you are waiting on.
- You mistype: say "I mistyped that, I'll fix it", fix it, then say what it now shows.
- A window overlaps another: move or minimize it, say you are doing so, then continue.
