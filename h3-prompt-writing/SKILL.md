---
name: h3-prompt-writing
description: Write general MiniMax H3 prompts for T2VA, I2VA, FL2VA, L2VA, and Ref2VA, including dialogue, vlog, hero shots, products, ambience, keyframe alignment, soundscape, and reference labels. Use for non-combat, non-anime-PV H3 production; route dense fights and anime PVs to their dedicated Skills.
compatibility: Portable to any agent that can read local files — no external API calls, MiniMax Hub tools, or proprietary runtime required. The agents/openai.yaml file only adds optional ChatGPT/Codex UI metadata; it does not restrict the skill to OpenAI agents.
---

# H3 Prompt Writing

## Mode Routing

Choose the mode before drafting:

- For high-density combat, continuous attack-and-defense, weapon fights, hand-to-hand fights, boss or giant-creature fights, or a request explicitly naming the high-density fight workflow, read [the fight-mode entrypoint](references/fight/SKILL.md) completely and follow it as the active director contract.
- For anime PV I2VA, use the separate `anime-pv-i2va-generator` companion Skill when it is available.
- For all other MiniMax H3 requests, use the general workflow below.

Fight mode remains part of MiniMax H3. Its Chinese director draft is the source timeline; when English output is requested, compile that same timeline into H3 Ref2VA six-section format without adding or deleting actions. The fight contract's required first-token rule, duration routing, asset ledger, physical continuity, and output rules take precedence within fight tasks. Do not apply fight-mode defaults to ordinary dialogue, ambience, product, or non-combat video.

## General Workflow

1. Identify the input mode: T2VA, I2VA, FL2VA, L2VA, or full-reference Ref2VA.
2. For base text/keyframe modes, read `references/base-en.txt` and follow its final prompt structure.
3. For full-reference mode, read `references/ref-en.txt` and follow its six-section rewrite format.
4. Preserve the exact field names, section order, labels, and timing notation from the selected guide.

## Base Modes

- T2VA: build the full audiovisual timeline from text.
- I2VA: start from the first frame and develop forward from it.
- FL2VA: describe the continuous path between the first and last frames.
- L2VA: infer a plausible opening and converge to the supplied last frame.

Use `integrated_multimodal_description`, `overall_soundscape`, and `non_diegetic_music` in the order shown in `references/base-en.txt`.

## Full-Reference Mode

Ref2VA rewrites use `subject_definitions`, `summary`, `retention_analysis`, `detailed_description`, `overall_soundscape`, and `non_diegetic_music` in that order. Reference labels stay consistent across all sections.

Read `references/ref-en.txt` for label rules, retention analysis, and complete examples.

## High-Density Fight Mode

The integrated fight branch lives under `references/fight/`:

- Read [fight/SKILL.md](references/fight/SKILL.md) for routing, deliverables, hard constraints, and the required `BUNNY` first token.
- It requires [the 15-second fight directing contract](references/fight/references/15s-fight-directing-contract.md) for reference-driven fight tasks.
- When an English MiniMax H3 Ref2VA version is needed, also read [the H3 dual-output compilation contract](references/fight/references/h3-ref2va-dual-output.md) and the general [Ref2VA format guide](references/ref-en.txt).

Do not invent weapons, powers, opponents, injuries, or scene mechanisms absent from user instructions and visible references. Preserve one causal action timeline across Chinese and English outputs. Duration determines structure: the fight branch's short-duration route applies at 10 seconds or less; its 15-second route applies around 15 seconds or when duration is unspecified.

## Output Rules

- Write rewrite sections in English; preserve dialogue, lyrics, and visible scene text in their original language.
- Describe each shot by composition, subjects, environment, actions, camera, sound, and the exact point where referenced content appears.
- Avoid plot summaries, unresolved reference labels, and timing that does not match the requested duration.
- In fight mode, follow the fight branch's requested Chinese-plus-English or Chinese-only deliverable instead of forcing the general single-format default.

## Tips for Better Results

- Always match the total duration of the description to the requested video length (4–15 seconds), except where a specialized companion explicitly supports a different verified range.
- Keep reference labels consistent (e.g. `<Picture 1>`, `<Video 1>`, `<Audio 1>`) across every section.
- Prefer concrete visual and audio details over abstract words like "cinematic" or "beautiful".
- When using keyframes (I2VA / FL2VA / L2VA), clearly state how the first and/or last frame connects to the timeline.
