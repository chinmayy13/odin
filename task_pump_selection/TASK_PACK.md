# Pump selection task: pack index

Idea status: approved. Apps: Visual Studio Code, Microsoft Word, PowerPoint.
This pack follows the approved text, `Project_Odin_Writer_Guidelines.md`, `guide.pdf` and `Project_Odin_Review_Lessons.md`.
**The recording itself is in `SCRIPT.docx` (also `SCRIPT.md`).** Read it start to finish before you record.

## 0. Two things to settle before you record

1. **Where the input files came from.** I (Claude) drafted the five inputs. The guide allows AI-made inputs only from Gemini, and the approved text says "AI-generated before recording". Ask @Loki: "My inputs were drafted by another AI. Can I use them, and how do I label them?" If the answer is no, rebuild the CSV and helper with Gemini and compare your results with the answer key below. Do not run my files through Gemini just to relabel them.
2. **Small gap in the approved text.** The approved starting materials list the CSV, the helper and the Word template. The recording also uses a starter notebook and a two-slide deck template. Say "prepared input" when you first show each, and include all five in `Deliverables.zip` as inputs. If you want the text to match exactly, submit a change request first.

## 1. Files

| File | Use |
|---|---|
| `SCRIPT.docx`, `SCRIPT.md` | word-by-word script with timing checkpoints, typing counter and trim lists |
| `Metadata.rtf` | filled in. Upload it separately, never in `Deliverables.zip` |
| `inputs/input_1_pump_curves.csv` | 24 rows: 3 pumps at 8 flow points |
| `inputs/input_2_pump_helpers.py` | fitting, plotting and table helpers |
| `inputs/input_3_starter_notebook.ipynb` | starter with 13 `FILL_IN` gaps (358 characters to type) |
| `inputs/input_4_memo_template.docx` | headings only, an empty line under each |
| `inputs/input_5_deck_template.pptx` | two empty slides, each with a title and a content box |
| `reference/` | answer key: executed notebook and outputs. **Never record or submit these** |
| `zips/pump_study_inputs.zip` | the five inputs in a folder called `pump_study`. Unzip onto the Recorder user's Desktop |
| `zips/Deliverables_starter.zip` | the five inputs already named `input 1.csv` to `input 5.pptx` |
| `zips/Odin_Pump_Task_Pack.zip` | everything above in one zip |

## 2. Answer key

System curve `H = 12 + 0.0064 Q^2` (Q in L/s). Duty 50 L/s at 28 m. NPSH available 6.0 m. 6,000 h a year, $0.12/kWh.

| Pump | Flow (L/s) | Head (m) | Efficiency | % of BEP flow | NPSH margin (m) | Shaft kW | Annual cost | Result |
|---|---|---|---|---|---|---|---|---|
| A | 49.91 | 27.94 | 77.2% | 107.3% | 2.32 | 17.72 | $12,762 | Pass |
| B | 50.00 | 28.00 | 83.6% | 92.6% | 1.99 | 16.42 | $11,824 | Pass |
| C | 50.20 | 28.13 | 86.7% | 86.5% | 1.08 | 15.98 | $11,505 | **Fail (NPSH)** |

Decision: **B**. C is cheapest ($319 a year below B) but its 1.08 m margin is under 1.5 m, so it risks cavitation. A is the runner-up, $938 a year more than B. I rehearsed the 13 typed lines against this key and the outputs matched exactly.

## 3. Text that must match everywhere

The **Goal** goes into four places: Studio (already approved), TaskRecorder, the opening Word note, and the `Metadata.rtf` Request. Paste only the Goal, never the Approval ID or the other headings.

> I am a mechanical engineer helping a facilities manager pick a replacement circulation pump for a building chilled-water loop. Using a synthetic CSV of head, efficiency and NPSH-required data for three candidate pumps, I will use Visual Studio Code to fit a head–flow curve for each pump in a Jupyter notebook and intersect it with the system curve to find its operating point. I will then check that the operating point sits within 70–110% of best-efficiency flow with at least 1.5 m of NPSH margin, and compare annual energy cost. In Microsoft Word I will write a one-page recommendation memo with the criteria table and operating-point chart. In PowerPoint I will build a two-slide approval deck so the facilities manager can approve the purchase.

- **TaskRecorder Used Apps:** Visual Studio Code, Microsoft Word, PowerPoint.
- **Metadata.rtf Topology:** Visual Studio Code (CREATE) -> Microsoft Word (CREATE) -> PowerPoint (CREATE) -> Visual Studio Code (LOOKUP). The last visit is the cross-check in Part 8.
- **Final Notes (exactly):** AI-generated before recording

## 4. Deliverables.zip (13 files, flat inside a folder named `Deliverables`)

Name every file with spaces. Build the zip after recording, from copies, with `zip -r -X "Deliverables.zip" Deliverables -x "*.DS_Store"`.

| In the study folder | In the zip |
|---|---|
| `input_1_pump_curves.csv` | `input 1.csv` |
| `input_2_pump_helpers.py` | `input 2.py` |
| `input_3_starter_notebook.ipynb` (untouched) | `input 3.ipynb` |
| `input_4_memo_template.docx` (untouched) | `input 4.docx` |
| `input_5_deck_template.pptx` (untouched) | `input 5.pptx` |
| `artifact_1.csv` (criteria table) | `artifact 1.csv` |
| `artifact_2.png` (cost chart) | `artifact 2.png` |
| `final_output_1.ipynb` | `final output 1.ipynb` |
| `final_output_2.csv` | `final output 2.csv` |
| `final_output_3.png` | `final output 3.png` |
| `final_output_4.docx` | `final output 4.docx` |
| `final_output_5.pdf` | `final output 5.pdf` |
| `final_output_6.pptx` | `final output 6.pptx` |

Upload four things to Studio: `Metadata.rtf`, `video.mp4` (from the `recording_...` folder, never renamed), the TaskRecorder zip `recording_*.zip`, and `Deliverables.zip`.

## 5. What to rehearse first

- Run the dry run in `SCRIPT.docx` once: it proves the kernel, the Word and PowerPoint menus, and that Export-to-PDF does not open Preview (a restricted app).
- Do the typing speed test and the ampersand key test. The less-than and greater-than keys are never typed in this task.
- Check that the memo fits on one page, because the script has you read "Page 1 of 1" aloud.
