# Pump selection task: complete pack

Idea status: approved. Apps: Visual Studio Code, Microsoft Word, PowerPoint.
Everything below follows the approved text, `Project_Odin_Writer_Guidelines.md` and `Project_Odin_Review_Lessons.md`.

## 0. Read this first

1. **Where the input files came from.** I (Claude) drafted `pump_curves.csv`, `pump_helpers.py`, the notebook skeleton and the memo template. The guide says AI-made inputs may only come from Gemini, and the approved text says "AI-generated before recording". Before you use them:
   - **Safest:** ask @Loki in the domain Loki channel: "My inputs were drafted by another AI. Can I use them, and how do I label them?"
   - **Fallback:** rebuild the CSV and helper yourself or with Gemini, and check your results against section 2. If Gemini's numbers differ, your results will differ slightly, which is fine as long as the logic holds.
   - Do not run my files through Gemini just to relabel them.
2. **Small gap in the approved text.** Step 1 says "prepared notebook". The approved starting materials list only the CSV, helper and Word template. Say "prepared notebook with empty cells" in the first narration, and include it in `Deliverables.zip` as an input.
3. **Typing budget is tight.** Non-coding tasks must stay under 20% typing. The pack is built for about 15%. See section 6.

## 1. Files in this folder

| File | Use |
|---|---|
| `inputs/pump_curves.csv` | input: 24 rows (3 pumps, 8 flow points) |
| `inputs/pump_helpers.py` | input: fitting report and chart function |
| `inputs/pump_selection.ipynb` | input: skeleton, comments and `...` placeholders where you type |
| `inputs/memo_template.docx` | input: headings only |
| `reference/pump_selection_solved.ipynb` | answer key, executed. **Do not record or submit this.** |
| `reference/operating_points.csv`, `.png` | what your outputs should look like |
| `Metadata.rtf` | filled in. Upload it separately, not in the zip |

