find_package(Threads REQUIRED)
find_package(Qt5 COMPONENTS Widgets Core Network REQUIRED)

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOUIC_SEARCH_PATHS ${CMAKE_SOURCE_DIR}/client/forms)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

include_directories(include)

include_directories(${CMAKE_INCLUDE_PATH})

file(GLOB SOURCES "src/*.cpp")
file(GLOB INCLUDES "include/*.h")
file(GLOB FORMS "forms/*.ui")

add_executable(client ${SOURCES} ${INCLUDES} ${FORMS})


target_link_libraries (client ${CMAKE_THREAD_LIBS_INIT} ${CONAN_LIBS} Qt5::Widgets Qt5::Network Qt5::Core)
