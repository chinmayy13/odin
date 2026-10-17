# Pump selection task: full pack

Apps: Visual Studio Code (Jupyter notebook), PowerPoint, Microsoft Word.
Rule reminder: use the Goal text that Studio approved. Paste it word for word into Studio, TaskRecorder, the opening Word document and the Metadata.rtf Request. Do not paste it from this file.

Last checked against Project_Odin_Review_Lessons.md and the Studio criteria list (items 1 to 35).

The finished files (working folder, reference deliverables, narration script) are in the pump_task folder. Where the numbers here differ from earlier drafts, the notebook output in pump_task is the source of truth, and this file now matches it.

---

## 1. The story and the answer key

The plant needs a new cooling water pump. The duty needs at least 110 m3/h through the existing piping. Three candidate pumps. The notebook shows the answer is Pump B, and why the cheapest pump (A) and the biggest pump (C) are the wrong choices.

Reference results (computed and checked before writing this pack, use them to confirm your notebook):

| Item | Pump A | Pump B | Pump C |
|---|---|---|---|
| Operating flow (m3/h) | 118.5 | 119.6 | 149.5 |
| Operating head (m) | 26.9 | 27.1 | 32.1 |
| Flow as % of best efficiency flow | 113% | 101% | 91% |
| Efficiency at operating point | 0.729 | 0.780 | 0.794 |
| Shaft power (kW) | 11.85 | 11.26 | 16.38 |
| NPSH available (m) | 4.28 | 4.27 | 3.90 |
| NPSH required (m) | 3.87 | 2.26 | 2.39 |
| NPSH margin (m) | 0.41 | 2.01 | 1.51 |
| NPSH ratio (avail / req) | 1.11 | 1.89 | 1.63 |
| Energy cost per year (USD) | 11,381 | 10,809 | 15,721 |
| Purchase price (USD) | 4,800 | 6,200 | 8,900 |
| 5 year cost (USD) | 61,703 | 60,247 | 87,504 |

Decision criteria to say out loud:
1. Delivers at least 110 m3/h.
2. Operates between 70% and 120% of its best efficiency flow.
3. NPSH ratio of at least 1.3 and margin of at least 1.0 m, so there is no cavitation risk.
4. Lowest 5 year cost among the pumps that pass 1 to 3.

Result: A fails criterion 3 (margin 0.41 m, ratio 1.11). C passes everything but costs far more and delivers a lot of flow the plant does not need. B passes everything and has the lowest 5 year cost. Recommend Pump B.

Hand check value (system head at 120 m3/h): velocity 1.790 m/s, Reynolds 343,010, friction factor 0.0167 (Colebrook), friction loss 2.39 m, fittings loss 1.71 m, heat exchanger 5.00 m, static 18.00 m, total 27.11 m. The notebook's independent hand check uses the Swamee-Jain friction factor (0.0168) and gets 27.12 m, a difference of 0.013 m.

---

## 2. Inputs to prepare before recording

| File name in Deliverables.zip | What it is |
|---|---|
| input 1 pump curves.csv | Flow, head, efficiency, NPSH required and price for the three pumps (33 rows) |
| input 2 piping data.json | Pipe diameter, roughness, lengths, fitting factors, static head, suction lift, water properties, running hours, electricity rate |
| input 3 helper.py | Functions for friction factor, head loss, system curve, curve fitting, operating point, NPSH, cost and plots (called helper.py in the working folder) |
| input 4 starter notebook.ipynb | Notebook with nine steps, one ready to run cell each (called pump selection.ipynb in the working folder) |
| input 5 data sheet template.docx | One page pump data sheet with empty fields and tables |
| input 6 starter deck.pptx | Three titled slides, with caption text already in place on slides 1 and 2 |

All six files are built and tested in the pump_task folder (Pump Task Working Folder.zip).

Generator for inputs 1 and 2 is in Appendix A. Run it once, before recording.

Provenance, read carefully:
- Studio only accepts Gemini for AI generated inputs. Files written by another AI tool must not be labelled "AI generated before recording".
- If you write or run the generator yourself and review every number, label the files "Manually created file".
- If Gemini made them, label them "AI generated before recording" and put exactly that text in Final Notes.
- If you are unsure, ask Loki before recording.

---

## 3. Studio fields (before recording)

- Resolution, Light or Dark mode, dock position (left or right), wallpaper changed: fill in exactly what your screen uses. Check again after recording.
- Mac spec: Apple menu, About This Mac for chip and memory. Storage from System Settings, General, Storage.
- Input and artifact files: tick the option that matches how you made the files (see provenance above).
- Apps: Visual Studio Code, Microsoft Word, PowerPoint. These must match TaskRecorder and Metadata.rtf.

---