To run the notebook, keep `pump_curves.csv`, `pump_helpers.py` and the notebook in **one folder** (for example `PumpTask` on the Recorder user's Desktop).

## 2. Answer key (use it to check yourself)

System curve: `H = 12 + 0.0064 Q^2` (Q in L/s). Duty 50 L/s at 28 m. NPSH available 6.0 m. 6,000 h/yr, $0.12/kWh.

| Pump | Operating flow (L/s) | Head (m) | Efficiency | % of BEP flow | NPSH margin (m) | Shaft kW | Annual cost | Result |
|---|---|---|---|---|---|---|---|---|
| A | 49.91 | 27.94 | 77.2% | 107.3% | 2.32 | 17.72 | $12,762 | Pass |
| B | 50.00 | 28.00 | 83.6% | 92.6% | 1.99 | 16.42 | $11,824 | Pass |
| C | 50.20 | 28.13 | 86.7% | 86.5% | 1.08 | 15.98 | $11,505 | **Fail (NPSH)** |

- **Decision:** buy **B**. C is cheapest ($319 a year less than B) but its 1.08 m margin is under 1.5 m, so it risks cavitation. A is the runner-up, about $938 a year more than B.
- **Hand check:** pump B's head at 50.00 L/s is 28.00 m on both curves, difference about 0.00 m (limit 0.1 m).
- **Fit error (largest, from `fit_report`):** head 0.04 m, efficiency 0.05 points, NPSHr 0.04 m, so the quadratic fits are tight.

## 3. Text to paste (all must match exactly)

**Goal** goes in four places: Studio (already approved), TaskRecorder Task Description, the opening Word note, and the `Metadata.rtf` Request. Paste **only the Goal**, never the Approval ID or the other headings.

> I am a mechanical engineer helping a facilities manager pick a replacement circulation pump for a building chilled-water loop. Using a synthetic CSV of head, efficiency and NPSH-required data for three candidate pumps, I will use Visual Studio Code to fit a head–flow curve for each pump in a Jupyter notebook and intersect it with the system curve to find its operating point. I will then check that the operating point sits within 70–110% of best-efficiency flow with at least 1.5 m of NPSH margin, and compare annual energy cost. In Microsoft Word I will write a one-page recommendation memo with the criteria table and operating-point chart. In PowerPoint I will build a two-slide approval deck so the facilities manager can approve the purchase.

**TaskRecorder Used Apps:** Visual Studio Code, Microsoft Word, PowerPoint.

**Metadata.rtf** is already filled in this folder: Topology `Visual Studio Code (CREATE) -> Microsoft Word (CREATE) -> PowerPoint (CREATE)`, Request = the Goal, and a six-line Task Description. The red example section is removed. Open it once to check the formatting, but never open it while recording.

**Studio, "Input and artifact files":** pick what is true after you resolve section 0, item 1. **Final Notes (exactly):** `AI-generated before recording`

## 4. Before you press Start

- [ ] Insightful running and minimized. Notifications off. Mac plugged in. At least 35 GB free.
- [ ] Recorder user account. Dock left or right. Clock shows seconds. New wallpaper plus dark mode (two changes). Cursor default.
- [ ] Accessibility Inspector running with its window closed (dot under the dock icon).
- [ ] **VS Code:**
  - Python and Jupyter extensions installed, and the kernel already selected.
  - Folder `PumpTask` open with the skeleton notebook.
  - Chat, Copilot and every AI panel closed or disabled (AI on screen fails the recording).
  - **Dry run** in a temporary copy so the first cell is fast, then reset the notebook to the skeleton.
- [ ] **Word:** licensed and signed in with the OTA account. No name, email or avatar visible in the title bar or ribbon. The Copilot ribbon button is never touched. The memo template is open in its own window, minimized.
- [ ] **PowerPoint:** same checks. A blank presentation is open, **Designer and design-idea suggestions turned off** (these look like AI).
- [ ] Opening note is the **only** window visible: the Goal pasted into a new Word document (not Notes or TextEdit). If you reuse Word for the memo, it counts as an app.
- [ ] No Studio, Slack, guidelines, Metadata.rtf or Drive tabs open. No file dialog should reveal a real name, so keep everything in `Desktop/PumpTask`.
- [ ] TaskRecorder: signed in with the OTA account, permissions green, microphone on, **window dragged larger until the whole Goal is visible**, Used Apps filled. 1-minute audio test done.

## 5. Recording script (about 17 minutes of script, so roughly 28 minutes of video)

Say every scroll, every shortcut, and the where, what and why of every click. Pause one second after every click. Never say "here" or "this" alone. Stop recording silently at the end, and never narrate TaskRecorder.

| # | Min | App | What you do | Typed (what) |
|---|---|---|---|---|
| 0 | 0:20 | Word (opening note) | Say only: "I will be beginning my task soon. Here is the workflow I have in mind." Minimize the note. | none |
| 1 | 2 | VS Code | Open the prepared notebook, run the import and `df.head(10)` cell, say what the columns and units are, then type the min/max check. Say the inputs are prepared files, royalty-free and copyright-free. | `df.groupby("pump").agg(["min", "max"])` |
| 2 | 2 | VS Code | Explain why a quadratic fits a pump curve. Type the fit and report cells, and read the error table. | `fits = fit_all(df)` and `fit_report(df, fits)` |
| 3 | 3 | VS Code | System curve: static head, and calibrate k from the duty point. Type the intersection line, then the hand check on pump B. Say the result out loud. | `static_head`, `k`, `system`; `roots = (f["head"] - system).roots`; the hand-check line |
| 4 | 4 | VS Code | Constants (state each assumption). Complete four lines in the criteria loop: `q_bep`, `margin`, `kw`, `cost`. Run it, explain each column. Type the pass/fail rule and explain C. | the constants line; four loop lines; the pass/fail line |
| 5 | 1.5 | VS Code | Run the save cell. Open `operating_points.png` and walk through the zoom panel. Type the two-sentence decision. | decision markdown (about 40 words) |
| 6 | 3 | Word | Open the memo template window. Fill Purpose and Criteria in one line each. Type the 3-row table (5 columns). Insert the chart (Insert > Pictures > Picture from File). Type the recommendation. | about 60 words plus 15 table cells |
| 7 | 1 | Word | File > Save As, set File Format to PDF, name it, and save the .docx too. Open the PDF check on screen. | none |
| 8 | 2.5 | PowerPoint | Slide 1: Title Only layout, insert the chart. Slide 2: new slide, 3-row table plus the recommendation line. Save as .pptx. | 2 titles, 9 table cells, 1 line |
| 9 | 0.5 | PowerPoint | Final read-through of both slides, then silent stop. | none |

Narration example for step 3: "I'll click the empty cell under 'System curve and operating points', then type the line that subtracts the system curve from pump B's head fit. I'm doing this because the operating point is where the two heads are equal, so the roots of the difference give the flow."

## 6. Typing plan (target under 15%; limit is 20%)

About 25 short lines of code (about 90 s), about 60 words in Word (about 90 s), the 15-cell table (about 45 s), and the deck text (about 60 s). That is about 4.5 minutes out of 28.

- Keep every burst **under 30 s**. Between bursts, review and point at what you typed.
- Rehearse once with a stopwatch. If the rehearsal is over 15%, copy numbers instead of retyping them. Say each shortcut aloud ("Command plus C").
- Mouse idle never over 20 s, and keep moving the pointer along the table while code runs.

## 7. Word memo and PowerPoint text (keep it this short)

**Word (one page):**
- Purpose: Select a replacement pump for the chilled-water loop (duty 50 L/s at 28 m).
- Criteria: Operating flow 70–110% of best-efficiency flow, NPSH margin at least 1.5 m (6.0 m available), annual energy cost at 6,000 h and $0.12/kWh.
- Table: Pump | % of BEP flow | NPSH margin (m) | Annual cost | Result, with rows A 107%, 2.3, $12,762, Pass; B 93%, 2.0, $11,824, Pass; C 87%, 1.1, $11,505, Fail.
- Recommendation: Buy pump B. It passes both criteria and is the cheapest pump that does. Pump C costs $319 a year less but its 1.1 m margin is below 1.5 m, which risks cavitation. Pump A is the runner-up, $938 a year more than B. Approval requested to order pump B.

**PowerPoint:**
- Slide 1 title: "Pump B meets duty at 50 L/s". Body: the chart image.
- Slide 2 title: "Pump B is the lowest-cost pump that passes". Table: Pump | Annual cost | Result (A $12,762 Pass; B $11,824 Pass; C $11,505 Fail NPSH). Line: "Recommend B; A is the runner-up."

## 8. Deliverables.zip (name with spaces, keep extensions)

Build it **after** recording, from copies. Rename only the copies, so the notebook still imports `pump_helpers` during the recording. Remove Mac junk with `zip -d "Deliverables.zip" "__MACOSX/*" "*.DS_Store"` or build with `zip -r -X "Deliverables.zip" Deliverables -x "*.DS_Store"`, not Finder's Compress.

| Name in the zip | From |
|---|---|
| `input 1.csv` | `pump_curves.csv` |
| `input 2.py` | `pump_helpers.py` |
| `input 3.ipynb` | the blank skeleton notebook |
| `input 4.docx` | `memo_template.docx` (blank) |
| `final output 1.ipynb` | your executed notebook |
| `final output 2.csv` | `operating_points.csv` |
| `final output 3.png` | `operating_points.png` |
| `final output 4.docx` | your memo |
| `final output 5.pdf` | your memo PDF |
| `final output 6.pptx` | your deck |

Do not include `Metadata.rtf` in the zip. Upload four things to Studio: `Metadata.rtf`, `video.mp4` (from the `recording_...` folder, unrenamed), the `recording_*.zip`, and `Deliverables.zip`.

## 9. After recording: checks that fail this task most often

- **Video 15:00–45:59** (aim for about 28). Wait for Stopping, then Archiving, then Idle. Open `video.mp4` in QuickTime and spot-check the start, middle and end.
- **Screenshots** more than 0.5 per second of video.
- **Intro** under 20 s, with only the one sentence and the opening note shown.
- **Windows:** no unused window covering over 25% of another. Minimize VS Code before showing Word, and Word before PowerPoint. File dialogs are fine.
- **No AI on screen:** Copilot, Designer, Chat, suggestions. No Studio, Mercor or Metadata window. No name or avatar in Word or PowerPoint. No TaskRecorder or Insightful after the start.
- **Narration:** under 220 words a minute, no silence over 45 s, every scroll and shortcut said. Never say "personal information".
- Everything promised in the Goal appears on screen: fit, intersection, 70–110% and NPSH checks, cost comparison, memo with table and chart, PDF export, two-slide deck. If you cut anything, change the Studio text first (change request).
- Fill Mac spec and display fields to match the recording actually made, then run both AutoQC checks, tick each manual box only after checking it, and tick the final box last.

## 10. Add the next review to `Project_Odin_Review_Lessons.md`

Copy its section 10 block when this task is reviewed.
