#include <iostream>
#include "pipe.hpp"

int main() {
	"test\n" | [](auto i){std::cout<<i;};
}