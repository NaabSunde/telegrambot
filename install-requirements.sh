#!/bin/sh
while read p; do
  pip install --upgrade $p
done < requirements.pip
