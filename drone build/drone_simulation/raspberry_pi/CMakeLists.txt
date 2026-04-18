cmake_minimum_required(VERSION 3.13)

include(pico_sdk_import.cmake)

project(raspberry_pi C CXX ASM)

pico_sdk_init()

add_executable(raspberry_pi
    mpu6050.c
    main.c
)

target_link_libraries(raspberry_pi 
    pico_stdlib
    hardware_i2c
    m
)

# This is what makes it show up as a COM port over USB
pico_enable_stdio_usb(raspberry_pi 1)
pico_enable_stdio_uart(raspberry_pi 0)

pico_add_extra_outputs(raspberry_pi)