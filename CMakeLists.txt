cmake_minimum_required(VERSION 3.5)
set(PROJECT_NAME as2_basic_behaviors)
project(${PROJECT_NAME} VERSION 0.2.0)

# Default to C++17
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

# find dependencies
set(PROJECT_DEPENDENCIES
  ament_cmake
  rclcpp
  rclcpp_action
  as2_behavior
  std_srvs
  as2_core
  builtin_interfaces
  rosidl_default_generators
  action_msgs
)

foreach(DEPENDENCY ${PROJECT_DEPENDENCIES})
  find_package(${DEPENDENCY} REQUIRED)
endforeach()

set(SOURCE_CPP_FILES 
)

set(HEADER_HPP_FILES
)

include_directories(
  include
  include/${PROJECT_NAME}
)

set(ACTION_FILES
  action/SetArmingState.action
  action/SetOffboardMode.action
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${ACTION_FILES}
  DEPENDENCIES builtin_interfaces action_msgs
)


add_executable(arm_behavior src/set_arming_state_behavior_main.cpp )
add_executable(offboard_behavior src/set_offboard_mode_behavior_main.cpp)

ament_target_dependencies(arm_behavior ${PROJECT_DEPENDENCIES})
ament_target_dependencies(offboard_behavior ${PROJECT_DEPENDENCIES})

rosidl_get_typesupport_target(cpp_typesupport_target ${PROJECT_NAME} "rosidl_typesupport_cpp")

target_link_libraries(arm_behavior "${cpp_typesupport_target}")

target_link_libraries(offboard_behavior "${cpp_typesupport_target}")

install(TARGETS
  arm_behavior
  offboard_behavior
  DESTINATION lib/${PROJECT_NAME}
)


if(BUILD_TESTING)
  find_package(ament_cmake_cppcheck REQUIRED)
  find_package(ament_cmake_clang_format REQUIRED)
  
  ament_cppcheck(src/ include/)
  ament_clang_format(src/ include/ tests/ --config ${CMAKE_CURRENT_SOURCE_DIR}/.clang-format)

endif()

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME})

ament_package()
