# General Architecture and Solution Design Tips

## General Tips
- Minimize the number of components in your solution.  Don't rely on 3 components when 1 will meet the requirements.
  - Example: You need a way to track when a set of lambda job completes.  If you can leverage an existing component
  to ask Cloudwatch, this can save setting up another component.
- ASK vs TELL interprocess communication -
  - Generally TELL solutions are better than continuous polling.  Better for a process to tell you when it's done than
    for you to ask it repeatedly. There are exceptions to this rule, for example if the service is external to your
    solution and runs many idependent jobs. 