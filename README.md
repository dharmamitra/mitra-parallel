![MITRA Logo](dm-logo-full.avif)

# MITRA-parallel: A Large-Scale Parallel Corpus for Sanskrit, Buddhist Chinese, and Tibetan

[![arXiv](https://img.shields.io/badge/arXiv-2024.XXXX-blue)](https://github.com/dharmamitra/mitra-semantic-similarity)

## Overview

**MITRA-parallel** is a large-scale, sentence-aligned parallel corpus for Sanskrit, Buddhist Chinese, and Tibetan. The dataset is designed to support research in machine translation, semantic retrieval, and philological studies of Buddhist and classical Asian literature. It is introduced in the paper:

> **MITRA: A Large-Scale Parallel Corpus and Multilingual Pretrained Language Model for Machine Translation and Semantic Retrieval for Pāli, Sanskrit, Buddhist Chinese, and Tibetan**  
> Sebastian Nehrdich, Kurt Keutzer  
> [arXiv preprint](https://github.com/dharmamitra/mitra-semantic-similarity)

The MITRA framework includes:
- A novel pipeline for multilingual parallel passage mining (MITRA-parallel)
- A corpus of 1.74 million parallel sentence pairs between Sanskrit, Chinese, and Tibetan
- Domain-specific pretrained language models (Gemma 2 MITRA) for translation and semantic retrieval

## Data Structure

The parallel data is provided in the `mitra-parallel/tsv/` directory as `.tsv` files. Each file contains sentence-level alignments between two ancient Buddhist languages. The typical columns are:

- `src_segmentnr`: Source segment identifier
- `src_original`: Source sentence (e.g., Sanskrit, Chinese, or Tibetan)
- `tgt_segmentnr`: Target segment identifier
- `tgt_original`: Target sentence (aligned translation)

Example (tab-separated):
```
src_segmentnr	src_original	tgt_segmentnr	tgt_original
XXn693u_007:1	 namo buddhāyaḥ |	T02D2243:122b-4	སངས་རྒྱས་ལ་ཕྱག་འཚལ་ལོ་༎
```

## Pretrained Models

The MITRA project also provides three models, one base model and two finetuned models for semantic retrieval and translation:

- **Gemma 2 MITRA** (base model)
- **Gemma 2 MITRA-MT** (machine translation)
- **Gemma 2 MITRA-E** (semantic embedding)

**Model links:**

- [Gemma 2 MITRA on HuggingFace](https://huggingface.co/buddhist-nlp/gemma-2-mitra)
- [Gemma 2 MITRA-MT on HuggingFace](https://huggingface.co/buddhist-nlp/gemma-2-mitra-it)
- [Gemma 2 MITRA-E on HuggingFace](https://huggingface.co/buddhist-nlp/gemma-2-mitra-e)

## Citation
If you use this dataset or models, please cite:

```
@article{nehrdich2024mitra,
  title={MITRA: A Large-Scale Parallel Corpus and Multilingual Pretrained Language Model for Machine Translation and Semantic Retrieval for Pāli, Sanskrit, Buddhist Chinese, and Tibetan},
  author={Sebastian Nehrdich and Kurt Keutzer},
  journal={arXiv preprint},
  year={2024},
  url={https://github.com/dharmamitra/mitra-semantic-similarity}
}
```

## Acknowledgments
- The MITRA project is supported by the [Tsadra Foundation](https://tsadra.org), and collaborative partners including [monlam.ai](http://monlam.ai) and the [https://khyentsefoundation.org/kf-projects/kumarajiva-project/](Kumarajiva project).
- For more information and updates, see the [project website](http://dharmamitra.org) 

## License
The MITRA-parallel dataset is released under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0). This means you are free to:
- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:
- Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made
- ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original

For more details, see the full [LICENSE](LICENSE) file. 