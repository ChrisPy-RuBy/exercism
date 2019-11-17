#!/usr/bin/env bash

var=$1
i=0
rev=""
rev=${var:i++:1}$rev
echo $rev

