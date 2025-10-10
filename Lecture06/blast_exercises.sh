#!/bin/bash
unset IFS
input="$PWD/blastoutput2.out"
goodlines=${grep -v '#'|
