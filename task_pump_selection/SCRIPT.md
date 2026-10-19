# Word-by-word recording script: chilled-water pump selection

Use this to **rehearse**, then record in your own natural voice. Keep it on a second device or on paper. It must never be a window on the recording Mac, because project materials on screen fail the recording (guide: Apps and Desktop, PII and Project information).

## How to read it

- **DO** is an action. You do not say it.
- **SAY** is spoken. The quoted words are the script.
- **TYPE** is typed exactly as written. Say aloud what you are typing as you type.
- **After every click, count "one" in your head before you speak or move** (guide: pause about 1 second after every click).
- Speak at about **120–135 words a minute**. The limit is 220, and slow is better.
- Say every scroll and where you stopped. Say every keyboard shortcut as you press it.
- Keep each typing burst **under 30 seconds**. Never leave the pointer still for more than 20 seconds. While a cell runs, keep talking and trace the code with the pointer.
- Numbers are rounded to what the cells print. They come from the answer key in `reference/`, so a correct run reads the same.

## Words and rules from `guide.pdf` this script follows

| Guide rule | How the script complies |
|---|---|
| Intro is the one required sentence, under 20 seconds, with the Goal document shown, then minimized (How To Record, Step 2) | Scene 0 |
| Say what, where and why for each step, with the cursor on the named item (Narration Quality) | Every SAY line names the control, its place, and the reason |
| No "this", "that", "here" alone (Name the Exact Target) | Controls are named in full |
| Announce every keyboard shortcut | Command plus S, Tab, Return are said aloud |
| Do not recite the Goal | Narration describes the work in your own words |
| Typing under 20% overall, no segment over 45 seconds | About 355 characters of code and about 80 words of text, in short bursts |
| Pointer idle never over 45 seconds | Pointer cues throughout |
| One clear window, Fill not Full Screen, no window covered over 25% | Minimize each app before the next |
| No AI interaction or branding on screen | Copilot, Chat and Designer are off; never mentioned |
| No PII, no Mercor, Odin, Studio or TaskRecorder on screen after the start | Neutral account, neutral folder, silent stop |
| Prepared inputs: explain contents, purpose and royalty- and copyright-free status without naming an AI tool | Scene 1 |
| Never launch or set up an app after Start | All three apps are open and minimized before recording |
| Small mistakes: notice, say it, fix it, check it | Recovery lines at the end |

**Never say:** "personal information", "TaskRecorder", "Mercor", "Odin", "Studio", "AI", "Gemini", "ChatGPT", "Copilot", "Designer". Never say "here" or "this" without naming the item.

---

## Scene 0: Opening (about 15 seconds)

**DO (silently):** In TaskRecorder, click **Start Recording**. Click its yellow minimize button. The only window on screen is the Word note holding the Goal.

**SAY (exactly this, once, and nothing else):**
"I will be beginning my task soon. Here is the workflow I have in mind."

**DO:** Wait 3 seconds with the note visible. Move the pointer to the yellow button at the top left of the note window.

**SAY:** "I'll minimize the note with the yellow button at the top left of its window, so the workspace is clear."

**DO:** Click it. Count one.

---

## Scene 1: Visual Studio Code, load and check the data (about 3 minutes)

**DO:** Move the pointer to the blue Visual Studio Code icon in the Dock.
**SAY:** "I'll click the blue Visual Studio Code icon in the Dock on the left edge, because the pump analysis runs in a Jupyter notebook inside it."
**DO:** Click. Count one.

**DO:** Trace down the file list in the **Explorer** panel at the left of the window.
**SAY:** "On the left, the Explorer panel shows my PumpTask folder with the prepared inputs. There is pump_curves.csv, the pump data. There is pump_helpers.py, a small helper module for fitting and plotting. And there is pump_selection.ipynb, my notebook, with some cells left empty for me to complete. The data file is a prepared input with synthetic values, free of royalties and copyright."

**SAY:** "I'm a mechanical engineer helping a facilities manager choose a replacement circulation pump. The chilled-water loop has to deliver fifty litres per second at twenty-eight metres of head, and I have three candidate pumps: A, B and C."

