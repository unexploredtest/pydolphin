cmake_minimum_required(VERSION 3.13)

project(cdolphin VERSION 0.1)

set(CMAKE_C_STANDARD 99)
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


# Add compiler flags for position-independent code as we're making a python extension
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC")

set(CMAKE_SHARED_LIBRARY_PREFIX "")

add_subdirectory(externals/dolphin)

find_package(PkgConfig REQUIRED)
find_package(X11 REQUIRED)

if(ENABLE_X11)
  pkg_check_modules(X11 x11 IMPORTED_TARGET)
  if(X11_FOUND)
    add_definitions(-DHAVE_X11=1)
    pkg_check_modules(XRANDR xrandr IMPORTED_TARGET)
    if(XRANDR_FOUND)
      add_definitions(-DHAVE_XRANDR=1)
    endif()
    pkg_check_modules(X11_INPUT REQUIRED xi>=1.5.0 IMPORTED_TARGET)
    message(STATUS "X11 support enabled")
  else()
    message(WARNING "X11 support enabled but not found. This build will not support X11.")
  endif()
endif()

# Find Python
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)

# Include Python headers
include_directories(${Python3_INCLUDE_DIRS})

# Link against Python libraries
link_directories(${Python3_LIBRARY_DIRS})

set(DOLPHIN_CORE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/externals/dolphin/Source/Core")
set(DOLPHIN_NO_GUI_PATH "${DOLPHIN_CORE_PATH}/DolphinNoGUI")

add_library(cdolphin SHARED
  cdolphin/script.cpp
  cdolphin/dolphin.cpp
  ${DOLPHIN_NO_GUI_PATH}/Platform.cpp
  ${DOLPHIN_NO_GUI_PATH}/PlatformHeadless.cpp
)


target_link_libraries(cdolphin PRIVATE ${Python3_LIBRARIES})

target_include_directories(cdolphin PUBLIC ${DOLPHIN_CORE_PATH})

if(X11_FOUND)
  target_sources(cdolphin PRIVATE ${DOLPHIN_NO_GUI_PATH}/PlatformX11.cpp)
  target_link_libraries(cdolphin PRIVATE PkgConfig::XRANDR PkgConfig::X11)
endif()

if(WIN32)
  target_sources(cdolphin PRIVATE ${DOLPHIN_NO_GUI_PATH}/PlatformWin32.cpp)
endif()

if(APPLE)
  target_sources(cdolphin PRIVATE ${DOLPHIN_NO_GUI_PATH}/PlatformMacos.mm)
  target_compile_options(cdolphin PRIVATE -fobjc-arc)
endif()

if(${CMAKE_SYSTEM_NAME} STREQUAL "Linux")
  target_sources(cdolphin PRIVATE ${DOLPHIN_NO_GUI_PATH}/PlatformFBDev.cpp)
endif()

set_target_properties(cdolphin PROPERTIES OUTPUT_NAME "_cdolphin")

target_link_libraries(cdolphin
PRIVATE
  core
  uicommon
  cpp-optparse
)

if(APPLE)
  target_link_libraries(cdolphin
    PRIVATE
      ${APPKIT_LIBRARY}
      ${COREFOUNDATION_LIBRARY}
      ${IOK_LIBRARY}
  )
endif()

if(WIN32)
  # needed for adjusting window decorations with DwmSetWindowAttribute
  target_link_libraries(cdolphin PRIVATE dwmapi.lib)
endif()

if(MSVC)
  # Add precompiled header
  target_link_libraries(cdolphin PRIVATE use_pch)
endif()

if(USE_DISCORD_PRESENCE)
  target_compile_definitions(cdolphin PRIVATE -DUSE_DISCORD_PRESENCE)
endif()

set(CPACK_PACKAGE_EXECUTABLES ${CPACK_PACKAGE_EXECUTABLES} cdolphin)
install(TARGETS cdolphin RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})

target_link_libraries(cdolphin PRIVATE ${Python3_LIBRARIES} imgui core)