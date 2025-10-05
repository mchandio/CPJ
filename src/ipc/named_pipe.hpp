#pragma once

#include <string>
#include <system_error>
#include <fcntl.h>
#include <sys/stat.h>
#include <unistd.h>
#include <vector>

namespace cpj
{
    namespace ipc
    {

        class NamedPipe
        {
        public:
            NamedPipe(const std::string &name, bool isWriter)
                : name_(name), isWriter_(isWriter)
            {
                // Create the named pipe if it doesn't exist
                if (mkfifo(name.c_str(), 0666) == -1 && errno != EEXIST)
                {
                    throw std::system_error(errno, std::system_category(),
                                            "Failed to create named pipe");
                }

                // Open the pipe
                int flags = isWriter ? O_WRONLY | O_NONBLOCK : O_RDONLY | O_NONBLOCK;
                fd_ = open(name.c_str(), flags);
                if (fd_ == -1)
                {
                    throw std::system_error(errno, std::system_category(),
                                            "Failed to open named pipe");
                }
            }

            ~NamedPipe()
            {
                if (fd_ != -1)
                {
                    close(fd_);
                }
                if (isWriter_)
                {
                    unlink(name_.c_str());
                }
            }

            // Write data to the pipe
            void write(const std::vector<uint8_t> &data)
            {
                if (!isWriter_)
                {
                    throw std::runtime_error("Pipe not opened for writing");
                }

                size_t totalWritten = 0;
                while (totalWritten < data.size())
                {
                    ssize_t written = ::write(fd_,
                                              data.data() + totalWritten,
                                              data.size() - totalWritten);

                    if (written == -1)
                    {
                        if (errno == EAGAIN || errno == EWOULDBLOCK)
                        {
                            // Pipe is full, wait a bit and retry
                            usleep(1000); // 1ms
                            continue;
                        }
                        throw std::system_error(errno, std::system_category(),
                                                "Failed to write to pipe");
                    }
                    totalWritten += written;
                }
            }

            // Read data from the pipe
            std::vector<uint8_t> read(size_t maxSize = 4096)
            {
                if (isWriter_)
                {
                    throw std::runtime_error("Pipe not opened for reading");
                }

                std::vector<uint8_t> buffer(maxSize);
                ssize_t bytesRead = ::read(fd_, buffer.data(), maxSize);

                if (bytesRead == -1)
                {
                    if (errno == EAGAIN || errno == EWOULDBLOCK)
                    {
                        // No data available
                        return std::vector<uint8_t>();
                    }
                    throw std::system_error(errno, std::system_category(),
                                            "Failed to read from pipe");
                }

                buffer.resize(bytesRead);
                return buffer;
            }

            // Check if pipe has data available
            bool hasData() const
            {
                fd_set readSet;
                FD_ZERO(&readSet);
                FD_SET(fd_, &readSet);

                struct timeval timeout = {0, 0}; // Non-blocking
                return select(fd_ + 1, &readSet, nullptr, nullptr, &timeout) > 0;
            }

        private:
            std::string name_;
            int fd_ = -1;
            bool isWriter_;
        };

    } // namespace ipc
} // namespace cpj