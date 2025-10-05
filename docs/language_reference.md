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
-------------------------

# CPJ Language Reference

## Overview
CPJ is a unified programming language that seamlessly integrates C++, Python, and Java paradigms. It is designed for next-generation developers who demand performance, safety, and expressiveness.

## Key Features
- Unified type system
- Advanced generics
- Seamless interop between C++, Python, and Java
- Modern concurrency and memory safety
- Cross-platform support

## Syntax and Semantics
- [See `LANGUAGE_SPEC.md` for full grammar]
- Example:

```cpj
class MyClass<T> {
    var value: T;
    def setValue(newValue: T) {
        value = newValue;
    }
}
```

## Interoperability
- Call C++/Python/Java code natively
- Use `import` to bring in modules from any supported language

## Memory Management
- Automatic and manual memory management
- Unified garbage collection and RAII

## Concurrency
- async/await, threads, actors

## Error Handling
- Exceptions, result types, and pattern matching

## More
- [See `CPJ_Guide.md` and `docs/` for tutorials and migration guides]
