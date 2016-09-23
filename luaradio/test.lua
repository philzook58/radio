local radio = require('radio')


local src = radio.SignalSource('square', 1e3, 44100)


local sink = radio.PulseAudioSink(2)
-- Top-level block
local top = radio.CompositeBlock()

top:connect(src, 'out', sink, 'in1')


-- Run top block
top:run()