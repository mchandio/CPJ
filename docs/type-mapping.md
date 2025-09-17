
# Type Mapping and ABI for CPJ

This document describes the type mapping and ABI (Application Binary Interface) conventions for marshaling data and events between CPJ, C++, Python, and Java runtimes. It is intended to ensure reliable, lossless, and predictable interop for all supported types and event payloads.

## Goals
- Define canonical type correspondences between CPJ, C++, Python, and Java
- Specify serialization and ABI conventions for event payloads and handler signatures
- Provide test cases and CI checks for round-trip marshaling
- Document edge cases and error handling

## 1. Canonical Type Mapping Table

| CPJ Type   | C++ Type         | Python Type   | Java Type      | Notes                       |
|------------|------------------|---------------|----------------|-----------------------------|
| int        | int32_t / int64_t| int           | int            | Use int64 for large values  |
| float      | double           | float         | double         | IEEE 754                    |
| bool       | bool             | bool          | boolean        |                             |
| string     | std::string      | str           | String         | UTF-8                       |
| list<T>    | std::vector<T>   | list          | List<T>        | Homogeneous, JSON array     |
| dict<K,V>  | std::map<K,V>    | dict          | Map<K,V>       | JSON object                 |
| event      | Event (struct)   | Event (class) | Event (class)  | See event-model.md          |
| any        | nlohmann::json   | Any           | Object         | JSON-encoded fallback       |

## 2. Serialization and ABI
- All cross-runtime payloads are serialized as JSON (UTF-8)
- Event delivery uses a canonical JSON schema (see event-model.md)
- Numeric types are upcast as needed (e.g., int32→int64)
- Strings are always UTF-8
- Lists and dicts must be homogeneous and serializable
- Custom types must provide to_json/from_json methods (C++), __dict__ (Python), or Jackson annotations (Java)

## 3. Event Handler Signatures
- All event handlers must accept a single event argument (dict/object/struct)
- Return values are serialized as JSON and delivered as event replies
- Errors are encoded as { "error": { "type": ..., "message": ... } }

## 4. Test Cases
- [ ] int/float/bool/string round-trip between all runtimes
- [ ] list/dict round-trip
- [ ] Event delivery with nested payloads
- [ ] Error propagation and decoding

## 5. CI Checks
- Add tests in tests/test_type_mapping.py and cross-runtime integration tests
- Validate round-trip for all supported types

## 6. Edge Cases
- Large integers: upcast to int64, error if overflow
- NaN/Infinity: encode as string or error
- Null: map to None/nullptr/null
- Unknown types: fallback to JSON string or error

## 7. References
- See docs/event-model.md for event schema
- See tests/ for marshaling tests

---

*Last updated: 2025-09-15*
