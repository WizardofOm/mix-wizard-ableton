---
name: compression-math
description: Use when the user asks how a compressor works, what ratio or threshold to use, or what makeup gain does, in Ableton Live or in general. Explains ratio with simple arithmetic and gives starting settings.
---

# Compression Math

Explain compression in plain numbers, then help set it.

## The idea

A compressor only acts on signal that rises above the threshold. The ratio says how much of that overshoot is allowed through.

**Output overshoot = input overshoot divided by the ratio.**

| Signal goes over threshold by | Ratio | Comes out over by |
| --- | --- | --- |
| 6 dB | 2:1 | 3 dB |
| 6 dB | 3:1 | 2 dB |
| 6 dB | 6:1 | 1 dB |
| 6 dB | 20:1 | 0.3 dB |
| 6 dB | 40:1 | 0.15 dB |

At very high ratios almost nothing gets past the threshold. That is limiting.

## Makeup gain

Compression turns the loud parts down, so the whole track ends up quieter. Makeup gain raises everything back up. The result is the original loudness with the peaks under control: quiet details are relatively louder, spikes are gone, and the track sits steadily among the others.

## Setting one in Live (Compressor)

1. Choose a ratio by job:
   - 2:1 to 3:1: gentle leveling, buses, mastering
   - 4:1 to 6:1: firm control of vocals, bass, drums
   - 10:1 and up: peak stopping
2. Lower the threshold until the gain-reduction meter shows the amount wanted on the loud passages (often 2 to 6 dB on a single track).
3. Set makeup so the level matches when the device is bypassed.
4. Compare on and off at matched level. It should sound steadier, not smaller.

## Don'ts

- Don't judge a compressor louder than the bypassed signal.
- Don't reach for a high ratio first. Lower threshold with a low ratio often sounds more natural.
- Don't compress to fix a balance problem a fader would solve.
