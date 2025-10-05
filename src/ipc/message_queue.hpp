#pragma once

#include <zmq.hpp>
#include <string>
#include <memory>
#include <stdexcept>
#include <thread>
#include <queue>
#include <mutex>
#include <condition_variable>

namespace cpj
{
    namespace ipc
    {

        class MessageQueue
        {
        public:
            enum class Mode
            {
                PUBLISHER,
                SUBSCRIBER,
                REQUEST,
                REPLY
            };

            MessageQueue(Mode mode, const std::string &address)
                : mode_(mode), address_(address)
            {
                context_ = std::make_unique<zmq::context_t>(1);

                switch (mode)
                {
                case Mode::PUBLISHER:
                    socket_ = std::make_unique<zmq::socket_t>(*context_, ZMQ_PUB);
                    socket_->bind(address);
                    break;
                case Mode::SUBSCRIBER:
                    socket_ = std::make_unique<zmq::socket_t>(*context_, ZMQ_SUB);
                    socket_->connect(address);
                    socket_->set(zmq::sockopt::subscribe, "");
                    startReceiveThread();
                    break;
                case Mode::REQUEST:
                    socket_ = std::make_unique<zmq::socket_t>(*context_, ZMQ_REQ);
                    socket_->connect(address);
                    break;
                case Mode::REPLY:
                    socket_ = std::make_unique<zmq::socket_t>(*context_, ZMQ_REP);
                    socket_->bind(address);
                    startReceiveThread();
                    break;
                }
            }

            ~MessageQueue()
            {
                if (receiveThread_.joinable())
                {
                    running_ = false;
                    receiveThread_.join();
                }
            }

            void publish(const std::string &message)
            {
                if (mode_ != Mode::PUBLISHER)
                {
                    throw std::runtime_error("Can only publish from PUBLISHER socket");
                }

                zmq::message_t msg(message.data(), message.size());
                socket_->send(msg, zmq::send_flags::none);
            }

            void send(const std::string &message)
            {
                if (mode_ != Mode::REQUEST)
                {
                    throw std::runtime_error("Can only send from REQUEST socket");
                }

                zmq::message_t msg(message.data(), message.size());
                socket_->send(msg, zmq::send_flags::none);
            }

            std::string receive()
            {
                std::unique_lock<std::mutex> lock(mutex_);
                cv_.wait(lock, [this]
                         { return !messageQueue_.empty(); });

                std::string message = messageQueue_.front();
                messageQueue_.pop();
                return message;
            }

            bool hasMessages() const
            {
                std::lock_guard<std::mutex> lock(mutex_);
                return !messageQueue_.empty();
            }

        private:
            void startReceiveThread()
            {
                running_ = true;
                receiveThread_ = std::thread([this]
                                             {
            while (running_) {
                zmq::message_t message;
                if (socket_->recv(message, zmq::recv_flags::dontwait)) {
                    std::string msgStr(static_cast<char*>(message.data()), message.size());
                    std::lock_guard<std::mutex> lock(mutex_);
                    messageQueue_.push(msgStr);
                    cv_.notify_one();
                }
                std::this_thread::sleep_for(std::chrono::milliseconds(1));
            } });
            }

            Mode mode_;
            std::string address_;
            std::unique_ptr<zmq::context_t> context_;
            std::unique_ptr<zmq::socket_t> socket_;

            std::thread receiveThread_;
            bool running_ = false;
            mutable std::mutex mutex_;
            std::condition_variable cv_;
            std::queue<std::string> messageQueue_;
        };

    } // namespace ipc
} // namespace cpj