**DO:** Place the pointer on the notebook scroll area.
**SAY:** "I'll scroll down the notebook with the mouse wheel, from the title to the bottom, so you can see the plan: load and check the data, fit the curves, find the operating points, apply the criteria and the cost, and then save the results."
**DO:** Scroll slowly to the bottom, then back to the top.
**SAY:** "Now I'm scrolling back up to the first code cell, under the heading 'Load the data and check units'."

**DO:** Hover on the **Run arrow** at the left edge of that cell.
**SAY:** "I'll click the Run arrow at the left edge of the first code cell. It imports NumPy, pandas and my helper functions, and loads pump_curves.csv. The first run takes a few seconds while the Python kernel starts."
**DO:** Click. Count one. While it loads, trace the imports with the pointer.
**SAY (while waiting):** "While it loads, I'm tracing the three imports and the read_csv line: NumPy for the polynomial maths, pandas for the table, and the helper module for the fits and the chart."

**SAY (when the table appears):** "The first ten rows are pump A and the start of pump B. The columns are pump, flow in litres per second, head in metres, efficiency in percent, and NPSH required in metres. Flow steps up by ten litres per second, and head falls as flow rises, which is what a centrifugal pump curve should do."

**DO:** Scroll down slightly to the next code cell.
**SAY:** "I'm scrolling down a little to the next code cell, which has a gap I need to fill."
**DO:** Double-click the three dots inside `agg(...)`.
**SAY:** "I'll double-click the three dots inside agg so they highlight, and replace them with the list of statistics I want, minimum and maximum. I'm doing this to check the range of every column for each pump."
**TYPE:** `["min", "max"]`
**DO:** Click the Run arrow. Count one.
**SAY:** "Every pump covers ten to eighty litres per second. Head runs from about six point six metres for pump A at the top flow up to forty-one at the lowest. Efficiency peaks at about seventy-seven percent for pump A, eighty-four for B and eighty-eight for C. NPSH required climbs with flow, reaching eight point five metres for pump C. The units and ranges are physical, so I can go on and fit the curves."

---

## Scene 2: Fit the pump curves (about 2 minutes)

**DO:** Scroll down to the heading **2. Fit a quadratic curve for each pump**.
**SAY:** "I'm scrolling down with the mouse wheel to heading 2, 'Fit a quadratic curve for each pump', and I'll stop at the next code cell."
**SAY:** "A pump curve comes as test points. To find where a pump meets the system, I need an equation. A second-degree polynomial describes head, efficiency and NPSH required against flow very well for a centrifugal pump, so I'll use degree two."

**DO:** Double-click the three dots after `fits =`.
**SAY:** "I'll double-click the three dots after 'fits equals' and type fit underscore all of df. That calls my helper to fit all three curves for every pump."
**TYPE:** `fit_all(df)`
**DO:** Click the Run arrow. Count one.
**SAY:** "The second line, fit_report, compares each fitted curve with the data. The largest errors are about 0.04 metres for head, 0.05 percentage points for efficiency and 0.04 metres for NPSH required. That is tight, so a quadratic is justified."
**DO:** Trace along the three error columns with the pointer.

---

## Scene 3: System curve and operating points (about 3 minutes)

**DO:** Scroll to heading **3. System curve and operating points**.
**SAY:** "I'm scrolling down to heading 3, system curve and operating points."
**SAY:** "The loop needs fifty litres per second at twenty-eight metres. Twelve metres of that is static head, which does not change with flow. The other sixteen metres is friction, which grows with flow squared. So the system curve is H equals twelve plus k times Q squared, and I find k from the duty point."

**DO:** Double-click the dots after `static_head =`.
**SAY:** "I'll replace the first set of dots with twelve point zero, the static head in metres."
**TYPE:** `12.0`
**DO:** Double-click the dots after `k =`.
**SAY:** "For k, I'll type twenty-eight minus the static head, divided by fifty squared. That is sixteen divided by two thousand five hundred."
**TYPE:** `(28 - static_head) / 50**2`
**DO:** Click the Run arrow. Count one.
**SAY:** "The last line prints k as zero point zero zero six four, so the system curve is defined."

