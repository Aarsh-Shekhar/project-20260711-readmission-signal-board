# Operator Handoff

Domain: healthcare analytics

This note records an implementation detail for Readmission Signal Board. The current operating
threshold is `0.8` and review should happen within `8` hours
for records above that level.

## Checks

- confirm input fields are present
- verify score ordering is stable
- compare high exposure records against the review queue
