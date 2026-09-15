# MITRA-MT evaluation suite

Held-out translation test sets released with the MITRA-MT paper (2026): 17
translation directions at sentence level, ten of them also at paragraph level.
This folder contains only the directions whose reference translations may be
redistributed. Six further directions that were evaluated under the identical
protocol (sa→ja, sa→de, sa→hi, zh→fr, zh→ko, pa→en) are not included because
their references cannot be redistributed.

Language codes: `sa` Sanskrit (IAST), `bo` Tibetan (Unicode, no Wylie),
`zh` Buddhist Chinese (traditional, unless noted), `en` English, and
`fr es de pt it nl` for French, Spanish, German, Portuguese, Italian, Dutch.
Modern Chinese (Lotsawa House) is also `zh`.

## Files

| direction | file | sentence pairs | paragraph blocks | source |
|---|---|---|---|---|
| sa→bo | `sa-bo/sa2bo.tsv` | 2,000 | – | TLB |
| bo→sa | `sa-bo/bo2sa.tsv` | 2,000 | – | TLB |
| sa→zh | `sa-zh/sa2zh.tsv` | 2,000 | – | TLB |
| zh→sa | `sa-zh/zh2sa.tsv` | 2,000 | – | TLB |
| bo→zh (Buddhist) | `bo-zh/bo2zh.tsv` | 2,000 | – | TLB |
| zh→bo | `bo-zh/zh2bo.tsv` | 2,000 | – | TLB |
| sa→en | `sa-en/sa2en.tsv`, `sa-en/sa2en-blocks.tsv` | 2,594 | 322 | Mitrasaṃgraha |
| en→sa | `sa-en/en2sa.tsv` | 2,594 | – | Mitrasaṃgraha |
| zh→en | `zh-en/zh2en.tsv`, `zh-en/zh2en-blocks.tsv` | 2,709 | 244 | MITRA-zh-eval |
| bo→en | `bo-en/bo2en.tsv` | 3,979 | 400 | 84000, Khyentse Vision Project, Lotsawa House, Tsadra Foundation |
| bo→fr | `bo-fr/lotsawahouse.tsv` | 2,000 | 200 | Lotsawa House |
| bo→es | `bo-es/lotsawahouse.tsv` | 2,000 | 200 | Lotsawa House |
| bo→de | `bo-de/lotsawahouse.tsv` | 2,000 | 200 | Lotsawa House |
| bo→zh (Modern) | `bo-zh/lotsawahouse.tsv` | 1,660 | 166 | Lotsawa House |
| bo→pt | `bo-pt/lotsawahouse.tsv` | 950 | 95 | Lotsawa House |
| bo→it | `bo-it/lotsawahouse.tsv` | 720 | 72 | Lotsawa House |
| bo→nl | `bo-nl/lotsawahouse.tsv` | 100 | 10 | Lotsawa House |

### Formats

All files are UTF-8, tab-separated, NFC- and whitespace-normalized. Fields are
never quoted: parse them by splitting on tabs (in Python, use
`csv.reader(..., delimiter="\t", quoting=csv.QUOTE_NONE)` or `str.split("\t")`).
Some English references begin or end with a literal `"` character, so a CSV
parser with default quoting will silently merge lines.

- **Two-column files without header** (`sa2bo`, `bo2sa`, `sa2zh`, `zh2sa`,
  `bo2zh`, `zh2bo`, `sa2en`, `en2sa`, `zh2en`): `source<TAB>target`, one
  sentence pair per line.
- **`sa-en/sa2en-blocks.tsv`** (header `work, block_id, block_pos, sa, en`):
  one paragraph per row, the native pseudo-paragraph test split of
  Mitrasaṃgraha (contiguous consecutive sentences of one work).
- **`zh-en/zh2en-blocks.tsv`** (header `work, translator, source_file,
  block_id, block_pos, source_line, zh, en`): blocks of consecutive sentence
  pairs of one text (`source_line` is the 0-based position within that text).
  Blocks have 10 rows; 14 blocks are longer (11–21 rows) because a quotation
  spanning several sentences was kept together with its block.
- **Lotsawa House files** (header `work, translator, source_file, block_id,
  block_pos, source_line, bo, <lang>`): 10 strictly consecutive pairs per
  block (`block_id`), never crossing a document; `translator` records the
  translation team.
- **`bo-en/bo2en.tsv`** (header `subset, package_id, bo, en`): four
  collections (`84000`, `Khyentse_Vision_Project`, `Lotsawa_House`,
  `Tsadra_Foundation`), 100 packages each of ~10 consecutive sentences.
  Paragraph-level evaluation joins the rows of one `(subset, package_id)`.

Paragraph-level evaluation joins the sentences of a block with `\n` on both
sides and translates the block as one unit.

## Construction

- **TLB**: sentence pairs sampled (seed 42) from the manually aligned
  multilingual editions of the Thesaurus Literaturae Buddhicae (Bibliotheca
  Polyglotta, University of Oslo), after filtering of editorial marks,
  folio/line references and verse numbers, and script checks. The two
  directions of a pair are disjoint halves of one 4,000-pair sample.
- **Mitrasaṃgraha**: the test split of the Mitrasaṃgraha Sanskrit–English
  dataset, restricted to pairs not occurring in the MITRA-MT training data,
  split by parity in document order into disjoint halves for sa→en and
  en→sa. Paragraphs are the dataset's native pseudo-paragraph test split.
- **MITRA-zh-eval**: the published Buddhist Chinese→English benchmark of the
  first MITRA release (32 canonical texts); blocks are consecutive sentences
  of one text.
- **bo→en**: 100 packages of ~10 consecutive sentences from each of four
  translation projects (84000, Khyentse Vision Project, Lotsawa House, Tsadra
  Foundation), allowing a per-collection breakdown.
- **Lotsawa House bo→X**: sampled only from natively interleaved pages
  (human paragraph-by-paragraph alignment); modern liturgical/devotional
  register with terse Tibetan verse lines. Scraped and redistributed with
  permission of Lotsawa House; site license CC BY-NC 4.0.

All training data of MITRA-MT and the MITRA-parallel v2 corpus were
decontaminated against every sentence of this suite (normalized substring
matching; see `../README.md`).

## Attribution

Please respect the terms of the original sources when reusing the reference
translations: Thesaurus Literaturae Buddhicae (University of Oslo),
Mitrasaṃgraha, 84000, Khyentse Vision Project, Lotsawa House (CC BY-NC 4.0),
Tsadra Foundation. Citation follows the repository root README.
