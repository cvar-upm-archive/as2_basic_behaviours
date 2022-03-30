// "Copyright [year] <Copyright Owner>"

#include "as2_basic_behaviour.hpp"
#include "land_behaviour.hpp"
#include "as2_core/core_functions.hpp"

int main(int argc, char * argv[])
{
  setvbuf(stdout, NULL, _IONBF, BUFSIZ);
  rclcpp::init(argc, argv);
  std::cout << "Starting Land Behaviour" << std::endl;

  auto node = std::make_shared<LandBehaviour>();
  node->preset_loop_frequency(30);
  as2::spinLoop(node);  
  
  rclcpp::shutdown();
  return 0;
}
