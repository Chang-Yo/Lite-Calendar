#pragma once
#include <string>

// Function prototype for sending a notification.
// The implementation will be platform-specific (Windows Toast Notifications).
void sendNotification(const std::wstring& title, const std::wstring& message);
