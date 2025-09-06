cmake_minimum_required(VERSION 3.10)
project(Notifier)

# Require C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add the executable and its source files
add_executable(notifier main.cpp notifier.cpp)

# We will need to add find_package and target_link_libraries for SQLite3
# and Windows-specific libraries later.
