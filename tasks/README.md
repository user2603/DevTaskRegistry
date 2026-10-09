# Registry rules

## Templates

A template is a folder under `tasks/templates/`. Each template's `README.md` lists the files a task built on that template must contain.

| Template | Requirements defined in |
| --- | --- |
| atlas | tasks/templates/atlas/README.md |
| beacon | tasks/templates/beacon/README.md |
| cipher | tasks/templates/cipher/README.md |
| delta | tasks/templates/delta/README.md |

## Citations

Every proposal's `docs/task.md` ends with a line of the form:

    Template: `tasks/templates/<name>`

A citation is only verified when the proposal folder contains every file the cited template requires. A proposal can also outgrow its citation: always attribute the template the proposal actually follows — the most demanding template (longest required-file list) whose requirements the proposal satisfies.

## Completion

A proposal counts as completed only when it satisfies the `delta` template. Otherwise it is in-progress.

Review cycles run monthly.
