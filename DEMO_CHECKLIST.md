# BloodLink CCA Demo Checklist

## Before demonstration

- [ ] Public GitHub repository
- [ ] At least 10 meaningful commits
- [ ] At least 1 merged pull request
- [ ] Main branch green
- [ ] Live Render URL working
- [ ] Footer shows commit ID
- [ ] Successful pipeline screenshot
- [ ] Failed pipeline screenshot
- [ ] README complete
- [ ] 4–6 page PDF report complete

## Live application demo

1. Open home page.
2. Show donor statistics.
3. Filter by O+.
4. Filter by Pune.
5. Open Register as Donor.
6. Add a fictional donor.
7. Return to directory and show the new record.
8. Open `/api/donors`.
9. Open `/health`.
10. Point out the commit ID in the footer.

## CI/CD demo

1. Open GitHub Actions.
2. Show a green run.
3. Show lint and test jobs.
4. Show Docker build and smoke test.
5. Show deployment job.
6. Show the live site's commit ID.
7. Show the intentionally failed run.
8. Explain that deploy was skipped because of `needs`.
9. Show the corrected green run.

## Viva points

- CI = automatically integrates and tests changes.
- CD = automatically releases a passing main-branch change.
- `needs` controls job dependency/order.
- GitHub Secrets protect the Render deploy hook.
- Docker gives a consistent runtime environment.
- `/health` is used for a basic service health/smoke check.
