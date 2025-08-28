# start.ps1
poetry install

if (-not $env:PORT) {
    $env:PORT = 9000
}

poetry run python -m flask --app src/main run --host=0.0.0.0 --port $env:PORT --debug