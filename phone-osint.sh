#!/bin/bash

clear
echo "==============================="
echo " 📞 PHONE NUMBER OSINT TOOL"
echo "        by CyberNemita"
echo "==============================="
echo
echo "1) Basic Phone Information"
echo "2) Advanced Phone Information"
echo "3) Exit"
echo
read -p "Choose an option: " choice

case $choice in
  1)
    echo
    python basic_info/phone_basic.py
    ;;
  2)
    echo
    python advanced_info/phone_advanced.py
    ;;
  3)
    echo "Exiting..."
    exit
    ;;
  *)
    echo "Invalid option!"
    ;;
esac
