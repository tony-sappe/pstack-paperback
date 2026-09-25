### Worktree and simulator cleanup

**Reclaim local disk without losing active or uncommitted work.**

1. Record free space with `df -h /` and enumerate exact worktree paths with `git worktree list --porcelain`. For each candidate, inspect status, branch, commits, and any PR. Check the host's task list or ask the user only when ownership or active use cannot be determined from available evidence.
2. Keep any worktree in use, any worktree with uncommitted changes, and any branch whose work has not been preserved elsewhere. Show the user the exact files and reason when an irreversible deletion needs their decision.
3. Remove only confirmed inactive, clean worktrees with `git worktree remove <path>`, then run `git worktree prune`. Do not force removal or delete surviving directories without inspecting their contents.
4. If requested, inspect stale simulator runtimes and caches separately. List exact candidates and confirm that they are unused before deleting them.
5. Recheck `git worktree list --porcelain` and `df -h /`.

**Reply:** space before and after, paths removed, and candidates retained with reasons.
