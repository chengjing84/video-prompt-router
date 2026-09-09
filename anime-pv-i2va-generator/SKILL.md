---
name: anime-pv-i2va-generator
description: Create MiniMax H3 anime promotional-video I2VA prompts from a first-frame reference image, with optional identity-reference images. Use for anime battle highlights, character or world-building PVs, and high-energy typography/flash edits. Not for text-only generation, non-anime footage, other H3 generation modes, or sexualized character content.
---

# Anime PV I2VA Generator

Turn an anime reference image into one executable MiniMax H3 I2VA prompt with a faithful first frame, stable character identity, a directed event chain, beat-aware cuts, layered sound, and a visible ending payoff.

This is an anime-specific companion to `h3-prompt-writing`. Route FL2VA, L2VA, Ref2VA, text-only T2VA, or general non-anime requests to the general H3 prompt workflow instead.

## Required input

- Require one readable image as `<Picture 1>`. It is the exact `00:00.000` first frame.
- Accept up to two optional identity references as `<Picture 2>` and `<Picture 3>`. They may stabilize face, hair, clothing, accessories, proportions, and other identity anchors, but they do not bind to the timeline.
- Accept optional duration, aspect ratio, platform, story, action, dialogue, lyrics, title, music, forbidden elements, and style direction.
- Default to 15 seconds and 16:9. Allow 10–20 seconds when the user asks.
- If `<Picture 1>` cannot be inspected, stop and ask for a usable image. Do not invent a visual-evidence card from text alone.

## Workflow

Perform the following internally unless the user asks to see the process.

1. Inspect the image before inventing story.
   - Record subjects, appearance locks, pose and gaze, props, spatial relations, environment topology, observable colors, composition, visible effects, camera position, hidden regions, motion affordances, and crop-expansion risk.
   - Separate visible facts from inference. Do not guess character names or unseen costume details.
2. Select one primary route: battle highlight, promotional/world-building PV, or high-budget flash edit. A secondary lens may influence 10–30% of the piece, but it must not replace the main purpose.
3. Develop three genuinely different director concepts: image-native, concept-transformation, and formal-experiment. Compare their hook, narrative geometry, camera spine, transition logic, music topology, and ending payoff; any pair must differ on at least four of these six dimensions.
4. Choose the concept that best balances image fit, H3 executability, identity stability, commercial hook, and novelty.
5. Build a silent director card with one main event and one visible result per shot, causal `state_out → state_in` continuity, a recurring image-derived anchor, beat-aware timestamps, and a concrete final payoff.
6. Compile only the visible, audible, and timed instructions H3 needs. Remove internal labels, scores, explanations, placeholders, and abstract directorial claims.
7. Run the quality gate in [references/h3-i2va-contract.md](references/h3-i2va-contract.md) before responding.

After choosing the primary route, read only its section in [references/directing-modes.md](references/directing-modes.md). Read [references/h3-i2va-contract.md](references/h3-i2va-contract.md) for every task because it contains the required output format and timing rules.

## Directing constraints

- Preserve face, hair, clothing structure, color relationships, key props, grip, body count, and first-frame composition unless a visible transformation with intermediate states is requested.
- Derive movement, motifs, colors, typography, and transitions from visible image evidence or explicit user input.
- Use one main visual focus, one main event, one visible result, one primary camera move, and one transition interface per shot.
- A camera move, glow, particle effect, gaze, or breath alone is not a sufficient main event.
- Every important action needs a readable trigger, direction, contact or change, and result.
- Do not default to eye close-ups, feet-first openings, 360-degree spins, blue-black-red palettes, shattered glass, giant moons, petals, tunnels, glitch, white flashes, sweeping giant titles, or a face-first ending. Use any such device only when the image or request supports it.
- When age is unclear or the character appears young, keep the result fully non-sexualized. This skill does not create erotic or fetishized anime-character content.

## Response behavior

By default output exactly one finished H3 prompt, not the evidence card, concepts, director card, scoring, negative prompt, or validation checklist. If the user asks for the process, show the requested intermediate material separately and still finish with the compiled prompt.

The final prompt must start with the exact first-frame sentence and then use the three required fields in the order defined in [references/h3-i2va-contract.md](references/h3-i2va-contract.md).

## Attribution

Adapted for personal Codex use from `MINIMAX-H3 动漫 PV 专属图生视频（I2VA）提示词生成模板` by Bilibili creator **是古手梨花sama**. Preserve this attribution when redistributing substantial portions of the workflow.
