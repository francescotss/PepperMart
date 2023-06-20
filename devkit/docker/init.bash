#!/bin/bash

SESSION=init

tmux -2 new-session -d -s $SESSION

tmux rename-window -t $SESSION:0 'pepper_tools'
tmux new-window -t $SESSION:1 -n 'naoqi'
tmux new-window -t $SESSION:2 -n 'playground'

tmux send-keys -t $SESSION:0 "cd src/pepper_tools" C-m
tmux send-keys -t $SESSION:1 "cd /opt/Aldebaran/naoqi-sdk-2.5.5.5-linux64" C-m
tmux send-keys -t $SESSION:2 "cd ~/playground" C-m


while [ 1 ]; do
  sleep 60;
done


