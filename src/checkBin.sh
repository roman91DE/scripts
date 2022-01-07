#!/bin/sh

# which program?
echo "\nprogram: ${1}"
echo "-----------------"
# which path is used?
echo "path: $(which ${1})"
# list available types
echo "type(s):"
echo "$(type -a ${1})\n"
