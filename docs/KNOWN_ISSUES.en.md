# Current scope and known limitations

[简体中文](KNOWN_ISSUES.md) | **English**

- Python projects are the main supported target. Windows was validated; this release has not completed macOS or Linux acceptance.
- Static scans, diagrams, and individual explanations have size and context limits. The interface reports omitted or unexpanded items.
- Reflection, dynamic dispatch, third-party internals, cross-process relationships, and some wrapped entry points may remain unresolved. You can select a reading root manually.
- No resolved downstream project call does not mean no output. Return-value uses are separate static records, not new outgoing call edges.
- Failed tests keep their actual exit reason and are not used to fill chain gaps. Passing tests do not establish that the whole business pipeline is verified.
- Source-semantic review usually adds a model request. Model review can still miss errors.
- Live acceptance used Codex with a dedicated sample project. DeepSeek's live behavior still needs user feedback.
- Runtime argument and return values are not collected. Container contents may change after unexpanded calls.
- Structural impact in a diff is a syntax comparison, not a complete proof of branch, data-flow, or runtime effects.
