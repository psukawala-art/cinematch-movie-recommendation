# SDLC Plan — CineMatch

## 01 — Requirements (Day 1)
Agree on the problem, users, scope, must-have features, constraints, and acceptance criteria.
Owner: all members; Member 1 records the agreed requirements.
Exit: everyone agrees what is included and excluded.

## 02 — Design (Days 1–2)
Agree on schema, ER diagram, architecture, data flow, and algorithm outline.
Owners: Member 1 leads schema/ERD; Member 3 leads algorithm; Member 4 documents integration.
Exit: team reviews design before building separate modules.

## 03 — Implementation (Days 2–5)
Build small complete slices in this order:
1. Create database and tables.
2. Load sample data and run basic queries.
3. Run a recommendation query.
4. Implement and test cosine similarity separately.
5. Connect Python to MySQL.
6. Add Streamlit UI.
Make small, reviewable changes rather than regenerating the whole application.

## 04 — Testing (Days 3–6)
Test normal cases, unknown users, empty results, already-rated movies, missing ratings, zero vectors, and database connection failure.
Each member tests their module; Member 4 coordinates integration tests.
Exit: tests pass and the team can explain expected results.

## 05 — Release (Days 6–7)
Freeze features, verify setup from README, check secrets are excluded, capture screenshots, and rehearse the demo.
Owner: Member 4 coordinates; every member reviews their own section.
Exit: another teammate can run the app from the instructions.

## 06 — Maintenance (after demo or as time allows)
Record bugs as GitHub Issues, prioritise fixes, add regression tests, update the changelog, and document limitations.
Owner: all members.

## Daily working agreement
- 10–15 minute check-in: done, next, blocker.
- Commit working code daily.
- Review before merging to main.
- Keep main runnable and never commit credentials.
