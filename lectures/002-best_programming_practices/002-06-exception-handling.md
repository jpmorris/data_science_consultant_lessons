# Exception Handling

## Tips
- Put as little code in the `try` as possible - one statement, one assignment, one line
  - The more you put in `try` the more you can get other exceptions you'll have to catch
- Narrow down to only exceptions you expect
- Don't use bare exceptions `except:` or `except Exception:`
  - Maybe only do this if you need to log and reraise
- reraise exceptions using `raise`
- You don't need to catch every possible exception
  - e.g if your script requires a file, you don't have to handle an exception just to craft a new
  -  custom error message.  The exception is the error in many cases (especially for scripting)

## References
- https://www.youtube.com/watch?v=tIh42X0oGQc