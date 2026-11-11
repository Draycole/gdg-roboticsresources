# Cohorts

One folder per session. A cohort folder records **what happened that year**: the schedule, what we covered, the projects, the challenge winners.

The teaching material itself lives in the stage folders, so it stays useful in any year. A cohort page links to those labs and does not duplicate them.

## Index

| Session | What we did | Folder |
|---|---|---|
| 2026-27 | Self-balancing robot: simulation and RL, then hardware | [2026-27](2026-27) |
| 2025-26 | Arduino foundations: ultrasonic, servos, circuit challenges, drone digital twin | [2025-26](2025-26) |

## Starting a new cohort

1. Create `cohorts/<year-range>/` with a `README.md` (copy the previous one and edit).
2. Add `session-notes/` as meetings happen: one short file per meeting.
3. If you run circuit challenges, keep them in `<year-range>/circuit-challenges/`.
4. Anything reusable (a new lab, a project) goes in the stage folders, and the cohort README links to it.

## What goes where

| Kind of material | Where |
|---|---|
| A lab or tutorial anyone can follow | Stage folder |
| What we covered, in what order, this year | Cohort README |
| Who won a challenge, photos, meeting notes | Cohort folder |
| A finished build | `projects/` |
