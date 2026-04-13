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

## Update: Custom Notes and Application Links

### Changes Made:
- **Worker Tab Custom Notes**: Replaced the hardcoded 'Active daily, looking for a stable company. PM me!' text with a blank text area so job seekers can provide their own specific notes without relying on repetitive boilerplate.
- **Hiring Tab Application Link**: Added a 'Company Link' input to the Hiring Tab. If provided, the generator appends a hyperlinked `[Apply Here]` button to the bottom of the forum post, streamlining the recruitment process.

### Reason for Changes:
- To encourage personalized and authentic forum posts from job seekers.
- To reduce friction for players applying to companies by providing direct links.

### Error Logging:
- **Type:** Human Error / Incomplete Specification
- **Detection:** User feedback.
- **Cause:** The previous prompt did not specify removing the default boilerplate text for workers, nor did it explicitly mention the need for an application link field for employers.
- **Resolution:** Added the requested inputs and modified the HTML template generators to consume them correctly.

## Update: UI Revamp, Themes, Live Preview, and LocalStorage

### Changes Made:
- **Responsive Layout:** Refactored CSS using Flexbox and Grid to ensure the layout is clean, fits well on desktop and mobile screens, and eliminates unnecessary vertical/horizontal scrolling.
- **Theme Toggle:** Added a Light/Dark theme toggle button in the header. The default theme inherits the user's OS preference via `prefers-color-scheme`, and changes are saved to `localStorage`.
- **Post Color Themes:** Added a dropdown selection (Default, Torn Blue, Green, Red, Purple, Orange) to choose the accent color for the generated HTML post.
- **HTML Card Format:** Wrapped the generated HTML output in a stylish inline CSS card to improve readability on the Torn forums.
- **Apply Button:** Converted the plain text link in the Hiring post to an attractive "Apply Here" button using inline CSS.
- **Live HTML Preview:** Added a section below the HTML code boxes to render and preview the HTML output dynamically in the current Light/Dark theme context.
- **Local Storage Integration:** Automatically saves form inputs (stats, preferences, notes) to `localStorage` to persist data across reloads, preventing data loss.
- **Clear Data Button:** Added a 'Clear' button to the header to easily purge `localStorage` and reset the form.
- **Footer:** Added a developer attribution footer linking to Jules AI and the project's GitHub repository.

### Reason for Changes:
- Requested by user to enhance the UX/UI experience, make the tool more professional, and provide better visual feedback (preview) of what the forum post will look like before copying.
- Implementing memory persistence (`localStorage`) greatly enhances usability by saving the user's work.

### Error Logging:
- **Type:** None
- **Detection:** N/A
- **Cause:** N/A
- **Resolution:** Successfully implemented all requested UI/UX improvements.
- **Future Prevention:** Detailed logging maintained.

## Update: UX/UI Improvements for Widescreens

### Changes Made:
- **Floating Header Controls**: Moved the 'Clear', 'Theme' buttons, and the footer credits to a fixed, semi-transparent container in the top-right corner of the screen. This ensures these controls are always accessible regardless of scroll position without cluttering the main content area.
- **Two-Column Layout (Desktop)**: Redesigned the main content area for both 'Worker' and 'Hiring' tabs to utilize a two-column grid layout on screens wider than 992px. The form inputs are positioned on the left, while the resulting data tables, HTML output, and Live Preview are displayed on the right.
- **Max Width Increase**: Increased the maximum width of the main container from `1000px` to `1400px` to better utilize the available screen real estate on 16:9 widescreen monitors.
- **Responsive Fallback**: Added CSS media queries to ensure the layout gracefully degrades back to a single-column layout on smaller screens (tablets and mobile devices) and adjustments for the floating controls on narrow screens.

### Reason for Changes:
- To address user feedback stating that the previous single-column design resulted in an excessively long, "scrolly" page on standard 16:9 desktop monitors, leading to a poor user experience.
- To improve usability by keeping relevant inputs and outputs visible simultaneously without requiring constant vertical scrolling.

### Error Logging:
- **Type:** Human Error / Suboptimal Design
- **Detection:** User feedback ("เนื้อหาในเว็บเป็นแท่งยาวจนหลุดขอบจอไปเยอะ" / The content is a long vertical bar that goes way off screen).
- **Cause:** The previous design iteration focused on responsiveness but failed to optimize layout for wider desktop screens, relying entirely on a single-column flow regardless of available horizontal space.
- **Resolution:** Implemented CSS Grid to create a responsive two-column layout that specifically targets and utilizes wider viewports, while maintaining a single column for mobile.
- **Future Prevention:** When designing responsive layouts, explicitly consider and test how the UI scales and utilizes space on larger desktop monitors (e.g., standard 1080p / 16:9 displays), not just mobile and tablet sizes.

## Update: Refined Top-Right UI Controls using Tailwind CSS

### Changes Made:
- **Tailwind Integration:** Imported Tailwind CSS via CDN (with preflight disabled to prevent conflicts with existing custom CSS styles) to enable rapid, utility-first styling for the UI controls.
- **FontAwesome Integration:** Added FontAwesome CDN link to replace text/emoji buttons with clean, modern vector icons (sun, moon, trash).
- **Floating Controls Redesign:** Replaced the custom CSS `.floating-controls` div with a new Tailwind-styled fixed container.
- **UI Elements:**
    - Combined the Clear (Trash), Light Theme (Sun), and Dark Theme (Moon) buttons into a single pill-shaped, semi-transparent (`backdrop-blur-sm`), glass-like container.
    - Added interactive hover states and color transitions to the icons.
    - Updated the "Dev by Jules AI | GitHub" credits box to match the new glassmorphic styling, positioned neatly below the control pill.
- **Theme Logic Update:** Updated the `setTheme` function and related Javascript logic to accurately toggle the active/inactive color states of the new Tailwind-styled Light and Dark mode icon buttons.
- **CSS Cleanup:** Removed the now-obsolete custom CSS rules that previously styled the old top-right controls to reduce clutter.

### Reason for Changes:
- To address user feedback stating that the previous custom CSS layout for the top-right UI controls was poorly designed and "sucked" (ห่วยแตกมาก). The user requested a specific, modern, and standardized UI layout using Tailwind classes.

### Error Logging:
- **Type:** Human Error / Poor UX Design
- **Detection:** User feedback ("ฟั่งชั่นขวาบน คุณจัดรูป ux ui แบบได้ห่วยแตกมาก" / "The top right function, you arranged the ux ui layout terribly").
- **Cause:** The previous iteration used basic, custom CSS for the floating controls which was deemed visually unappealing and not up to the user's standard.
- **Resolution:** Removed the custom CSS implementation and replaced it entirely with the user-provided, standardized Tailwind HTML structure incorporating glassmorphism and FontAwesome icons, adjusting the Javascript to support the new element IDs.
- **Future Prevention:** Pay closer attention to modern UI/UX trends (like glassmorphism and icon usage) and proactively use utility frameworks like Tailwind if permitted, to ensure a polished look, rather than relying on basic custom CSS that might look dated or poorly aligned.
