# MITRA-parallel v2

Trilingual parallel corpus of classical Buddhist literature: Sanskrit–Tibetan,
Sanskrit–Chinese, and Chinese–Tibetan, mined with the embedding-based
span-mining pipeline described in the accompanying paper (MITRA-MT, 2026).
Supersedes the v1 release (`../v1/`); v2 is a new mining run with a pivot-free
pipeline, provenance and alignment-confidence metadata on every record,
decontamination against the published evaluation suite, and exact
deduplication.

## Contents

One gzipped NDJSON file per direction (mirrored directions are separate
mappings, not byte mirrors: each direction unions target segments per source
segment independently):

| file | records | segment pairs |
|---|---|---|
| `sa-bo_matches.ndjson.gz` / `bo-sa_…` | 555,558 | 1,005,439 (sa→bo) |
| `zh-bo_matches.ndjson.gz` / `bo-zh_…` | 836,559 | 836,559 (zh→bo) |
| `sa-zh_matches.ndjson.gz` / `zh-sa_…` | 301,613 | 496,402 (sa→zh) |
| total (one direction each) | 1,693,730 | 2,338,400 |

Record schema (one JSON object per line): `id`, `score` (mean alignment
cosine), `root_segnr` / `par_segnr` (source/target segment IDs, DharmaNexus
numbering), `root_segtext` / `par_segtext` (segment texts), `root_string` /
`par_string` (concatenations), position fields, `root_length` / `par_length`
(character lengths).

## Provenance and cleaning

- Mined from the DharmaNexus corpora with the spanmine pipeline
  (margin-scored kNN anchors → monotone chain detection → vecalign sentence
  reconstruction → dictionary/density/length-ratio ensemble gates → supervised
  aligner drift screen). See the paper for validation numbers.
- Decontaminated against the MITRA-MT evaluation suite: 29,284 distinctive
  evaluation sentences (both sides of the sa-bo / sa-zh / bo-zh MT test sets
  and the cross-lingual retrieval benchmarks in `../v1/eval/`), NFC/
  whitespace/lowercase-normalized, matched as substrings; matching records
  dropped (sa-bo 93, zh-bo 4,686, sa-zh 1,228 per direction).
- Exact-deduplicated on normalized (source, target) text
  (sa-bo 14,862, zh-bo 35,312, sa-zh 6,916 duplicates removed per direction).
- Build statistics: `build_stats.json`.

Pāli is not part of this release. License and citation follow the repository
root README.
