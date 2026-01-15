# Review Action Items

Review and clean up an action items file using hygiene principles.

## Arguments
- $ARGUMENTS: Path to action items file (optional, will prompt if not provided)

## Instructions

You are helping clean up and organize an action items document. Follow these principles:

### Principles

1. **Separate tasks from reference** - Action items = what to DO. Reference docs = context/details. Link, don't embed.
2. **Single source of truth** - Each piece of info lives in ONE place. Everything else links to it.
3. **Your list, your tasks** - Only tasks the owner owns belong here. Team tasks → team tools.
4. **Progressive disclosure** - Task name → key questions/blockers → link to details.
5. **Done = gone** - Completed items are noise. Remove or archive immediately.
6. **Cluster related work** - Group tasks with dependencies. Sequence them. Name the cluster.
7. **Clarify or it stays undone** - Vague tasks don't get done. Sharpen the wording.
8. **Links over duplication** - Copy-paste creates drift. Links stay current.

### Workflow

**Step 1: Load and scan**
- If $ARGUMENTS provided, read that file. Otherwise ask which file to review.
- Identify all sections and count tasks per section.
- Report: "Found X sections with Y total tasks, Z completed"

**Step 2: Find issues**

Analyze the file for these problems:

| Issue | How to spot it |
|-------|----------------|
| **Duplicates** | Same task appears in multiple sections |
| **Done items** | `[x]` tasks still in the list |
| **Wrong owner** | Tasks assigned to others (look for other people's names) |
| **Bloated tasks** | >5 lines of sub-bullets (not always bad - inline context can be valuable) |
| **Vague tasks** | Can't tell what "done" looks like - ask user to clarify |
| **Orphan clusters** | Related tasks scattered, not grouped |
| **Reference sections** | Info sections mixed with task sections - should be marked or moved |

**Step 3: Report findings**

Present a summary:
```
## Review Findings

- Duplicates: X found
- Completed items to remove: X found
- Tasks belonging to others: X found
- Bloated tasks (may need extraction): X found
- Vague tasks needing clarification: X found
- Reference sections (not tasks): X found
```

**Step 4: Interactive cleanup**

For each category with findings:

1. Show the specific items
2. Propose the fix
3. Ask user to approve before making changes
4. Use AskUserQuestion for choices (e.g., "Where should this detail go?")

**For bloated tasks:**
- Review one by one (don't batch)
- Options: extract to doc, keep inline, or shorten
- Inline is often preferred when context is needed to do the task
- If extracting: replace with link, keep task name + key blockers

**For reference sections:**
- Options: move to separate doc, mark with *(reference, not tasks)*, or delete
- Marking inline is often preferred to keep context visible

**For vague tasks:**
- Ask: "What does 'done' look like for this task?"
- Offer concrete options based on task type
- Update task with clear completion criteria

**Step 5: Summary**

After all changes:
- List files modified
- Count tasks removed/consolidated
- Note any cross-references added

### Example interaction

```
## Review Findings

Found 5 completed items still in list:
1. [x] Follow up with IT (Javier) - line 50
2. [x] Sprint planning completed - line 155
...

**Proposal:** Remove these completed items.
Approve? (will ask before making changes)
```

### Conservative by default

- Always ask before making changes
- Preserve user's task descriptions (don't rewrite unless asked)
- When in doubt, ask rather than assume
- Don't create new files without explicit approval
