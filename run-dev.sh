#!/bin/bash
export PATH="$HOME/.local/bin:$PATH"

poetry install

if ! grep -q "$PATH" /home/coder/.bashrc; then
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> /home/coder/.bashrc
fi

poetry run python3 -u -m flask --app src/main run --host=0.0.0.0 -p $PORT --debug