# Install script for directory: /Users/philip/Documents/radio/gnuradio_blocks/gr-testblock

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/testblock" TYPE FILE FILES "/Users/philip/Documents/radio/gnuradio_blocks/gr-testblock/cmake/Modules/testblockConfig.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/Users/philip/Documents/radio/gnuradio_blocks/gr-testblock/build/include/testblock/cmake_install.cmake")
  include("/Users/philip/Documents/radio/gnuradio_blocks/gr-testblock/build/lib/cmake_install.cmake")
  include("/Users/philip/Documents/radio/gnuradio_blocks/gr-testblock/build/swig/cmake_install.cmake")
  include("/Users/philip/Documents/radio/gnuradio_blocks/gr-testblock/build/python/cmake_install.cmake")
  include("/Users/philip/Documents/radio/gnuradio_blocks/gr-testblock/build/grc/cmake_install.cmake")
  include("/Users/philip/Documents/radio/gnuradio_blocks/gr-testblock/build/apps/cmake_install.cmake")
  include("/Users/philip/Documents/radio/gnuradio_blocks/gr-testblock/build/docs/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/Users/philip/Documents/radio/gnuradio_blocks/gr-testblock/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
