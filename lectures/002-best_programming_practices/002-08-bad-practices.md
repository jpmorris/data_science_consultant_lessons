# (Generally) Bad Practices

## 1. Using `eval()`
 - There is almost always a better way to do it
 - Insecure
 - Makes debugging difficult
 - Slow
 - https://stackoverflow.com/questions/1832940/why-is-using-eval-a-bad-practice
## 2. Using `globals()`
 - Ok for CONSTANTS, but not for variables
    - Python makes a distinction for a reason:
      - CONSTANTS ARE CAPITALIZED
      - globals are not
 - Problems
    - They cause side effects and make code harder to read
## 3. Using `exec()`
## 4. Using `import *`
 - You should import only what you need.  

