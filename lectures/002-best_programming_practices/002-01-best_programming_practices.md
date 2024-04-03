# Number systems
- **Decimal**: base 10
    - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    - Representation: 10
- **Binary**: base 2
   - 0, 1
   - Representation: 0b1010
   - Used in:
      - bitwise operations
   - In python use the `bin()` function
- **Octal**: base 8
  - 0, 1, 2, 3, 4, 5, 6, 7
  - Representation: 0o12
  - Used in:
    - Unix file permissions
- **Hexadecimal**: base 16
  - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F
  - Representation: 0x10
  - Used in:
    - memory addresses
    - color representation
      - #FF0000 is red
    - binary files
      - 0x0A is a newline
    - character encoding
      - 0x41 is 'A'
    - URL encoding
      - %20 is a space
    - Unicode
      - 0x03B1 is α


# Critiques of this code?:
```python
def get_hex(x):
    return hex(x)


def get_suffix(x):
    # '0xf3' -> f3
    return get_hex()[2:]


def custom_hex(a):
    return 'HEX' + get_suffix(a)


def main():
    custom_hex(243)
```

# Here's an alternative:
```python
def main(a):
    b = get_hex(a)
    c = get_suffix(b)
    d = custom_hex(c)
```


This example demonstrates some interesting points/questions:
1. **How much should each function/class do?**
  - Common answer: Single Responsibility Principle (SRP) - a class, modeule, or function should  be responsble for
only one part of the functionality
    - Coined by Robert C. Martin in the early 2000s (signatory of the Agile Manifesto, author of Clean Code)
    - A part of the SOLID principles (some out of scope here)
      - S - **Single Responsibility Principle** - A class should have only one reason to change
      - O - Open/Closed Principle - Objects or entities should be open for extension, but closed for modification
      - L - Liskov Substitution Principle - Objects of a superclass should be replaceable with objects of a subclass without breaking the application
      - I - Interface Segregation Principle - Many client-specific interfaces are better than one general-purpose interface
      - D - Dependency Inversion Principle - One should depend upon abstractions, not concretions
  - Other texts say things like "each function should have no more than 5 lines"
  - However this (and SRP) can cause  conflict:
      - SRP says that a function should do one thing
      - But the more functions the more mental transitioning when you're reading the code--procedural code without
function calls will always be easier to read
      - Surely not *every* function must have a single responsiblity? What about `main()` (in python scripts)?
        - Moreover, what defines a 'single responsibility'? Is multiplying 3 numbers a single responsibility?
      - For this reason there has been some pushback against 'Clean Code'

single principle in action
``` javascript
func saveUser(db *sql.DB, user User) error {
	if user.EmailAddress == "" {
		return errors.New("user requires an email")
	}
	if len(user.Password) < 8 {
		return errors.New("user password requires at least 8 characters")
	}
	hashedPassword, err = hash(user.Password)
	if err != nil {
		return err
	}
	_, err := db.Exec(`
		INSERT INTO users (password, email_address, created)
		VALUES ($1, $2, $3);`,
		hashedPassword, user.EmailAddress, time.Now(),
	)
	return err
}
```

first 3 if statments should be out of this function

2. However, even if we don't take the Clean Code dictums as sacrosant, they are good principles to consider.
  - DRY (Don't Repeat Yourself) flows naturally from these principles
    - Though there may be occasions to violate DRY: "repetition is better than the wrong abstraction"
  - 'Never Nester' - Keep the code as flat as possible without too many nested loops, if statements, etc.
     - unhappy paths should go first
     - Linux kernel style guide: "If you need more than 3 levels of indentation, you're screwed anyway, and should fix your program."

The Zen of Python (PEP 20) states:

> Beautiful is better than ugly.<br>
> Explicit is better than implicit.<br>
> Simple is better than complex.<br>
> Complex is better than complicated.<br>
> _**Flat is better than nested.**_<br>
> Sparse is better than dense.<br>
> Readability counts.<br>
> Special cases aren't special enough to break the rules.<br>
> Although practicality beats purity.<br>
> Errors should never pass silently.<br>
> Unless explicitly silenced.<br>
> In the face of ambiguity, refuse the temptation to guess.<br>
> There should be one-- and preferably only one --obvious way to do it.<br>
> Although that way may not be obvious at first unless you're Dutch.<br>
> Now is better than never.<br>
> Although never is often better than *right* now.<br>
> If the implementation is hard to explain, it's a bad idea.<br>
> If the implementation is easy to explain, it may be a good idea.<br>
> Namespaces are one honking great idea -- let's do more of those!
