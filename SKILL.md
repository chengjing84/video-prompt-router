---
name: video-prompt-router
description: Route video-prompt production requests to exactly one MiniMax H3 or Seedance specialist before drafting. Use for video prompts, story clips, I2V/T2V/Ref2V, dialogue scenes, anime PVs, fight scenes, camera requests, continuations, blocked prompts, and prompt troubleshooting when production speed and low context usage matter.
metadata:
  short-description: Route each video request to one specialist Skill
---

# Video Prompt Router

Route first; do not draft inside this Skill.

## Production rule

1. Inherit the active project's platform, references, duration, aspect ratio, characters, and output location when the user says “再来一版”, “继续”, or changes only one parameter.
2. Select exactly one target Skill from the table below. Load no parent, companion, example, vocabulary, or secondary specialist unless the selected Skill explicitly requires it for the chosen mode.
3. Default delivery is one directly copyable final prompt. Do not produce analysis, evidence cards, bilingual duplicates, alternate versions, call instructions, or files unless requested.
4. Do not save to disk unless the user says to save. Do not browse or inspect already-readable references again unless the asset changed or visual evidence is uncertain.
5. Ask a question only when platform or reference role is unknown and the answer changes the executable prompt format. Otherwise inherit context and proceed.

## MiniMax H3 routing

| Request | Load only |
|---|---|
| Continuous combat, weapon fight, hand-to-hand fight, boss fight, dense action exchange | `high-density-fight-prompt` |
| Anime PV, anime battle highlight, typography-heavy anime promo from a first frame | `anime-pv-i2va-generator` |
| All other H3 T2VA, I2VA, FL2VA, L2VA, Ref2VA, dialogue, vlog, hero shot, product or ambience | `h3-prompt-writing` |

Do not load `h3-prompt-writing` in addition to `high-density-fight-prompt`; the fight Skill already contains its H3 compilation route. Do not load the anime companion for live-action cosplay merely because the costume is anime-inspired.

## Seedance routing

| Dominant request | Load only |
|---|---|
| Write or improve an ordinary prompt | `seedance-prompt` |
| Long connected story or multiple generated clips | `seedance-sequence` |
| Continue accepted footage or repair its tail | `seedance-continuation` |
| Dialogue, voice, lip-sync, sound or music timing is the main problem | `seedance-audio` |
| Camera, framing or shot movement is the main problem | `seedance-camera` |
| Character identity, wardrobe, blocking, hands or expressions are the main problem | `seedance-characters` |
| Body choreography or physical motion is the main problem | `seedance-motion` |
| Prompt rejection or policy false positive | `seedance-filter` |
| Bad, blurry, unstable, off-prompt or desynchronized output | `seedance-troubleshoot` |

For mixed Seedance requests, route to the Skill matching the failure or deliverable that dominates the user's latest sentence. The selected Skill may use its own required supporting references; do not independently preload neighboring specialists.

## Fast revision rule

For a same-project revision, preserve everything not explicitly changed. Recompile only the affected prompt layer. Examples: changing 16:9 to 9:16 changes framing, not story; requesting a face close-up changes shot coverage, not identity or action ownership; changing a first-frame image to a last-frame image changes I2VA to L2VA, not the character design.

## Escalation to full workflow

Use a target Skill's extended contracts, audits, dual-language output, or project-state documents only when the user requests them, the sequence spans multiple generations, reference ownership is ambiguous, or an earlier generation failed in a way that requires diagnosis. A simple 10-second prompt should stay on the target Skill's shortest valid production path.
