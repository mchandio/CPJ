#pragma once

#include <memory>
#include <functional>

namespace cpj::collections
{

    template <typename T>
    class Collection
    {
    public:
        virtual ~Collection() = default;

        // Basic operations
        virtual void add(const T &element) = 0;
        virtual bool remove(const T &element) = 0;
        virtual bool contains(const T &element) const = 0;
        virtual size_t size() const = 0;
        virtual bool isEmpty() const = 0;
        virtual void clear() = 0;

        // Iteration
        virtual void forEach(std::function<void(const T &)> action) = 0;

        // Conversion
        virtual std::vector<T> toVector() const = 0;

        // Stream operations
        virtual Collection<T> &filter(std::function<bool(const T &)> predicate) = 0;
        virtual Collection<T> &map(std::function<T(const T &)> mapper) = 0;

        // Language interop
        virtual void *toPythonList() const = 0;
        virtual void *toJavaList() const = 0;
    };

    // Smart pointer alias for collections
    template <typename T>
    using CollectionPtr = std::shared_ptr<Collection<T>>;

}