User-Defined Types
------------------
CPJ supports user-defined types using `struct` and `class` declarations.

**Struct Example:**
```cpj
struct Point {
    x: int
    y: int
}
```

**Class Example:**
```cpj
class Person {
    name: string
    age: int

    def greet(self):
        print("Hello, " + self.name)
}
```

- `struct` defines a simple type with fields.
- `class` supports fields and methods.
- Fields are declared as `name: type`.
- Methods are defined like functions inside the class block.

User-defined types are supported in all backends (Python, C++, Java).
Language Reference (v0.1)

CPJ is a lightweight language focused on GUI DSL constructs and interop with Python, Java, and C++.

Key features

- Function definitions (`def name(params):`)
- Indentation-aware blocks and an alternative `GUI { ... }` braced form
- GUI block with widget constructors: `addTextField`, `addButton`, `addCheckBox`, `addSlider`
- Optional `types` annotations at block or per-widget level
- Expressions: dotted identifiers, calls, arithmetic and boolean operators

Example

```cpj
GUI {
    types count:int flag:bool
    addTextField("count")
    addTextField('flag')
    addButton("Run", handler(count, flag))
}
```

See `samples/` for more examples.