## 4. Notebook plan (all cells ready, you click Run)

1. Load the CSV and JSON. Show the first rows. Print the duty requirement.
2. Compute friction factor and head loss at 120 m3/h with the helper. Print velocity, Reynolds number and friction factor.
3. Hand check cell: the Darcy-Weisbach arithmetic written out line by line. Compare with step 2 (27.11 m).
4. Build the system curve from 20 to 200 m3/h and plot it.
5. Overlay the three pump curves. Mark each operating point.
6. Table: flow, head, percent of best efficiency flow, efficiency, power.
7. NPSH available curve against each NPSH required curve. Print margin and ratio.
8. Energy and 5 year cost table.
9. Decision table with pass or fail for each criterion. Save the main chart as a PNG.

Typing: almost none. You only change one number (for example the electricity rate) to show the sensitivity, about 15 seconds. Keep each typing burst short.

---

## 5. Recording flow (script time about 17 minutes, video usually 1.6 to 1.7 times longer)

Before Start: all three apps open and loaded, notebook already open with kernel ready, PowerPoint blank deck ready, Word data sheet template open, everything minimized. Only the Word window with the Goal is visible behind TaskRecorder.

| Step | Time | What you do | Why you say |
|---|---|---|---|
| 0 | 0:20 | Start, minimize TaskRecorder, say only: "I will be beginning my task soon. Here is the workflow I have in mind." Minimize the Goal document. | Required intro |
| 1 | 2:00 | Open VS Code from the Dock. Run the load cell. Scroll and say every scroll. | State the duty and the three candidate pumps |
| 2 | 3:00 | Run the head loss cell. Run the hand check cell. Compare 27.11 m. | Shows you trust but verify the calculation |
| 3 | 2:30 | Run the system curve cell. Run the overlay cell. Point to each intersection. | Operating point is where system and pump heads match |
| 4 | 3:00 | Run the table, NPSH and cost cells. Point to margin and ratio. Change the electricity rate once, rerun, show the ranking stays the same. | Cavitation risk and cost drive the choice |
| 5 | 1:00 | Run the decision table cell. Save the chart PNG. | Pick Pump B and say why A and C lose |
| 6 | 3:30 | PowerPoint: 3 slides. Insert the PNG, add a small table and three bullets. Export to PDF (File, Export). | Briefing for the plant manager |
| 7 | 2:30 | Word: fill the data sheet fields, duty point, selected pump, NPSH check. Save. | Procurement needs a single page spec |
| 8 | 0:30 | Check the saved files in the app folders. Bring TaskRecorder forward and stop silently. | Do not narrate TaskRecorder |

Sample narration lines (what, where, why):
- "I will click the green Run arrow at the left edge of the first code cell to load the pump curves, so we can see the three candidates."
- "I am scrolling down with the mouse wheel until I reach the heading Hand check, because I want an independent calculation of the system head at 120 cubic metres per hour."
- "The hand check gives 27.11 metres and the helper gives the same value, so the head loss function is correct."
- "On the plot, the red dot on the left is Pump A. Its flow is 113 percent of its best efficiency flow, and its NPSH margin is only 0.41 metres, so it is a cavitation risk."
- "I will press Command plus S to save the deck." (Say every shortcut.)

Say once, at the first use: "These input files are prepared inputs, free of royalties and copyright." Do not name any AI tool. Never read the Goal aloud.

---

## 6. Deliverables.zip

Name every file with spaces. Inputs first, then artifacts, then final outputs. Do not include Metadata.rtf.

- input 1 pump curves.csv
- input 2 piping data.json
- input 3 helper.py
- input 4 starter notebook.ipynb
- input 5 data sheet template.docx
- input 6 starter deck.pptx
- artifact 1 executed notebook.ipynb
- artifact 2 system and pump curves.png
- artifact 3 comparison table.png
- final output 1 briefing.pdf
- final output 2 briefing.pptx
- final output 3 pump data sheet.docx

Zip from Terminal before or after recording is fine, but not during. Use: `zip -r -X "Deliverables.zip" Deliverables -x "*.DS_Store"`. Then check with `unzip -l "Deliverables.zip"`.

---

## 7. Metadata.rtf (use the template, delete the red example section)

Topology:
Visual Studio Code (LOOKUP) -> Visual Studio Code (CREATE) -> PowerPoint (CREATE) -> Microsoft Word (MODIFY)

Request:
Paste the approved Goal word for word.

Task Description:
1. Load the piping data sheet and manufacturer pump curves in Visual Studio Code and review the duty requirement.
2. Calculate pipe head loss with the Darcy-Weisbach method, build the system curve and verify one point by hand.
3. Overlay the three pump curves, find each operating point, and check best efficiency position and NPSH margin.
4. Calculate power and yearly energy cost, compare five year cost and choose Pump B.
5. Build a 3 slide PowerPoint briefing with the chart, comparison table and recommendation, and export it to PDF.
6. Complete the Word pump data sheet for procurement with the duty point, selected pump and checks.

