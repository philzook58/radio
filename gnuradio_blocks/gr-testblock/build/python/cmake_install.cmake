# Install script for directory: /Users/philip/Documents/radio/gnuradio_blocks/gr-testblock/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/site-packages/testblock" TYPE FILE FILES
    "/Users/philip/Documents/radio/gnuradio_blocks/gr-testblock/python/__init__.py"
    "/Users/philip/Documents/radio/gnuradio_blocks/gr-testblock/python/copy_ff.py"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/site-packages/testblock" TYPE FILE FILES
    "/Users/philip/Documents/radio/gnuradio_blocks/gr-testblock/build/python/__init__.pyc"
    "/Users/philip/Documents/radio/gnuradio_blocks/gr-testblock/build/python/copy_ff.pyc"
    "/Users/philip/Documents/radio/gnuradio_blocks/gr-testblock/build/python/__init__.pyo"
    "/Users/philip/Documents/radio/gnuradio_blocks/gr-testblock/build/python/copy_ff.pyo"
    )
endif()

