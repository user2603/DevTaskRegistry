# Registry rules

## Templates

A template is a folder under `tasks/templates/`. Each template's `README.md` lists the files a task built on that template must contain.

| Template | Requirements defined in |
| --- | --- |
| atlas | tasks/templates/atlas/README.md |
| beacon | tasks/templates/beacon/README.md |
| cipher | tasks/templates/cipher/README.md |
| delta | tasks/templates/delta/README.md |

## Completion

A proposal counts as completed only when it satisfies the `delta` template. Otherwise it is in-progress.