**DO:** Scroll down to the next code cell, the loop.
**SAY:** "I'll scroll down to the loop that finds the operating points. For each pump it takes the head fit, subtracts the system curve, and solves for where the difference is zero. I'll replace the dots after 'roots equals' with the head fit minus the system curve, then dot roots."
**DO:** Double-click the dots after `roots =`.
**TYPE:** `(f["head"] - system).roots`
**DO:** Click the Run arrow. Count one.
**SAY:** "The next line keeps the one positive, real root, which is the operating flow. Pump A settles at forty-nine point nine one litres per second, pump B at fifty point zero zero, and pump C at fifty point two zero, all close to the fifty litres per second duty."

**DO:** Scroll down to the cell under the heading **Hand check on one pump**.
**SAY:** "Next is a hand check on pump B. The cell sets p to B and q to B's operating flow. I'll replace the dots with pump B's head fit at q, minus the system curve at q. If the intersection is right, the two heads are equal, so the difference should be under zero point one metres."
**DO:** Double-click the dots at the start of the last line.
**TYPE:** `fits[p]["head"](q) - system(q)`
**DO:** Click the Run arrow. Count one.
**SAY:** "The difference is essentially zero, far below my zero point one metre limit, so the intersection is correct."

*(If the cell prints something like `np.float64(0.0)` or a number such as `1e-14`, say "essentially zero" either way.)*

---

## Scene 4: Criteria and annual cost (about 5 minutes)

**DO:** Scroll to heading **4. Criteria and annual energy cost**.
**SAY:** "I'm scrolling down to heading 4. I apply two criteria. First, the pump must run between seventy and one hundred and ten percent of its best-efficiency flow, otherwise it suffers wear and wastes energy. Second, the NPSH margin, which is NPSH available minus NPSH required, must be at least one point five metres, or the pump can cavitate."

**DO:** Double-click the dots in the constants cell.
**SAY:** "In the constants cell, I'll replace the dots with five assumptions: water density one thousand kilograms per cubic metre, gravity nine point eight one, six thousand running hours a year, a tariff of twelve cents per kilowatt-hour, and six metres of NPSH available at the pump suction."
**TYPE:** `1000, 9.81, 6000, 0.12, 6.0`
**DO:** Click the Run arrow. Count one.

**DO:** Scroll down to the criteria loop and trace the prefilled lines.
**SAY:** "Now the criteria loop. I'll read it first. For each pump it takes the operating flow q, reads the head from the head fit, and reads the efficiency from the efficiency fit as a fraction. Four lines are left for me."

**DO:** Double-click the dots after `q_bep =`.
**SAY:** "First, the best-efficiency flow. It is the top of the efficiency parabola, minus b over two a. I'll type minus the linear coefficient, divided by two times the squared coefficient."
**TYPE:** `-f["eff"].coeffs[1] / (2 * f["eff"].coeffs[0])`
**DO:** Double-click the dots after `margin =`.
**SAY:** "Second, the NPSH margin: NPSH available minus NPSH required at the operating flow."
**TYPE:** `npsh_avail - f["npshr"](q)`
**DO:** Double-click the dots after `kw =`.
**SAY:** "Third, shaft power in kilowatts. It is density times gravity times flow in cubic metres per second times head, divided by efficiency, then divided by a thousand to get kilowatts."
**TYPE:** `rho * g * (q / 1000) * h / eta / 1000`
**DO:** Double-click the dots after `cost =`.
**SAY:** "Fourth, the annual cost: kilowatts times hours times tariff."
**TYPE:** `kw * hours * tariff`
**DO:** Click the Run arrow. Count one.

**SAY (when the table appears, scroll the output sideways if needed and say so):** "Pump A runs at about one hundred and seven percent of its best-efficiency flow, with an NPSH margin of two point three two metres. It draws seventeen point seven kilowatts and costs about twelve thousand seven hundred and sixty-two dollars a year. Pump B runs at ninety-three percent, with a margin of one point nine nine metres, sixteen point four kilowatts, and eleven thousand eight hundred and twenty-four dollars. Pump C runs at eighty-seven percent, but its margin is only one point zero eight metres. It draws sixteen kilowatts and costs eleven thousand five hundred and five dollars."

