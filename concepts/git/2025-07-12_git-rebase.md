

---

### `2025-07-12_git-rebase.md`

```markdown
# Git: Rebase

## Rebase vs Merge

"Rebase vs Merge" is one of the most hotly debated topics in the Git world.

Many developers — even professionals — misunderstand rebase, misuse it, create Git havoc, and blame the tool. It's not Git's fault. It's a **skill issue**.

## Visualizing Rebase

Initial commit history:

```

A - B - C    main

D - E  feature\_branch

```

We want to bring in changes from `main` without a merge commit. Rebase replays the commits from `feature_branch` on top of `main`. After rebasing, it looks like:

```

A - B - C         main

D - E   feature\_branch (rebased)

````

## Assignment: New Branch

Create a new branch off of an earlier commit to simulate working with stale code and prepare to rebase:

```bash
git switch -c update_dune <COMMITHASH>
````

Where `<COMMITHASH>` is the hash of commit `D`, found via:

```bash
git log
```

Verify position:

```bash
git log --oneline -n 1
```

Then run and submit CLI tests from the `update_dune` branch.

## Assignment: Run Rebase

To rebase a feature branch (e.g., `jdsl`) onto `main`:

```bash
git rebase main
```

Steps:

1. Git uses the latest commit from `main` as a temporary base.
2. Replays each `jdsl` commit one by one onto that base.
3. Updates `jdsl` to point to the final replayed commit.
4. `main` remains unaffected.

## Assignment: Update Dune Branch

While on `update_dune`:

1. Add two commits to `quotes/dune.md`:

   * `"The spice must flow."` — commit message starts with `H:`
   * `"Fear is the mind-killer."` — commit message starts with `I:`

2. Rebase `update_dune` onto `main`:

```bash
git rebase main
```

3. Verify linear history:

```bash
git log --oneline
```

Should show a clean sequence from `A` to `I`.

4. Run and submit CLI tests from the `update_dune` branch.

---

**Notes:**
Not too much today — just keeping the ball rolling.

```

---

