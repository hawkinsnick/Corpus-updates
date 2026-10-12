---
layout: post
title: "The corpus project: what all 18 projects can do today"
date: 2026-10-12 16:36:00 -0500
categories: [project, overview]
summary: "A researcher’s guide to every corpus, its present evidence, and the master AI skill."
---

The ancient scripts corpus initiative builds traceable reference corpora and practical research tools for ancient writing. Its goal is to bring scattered source records, bibliographic references, editorial disagreements, and computational workflows into an inspectable framework. Researchers should be able to find the evidence behind a claim, understand its limitations, and reproduce the permitted analysis.

The collection currently registers **18 projects**, covering deciphered languages, undeciphered scripts, individual artefacts, and disputed classifications. Shared software architecture does not imply that these writings are linguistically related. The Egyptian hieroglyphic and LightroomIsSlow projects are separate.

**Status date: 12 October 2026.** This overview describes published main-branch documentation checked for this post. It does not include pending branch work. Counts preserve their native units: catalogue entries, editorial rows, sign slots, and source assertions cannot be summed as independent ancient inscriptions. The source snapshots behind this overview are linked under every section.

## Start with the master AI skill

- [Start here: download, upload, and ask a first question](https://github.com/hawkinsnick/Linear-A/blob/main/combined-ai-skill/START-HERE.md)
- [Master AI skill and researcher guide](https://github.com/hawkinsnick/Linear-A/blob/main/combined-ai-skill/README.md)
- [Starter downloads](https://github.com/hawkinsnick/Linear-A/blob/main/combined-ai-skill/downloads/README.md)
- [Choose a corpus and its evidence bundle](https://github.com/hawkinsnick/Linear-A/blob/main/combined-ai-skill/CORPUS-DOWNLOADS.md)
- [Master governing instructions](https://github.com/hawkinsnick/Linear-A/blob/main/combined-ai-skill/SKILL.md)

The master skill routes questions to the relevant individual corpus skills and evidence, preserves provenance and rights, and checks whether a cross-corpus comparison is justified. It can help with source tracing, coverage questions, reproducible queries, and identifying missing evidence. It does not decipher undeciphered texts or turn incompatible data into comparable observations.

Download the starter and supply it to your AI assistant, then add the member evidence needed for your question. The starter contains instructions and a directory, not all corpus data; uploading it does not automatically give an assistant GitHub access. Check that the assistant can read the supplied files and that the evidence bundle matches the corpus state.

## The corpora

### Linear A

Linear A is our research platform for the undeciphered writing of Bronze Age Crete. It is intended for tracing sign sequences, source-defined groups, administrative patterns, and competing scholarly assertions without treating a proposed interpretation as a translation.

Today its documented SigLA-derived baseline contains 802 documents, 5,144 sign attestations, and 1,401 source-defined Word objects, including 1,283 nonempty ones. Researchers can search documents and signs, examine keyword-in-context and co-occurrence patterns, export attributed records, and run explicitly defined accounting models. The added layout view preserves source rectangles rather than certified physical geometry. Known-answer linguistic calibration has not been executed; source rights, independent evidence, and epigraphic review remain open. We do not have permission to redistribute GORILA material.

[Repository](https://github.com/hawkinsnick/Linear-A) · [Individual AI skill](https://github.com/hawkinsnick/Linear-A/blob/main/ai-skill/SKILL.md) · [Documentation snapshot used here](https://github.com/hawkinsnick/Linear-A/blob/01d8e8bf1d21f59081edcc8a13a7d60a7a43e05b/README.md)

### Linear B

Linear B provides the deciphered Mycenaean Greek reference needed to test methods before applying them to undeciphered material. Its role includes organising source transcriptions and preparing controlled experiments with observation data kept separate from linguistic answer keys.

The authenticated DĀMOS mapping covers 5,932 digital records, with 5,890 nonempty transcription surfaces and 42 missing or empty surfaces. Researchers can inspect pinned records and metadata, use the evidence workbench, and prepare source-preserving exports. The real observation package exists, but the required linguistic annotation package and authoritative graphical baseline remain source-delivery dependencies. No linguistic calibration performance is claimed.

[Repository](https://github.com/hawkinsnick/Linear-B) · [Individual AI skill](https://github.com/hawkinsnick/Linear-B/blob/main/ai-skill/SKILL.md) · [Documentation snapshot used here](https://github.com/hawkinsnick/Linear-B/blob/8fe16f1fef876ba45dfafa9f26a0538073cd7365/README.md)

### Cretan hieroglyphs

This corpus organises Cretan Hieroglyphic catalogue identities, sign registries, contextual assertions, and edition-specific reading versions. It helps researchers see which evidence is available for an entry and which comparisons still require primary sources.

Today all 331 CHIC catalogue identities have review dossiers. The published layer includes 234 contextual assertions on 26 identities, 13 reading versions on six identities, and 193 dependent DBAS catalogue leads. Researchers can inspect context and bibliography, compare attributed reading versions, and trace unresolved apparatus and identity questions. These are partial readings and discovery leads, not 331 complete transcriptions; independent review and physical-object certification remain absent.

[Repository](https://github.com/hawkinsnick/Cretan-hieroglyphs) · [Individual AI skill](https://github.com/hawkinsnick/Cretan-hieroglyphs/blob/main/ai-skill/SKILL.md) · [Documentation snapshot used here](https://github.com/hawkinsnick/Cretan-hieroglyphs/blob/4b80f38ca02788b18a3806d6016405551259728b/README.md)

### Cypro-Minoan

Cypro-Minoan supports source-critical work on the undeciphered Bronze Age Cypriot script. It separates controlled catalogue labels, richer object records, source-attributed sign occurrences, and disputed interpretations so researchers can inspect evidence without silently harmonising competing editions.

The published corpus has 254 controlled catalogue slots, 21 rich records, and 16 source-attributed occurrence assertions. Researchers can explore dossiers, inspect inventory and edition joins—including nine exact Louvre inventory/edition assertions—and export the partial occurrence layer through a tested EpiDoc view. The primary Tiryns context remains qualified. Complete transcriptions, comprehensive palaeographic variants, and independent scholarly acceptance remain open; catalogue slots are not independently verified physical objects.

[Repository](https://github.com/hawkinsnick/Cypro-Minoan) · [Individual AI skill](https://github.com/hawkinsnick/Cypro-Minoan/blob/main/ai-skill/SKILL.md) · [Documentation snapshot used here](https://github.com/hawkinsnick/Cypro-Minoan/blob/fbc718ae5103575223a947c09c6daf7d2777421c/README.md)

### Phaistos Disc

The Disc corpus is a focused workbench for one object with two faces. It is designed for inspecting graphical groups, source disagreements, traversal choices, and the effect of unknown marks on descriptive analysis.

Today it exposes 61 source-delimited graphical groups and 242 project-transcribed occurrence slots: 241 identified and one erased or unknown. Researchers can navigate the offline workbench, inspect source-linked apparatus and photographic comparisons, and replay descriptive statistics and sensitivity scenarios. The historical edition's reported total of 241 remains visible alongside the project's graphical-slot count. Groups are not presumed words, no sound values are assigned, and final independent acceptance of the 2.0 release candidate remains blocked.

[Repository](https://github.com/hawkinsnick/Phaistos-Disc) · [Individual AI skill](https://github.com/hawkinsnick/Phaistos-Disc/blob/main/ai-skill/SKILL.md) · [Documentation snapshot used here](https://github.com/hawkinsnick/Phaistos-Disc/blob/1941c5631f72b1108374cfc3587b9ff4d9800c65/README.md)

### Byblos syllabary

This corpus is a source and catalogue workspace for the undeciphered Byblos script. The conventional name “syllabary” does not establish its sign values or language affiliation. Its practical purpose is to reconcile reported entries, surfaces, counts, type labels, and edition relationships before admitting text for analysis.

Today it records 14 reported core entries and 25 disputed candidates, with a searchable catalogue, source ledger, comparison tools, and review packets. The stele-a review examines 123 source drawing positions, while the separate type-table layer preserves competing classifications. Researchers can trace count disagreements and prepare corrections with exact locators. There are zero verified sign sequences and zero independent reviews, so linguistic sequence statistics and proposed decipherments are not supported.

[Repository](https://github.com/hawkinsnick/Byblos-syllabary) · [Individual AI skill](https://github.com/hawkinsnick/Byblos-syllabary/blob/main/ai-skill/SKILL.md) · [Documentation snapshot used here](https://github.com/hawkinsnick/Byblos-syllabary/blob/e928df2b47a2e2c3a3f9c33ae43d01e5098ea825/README.md)

### Cypriot syllabic Greek

This corpus supports research into Greek written in the Cypriot syllabary. It preserves the IG XV 1 digital edition and distinguishes ancient syllabic transliteration, Greek interpretation, modern translation, and uncertain language classification.

The snapshot has 593 retrieved source entries, 592 parsed records, and one unchanged malformed response in quarantine. Its admitted source-interpreted Greek subset has 170 records; conservative frequency analysis counts 1,341 clear sign tokens on 149 entries. Researchers can search, inspect XML, reproduce subset statistics, and export records. A separate geographic discovery register adds 210 squeeze-catalogue identifiers without admitting new readings. This is not all Cypriot syllabic Greek: the Idalion tablet is outside the snapshot, and digital subentries are not certified objects.

[Repository](https://github.com/hawkinsnick/Cypriot-syllabic-Greek) · [Individual AI skill](https://github.com/hawkinsnick/Cypriot-syllabic-Greek/blob/main/ai-skill/SKILL.md) · [Documentation snapshot used here](https://github.com/hawkinsnick/Cypriot-syllabic-Greek/blob/fe81f05d8aa8451bed409bb04e3171b180aa9495/README.md)

### Eteocypriot

Eteocypriot isolates source-attributed non-Greek Cypriot material from Greek parallels and uncertain classifications. It is intended for careful comparison of editorial components and historical correspondences while keeping the language's interpretation unresolved.

Of 26 selected candidate responses, 25 parse into 29 source components. Seventeen entries carry source-attributed Eteocypriot classifications, represented by 18 components; uncertain and Greek parallel components are excluded from Eteocypriot analysis. Researchers can search, inspect bilingual component boundaries, export attributed data, and reproduce the conservative clear-label frequency subset. These records share an upstream witness with the Cypriot Greek project; copying them into a second repository does not create independent evidence or a new decipherment.

[Repository](https://github.com/hawkinsnick/Eteocypriot) · [Individual AI skill](https://github.com/hawkinsnick/Eteocypriot/blob/main/ai-skill/SKILL.md) · [Documentation snapshot used here](https://github.com/hawkinsnick/Eteocypriot/blob/71e8551b1f520d7ad9bc33f4861ea8aefef68a9b/README.md)

### Eteocretan

Eteocretan is a source and reading archive for non-Greek Cretan inscriptions and disputed candidates. It is useful for tracking alternative reading versions, historical edition genealogy, classification conflicts, and object context without forcing agreement.

Today the archive distinguishes eight named inscriptions, twelve reading versions, and 101 source-text rows. Researchers can search the permitted evidence, compare attributed versions, inspect source-reconciliation dossiers and Dreros context, and prepare source-bound review material. Zero rows or tokens are analytically admitted: searchability does not make excluded readings eligible for frequency analysis. Further critical-edition reconciliation, reuse rights, object identity, and specialist adjudication remain separate gates.

[Repository](https://github.com/hawkinsnick/Eteocretan) · [Individual AI skill](https://github.com/hawkinsnick/Eteocretan/blob/main/ai-skill/SKILL.md) · [Documentation snapshot used here](https://github.com/hawkinsnick/Eteocretan/blob/6c581711fd0932c22993981e1bc0b1709efdd0ae/README.md)

### Lycian and Carian

This repository provides a partitioned Anatolian reference corpus for Lycian and Carian, with a separately labelled Milyan source partition. It supports inspection of source readings and metadata while preserving language boundaries and editorial uncertainty.

The frozen eDiAna snapshot contains 453 digital catalogue entries: 264 Carian, 187 Lycian, and two Milyan. Researchers can browse, query and export the source-attributed layers, follow edition dependencies, and inspect the declared exclusions and analytical eligibility rules. Catalogue entries do not equal physical monuments, and this snapshot is neither a worldwide census nor an independently verified critical edition. The Milyan partition overlaps the dedicated Milyan project and must not be counted as new evidence.

[Repository](https://github.com/hawkinsnick/Lycian-and-Carian) · [Individual AI skill](https://github.com/hawkinsnick/Lycian-and-Carian/blob/main/ai-skill/SKILL.md) · [Documentation snapshot used here](https://github.com/hawkinsnick/Lycian-and-Carian/blob/88a0346c7a4530bd45ef25c062f06c345f7cc812/README.md)

### Milyan (Lycian B)

The dedicated Milyan corpus gives this language its own evidence model and researcher interface. Milyan and “Lycian B” name the same language here; Milyan is kept distinct from Lycian A.

Today two frozen eDiAna catalogue records supply 114 source text rows across three provisional segments on two reported monuments. Researchers can explicitly query the reference layer, use keyword-in-context and exports, inspect source crosswalks, and follow exact primary-edition locators. Canonical verified readings and independent reviews remain zero. The TL 55 discrepancy—nine digital rows versus a historical eight-line description—is retained rather than silently resolved. Structural fleet admission does not establish a scholarly text-level release.

[Repository](https://github.com/hawkinsnick/Milyan-Lycian-B) · [Individual AI skill](https://github.com/hawkinsnick/Milyan-Lycian-B/blob/main/ai-skill/SKILL.md) · [Documentation snapshot used here](https://github.com/hawkinsnick/Milyan-Lycian-B/blob/1cba0dfe51a33f3aea6e4171e3a11409222ff1fe/README.md)

### Phrygian

Phrygian is intended for source-attributed research across Old, Middle, and Neo-Phrygian material. Its architecture keeps linguistic reference annotations separate from epigraphically verified text, and retains source directionality, editorial interventions, and edition dependence.

Today the licensed UD Phrygian-KUL reference snapshot supplies 203 sentences, 1,921 tokens, and 162 distinct Trismegistos identifiers. Researchers can query and export that attributed reference, inspect source genealogy and catalogue reconciliation, and use the Kerkenes metadata crosswalk and reference EpiDoc export. The canonical epigraphic layer remains empty pending source-level verification. Linguistic reference tokens are not independently checked ancient sign occurrences, and shared edition ancestry is not replication.

[Repository](https://github.com/hawkinsnick/Phrygian) · [Individual AI skill](https://github.com/hawkinsnick/Phrygian/blob/main/ai-skill/SKILL.md) · [Documentation snapshot used here](https://github.com/hawkinsnick/Phrygian/blob/c95062b725b9a0ecaeb2b627c25ede045e00c8ec/README.md)

### Anatolian Hieroglyphic

This project organises Anatolian, or Luwian, Hieroglyphic inscription evidence. Its present strength is catalogue identity, object classification, chronology, and bibliography; it separates those assertions from sign readings and linguistic interpretation.

All 287 eDiAna digital entries now have identity and bibliography dossiers. These include 274 bibliographic assertions on 262 entries, 32 object classes, and 118 secondary period candidates, with a period conflict retained. Researchers can query and export the full dossier view and inspect internal references, notices, unknown classes, and unverified edition locators. These are digital entries, not a certified object census or complete critical transcription; protected edition readings and direct scholarly collation remain outside the current layer.

[Repository](https://github.com/hawkinsnick/Anatolian-Hieroglyphic) · [Individual AI skill](https://github.com/hawkinsnick/Anatolian-Hieroglyphic/blob/main/ai-skill/SKILL.md) · [Documentation snapshot used here](https://github.com/hawkinsnick/Anatolian-Hieroglyphic/blob/277321ab9a45ad67e810eaba03df8545b90584d2/README.md)

### Archanes Script

Archanes focuses on early Cretan writing evidence and the so-called Archanes Formula. Its purpose is to make competing corpus definitions, signaries, and formula models inspectable rather than presume that scholarship recognises one independent script.

Today the repository preserves Decorte's 16-object authority corpus alongside competing script models and authority-specific signaries and formula patterns. Researchers can use its browser, API and exports to inspect attributed classifications, source lineage, and disagreements. The corpus does not establish a consensus Archanes script or automatically merge its objects into Cretan Hieroglyphic or Linear A. Cross-repository links require identity and dependence checks before counting or comparison.

[Repository](https://github.com/hawkinsnick/Archanes-Script) · [Individual AI skill](https://github.com/hawkinsnick/Archanes-Script/blob/main/ai-skill/SKILL.md) · [Documentation snapshot used here](https://github.com/hawkinsnick/Archanes-Script/blob/71f33a770fcd4e6c1c4747177cb64978390ed27a/README.md)

### Aegean anomalous inscriptions

This is a controlled comparison and quarantine workspace for Aegean objects whose writing status or script classification is disputed. It does not propose an “Aegean anomalous language” or a unified anomalous writing system.

Researchers can inspect source-attributed classification disagreements and provenance around anchors such as the Arkalochori Axe and Malia Altar Stone, using read-only queries, exports, and explicit home-corpus cross-references. The Phaistos Disc remains in its own project. Zero canonical script claims is intentional: a useful comparison record is not an admission that marks are writing, a linguistic identification, or an extra independent witness.

[Repository](https://github.com/hawkinsnick/Aegean-anomalous) · [Individual AI skill](https://github.com/hawkinsnick/Aegean-anomalous/blob/main/ai-skill/SKILL.md) · [Documentation snapshot used here](https://github.com/hawkinsnick/Aegean-anomalous/blob/9433be788a5e978852c89ac9354871ae3ead4ef2/README.md)

### Lydian

Lydian provides an attributed digital reference for inscription research. It is designed for following source readings, uncertainty, bibliography, and unresolved identities back to the eDiAna capture and its underlying edition genealogy.

Today its frozen reference has 118 digital document records and 471 nonempty source rows. Researchers can search the admitted layer, use read-only queries and loss-aware exports, inspect source-bound review packets, and obtain a reversible EpiDoc reference view. The source and its derived reference retain CC BY-SA terms. Direct critical-edition collation and independent epigraphic acceptance remain pending; dependent eDiAna, TITUS, and edition readings are not separate confirmations.

[Repository](https://github.com/hawkinsnick/Lydian) · [Individual AI skill](https://github.com/hawkinsnick/Lydian/blob/main/ai-skill/SKILL.md) · [Documentation snapshot used here](https://github.com/hawkinsnick/Lydian/blob/192d53d5a316625055927111f549c2ccf1392343/README.md)

### Sidetic

Sidetic is a compact reference project for the inscriptional evidence associated with Side. It keeps source readings and competing sign-value proposals attributable, allowing researchers to examine disagreements without replacing them with an invented canonical decipherment.

The frozen eDiAna reference contains 11 digital document records and 32 nonempty rows, with a reversible EpiDoc view, browser, queries, exports, and record-level review packets. Researchers can distinguish that frozen reference from the later publication frontier and inspect numbering and sign disagreements. New finds are not silently renumbered, source copies are not independent witnesses, and primary-edition and specialist review remain open.

[Repository](https://github.com/hawkinsnick/Sidetic) · [Individual AI skill](https://github.com/hawkinsnick/Sidetic/blob/main/ai-skill/SKILL.md) · [Documentation snapshot used here](https://github.com/hawkinsnick/Sidetic/blob/9bda1ff5d14b98d431f81c0dbb76bf169a091536/README.md)

### Pisidian

Pisidian supplies a source-attributed digital reference for researching its inscriptional records, source readings, and bibliography. It follows the same separation between digital catalogue evidence, object identity, editorial claims, and later scholarly interpretation.

Today the frozen eDiAna reference offers 54 digital document records and 99 nonempty source rows. Researchers can inspect the records and upstream snapshot, reproduce the reference build, export a reversible EpiDoc view, and prepare source-bound expert-review packets. This is an attributed digital layer rather than a newly collated critical edition; complete raw-source annotations, physical geometry, and independent acceptance remain outside its scope.

[Repository](https://github.com/hawkinsnick/Pisidian) · [Individual AI skill](https://github.com/hawkinsnick/Pisidian/blob/main/ai-skill/SKILL.md) · [Documentation snapshot used here](https://github.com/hawkinsnick/Pisidian/blob/b5f40b7b8e4d58ba0c75963f8942b0d61ccfb82f/README.md)

## What the collection can do together

The shared platform helps researchers find and inspect each member's admitted evidence, organise review work, and compare coverage and methods without erasing source-specific restrictions. The [mega-corpus tooling](https://github.com/hawkinsnick/Linear-A/blob/main/corpus-factory/MEGA-CORPUS.md) materialises declared native views with provenance and component rights retained. Its heterogeneous, overlapping view rows are not a pooled linguistic dataset or a count of unique inscriptions. Restricted source-dependent packages are not automatically public downloads.

## Standards, rights, and what remains

Software validation checks declared behaviour and data integrity. It does not independently certify readings, physical identities, chronology, sign values, or a decipherment. Further source access, lawful reuse, source delivery, primary reconciliation, and independent scholarly review remain distinct tasks. We aim to finish the permitted preparatory work before asking specialists to adjudicate it; this post does not claim that every member has reached an expert-only stopping point.

Project-original content and code use attribution and noncommercial licensing as documented in each repository. Imported components retain their own upstream terms, including applicable CC BY, CC BY-SA, and CC BY-NC-SA obligations; project terms do not override those grants. We do not have permission to redistribute GORILA material. An online reference, a bibliography entry, or access to a book does not establish redistribution permission.

This blog describes the published tools and evidence. The individual repositories remain authoritative for their records and current gates, and every corpus change must carry matching documentation and individual/master AI skill updates.
