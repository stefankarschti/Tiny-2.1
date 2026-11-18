# Dataset license and attribution

The files in `facts/` are adaptations of text by **OpenStreetMap Wiki
contributors**, licensed under the
[Creative Commons Attribution-ShareAlike 2.0 Generic license](https://creativecommons.org/licenses/by-sa/2.0/).
The [legal code](https://creativecommons.org/licenses/by-sa/2.0/legalcode)
provides the license terms.

Each fact file names its source page. `SOURCES.tsv` maps every file to the
original page and its contributor history. Sources were consulted on
2026-11-17; the URLs are live references, not pinned revision snapshots.

Changes made for this project: selected mapping concepts were paraphrased
into short English answers, paired with three question phrasings, grouped by
topic, and restricted to printable ASCII and TINY's context length. No wiki
images or geographic database extracts are included. This is an unofficial
adaptation with no implied endorsement by the original contributors.

The adapted fact files are distributed under CC BY-SA 2.0, **not the
repository's MIT code license**. Retain this attribution and source manifest
when copying or redistributing them. Copies staged in another training
directory retain the same license. Original documentation and metadata in
this folder are also offered under CC BY-SA 2.0. The `train.py` program is
original project code under the repository's MIT license.

The wiki's [content license](https://wiki.openstreetmap.org/wiki/Wiki_content_license)
is the basis for this attribution. The OSM geographic database's ODbL license
does not replace the wiki text license. No claim is made here about the
license of future trained weights; retain the training-data provenance when
publishing a model trained on this material.

The 2026-11-18 expansion incorporates English tag descriptions by
OpenStreetMap Wiki contributors retrieved through Taginfo. Each tag record
in `facts/osm_tag_dictionary.txt` links to the source wiki page, also listed
in `TAG_SOURCES.tsv`. The descriptions retain their source wording. The
questions are new adaptations under the same CC BY-SA 2.0 license.
The original topic files received additional training paraphrases.
The comparison script is project code under the repository's MIT license.
