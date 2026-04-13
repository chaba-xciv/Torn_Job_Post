## Log: Refactor to English and use JS data

**Issue:**
1. The web application (`index.html`) was in Thai, violating the project guideline "เนื้อหาในโปรเจคทั้งหมดจะต้องเป็นภาษาอังกฤษเสมอ ทุกกรณี" (All content in the project must always be in English).
2. The application used hardcoded data (`jobsDB` array) inside `index.html` instead of utilizing the detailed data available in the external file `company_positions.js`.

**Detection:**
- Human Error: The user explicitly pointed out these issues in their prompt, indicating that the current state of the code did not align with their expectations and project guidelines.

**Root Cause:**
- The initial codebase was developed in Thai and with hardcoded data, likely for quick prototyping or before the English-only rule was established.

**Resolution:**
1.  **Refactor Data Source:**
    - Added `<script src="company_positions.js"></script>` to `index.html`.
    - Removed the hardcoded `const jobsDB = [...]` array.
    - Created a `generateJobsDB()` function to dynamically iterate through `window.TORN_COMPANY_POSITIONS` (provided by `company_positions.js`), extract relevant stats, sort them to determine primary/secondary requirements, and populate the `jobsDB` array in the format expected by the rest of the application.
    - Modified `initDropdowns()` to call `generateJobsDB()` before initializing the UI.
2.  **Internationalization (i18n):**
    - Translated all Thai text strings (HTML content, button labels, placeholders, JavaScript alerts, generated HTML templates) in `index.html` to English.
    - Changed `<html lang="th">` to `<html lang="en">`.
3. **Bug Fix (AI Error detection during Playwright testing):**
    - While verifying the frontend with Playwright, the script failed to click the 'Hiring' tab.
    - **Cause:** The `switchTab(tabId)` function relied on the deprecated global `event` object to determine which element was clicked (`event.target`). Playwright's `evaluate()` or explicit clicking mechanism doesn't reliably set this global object in all contexts, leading to a `TypeError`.
    - **Fix:** Modified `switchTab(tabId, evt)` to accept the event object explicitly. Updated the `onclick` handlers in HTML to pass the event (`onclick="switchTab('worker', event)"`). Added a fallback for older environments if the explicit event wasn't passed.
    - **Prevention:** Always pass the `event` object explicitly in inline event handlers rather than relying on the implicit global `window.event`.

**Prevention/Future Mitigation:**
- Always check the `AGENTS.md` or memory for project-wide guidelines (like language requirements) before making changes.
- When dealing with data, ensure it's loaded from the single source of truth (e.g., external configuration files) rather than being duplicated or hardcoded.
- Always use modern JavaScript practices, such as explicitly passing event objects, to ensure broad compatibility and testability.

## Update: Advanced Table UI and Work Styles

### Changes Made:
- **Worker Tab Redesign**: Replaced the 3-dropdown limit with a dynamic, sortable, and filterable table showing all available jobs, their required stats, and the calculated efficiency based on the user's input.
- **Hiring Tab Redesign**: Replaced the single-dropdown position selection with a table displaying all positions for the selected company, allowing multiple selections, and showing dynamically calculated required stats based on the target efficiency.
- **Work Style Options**: Added radio button options to both tabs allowing users to define their desired work style (e.g., Salary, Tax, Unpaid) to clarify the mutually beneficial relationships between employees and companies in Torn City.
- **Tooltips**: Implemented hover tooltips using CSS on important fields (Target Eff, Work Styles) to provide clear explanations and improve UX.
- **HTML Generation**: Updated the final HTML output generation logic to iterate over the checked checkboxes in the tables and include the selected Work Style in the generated forum post code.

### Reason for Changes:
- To provide a more robust and scalable way for users to browse and select jobs, rather than being limited to 3 dropdowns.
- To improve user experience by allowing sorting by efficiency and filtering out unwanted companies.
- To better align the tool with actual Torn City gameplay dynamics, where employment often involves negotiating salaries, taxes, or unpaid arrangements for perks.

### Error Logging:
- **Type:** AI Error / Oversight
- **Detection:** During code review.
- **Cause:** Temporary python helper scripts (`update_index.py`, etc.) used to apply the complex multiline string replacements were left in the repository directory after execution.
- **Resolution:** Deleted the temporary python files using `rm`.
- **Future Prevention:** Remember to clean up temporary sandbox files or create them outside the repository root (e.g., in `/tmp` or the home directory).

## Update: Fix Merit Calculation and HTML Generation

### Changes Made:
- **Merit Values**: Updated the merit dropdown to correctly represent 1% per upgrade (up to 10%), fixing the previous incorrect assumption of 3%.
- **Stat Calculation**: Removed the merit multiplier from the base `calculateMyStats()` function, ensuring efficiency is calculated strictly using raw stats.
- **Worker HTML Generator**: Modified `generateWorkerHTML()` to format the text output exactly as requested: `with X% eff job stats + Y% merit Y/10`.
- **Hiring HTML Generator**: Removed the hardcoded fallback text "Good Pay / Daily Trains" from `generateHiringHTML()`. The "What we offer" section is now conditionally generated only if the user types something into the text area.

### Reason for Changes:
- To adhere to actual game mechanics (1 merit = 1% stat boost, applied as a flat percentage on top of base efficiency, rather than modifying raw stats before calculation).
- To make the generated forum posts cleaner and more accurate to the user's intent.

### Error Logging:
- **Type:** Human Error / Incomplete Specification
- **Detection:** User feedback.
- **Cause:** The initial instructions did not specify that merits provide exactly a 1% boost and are calculated differently than base stats, nor did it specify the exact wording required for the HTML output.
- **Resolution:** Adjusted the math and the string generation templates based on the user's clarifying feedback.
