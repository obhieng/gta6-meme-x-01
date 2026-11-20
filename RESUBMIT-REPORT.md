# gta6-meme-x-01 — RESUBMIT REPORT (ref6 "I Got So Mad")

Date: 20 Nov 2026, 11:24:39 WIB (2026-11-20T04:24:39.831Z server time).
Submitter: parent (main agent) on Noe's explicit tap "Ya, resubmit ref6 sekarang" (20 Nov 2026 11:23 WIB).

## Result: ACCEPTED (HTTP 202) — REPLACES v1 (Force_Last)

- **Submission ID:** `01a1f733-0a9e-76e3-85d9-a54edd0c4c12` (round 2)
- **Title:** "I Got So Mad"
- **Repo:** https://github.com/obhieng/gta6-meme-x-01
- **Commit:** `16082ff3cd117ce6c09c9cc00b13c2660cc102c2`
- **Transcripts bundle:** `~/workspace/makefun/gta6-meme-x-01-support/transcripts-ref6.tar.gz`
  (2,645,047 bytes, sha256 `3aa9721627824d0560a8cea4d43b715ecb7f4a102a3b3136e251c4a5341c4e83`,
  27 sessions; declared harness muse-app v1, model ipnext/avocado-5.17-v2,
  provider ipnext, effort default, --mcp none)
- **Signed by payout wallet:** `qtAVgdxQ3wcNCHqN8N6F6QCwJhSTKo2KLYxKgFtq3ar`
- **X post:** https://x.com/adeldea2/status/2123621203432935722 (posted by Noe from @adeldea2,
  2026-11-20T03:35:24Z; VERIFIED by the site's entry_link check: 1 photo,
  mentions @makefunai, links make.fun, carries play code makefun-coyote-elk-alpaca)
- **Status right after submit (verified via `makefun status --submission`):** submitted,
  round 2, outcome not decided yet. ALL intake checks pass (account_wallet,
  competition_open, quota, form, entry_signature, repo_owner, repo_public,
  license_osi, repo_created_after_open, commit_in_repo, duplicate_snapshot,
  committed_secret, security_audit, entry_link, repo_readme, repo_about).
  Grading running behind — wait, do not resubmit.
- **Quota after submit:** 2 entries made, 1 of 3 day slots left, can submit now: yes.

## Deadlines

- Entries close: 23 Nov 2026 21:00 WIB (2026-11-23T14:00:00Z)
- Result due: 8 Dec 2026 09:00 WIB (2026-12-08T02:00:00Z)
- Claim deadline: not set

## Path to resubmit (what it took)

1. Noe picked ref6 "I Got So Mad" from the v3 set (10:33 WIB) and posted it to X himself,
   sending the post link (10:35 WIB).
2. Repo prep: POST.json -> new post URL, meme.png -> ref6.png, README updated to ref6.
   BLOCKED mid-way by VM EPERM wave: a failed `cat > meme.png` truncated meme.png to
   0 bytes; restored once git recovered (md5 matches ref6.png). Commit 16082ff pushed.
3. `makefun check` without transcripts: 4 passed, 1 failed (transcripts_present).
   Bundle built with v1's declared facts (harness muse-app v1, provider ipnext,
   model ipnext/avocado-5.17-v2, effort default, --mcp none) + old usage file.
   `makefun check --transcripts`: **14 passed, 0 failed** (thinking_priced 16 records).
4. First submit attempt with `--source` FAILED (client-side): --source needs a repo
   started with `makefun init` (beacon root); this repo's root commit holds the
   meme files. Did NOT burn quota (pre-upload refusal). Fixed: use `--repo-url`
   (GitHub repo path, as in v1).
5. Second submit (`--repo-url`): **accepted HTTP 202**, submission 01a1f733.

## Notes

- Claim code: stored privately in the support folder (0600 file, NOT in this repo,
  NOT in chat). Retrievable via `makefun status --submission 01a1f733-0a9e-76e3-85d9-a54edd0c4c12`.
- Replaces v1 submission 01a1f66e ("WANTED: THE MAKE.FUN GHOST") — Force_Last:
  the newest submission is the final entry.
- v1's entry ranked ~381-394 (judge 749.730) before replacement; ref6 starts ungraded.
