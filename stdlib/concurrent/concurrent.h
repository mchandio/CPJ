#pragma once

#include <memory>
#include <future>
#include <functional>

namespace cpj::concurrent
{

    template <typename T>
    class Future
    {
    public:
        virtual ~Future() = default;

        // Basic operations
        virtual bool isDone() const = 0;
        virtual T get() = 0;
        virtual T get(long timeout, TimeUnit unit) = 0;
        virtual void cancel() = 0;
        virtual bool isCancelled() const = 0;

        // Composition
        virtual Future<T> &thenApply(std::function<T(T)> fn) = 0;
        virtual Future<void> &thenAccept(std::function<void(T)> consumer) = 0;
        virtual Future<T> &exceptionally(std::function<T(std::exception_ptr)> fn) = 0;

        // Language interop
        virtual void *toPythonFuture() const = 0;
        virtual void *toJavaCompletableFuture() const = 0;
    };

    class Executor
    {
    public:
        virtual ~Executor() = default;

        template <typename T>
        Future<T> submit(std::function<T()> task) = 0;

        virtual void shutdown() = 0;
        virtual bool isShutdown() const = 0;
        virtual bool isTerminated() const = 0;

        static Executor &getGlobalExecutor();
    };

    // Actor system for message-passing concurrency
    class Actor
    {
    public:
        virtual ~Actor() = default;

        virtual void tell(const Message &message) = 0;
        virtual Future<Message> ask(const Message &message) = 0;

        template <typename Handler>
        void receive(Handler &&handler);

    protected:
        virtual void preStart() {}
        virtual void postStop() {}
    };

} // namespace cpj::concurrent