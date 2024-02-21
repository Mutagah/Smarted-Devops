#!/bin/bash

if [ "${1,,}" = herbert ]; then
	echo "Ooh, you are the boss, Welcome!"
elif [ "${1,,}" = help ]; then
	echo "Just enter your username, duh!"
else
	echo "I dont know who you are, But you are not my boss!"
fi