**DO:** Scroll to the next cell. Double-click the dots after `res["pass"] =`.
**SAY:** "Now the pass or fail rule. I'll type: the percent of best-efficiency flow is between seventy and one hundred and ten, and the NPSH margin is at least one point five."
**TYPE:** `res.pct_of_bep.between(70, 110) & (res.npsh_margin_m >= 1.5)`
**DO:** Click the Run arrow. Count one. Point at the new **pass** column.
**SAY:** "Pumps A and B are True, and pump C is False."
**SAY:** "Pump C is the cheapest, about three hundred and nineteen dollars a year less than pump B. But its margin of one point zero eight metres is below the one point five minimum, so it risks cavitation, and I reject it. Between A and B, pump B runs at eighty-three point six percent efficiency against seventy-seven point two, which saves about nine hundred and thirty-eight dollars a year. Pump A is also close to the one hundred and ten percent edge. So I recommend pump B, with pump A as the runner-up."

---

## Scene 5: Save the results and check the chart (about 2 minutes)

**DO:** Scroll to heading **5. Save the table and the chart**.
**SAY:** "I'm scrolling down to heading 5. The first line writes the results table to operating_points.csv, and the second draws the chart and saves it as operating_points.png. Failed pumps are drawn hollow."
**DO:** Click the Run arrow. Count one.
**SAY:** "It prints the file name operating_points.png, so the chart was saved."

**DO:** Point at the Explorer panel.
**SAY:** "In the Explorer panel, the two new files have appeared in the PumpTask folder. I'll click operating_points.csv to confirm the table saved."
**DO:** Click it. Count one. Pause 4 seconds with the pointer on the three rows.
**SAY:** "It has one row per pump with the flow, percent of best-efficiency flow, NPSH margin, power, cost and the pass column."
**DO:** Click operating_points.png in the Explorer. Count one.
**SAY:** "Now I'll open operating_points.png. The left panel shows the three pump head curves and the dashed system curve. The small box near fifty litres per second marks the zoom area. The right panel shows the three operating points. Pump A is the blue filled dot at forty-nine point nine one, pump B is the green dot at fifty point zero zero, and pump C is the hollow orange dot at fifty point two zero. Hollow means it failed the NPSH margin."

**DO:** Click the notebook tab. Press **Command + S**.
**SAY:** "I'll press Command plus S to save the executed notebook, so its outputs are kept."
**DO:** Click the yellow minimize button of the VS Code window. Count one.
**SAY:** "I'll minimize Visual Studio Code with the yellow button at the top left."

---

## Scene 6: Word, the recommendation memo (about 5 minutes)

**DO:** Click the blue Word icon in the Dock. Count one.
**SAY:** "I'll click the blue Word icon in the Dock to open the memo template. It has headings only: Purpose, Duty point and criteria, Results, Operating-point chart, and Recommendation. The To and From lines are roles, not names."

**DO:** Click the empty line under **1. Purpose**.
**SAY:** "I'll click the empty line under heading 1, Purpose, and write one sentence on what the memo is for."
**TYPE:** `Select a replacement pump for the chilled-water loop; duty is 50 L/s at 28 m.`

**DO:** Click the empty line under **2. Duty point and criteria**.
**SAY:** "Under heading 2, I'll state the criteria the pumps must meet."
**TYPE:** `Flow 70 to 110% of best-efficiency flow; NPSH margin at least 1.5 m; cost at 6,000 h and $0.12 per kWh.`

