#pragma once

#include <string>
#include <memory>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
#include <system_error>

namespace cpj
{
    namespace ipc
    {

        class SharedMemory
        {
        public:
            SharedMemory(const std::string &name, size_t size, bool create = false)
                : name_(name), size_(size)
            {
                int flags = O_RDWR;
                if (create)
                {
                    flags |= O_CREAT;
                }

                fd_ = shm_open(name.c_str(), flags, 0666);
                if (fd_ == -1)
                {
                    throw std::system_error(errno, std::system_category(),
                                            "Failed to open shared memory");
                }

                if (create && ftruncate(fd_, size) == -1)
                {
                    close(fd_);
                    throw std::system_error(errno, std::system_category(),
                                            "Failed to set shared memory size");
                }

                void *ptr = mmap(nullptr, size, PROT_READ | PROT_WRITE, MAP_SHARED, fd_, 0);
                if (ptr == MAP_FAILED)
                {
                    close(fd_);
                    throw std::system_error(errno, std::system_category(),
                                            "Failed to map shared memory");
                }

                data_ = ptr;
            }

            ~SharedMemory()
            {
                if (data_)
                {
                    munmap(data_, size_);
                }
                if (fd_ != -1)
                {
                    close(fd_);
                }
            }

            void *getData() { return data_; }
            const void *getData() const { return data_; }
            size_t getSize() const { return size_; }

            template <typename T>
            T *as() { return static_cast<T *>(data_); }

            template <typename T>
            const T *as() const { return static_cast<const T *>(data_); }

        private:
            std::string name_;
            size_t size_;
            int fd_ = -1;
            void *data_ = nullptr;
        };

    } // namespace ipc
} // namespace cpj