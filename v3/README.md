# MITRA-parallel v3

Trilingual parallel corpus of classical Buddhist literature (Sanskrit–Tibetan, Sanskrit–Chinese,
Chinese–Tibetan). Supersedes [`../v2/`](../v2/). v3 re-aligns the mined spans at sentence level and
runs every alignment through a trained post-corrector that checks it pair by pair. This replaces v2's
ensemble gates. It also adds spans that were missing in v2.

## Contents

One gzipped NDJSON file per direction. Both directions hold the same aligned pairs, with root and par
swapped.

| files | records | work pairs | source segments | target segments |
|---|---|---|---|---|
| `sa-bo_matches.ndjson.gz` / `bo-sa_…` | 625,148 | 1,726 | 606,434 sa | 884,639 bo |
| `bo-zh_matches.ndjson.gz` / `zh-bo_…` | 709,769 | 4,259 | 925,776 bo | 837,279 zh |
| `sa-zh_matches.ndjson.gz` / `zh-sa_…` | 355,738 | 2,101 | 341,605 sa | 434,667 zh |
| total (one direction each) | 1,690,655 | 8,086 | | |

Each record is one aligned bead: one or more consecutive source segments aligned to one or more
consecutive target segments. Fields: `id`, `score` (density of the aligned stretch the bead belongs
to, 0.5 to 1), `root_segnr` / `par_segnr` (segment IDs, DharmaNexus numbering), `root_segtext` /
`par_segtext`, `root_string` / `par_string`, `root_length` / `par_length`, `src_lang` / `tgt_lang`,
plus position fields kept for DharmaNexus compatibility.

## How it was built

1. Span mining as in v2: margin-scored kNN anchors, then monotone chain detection, which finds
   stretches of two texts that are translations of each other.
2. Sentence alignment of every span with vecalign.
3. Post-correction: a trained model checks each aligned pair, rejects wrong links and adds links
   vecalign missed. A probe at the start of each span throws out whole spans that are not parallel.
4. Triangle fill: where two texts are both aligned to a third text in the other language (for
   example a Sanskrit and a Chinese text both aligned to the same Tibetan text), the implied stretches
   with no direct alignment were aligned directly and post-corrected the same way. They were kept
   only where at least half of the resulting pairs agree with the pivot links.
5. Shape filter: a pair is kept only inside a run of at least 20 aligned beads with density of at
   least 0.5, which removes isolated links.
6. Overlapping spans of the same text pair are deduplicated (each segment is claimed once per text
   pair, largest span first).
7. Decontaminated against the MITRA-MT evaluation suite exactly as v2 (29,284 distinctive evaluation
   sentences, normalized substring match): sa-bo 156, sa-zh 1,185, bo-zh 2,254 records dropped.
   Also dropped: 576 records from Tibetan lines that are mixed into one Sanskrit source file
   (Ḍākārṇavatantra, Sugiki 2022).

