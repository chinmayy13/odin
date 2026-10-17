# pump_task

| File | Use |
|---|---|
| Pump Task Working Folder.zip | Unzip to the Desktop of the Recorder account before recording. Contains the six prepared inputs with the names the notebook expects (helper.py, input 1 pump curves.csv, input 2 piping data.json, pump selection.ipynb, data sheet template.docx, starter deck.pptx). Keep the zip as a clean backup of the starter notebook. |
| Deliverables REFERENCE.zip | Shows the correct Deliverables.zip layout and file names, and the expected outputs (executed notebook, two charts, briefing PDF and PPTX, data sheet). Use it to check your own results. Do not submit it. |
| Narration_Script.md | Word by word script, with actions, timings and guide.pdf page references. Read it from paper or a phone, never on the recorded screen. |

Do not submit the reference outputs. The video must show you creating the files, and Deliverables.zip must match what the video shows. Build your own Deliverables.zip after recording from the files you made, with the names in the reference zip.

Provenance: these files were written and tested by Claude, not Gemini. Studio only accepts Gemini for AI generated inputs, so do not label them "AI-generated before recording" unless that is true. If you review and run them yourself, label them as manually created, or ask Loki if unsure.

Needs on your Mac: Python 3 with numpy, pandas and matplotlib, plus the Jupyter extension in Visual Studio Code. Run the notebook once in a temporary folder before recording.

Tested here: the starter notebook runs from a clean unzip with no errors. Reference results: Pump B recommended at 119.6 m3/h, 27.1 m head, 2.01 m NPSH margin, 60,247 USD over five years. Pump A fails NPSH (margin 0.41 m). Pump C costs 87,504 USD.
