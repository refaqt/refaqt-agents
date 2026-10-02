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
- Do not trust a subagent's "pass" on its own. Ask how it measured. Reject a pass if the method
  leaves out part of what was asked. For example, a check that compares only the bounding box does
  not prove that every feature is there.

## Clean-room helpers

Sometimes a subagent must see data that the main agent must not see, for example a supplier model
under licence.

- The subagent works in its own temporary folder, outside every folder of the main agent.
- It never saves the files it reads, and it never copies their values into the main agent's
  folders.
- It reports only results and facts about the shape, in words. It does not report raw values or
  files.

## Safety

- Pause for user confirmation before you delete files, run migrations, or change environment configuration.
