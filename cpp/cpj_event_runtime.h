// Minimal CPJ event runtime API (C++)
#pragma once
#include <nlohmann/json.hpp>
// Unified CPJ event schema validation utility
inline void validate_event_json(const nlohmann::json& event) {
    if (!event.is_object()) throw std::invalid_argument("Event must be a JSON object");
    if (!event.contains("id") || !event["id"].is_string())
        throw std::invalid_argument("Event missing required string field: id");
    if (!event.contains("type") || !event["type"].is_string())
        throw std::invalid_argument("Event missing required string field: type");
    if (event.contains("payload") && !(event["payload"].is_object() || event["payload"].is_null()))
        throw std::invalid_argument("payload must be an object or null");
    if (event.contains("reply_to") && !event["reply_to"].is_string())
        throw std::invalid_argument("reply_to must be a string");
    if (event.contains("error") && !event["error"].is_string())
        throw std::invalid_argument("error must be a string");
    if (event.contains("runtime") && !event["runtime"].is_string())
        throw std::invalid_argument("runtime must be a string");
    if (event.contains("timestamp") && !event["timestamp"].is_number())
        throw std::invalid_argument("timestamp must be a number");
}
#include <string>
#include <functional>
#include <unordered_map>
#include <vector>

#include <optional>
#include <queue>

struct Event
{
    std::string type;
    std::string payload_json;
    std::string source;
    std::string target;
    std::string id;
    std::string reply_to;
    std::string error_json;  // JSON-encoded error object
    std::string result_json; // JSON-encoded result
    uint64_t timestamp = 0;

    // Validate this event as JSON (throws if invalid)
    void validate() const {
        nlohmann::json j;
        j["id"] = id;
        j["type"] = type;
        if (!payload_json.empty()) j["payload"] = nlohmann::json::parse(payload_json);
        if (!reply_to.empty()) j["reply_to"] = reply_to;
        if (!error_json.empty()) j["error"] = error_json;
        if (!source.empty()) j["runtime"] = source;
        if (timestamp) j["timestamp"] = timestamp;
        validate_event_json(j);
    }
};

class EventRuntime
{
public:
    using Handler = std::function<void(const Event &)>;
    void emit_event(const Event &event, bool sync = true)
    {
        try {
            event.validate();
        } catch (const std::exception& ex) {
            throw std::runtime_error(std::string("Invalid event schema: ") + ex.what());
        }
        if (sync)
        {
            auto it = handlers.find(event.type);
            if (it != handlers.end())
            {
                for (auto &h : it->second)
                    h(event);
            }
        }
        else
        {
            event_queue.push(event);
        }
    }
    void on_event(const std::string &type, Handler handler)
    {
        handlers[type].push_back(handler);
    }
    std::optional<Event> poll_event()
    {
        if (event_queue.empty())
            return std::nullopt;
        Event e = event_queue.front();
        event_queue.pop();
        try {
            e.validate();
        } catch (const std::exception& ex) {
            throw std::runtime_error(std::string("Invalid event polled: ") + ex.what());
        }
        return e;
    }

private:
    std::unordered_map<std::string, std::vector<Handler>> handlers;
    std::queue<Event> event_queue;
};
