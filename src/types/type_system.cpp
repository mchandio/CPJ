#include "type_system.hpp"
#include <sstream>
#include <iomanip>
#include <stdexcept>

namespace cpj
{
    namespace types
    {

        // PrimitiveTypeDescriptor implementation
        std::string PrimitiveTypeDescriptor::toString(const std::any &value) const
        {
            try
            {
                switch (typeId_)
                {
                case PrimitiveTypeId::BOOL:
                    return std::any_cast<bool>(value) ? "true" : "false";
                case PrimitiveTypeId::INT32:
                    return std::to_string(std::any_cast<int32_t>(value));
                case PrimitiveTypeId::INT64:
                    return std::to_string(std::any_cast<int64_t>(value));
                case PrimitiveTypeId::FLOAT32:
                    return std::to_string(std::any_cast<float>(value));
                case PrimitiveTypeId::FLOAT64:
                    return std::to_string(std::any_cast<double>(value));
                case PrimitiveTypeId::STRING:
                    return std::any_cast<std::string>(value);
                default:
                    throw std::runtime_error("Unsupported primitive type");
                }
            }
            catch (const std::bad_any_cast &e)
            {
                throw std::runtime_error("Type conversion error: " + std::string(e.what()));
            }
        }

        ConversionResult PrimitiveTypeDescriptor::fromString(const std::string &str) const
        {
            try
            {
                switch (typeId_)
                {
                case PrimitiveTypeId::BOOL:
                    return {true, str == "true", ""};
                case PrimitiveTypeId::INT32:
                    return {true, std::stoi(str), ""};
                case PrimitiveTypeId::INT64:
                    return {true, std::stoll(str), ""};
                case PrimitiveTypeId::FLOAT32:
                    return {true, std::stof(str), ""};
                case PrimitiveTypeId::FLOAT64:
                    return {true, std::stod(str), ""};
                case PrimitiveTypeId::STRING:
                    return {true, str, ""};
                default:
                    return {false, std::any(), "Unsupported primitive type"};
                }
            }
            catch (const std::exception &e)
            {
                return {false, std::any(), "Conversion error: " + std::string(e.what())};
            }
        }

        bool PrimitiveTypeDescriptor::equals(const std::any &lhs, const std::any &rhs) const
        {
            try
            {
                switch (typeId_)
                {
                case PrimitiveTypeId::BOOL:
                    return std::any_cast<bool>(lhs) == std::any_cast<bool>(rhs);
                case PrimitiveTypeId::INT32:
                    return std::any_cast<int32_t>(lhs) == std::any_cast<int32_t>(rhs);
                case PrimitiveTypeId::INT64:
                    return std::any_cast<int64_t>(lhs) == std::any_cast<int64_t>(rhs);
                case PrimitiveTypeId::FLOAT32:
                    return std::abs(std::any_cast<float>(lhs) - std::any_cast<float>(rhs)) < 1e-6f;
                case PrimitiveTypeId::FLOAT64:
                    return std::abs(std::any_cast<double>(lhs) - std::any_cast<double>(rhs)) < 1e-9;
                case PrimitiveTypeId::STRING:
                    return std::any_cast<std::string>(lhs) == std::any_cast<std::string>(rhs);
                default:
                    throw std::runtime_error("Unsupported primitive type");
                }
            }
            catch (const std::bad_any_cast &e)
            {
                throw std::runtime_error("Type comparison error: " + std::string(e.what()));
            }
        }

        std::size_t PrimitiveTypeDescriptor::hash(const std::any &value) const
        {
            try
            {
                switch (typeId_)
                {
                case PrimitiveTypeId::BOOL:
                    return std::hash<bool>{}(std::any_cast<bool>(value));
                case PrimitiveTypeId::INT32:
                    return std::hash<int32_t>{}(std::any_cast<int32_t>(value));
                case PrimitiveTypeId::INT64:
                    return std::hash<int64_t>{}(std::any_cast<int64_t>(value));
                case PrimitiveTypeId::FLOAT32:
                    return std::hash<float>{}(std::any_cast<float>(value));
                case PrimitiveTypeId::FLOAT64:
                    return std::hash<double>{}(std::any_cast<double>(value));
                case PrimitiveTypeId::STRING:
                    return std::hash<std::string>{}(std::any_cast<std::string>(value));
                default:
                    throw std::runtime_error("Unsupported primitive type");
                }
            }
            catch (const std::bad_any_cast &e)
            {
                throw std::runtime_error("Type hash error: " + std::string(e.what()));
            }
        }

        std::string PrimitiveTypeDescriptor::getCppTypeName() const
        {
            switch (typeId_)
            {
            case PrimitiveTypeId::BOOL:
                return "bool";
            case PrimitiveTypeId::INT32:
                return "int32_t";
            case PrimitiveTypeId::INT64:
                return "int64_t";
            case PrimitiveTypeId::FLOAT32:
                return "float";
            case PrimitiveTypeId::FLOAT64:
                return "double";
            case PrimitiveTypeId::STRING:
                return "std::string";
            default:
                return "void";
            }
        }

        std::string PrimitiveTypeDescriptor::getPythonTypeName() const
        {
            switch (typeId_)
            {
            case PrimitiveTypeId::BOOL:
                return "bool";
            case PrimitiveTypeId::INT32:
                return "int";
            case PrimitiveTypeId::INT64:
                return "int";
            case PrimitiveTypeId::FLOAT32:
                return "float";
            case PrimitiveTypeId::FLOAT64:
                return "float";
            case PrimitiveTypeId::STRING:
                return "str";
            default:
                return "None";
            }
        }

        std::string PrimitiveTypeDescriptor::getJavaTypeName() const
        {
            switch (typeId_)
            {
            case PrimitiveTypeId::BOOL:
                return "boolean";
            case PrimitiveTypeId::INT32:
                return "int";
            case PrimitiveTypeId::INT64:
                return "long";
            case PrimitiveTypeId::FLOAT32:
                return "float";
            case PrimitiveTypeId::FLOAT64:
                return "double";
            case PrimitiveTypeId::STRING:
                return "String";
            default:
                return "void";
            }
        }

        // TypeRegistry implementation
        void TypeRegistry::registerType(std::shared_ptr<TypeDescriptor> descriptor)
        {
            typesByName_[descriptor->getName()] = descriptor;
        }

        std::shared_ptr<TypeDescriptor> TypeRegistry::getType(const std::string &name) const
        {
            auto it = typesByName_.find(name);
            if (it == typesByName_.end())
            {
                throw std::runtime_error("Type not found: " + name);
            }
            return it->second;
        }

        std::shared_ptr<TypeDescriptor> TypeRegistry::getType(const std::type_index &typeIndex) const
        {
            auto it = typesByIndex_.find(typeIndex);
            if (it == typesByIndex_.end())
            {
                throw std::runtime_error("Type not found for type index");
            }
            return it->second;
        }

        bool TypeRegistry::isTypeRegistered(const std::string &name) const
        {
            return typesByName_.find(name) != typesByName_.end();
        }

    } // namespace types
} // namespace cpj