#include <iostream>
#include <string>

// Placeholder function to add the notifier to the Windows Registry for startup
void addToStartup(const std::wstring& appPath) {
    // On a real Windows system, this function would:
    // 1. Use RegOpenKeyExW to open HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
    // 2. Use RegSetValueExW to add a new value.
    //    - Value Name: L"LiteCalendarNotifier"
    //    - Value Data: The path to the notifier executable (appPath)
    std::wcout << L"Adding to startup registry: " << appPath << L" (Placeholder)" << std::endl;
    std::wcout << L"This would write to HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" << std::endl;
}

// Placeholder function to remove the notifier from startup
void removeFromStartup() {
    // On a real Windows system, this function would:
    // 1. Use RegOpenKeyExW to open HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
    // 2. Use RegDeleteValueW to remove the "LiteCalendarNotifier" value.
    std::wcout << L"Removing from startup registry. (Placeholder)" << std::endl;
}

int main(int argc, char *argv[]) {
    // Set locale for wide character output
    std::locale::global(std::locale(""));
    std::wcout.imbue(std::locale());

    if (argc < 2) {
        std::wcerr << L"A simple command-line utility to manage startup settings.\n"
                   << L"Usage: startup.exe [add|remove] [path_to_notifier.exe]" << std::endl;
        return 1;
    }

    std::string command = argv[1];
    if (command == "add") {
        if (argc < 3) {
            std::wcerr << L"Error: 'add' command requires the full path to the notifier executable." << std::endl;
            std::wcerr << L"Usage: startup.exe add C:\\path\\to\\notifier.exe" << std::endl;
            return 1;
        }
        // Convert the path from char* to wstring for the Windows API
        std::string appPathStr = argv[2];
        std::wstring appPath(appPathStr.begin(), appPathStr.end());
        addToStartup(appPath);
    } else if (command == "remove") {
        removeFromStartup();
    } else {
        std::wcerr << L"Unknown command: " << command.c_str() << std::endl;
        return 1;
    }

    return 0;
}