**DO:** Click the empty line under **3. Results**. Click the **Insert** tab at the top, click **Table**, and move across the grid to five columns by four rows. Click.
**SAY:** "For the results, I'll click the empty line under heading 3, then the Insert tab, then Table, and drag across the grid to five columns and four rows. That gives one header row and one row per pump."
**SAY:** "I'll type the header, then press the Tab key to move to the next cell. Tab moves one cell to the right."
**TYPE (burst 1):** `Pump` Tab `% of BEP flow` Tab `NPSH margin (m)` Tab `Annual cost` Tab `Result` Tab `A` Tab `107%` Tab `2.32` Tab `$12,762` Tab `Pass` Tab
**TYPE (burst 2):** `B` Tab `93%` Tab `1.99` Tab `$11,824` Tab `Pass` Tab `C` Tab `87%` Tab `1.08` Tab `$11,505` Tab `Fail (NPSH)`
**SAY (while typing the values):** "Pump A, a hundred and seven percent, margin two point three two, twelve thousand seven hundred and sixty-two dollars, pass. Pump B, ninety-three percent, one point nine nine, eleven thousand eight hundred and twenty-four dollars, pass. Pump C, eighty-seven percent, one point zero eight, eleven thousand five hundred and five dollars, fails the NPSH margin."

**DO:** Click the empty line under **4. Operating-point chart**. Click **Insert**, then **Pictures**, then **Picture from File**.
**SAY:** "Under heading 4, I'll click the empty line, then the Insert tab, Pictures, and Picture from File, to place the chart."
**DO:** In the dialog, click **Desktop**, double-click **PumpTask**, single-click **operating_points.png**, click **Insert** at the bottom right.
**SAY:** "In the dialog I'll open Desktop, then PumpTask, click operating_points.png, and click the Insert button at the bottom right."
**SAY:** "The chart sits under heading 4 at the page width, with the pump curves on the left and the zoomed operating points on the right."
*(If it is too large, drag one corner handle inward and say so.)*

**DO:** Click the empty line under **5. Recommendation and next step**.
**SAY:** "Under heading 5, I'll write the recommendation, in three short pieces."
**TYPE (burst 1):** `Buy pump B: it passes both criteria and is the cheapest pump that does.`
**TYPE (burst 2):** `Pump C is $319 a year cheaper but fails the NPSH margin, so it risks cavitation.`
**TYPE (burst 3):** `Pump A is the runner-up, $938 a year more than B.`

**DO:** Point at the page count in the status bar at the bottom left.
**SAY:** "The status bar at the bottom left reads Page 1 of 1, so the memo fits on one page. Every number matches the notebook table."

**DO:** Press **Command + S**.
**SAY:** "I'll press Command plus S to save the memo. In the dialog I'll type the name recommendation memo, make sure the location is PumpTask on this Mac, and click Save."
**TYPE:** `recommendation memo`
**DO:** Click **Save**. Count one.

**DO:** Click the **File** menu, then **Export**.
**SAY:** "To make the PDF, I'll open the File menu and choose Export. I'll set File Format to PDF, keep the name recommendation memo, and click Export."
**DO:** Choose **PDF**. Click **Export**. Count one.
**DO:** Click **File**, then **Open**. In the list, point at **recommendation memo.pdf** and **recommendation memo.docx**.
**SAY:** "To confirm both files exist, I'll open the File menu and Open. The list in PumpTask shows recommendation memo, dot docx, and recommendation memo, dot pdf, with their sizes. I'll click Cancel."
**DO:** Click **Cancel**. Click the yellow minimize button of Word.
**SAY:** "I'll minimize Word with the yellow button at the top left."

*(Do not open the PDF in Preview. Preview is a restricted app. Confirming through the Open list is enough.)*

---

## Scene 7: PowerPoint, the two-slide approval deck (about 3 minutes)

**DO:** Click the orange PowerPoint icon in the Dock. Count one.
**SAY:** "I'll click the orange PowerPoint icon in the Dock. A blank presentation is open, and I need two slides for the facilities manager's approval."

**DO:** Click **Home**, then **Layout**, then **Title Only**.
**SAY:** "On the Home tab, I'll click Layout and choose Title Only, because each slide needs a title and then my own content."
**DO:** Click the title placeholder.
**SAY:** "I'll click the title box and write the conclusion as the title."
**TYPE:** `Pump B meets the 50 L/s duty`

