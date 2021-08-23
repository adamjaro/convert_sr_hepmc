# Conversion of Synrad output to HepMC3

## Dependencies

- Boost
- HepMC3

## Compile

It is based on cmake (mkdir build && cd build && cmake ../ && make)

## Run

<pre><code> ./convert_sr -i input.csv -o output.hepmc -n number-of-events </pre></code>

The number of events is optional. All events are converted when not present or negative.

