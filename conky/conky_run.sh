#!/bin/env sh

killall conky

sleep 0.8
conky -c $HOME/.conky/conky_clock &

sleep 0.8
conky -c $HOME/.conky/conky_memory &

sleep 0.8
conky -c $HOME/.conky/conky_cpu &

sleep 0.8
conky -c $HOME/.conky/conky_network &

sleep 0.8
conky -c $HOME/.conky/conky_record_data &
