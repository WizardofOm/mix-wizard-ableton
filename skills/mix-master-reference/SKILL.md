---
name: mix-master-reference
description: Use for quick mixing and mastering facts in Ableton Live - gain staging targets, typical EQ and compression settings, stereo rules, mastering chain order, loudness and true-peak targets, common mistakes, and psychoacoustic reminders.
---

# Mix and Master Reference

A compact working reference. Use it to answer quick questions and to sanity-check a plan. It sits alongside the other Mix Wizard skills; where they differ, both approaches are valid and the section below says when to pick each.

## Where methods differ

| Topic | Option A | Option B | How to choose |
| --- | --- | --- | --- |
| Master chain order | **Polish chain** (`master-polish`): exciter first, light compression, saturation, resonance control, low-end check, dynamic EQ, limiter | **Standard chain** (section 8 below): Utility, surgical EQ, tonal EQ, glue compression, optional multiband, saturation, limiter | Polish chain when the mix is already balanced and needs shine and loudness. Standard chain when the mix needs corrective EQ first, or for a neutral, conservative master. |
| Limiter ceiling | about -1 dBTP | down to -0.3 dBTP | -1 dBTP for streaming and anything that will be encoded to a lossy format. Closer to -0.3 only for club or WAV delivery where every bit of level matters. |
| High-pass points | **Handoff** (`low-end-handoff`): guitars and keys about 110 Hz, drums about 80 Hz, gentle slopes, bass walled at 30 Hz | **General**: 30 to 80 Hz on most non-bass sources | Handoff when building the low end of a band or dense arrangement as one unit. General range for individual tracks in sparse or electronic mixes. |
| 250 Hz cut | **Blanket pass** (`clean-eq`): about -2 dB, wide, on nearly every track before listening | **Targeted**: cut 200 to 500 Hz only where a track shows build-up | Blanket pass as a fast first move on a cloudy mix. Targeted cuts when the mix is already clean and only one or two tracks are thick. |

Say which option you are using and why, then let the user's ears decide.

## 1. Core principles

- Balance (levels and panning) solves most mix problems before plugins.
- Subtractive processing before additive.
- Mastering moves are small, usually 0.5 to 2 dB.
- Headroom is non-negotiable.
- Reference constantly at matched loudness.
- Check mono compatibility, especially the low end.
- Ears respond more to average energy and spectral balance than to peaks.
- Upward spread of masking: cleaning 200 to 500 Hz often clarifies everything above it.
- Perceived loudness is not LUFS. Spectral density, micro-dynamics, contrast, and harmonic content matter more.

## 2. Gain staging

- Tracks: average around -18 dBFS, peaks roughly -12 to -8 dBFS.
- Master while mixing: peaks between -6 and -3 dBFS with no processing.
- Use Utility or clip gain for consistent levels.
- Never mix into a brick-wall limiter.
- Bad gain staging is the most common cause of weak masters.

## 3. EQ

- High-pass almost everything that is not kick or bass (start 30 to 80 Hz depending on the source).
- Cut problem frequencies before boosting. Common mud zone: 200 to 500 Hz.
- Complementary EQ: when two elements fight, cut on one and leave or boost the other.
- Narrow Q for resonances, wide Q for tonal balance.
- Mid/Side: keep low end in Mid; add air and width on Sides carefully.
- Never boost without a reason. Cuts usually sound more natural.

## 4. Compression

| Source | Ratio | Attack | Gain reduction | Goal |
| --- | --- | --- | --- | --- |
| Vocals | 3:1 to 4:1 | 10 to 30 ms | 3 to 6 dB | steady level, consonants intact |
| Drums | to taste | slow to keep transients, fast for control | to taste | punch or tightness |
| Bass | moderate | slower | moderate | even notes with punch |
| Bus / glue (Glue Compressor) | 1.5:1 to 2:1 | 10 to 30 ms | 1 to 3 dB | cohesion |

- Parallel (New York style): heavy compression on a send, blended under the dry signal.
- Multiband: sparingly, for frequency-specific control, with gentle reduction.

## 5. Parallel and bus processing

- Parallel compression adds punch and density without killing transients.
- Serial bus limiting or compression gives controlled loudness.
- Group related elements (drums, vocals, synths) and process the group.
- Sidechain is an arrangement and clarity tool, not only a pumping effect.

## 6. Stereo and imaging

- Kick, bass, and lead vocal stay centered.
- Low end in mono: Utility Bass Mono around 120 to 150 Hz.
- Width is addictive. Check mono regularly.
- Haas effect and short delays can add width if used carefully; verify in mono.
- Mid/Side EQ and processing control center against sides.

## 7. Space and effects

- Reverb and delay on sends, not inserts.
- High-pass and low-pass the returns.
- Pre-delay on reverb keeps the source clear.
- Automating sends and effects beats static settings.
- Less is usually more.

## 8. Mastering chain (typical order)

1. Utility (Bass Mono, width if needed)
2. Surgical EQ (high-pass and narrow cuts)
3. Tonal EQ (broad, small moves)
4. Light glue compression (1 to 2 dB reduction)
5. Optional Multiband Dynamics
6. Subtle saturation
7. Limiter (true peak, ceiling -0.3 to -1.0 dBTP)
8. Metering (LUFS, Spectrum, correlation)

## 9. Loudness targets

- Streaming: commonly -14 to -9 LUFS integrated, depending on genre.
- Club and loud electronic: -8 to -6 LUFS is possible, but keep the punch.
- Translation and dynamics come before maximum loudness.
- True peak at or below -1 dBTP, or -2 dBTP for a very loud master.

## 10. Referencing

- Level-match references within 0.5 dB.
- Compare section by section.
- Listen for low-end weight, midrange clarity, high-end smoothness, stereo width, transient impact, and overall density.
- Several references beat one.

## 11. Ableton Live notes

- EQ Eight in Mid/Side mode is extremely capable.
- Glue Compressor is excellent for bus work.
- Utility is essential for gain, mono, and width.
- Multiband Dynamics can act as transparent pressure when used lightly.
- Build parallel chains with Return tracks or Groups.
- Automating filters, sends, and group processing is a core arrangement and mixing tool.

## 12. Common mistakes

- Mixing too loud.
- Over-compressing and killing micro-dynamics.
- Boosting instead of cutting.
- Ignoring mono compatibility.
- Adding a limiter too early.
- Treating mastering as a fix for a bad mix.
- Chasing LUFS numbers instead of perceived impact.
- Static processing with no automation or movement.

## 13. Psychoacoustic reminders

- The ear is most sensitive from about 2 to 5 kHz.
- Low-frequency energy masks higher frequencies more than the reverse.
- Contrast creates the sensation of loudness and impact.
- Harmonic density raises perceived loudness without raising peak level.
- Space and silence make dense sections hit harder.
