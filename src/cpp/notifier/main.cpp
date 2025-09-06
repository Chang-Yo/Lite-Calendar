#include <iostream>
#include <vector>
#include <string>
#include <chrono>
#include <thread>
#include "notifier.h"

// Placeholder for an event structure
struct Event {
    int id;
    std::wstring title;
    std::wstring description;
};

// Placeholder function for getting due events from the database
std::vector<Event> getDueEvents() {
    // In the actual implementation, this function will:
    // 1. Connect to the SQLite database (../calendar.db).
    // 2. Query the 'events' table for rows where date and time match the current time
    //    and the 'notified' flag is 0.
    // 3. Populate a vector of Event structs.
    std::wcout << L"Checking for due events... (placeholder)" << std::endl;
    return {}; // Return an empty vector for now
}

// Placeholder function to mark an event as notified in the database
void markEventAsNotified(int eventId) {
    // This function will execute an UPDATE SQL statement on the database
    // to set the 'notified' flag to 1 for the given eventId.
    std::wcout << L"Marking event " << eventId << L" as notified. (placeholder)" << std::endl;
}

int main() {
    // Set console to output wide characters
    // This is for demonstration purposes
    std::locale::global(std::locale(""));
    std::wcout.imbue(std::locale());

    std::wcout << L"Notifier service started. Will check for events every 60 seconds." << std::endl;

    while (true) {
        std::vector<Event> dueEvents = getDueEvents();

        for (const auto& event : dueEvents) {
            sendNotification(event.title, event.description);
            markEventAsNotified(event.id);
        }

        // Sleep for 60 seconds
        std::this_thread::sleep_for(std::chrono::seconds(60));
    }

    return 0;
}