**DO:** Click **Insert**, **Pictures**, **Picture from File**. Choose **operating_points.png** in PumpTask. Click **Insert**.
**SAY:** "Now I'll click the Insert tab, Pictures, Picture from File, open PumpTask, select operating_points.png and click Insert. This is the chart that shows each pump's operating point."
**DO:** Drag a corner handle to enlarge the picture to the width below the title, then drag it into place.
**SAY:** "I'll drag a corner handle outward to enlarge the chart, and drag it below the title so both panels are readable."

**DO:** Click **Home**, then **New Slide**.
**SAY:** "On the Home tab, I'll click New Slide. It uses the same Title Only layout."
**DO:** Click the title box.
**TYPE:** `Pump B is the lowest-cost pump that passes`

**DO:** Click **Insert**, then **Table**, and drag across three columns by four rows. Click.
**SAY:** "For the cost comparison, I'll click the Insert tab, then Table, and drag across the grid to three columns and four rows."
**TYPE (burst 1):** `Pump` Tab `Annual cost` Tab `Result` Tab `A` Tab `$12,762` Tab `Pass` Tab
**TYPE (burst 2):** `B` Tab `$11,824` Tab `Pass` Tab `C` Tab `$11,505` Tab `Fail (NPSH)`
**SAY (while typing):** "Pump A costs twelve thousand seven hundred and sixty-two dollars and passes. Pump B costs eleven thousand eight hundred and twenty-four and passes. Pump C costs eleven thousand five hundred and five, the lowest, but fails the NPSH margin."

**DO:** Click **Insert**, **Text Box**. Click under the table.
**SAY:** "I'll click Insert, then Text Box, and click on the slide under the table to write the recommendation."
**TYPE:** `Recommend pump B; pump A is the runner-up.`

**DO:** Press **Command + S**.
**SAY:** "I'll press Command plus S to save the deck. I'll type the name approval deck, choose PumpTask on this Mac, and click Save."
**TYPE:** `approval deck`
**DO:** Click **Save**. Count one.

**DO:** Click the slide 1 thumbnail in the left panel, then slide 2.
**SAY:** "To check the deck, I'll click the slide 1 thumbnail in the left panel. The title states the conclusion, and the chart shows each pump's operating point. Now I'll click the slide 2 thumbnail. The table shows the cost comparison, and the line under it gives the recommendation. The numbers match the notebook and the memo."

---

## Scene 8: Wrap-up and stop (about 30 seconds)

**SAY:** "The work is complete and saved. The notebook, the results table and the chart are in PumpTask. The memo is saved as a Word file and a PDF, and the approval deck is saved. My recommendation to the facilities manager is pump B."
**DO:** Stay quiet. Open TaskRecorder from the Dock and click **Stop Recording**. **Do not narrate this.** Wait for Stopping, then Archiving, then Idle.

---

## If something goes wrong (guide: small mistakes)

Say what happened, fix it once, and check the fix:
- Typo in code: "I mistyped the bracket, so I'll select the line, retype it, and run the cell again to confirm the result."
- Wrong cell run: "That ran the wrong cell. I'll scroll back to the right one and run it from there."
- Chart or table too big: "The chart is wider than the margins, so I'll drag the corner handle inward until the page count reads one of one."
- A file dialog opens at the wrong folder: "The dialog opened in the wrong folder, so I'll click Desktop and then PumpTask."
- Restart the recording if searching, guessing, undoing and redoing take over, or if the final result is wrong and you cannot fix it on screen.

## Before you submit: spot-check against `guide.pdf`

- Clock shows seconds, dock on the left or right, one UI element changed, cursor default.
- Accessibility Inspector icon has a dot in the Dock, and its window is never visible.
- TaskRecorder appears only at Start and Stop. No Studio, Mercor, Odin, Insightful or `Metadata.rtf` on screen.
- No AI, Copilot or Designer on screen. No name or avatar in Word or PowerPoint.
- Narration under 220 words a minute, no silence over 45 seconds, every shortcut said.
- Video between 15:00 and 45:59, screenshots more than 0.5 per second, and the file named `video.mp4`.
