llama.cpp szerverek indítása:

```bash
./server -m ../kmdb_keyword_generation-q4_0.gguf --port 8086
```

```bash
./server -m ../qlora-combined_people_institution-7b-v1.0.0-q4_0.gguf --port 8087
```

spacy api indítása:

```bash
uvicorn spacy_api:app --reload
```

bert api indítása:

```bash
python bert_api.py
```
