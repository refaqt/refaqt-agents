# Subagents

## Delegation

- Before you start a subagent, define the scope, the inputs, the expected outputs, and what counts as failure.
- Subagents must stay inside their scope. If work is outside the scope, stop and report back.
- Each subagent returns a short completion report: done, skipped, and issues found. Write that report in B2 English. Follow [communication.md](communication.md).
- Subagents do not call other subagents unless the workflow says they must.

## Coordination

- The main agent owns the final merge. Check subagent output before you merge it.
- Parallel subagents must not edit the same file. Give each one its own files first.
- Subagents can read by default. Give write access only when the task needs it.

## Safety

- Pause for user confirmation before you delete files, run migrations, or change environment configuration.