Open question: the opening Goal document is in Word, but Word is also used later for real work, so it is already listed. If you want certainty on whether to add a Word LOOKUP at the start of the Topology, ask Loki.

Upload Metadata.rtf as its own file in Studio, separate from Deliverables.zip. The apps in it must match Studio.

---

## 8. Final note (Studio)

Choose the one that is true:
- Gemini made the inputs: `AI-generated before recording`
- You made them yourself: `Input files are synthetic data prepared by me before recording. No personal information. No third party content.`

---

## 9. Checklist mapped to the Studio criteria

Before Start:
- Dock on left or right, visible. Seconds on the clock. Wallpaper changed. (7, 8, 9, 15)
- Accessibility Inspector running with a dot, window closed. (10, 11)
- TaskRecorder shows the exact Goal and the three apps. Enlarge the window so every line is visible. (12)
- Goal document visible at start, intro under 20 seconds. (13, 14)
- Insightful minimized, notifications off, Finder closed, Mac plugged in.
- VS Code: Copilot and any AI chat panel closed, inline suggestions off, no signed in account visible, folder path has no real name. (29, 30)
- Run the whole notebook once in a temporary folder just before recording so the first cell on camera is quick.

While recording:
- Pause 1 second after every click. Say every scroll and every shortcut. (21, 24, 28)
- Keep windows to one clear window at a time, use Fill, never Full Screen. (17)
- No pointer idle over 20 seconds, no silence over 45 seconds, no typing burst over 30 seconds. (18, 19, 22)
- Never show Metadata.rtf, Studio, Slack, Mercor or Insightful. (16, 27, 31)
- Do not narrate personal information or TaskRecorder.

After recording:
- Wait for Idle (Stopping, Archiving, Idle).
- Video length 15:00 to 45:59, open the file in QuickTime and scrub start, middle, end. (3, 4)
- Upload `video.mp4` unchanged from the `recording_...` folder, plus `recording_...zip`. (1, 2)
- Run both AutoQC checks, tick each manual check only after checking it against the video.

---

## Appendix A: generator for input 1 and input 2

```python
import csv, json
rho, mu = 995.7, 0.8e-3

PIPING = dict(
    fluid="Cooling water at 30 C", density_kg_m3=rho, viscosity_Pa_s=mu,
    vapor_pressure_Pa=4242, atmospheric_pressure_Pa=101325,
    pipe_inner_diameter_m=0.154, roughness_m=0.000045,
    discharge_length_m=120, suction_length_m=15,
    discharge_fittings_K=8.0, suction_fittings_K=2.5,
    static_head_m=18.0, suction_lift_m=5.0,
    heat_exchanger_head_m_at_120_m3h=5.0,
    required_flow_m3h=110, running_hours_per_year=8000, electricity_usd_per_kwh=0.12,
)
PUMPS = {
 "Pump A": dict(H0=36.0, a=6.5e-4, Qbep=105, eta=0.74, w=110, n0=2.4, b=1.05e-4, price=4800),
 "Pump B": dict(H0=38.5, a=8.0e-4, Qbep=118, eta=0.78, w=120, n0=1.4, b=0.6e-4, price=6200),
 "Pump C": dict(H0=41.0, a=4.0e-4, Qbep=165, eta=0.80, w=180, n0=1.5, b=0.4e-4, price=8900),
}
with open("input 1 pump curves.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["pump", "flow_m3h", "head_m", "efficiency", "npshr_m", "purchase_price_usd"])
    for name, p in PUMPS.items():
        for Q in range(0, 201, 20):
            eta = max(p["eta"] * (1 - ((Q - p["Qbep"]) / p["w"]) ** 2), 0)
            w.writerow([name, Q, round(p["H0"] - p["a"] * Q ** 2, 2), round(eta, 3),
                        round(p["n0"] + p["b"] * Q ** 2, 2), p["price"]])
with open("input 2 piping data.json", "w") as f:
    json.dump(PIPING, f, indent=2)
```

Model used for the reference results: Colebrook friction factor, Darcy-Weisbach head loss on 135 m of 154 mm pipe (120 m discharge, 15 m suction) with fitting factors 8.0 and 2.5, 18 m static head, heat exchanger loss 5 m at 120 m3/h scaled by flow squared, suction lift 5 m, 8000 running hours per year at 0.12 USD per kWh. Pump head, efficiency and NPSH required follow the simple curves in the generator, and the operating point is where pump head equals system head.
