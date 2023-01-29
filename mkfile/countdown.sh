#!/bin/bash

# Set the counter (default:5 secs.)
COUNTER=$((${1:-5}*10))

NC='\033[0m'
YELLOW='\033[33m'
YELLOW_B='\033[33;1m'
WHITE_B='\033[37;1m'
H_CURSOR='\033[?25l'
S_CURSOR='\033[?25h'

terminate() {
    printf "${S_CURSOR}\n"
    printf "${YELLOW_B}Terminate${NC}"
    exit 0
}

# hide ^C
stty -echoctl

trap 'terminate' SIGINT

printf "${H_CURSOR}"
while [ $COUNTER -gt 0 ]; do
  if read -t 0; then
    break
  fi
  printf "\rStart in ${WHITE_B}$((COUNTER/10))${NC} Sec. ${YELLOW}<ENTER>${NC} to continue"
  ((COUNTER--))
  sleep 0.1
done
printf "${S_CURSOR}\n"
printf "${YELLOW_B}Program is starting...${NC}\n"
