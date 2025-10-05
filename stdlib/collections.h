#ifndef CPJ_STDLIB_COLLECTIONS_H
#define CPJ_STDLIB_COLLECTIONS_H

#include <vector>
#include <map>
#include <set>
#include <string>
#include <functional>
#include <memory>
#include <stdexcept>
#include <nlohmann/json.hpp>

namespace cpj
{
    namespace stdlib
    {

        using json = nlohmann::json;

        template <typename T>
        class Collection
        {
        protected:
            std::string type;
            virtual json to_json_impl() const = 0;

        public:
            Collection(const std::string &t) : type(t) {}
            virtual ~Collection() = default;

            std::string to_json() const
            {
                json j;
                j["type"] = type;
                j["data"] = to_json_impl();
                return j.dump();
            }
        };

        template <typename T>
        class List : public Collection<T>
        {
            std::vector<T> data;

        public:
            List() : Collection<T>("list") {}
            List(const std::vector<T> &items) : Collection<T>("list"), data(items) {}

            static List<T> from_json(const std::string &json_str)
            {
                auto j = json::parse(json_str);
                if (j["type"] != "list")
                {
                    throw std::runtime_error("Invalid collection type");
                }
                std::vector<T> items = j["data"].get<std::vector<T>>();
                return List<T>(items);
            }

            void append(const T &item)
            {
                data.push_back(item);
            }

            template <typename F>
            List<typename std::result_of<F(T)>::type> map(F func) const
            {
                using R = typename std::result_of<F(T)>::type;
                List<R> result;
                for (const auto &item : data)
                {
                    result.append(func(item));
                }
                return result;
            }

            template <typename F>
            List<T> filter(F pred) const
            {
                List<T> result;
                for (const auto &item : data)
                {
                    if (pred(item))
                    {
                        result.append(item);
                    }
                }
                return result;
            }

        protected:
            json to_json_impl() const override
            {
                return json(data);
            }
        };

        template <typename K, typename V>
        class Dict : public Collection<std::pair<K, V>>
        {
            std::map<K, V> data;

        public:
            Dict() : Collection<std::pair<K, V>>("dict") {}

            static Dict<K, V> from_json(const std::string &json_str)
            {
                auto j = json::parse(json_str);
                if (j["type"] != "dict")
                {
                    throw std::runtime_error("Invalid collection type");
                }
                Dict<K, V> result;
                for (auto it = j["data"].begin(); it != j["data"].end(); ++it)
                {
                    result.set(it.key(), it.value());
                }
                return result;
            }

            void set(const K &key, const V &value)
            {
                data[key] = value;
            }

            V get(const K &key, const V &default_value = V()) const
            {
                auto it = data.find(key);
                return it != data.end() ? it->second : default_value;
            }

        protected:
            json to_json_impl() const override
            {
                return json(data);
            }
        };

        template <typename T>
        class Set : public Collection<T>
        {
            std::set<T> data;

        public:
            Set() : Collection<T>("set") {}
            Set(const std::set<T> &items) : Collection<T>("set"), data(items) {}

            static Set<T> from_json(const std::string &json_str)
            {
                auto j = json::parse(json_str);
                if (j["type"] != "set")
                {
                    throw std::runtime_error("Invalid collection type");
                }
                std::set<T> items;
                for (const auto &item : j["data"])
                {
                    items.insert(item.get<T>());
                }
                return Set<T>(items);
            }

            void add(const T &item)
            {
                data.insert(item);
            }

            void remove(const T &item)
            {
                data.erase(item);
            }

            Set<T> union_with(const Set<T> &other) const
            {
                Set<T> result(*this);
                for (const auto &item : other.data)
                {
                    result.add(item);
                }
                return result;
            }

        protected:
            json to_json_impl() const override
            {
                return json(std::vector<T>(data.begin(), data.end()));
            }
        };

    } // namespace stdlib
} // namespace cpj

#endif // CPJ_STDLIB_COLLECTIONS_H