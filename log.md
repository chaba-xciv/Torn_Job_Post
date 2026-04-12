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
