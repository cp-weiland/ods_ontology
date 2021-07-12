# ods_ontology
draft ontology for openDS break discussion 2021/07/12

A simple draft ods ontology for the DiSSCo Prepare as a demo and starting point for the ODS breakout sessions.

This is based on ongoing JSON-LD work: <https://github.com/hardistyar/openDS/blob/json-schemas/json-examples-and-schemas/digital-specimen-object/basic-json-example3.md>

Create the ontology:

```python
python create_ods_ont.py
```

Provides an

```ods.owl```

file, which is currently converted to JSON-LD with protege (output can pretty printed with a onliner)

```python
python format_ods.py ods.json.owl > ods.json
```

