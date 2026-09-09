# H3 anime I2VA output contract

Operational distillation of `MINIMAX-H3 动漫 PV 专属图生视频（I2VA）提示词生成模板` by Bilibili creator **是古手梨花sama**.

## Reference roles

```yaml
reference_images:
  - <Picture 1>:
      role: first_frame
      timeline_binding: 00:00.000
  - <Picture 2>:
      role: character_identity_reference
      timeline_binding: none
  - <Picture 3>:
      role: character_identity_reference
      timeline_binding: none
```

Only `<Picture 1>` is the I2VA first frame. Never turn `<Picture 2>` or `<Picture 3>` into Shot 2, a later keyframe, a destination composition, or an ending frame. When optional identity images exist, declare their identity-only role in Shot 1.

## Exact output shell

The first line must be exactly:

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.
```

Leave one blank line, then output these fields in this order:

```text
integrated_multimodal_description: [Shot 1] <English final prompt> [Shot 2] At <strictly increasing timestamp>, ...

overall_soundscape: <1–4 English sentences>

non_diegetic_music: <1–3 English sentences>
```

## Field rules

### integrated_multimodal_description

- Write in English, except that dialogue, lyrics, and visible on-screen text may retain their original language inside English double quotes.
- Shot 1 has no timestamp. Establish the exact observable first-frame composition, subjects, clothing, props, colors, spatial anchors, and camera relationship before starting the first motion.
- Do not name or infer the image's art style, rendering method, line treatment, material style, or lighting style. Describe only observable visual facts.
- Later shots use strictly increasing timestamps: `[Shot N] At 00:SS.mmm, ...`.
- Each cut must introduce a new subject state, spatial fact, result, viewpoint, or time fact.
- Put dialogue, singing, instruments, broadcasts, television audio, phone audio, and other diegetic music here because characters can hear them.

### overall_soundscape

- Use one continuous paragraph of 1–4 English sentences.
- Cover environmental sound, physical action sound, and nonverbal vocal sound.
- Do not repeat dialogue, singing, diegetic music, or the audience-only background music.
- Use `N/A` only when the user explicitly asks for complete silence.

### non_diegetic_music

- Use 1–3 English sentences for music only the audience can hear.
- Specify instruments, tempo or BPM, meter when useful, rhythmic profile, dynamic structure, and the relationship between visual events and hits, drops, breaks, or the final beat.
- Avoid abstract mood-only descriptions and explanations of emotional function.
- Use `N/A` when there is no non-diegetic music.

## Timing

Calculate from zero using full precision, then round final cut times to milliseconds:

```text
seconds_per_beat = 60 / BPM
seconds_per_bar = beats_per_bar × 60 / BPM
cut_time = accumulated_beats × seconds_per_beat
```

For 6/8, normally count two dotted-quarter beats per bar unless the director card explicitly chooses six eighth-note beats. Do not force arbitrary BPM values onto a 0.5-second grid. Prefer bar starts, phrase changes, strong beats, breaks, drops, timbre changes, or completed action results. If action causality and a theoretical beat disagree, first adjust action length, then choose a nearby beat, then adjust BPM, then reduce shots or events.

## Complexity budget

For a 15-second result:

| Primary route | Suggested shots | Main events across the film | Per-shot event budget |
|---|---:|---:|---:|
| Battle highlight | 4–6 | 6–12 | One main exchange, optionally followed by one result action |
| Promotional/world-building PV | 4–7 | 4–7 | One main event |
| High-budget flash edit | 6–9 | 6–9 | One main event |

Reduce shots, environments, full-body motion, and risky inventions when identity risk is high. Typography consumes complexity even when it is not counted as a separate main event.

## Silent quality gate

Revise before output if any check fails:

- Shot 1 is the exact reference frame, not a similar redraw.
- Face, hair, clothing, colors, props, grip, body count, and composition remain stable.
- Hidden content is not presented as known fact; crop expansion matches visible evidence.
- The first 0.8 seconds contain an image-derived hook.
- Each shot has one clear focus, event, and visible result.
- State changes are causal and physically readable; transformations show intermediate states.
- The ending payoff is visible and worth waiting for.
- The concept is not a fixed shot skeleton with only character, color, and prop substitutions.
- Shot count, events, camera moves, effects, transitions, and typography stay within the complexity budget.
- BPM math is correct; timestamps increase and remain within duration.
- Major music cues bind to visible results; the sound mix has foreground, background, buildup, peak, and decay where appropriate.
- The first-frame sentence and all three fields exist in the required order.
- The final compiled content contains no director-card labels, scores, Chinese writing instructions, unresolved references, or placeholders.
- The result is non-sexualized when age is unclear or the character appears young.

Fatal failures include missing output fields, first-frame drift, identity drift, random montage without causality, important actions without results, overloaded shots, invalid timestamps, and leftover internal scaffolding.
