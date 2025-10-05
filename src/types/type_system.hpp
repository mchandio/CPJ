#pragma once

#include <string>
#include <vector>
#include <map>
#include <memory>
#include <typeindex>
#include <any>
#include <functional>

namespace cpj
{
    namespace types
    {

        // Forward declarations
        class TypeDescriptor;
        class TypeRegistry;

        // Type categories
        enum class TypeCategory
        {
            PRIMITIVE,
            COLLECTION,
            OBJECT,
            FUNCTION,
            GENERIC
        };

        // Primitive type IDs
        enum class PrimitiveTypeId
        {
            BOOL,
            INT8,
            INT16,
            INT32,
            INT64,
            UINT8,
            UINT16,
            UINT32,
            UINT64,
            FLOAT32,
            FLOAT64,
            STRING,
            VOID
        };

        // Type conversion result
        struct ConversionResult
        {
            bool success;
            std::any value;
            std::string error;
        };

        // Type descriptor base class
        class TypeDescriptor
        {
        public:
            TypeDescriptor(const std::string &name, TypeCategory category)
                : name_(name), category_(category) {}

            virtual ~TypeDescriptor() = default;

            const std::string &getName() const { return name_; }
            TypeCategory getCategory() const { return category_; }

            // Virtual interface for type operations
            virtual std::string toString(const std::any &value) const = 0;
            virtual ConversionResult fromString(const std::string &str) const = 0;
            virtual bool equals(const std::any &lhs, const std::any &rhs) const = 0;
            virtual std::size_t hash(const std::any &value) const = 0;

            // Language-specific type names
            virtual std::string getCppTypeName() const = 0;
            virtual std::string getPythonTypeName() const = 0;
            virtual std::string getJavaTypeName() const = 0;

        protected:
            std::string name_;
            TypeCategory category_;
        };

        // Primitive type descriptor
        class PrimitiveTypeDescriptor : public TypeDescriptor
        {
        public:
            PrimitiveTypeDescriptor(const std::string &name, PrimitiveTypeId typeId)
                : TypeDescriptor(name, TypeCategory::PRIMITIVE), typeId_(typeId) {}

            PrimitiveTypeId getTypeId() const { return typeId_; }

            // Implement base class methods
            std::string toString(const std::any &value) const override;
            ConversionResult fromString(const std::string &str) const override;
            bool equals(const std::any &lhs, const std::any &rhs) const override;
            std::size_t hash(const std::any &value) const override;

            std::string getCppTypeName() const override;
            std::string getPythonTypeName() const override;
            std::string getJavaTypeName() const override;

        private:
            PrimitiveTypeId typeId_;
        };

        // Collection type descriptor
        class CollectionTypeDescriptor : public TypeDescriptor
        {
        public:
            CollectionTypeDescriptor(const std::string &name,
                                     std::shared_ptr<TypeDescriptor> elementType)
                : TypeDescriptor(name, TypeCategory::COLLECTION), elementType_(elementType) {}

            std::shared_ptr<TypeDescriptor> getElementType() const { return elementType_; }

            // Implement base class methods
            std::string toString(const std::any &value) const override;
            ConversionResult fromString(const std::string &str) const override;
            bool equals(const std::any &lhs, const std::any &rhs) const override;
            std::size_t hash(const std::any &value) const override;

            std::string getCppTypeName() const override;
            std::string getPythonTypeName() const override;
            std::string getJavaTypeName() const override;

        private:
            std::shared_ptr<TypeDescriptor> elementType_;
        };

        // Object type descriptor for user-defined types
        class ObjectTypeDescriptor : public TypeDescriptor
        {
        public:
            using FieldMap = std::map<std::string, std::shared_ptr<TypeDescriptor>>;

            ObjectTypeDescriptor(const std::string &name, const FieldMap &fields)
                : TypeDescriptor(name, TypeCategory::OBJECT), fields_(fields) {}

            const FieldMap &getFields() const { return fields_; }

            // Implement base class methods
            std::string toString(const std::any &value) const override;
            ConversionResult fromString(const std::string &str) const override;
            bool equals(const std::any &lhs, const std::any &rhs) const override;
            std::size_t hash(const std::any &value) const override;

            std::string getCppTypeName() const override;
            std::string getPythonTypeName() const override;
            std::string getJavaTypeName() const override;

        private:
            FieldMap fields_;
        };

        // Type registry for managing type descriptors
        class TypeRegistry
        {
        public:
            static TypeRegistry &getInstance()
            {
                static TypeRegistry instance;
                return instance;
            }

            // Register a new type descriptor
            void registerType(std::shared_ptr<TypeDescriptor> descriptor);

            // Get type descriptor by name
            std::shared_ptr<TypeDescriptor> getType(const std::string &name) const;

            // Get type descriptor by std::type_index
            std::shared_ptr<TypeDescriptor> getType(const std::type_index &typeIndex) const;

            // Check if a type is registered
            bool isTypeRegistered(const std::string &name) const;

        private:
            TypeRegistry() = default;
            std::map<std::string, std::shared_ptr<TypeDescriptor>> typesByName_;
            std::map<std::type_index, std::shared_ptr<TypeDescriptor>> typesByIndex_;
        };

    } // namespace types
} // namespace cpj