cmake_minimum_required(VERSION 3.10)
project(Startup)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(startup main.cpp)

# On Windows, this will need to link against Advapi32.lib for Registry functions.
