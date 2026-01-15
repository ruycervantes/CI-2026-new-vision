# /handwritten - Transcribe handwritten notes to action items

Transcribes handwritten notes from images and proposes additions to the action items document.

## Instructions

### Step 1: Find and prepare images

1. Look for images in `handwritten/` folder (supports HEIC, JPG, PNG)
2. If HEIC files exist and are too large to read (>256KB), convert them:
   ```bash
   for f in handwritten/*.HEIC; do
     sips -Z 1200 -s format jpeg -s formatOptions 60 "$f" --out "${f%.HEIC}_small.jpg" 2>/dev/null
   done
   ```

### Step 2: Transcribe each image

Read each image and transcribe the handwritten content:
- Preserve original language (Spanish/English mix is expected)
- Note visual markers: checkmarks (☑️), empty boxes (□), arrows (→), underlines
- Identify dates if present
- Group transcription by page/image

### Step 3: Parse into categories

Organize transcribed content into:
- **TODO items** - Actionable tasks with clear next steps
- **Reflections/insights** - Quotes, realizations, context worth preserving
- **Process notes** - Systems or workflows to build
- **Questions** - Things to resolve or discuss with others
- **External requests** - Items from other people (Nelson, Leo, etc.)

### Step 4: Compare with existing action items

Read `action-items-ruy-jan2026.md` and identify:
- Items already captured (skip these)
- New items to add
- Which section each new item belongs in

### Step 5: Present proposed additions

Show the user:
1. Full transcription organized by page
2. Summary of what's new vs already captured
3. Proposed additions with target sections
4. Any questions or clarifications needed

**Wait for user input before making edits.**

### Step 6: Apply changes (after user approval)

Edit `action-items-ruy-jan2026.md` to add approved items:
- Place items in appropriate sections
- Update the intro line to mention new source date
- Add reference to handwritten folder in Reference section

### Step 7: Clean up

Remove temporary converted files (keep original HEIC):
```bash
rm handwritten/*_small.jpg 2>/dev/null
```

## Section mapping reference

| Content type | Target section |
|--------------|----------------|
| Tasks for this week | This Week (Before Sprint Planning Thursday) |
| Sprint stories | Sprint Planning Prep |
| Shipping/process items | Process & Systems |
| Contracts, accounts, email | Administrative Tasks |
| Items needing Leo | With Leo (This Week) |
| External requests (Nelson, etc.) | Operations Requests |
| Strategic questions | Strategic Questions to Resolve |
| Blocked items | Blocked Items |
| Backlog/future items | CI Automation Backlog |

## Parameters

You can specify:
- Custom folder: "transcribe notes from `photos/jan15/`"
- Custom output: "add to `action-items-q1.md`"

Default: `handwritten/` → `action-items-ruy-jan2026.md`
