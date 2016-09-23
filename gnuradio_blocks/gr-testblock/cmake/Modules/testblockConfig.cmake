INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_TESTBLOCK testblock)

FIND_PATH(
    TESTBLOCK_INCLUDE_DIRS
    NAMES testblock/api.h
    HINTS $ENV{TESTBLOCK_DIR}/include
        ${PC_TESTBLOCK_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    TESTBLOCK_LIBRARIES
    NAMES gnuradio-testblock
    HINTS $ENV{TESTBLOCK_DIR}/lib
        ${PC_TESTBLOCK_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(TESTBLOCK DEFAULT_MSG TESTBLOCK_LIBRARIES TESTBLOCK_INCLUDE_DIRS)
MARK_AS_ADVANCED(TESTBLOCK_LIBRARIES TESTBLOCK_INCLUDE_DIRS)

