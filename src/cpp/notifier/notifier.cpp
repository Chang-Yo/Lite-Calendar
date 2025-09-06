#include "notifier.h"
#include <iostream>

void sendNotification(const std::wstring& title, const std::wstring& message) {
    // This is a placeholder implementation.
    // On Windows, this function will use the WinRT API to create and show a toast notification.
    // For now, we'll just print to the console to verify it's being called.
    // We use wcout for wide strings.
    std::wcout << L"--- NOTIFICATION --- " << std::endl;
    std::wcout << L"Title: " << title << std::endl;
    std::wcout << L"Message: " << message << std::endl;
    std::wcout << L"--------------------" << std::endl;
}
