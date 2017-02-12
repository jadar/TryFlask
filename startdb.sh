#!/bin/sh

if [ ! -d ./data ]; then
	mkdir data
fi

mongod --dbpath ./data/