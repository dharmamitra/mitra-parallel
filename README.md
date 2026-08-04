# MITRA-parallel

Parallel corpora of classical Buddhist literature, mined and released by the
[Dharmamitra](https://dharmamitra.org) project.

- **[`v2/`](v2/)** — current release (2026): trilingual Sanskrit–Tibetan,
  Sanskrit–Chinese, and Chinese–Tibetan corpus of 1,693,730 aligned records
  (2,338,400 segment pairs), mined with a pivot-free embedding-based
  span-mining pipeline, decontaminated against the published evaluation
  suite, and exactly deduplicated. See [`v2/README.md`](v2/README.md) for
  statistics, record schema, and cleaning details.
- **[`v1/`](v1/)** — the previous release (1.74M sentence pairs) together
  with the multilingual retrieval evaluation benchmarks
  ([`v1/eval/`](v1/eval/)).

Fine-tuned translation and embedding models are available in the
[MITRA Qwen3.5 collection](https://huggingface.co/collections/buddhist-nlp/mitra-qwen35-2026)
on Hugging Face. The parallel data can be explored interactively at
[dharmamitra.org/db](https://dharmamitra.org/db).
