
---


```markdown
# Merging and Merge Commits

## Why Merge?

Branches are used to safely isolate changes without affecting the main branch. Once work on a branch is complete and stable, it's typically merged back into the main branch to integrate the changes.

## Basic Merge

Consider two branches with unique commits:

```

A - B - C    main

D - E  other\_branch

```

Merging `other_branch` into `main` results in a new commit that combines both histories:

```

A - B - C - F    main
\     /
D - E      other\_branch

```

- `F` is a **merge commit**, with two parents: `C` and `E`.
- This kind of merge preserves the full history of both branches.

## Merge Commits

A merge commit:
- Identifies the **merge base** (common ancestor, e.g. `A`)
- Replays changes from both branches
- Records the result in a commit with two parents

This allows Git to track the lineage of the combined histories and is useful for visualizing development over time.

## Merge History Example

An example of a merge log:

```

* F: Merge branch 'add\_classics'
  |
  \| \* D: add classics
* \| E: update contents
  |/
* C: add quotes
* B: add titles.md
* A: add contents.md

```

- Branch divergence and reintegration are clearly visualized.
- The graph shows which commits originated on which branch.

## Fast-Forward Merges

When the main branch has no new commits since the feature branch was created, Git performs a **fast-forward** merge:

**Before:**
```

```
  C     feature
 /
```

A - B       main

```

**After:**
```

```
        feature
```

A - B - C   main

```

- The `main` branch pointer simply advances to `C`
- No merge commit is created
- History appears linear

Fast-forward merges are common for short-lived feature branches and maintain a simpler commit graph.
```

