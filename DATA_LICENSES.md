# Data licences

The code in this repository is under the MIT licence (see `LICENSE`).
The following data is derived from public sources and retains its own
licence, so it is **not** MIT:

| File | Source | Licence |
|------|--------|---------|
| `training/facts/geo2.tsv` (languages, currencies, demonyms, landlocked) | [mledoze/countries](https://github.com/mledoze/countries) | [ODC Open Database License (ODbL) 1.0](https://opendatacommons.org/licenses/odbl/1-0/) |
| `training/facts/geo3.tsv` (subregions, borders, web domains) | [mledoze/countries](https://github.com/mledoze/countries) | ODbL 1.0 |
| `training/facts/elements.tsv` (symbols, atomic numbers, kinds, phases) | [Bowserinator/Periodic-Table-JSON](https://github.com/Bowserinator/Periodic-Table-JSON) | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) |
| `training/osm/` data and documentation (not `train.py`) | [OpenStreetMap Wiki contributors](https://wiki.openstreetmap.org/); per-file sources in `training/osm/SOURCES.tsv` | [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/); see `training/osm/LICENSE.md` |

`training/geo2.py` and `training/extra_facts.py` rebuild these files from the
original datasets (download them into `training/mledoze/` and
`training/ptable/`).

Except for copies of the OSM-derived data, all other fact files
(`training/facts/*.txt`, the other `.tsv` files and
`training/raw/`) were written for this project and are under the MIT licence.

The trained network (`dos/TINY.BIN`, `training/tiny2.pt`) was trained partly
on the data above. Contains information from mledoze/countries, which is made
available under the ODbL, and from Periodic-Table-JSON (CC BY-SA 3.0).

The separate OSM dataset has not been used to retrain the released network.
