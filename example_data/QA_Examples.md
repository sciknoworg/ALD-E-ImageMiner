# ALD/MLD Image Annotation – Question Types, Answer Types, and Examples

This document defines the four question types for **Materials Science (ALD/E images)**, adapted from prior QA designs in other domains.  
Each type is illustrated with examples tailored to the figures in this project.  
Questions can be answered in **yes/no, factoid, list, or paragraph** format. At least one **paragraph-style answer** (3+ sentences) should be provided per figure.

---

## 1. Process-Oriented Questions
**Purpose:** Test understanding of ALD/MLD cycles, precursor chemistry, and reaction mechanisms.  
**Typical Figures:** Process schematics, reaction diagrams, FRET energy transfer schemes.  

**Examples:**
- Q: *What are the four main steps of the ALD/MLD cycle shown in this schematic, and why is purging essential?*  
  A (list/paragraph): Steps: (1) Precursor pulse, (2) Purge, (3) Co-reactant pulse, (4) Purge. Purging removes unreacted precursors and gaseous byproducts from the chamber. This step is essential because it prevents unwanted chemical reactions, ensuring the self-limiting nature of ALD and maintaining uniform thin film growth.  

- Q: *How does energy transfer between Eu³⁺ and AF 647 enable FRET emission?*  
  A (paragraph): Eu³⁺ ions absorb excitation light near 400 nm and become electronically excited. Instead of emitting directly, Eu³⁺ transfers energy non-radiatively to nearby AF 647 molecules via dipole–dipole interactions. AF 647 then emits at ~660 nm, shifting the emission to a different spectral region and enabling FRET-based bio-detection applications.  

---

## 2. Comparative/Trend Questions
**Purpose:** Probe reasoning about experimental variables (e.g., temperature, pulse length, cycles) and their impact on outcomes (growth rate, thickness, emission intensity).  
**Typical Figures:** Growth-per-cycle plots, thickness vs cycles, publication trends, efficiency curves.  

**Examples:**
- Q: *How has the number of ALD publications changed since 2000, and when did ALD/MLD publications first appear?*  
  A (paragraph): The number of ALD publications increased steadily after 2000, reflecting growing interest in thin film deposition techniques. Around 2010, the publication rate accelerated, signaling the field’s maturation and broader adoption in industry. ALD/MLD papers appeared after 2015 and have been gaining traction, showing that hybrid approaches are becoming an active research frontier.  

- Q: *How does growth per cycle vary with deposition temperature?*  
  A (factoid): GPC decreases from 7.3 Å at 210 °C to 5.4 Å at 240 °C.  

- Q: *What effect does adding an upconversion layer have on solar cell current density compared to the reference cell?*  
  A (paragraph): Adding an upconversion layer increases the short-circuit current density compared to the reference cell. This enhancement occurs because the layer converts infrared photons into visible ones, which can then be absorbed by the active layer. The improvement demonstrates the potential of rare-earth-doped layers to boost solar cell efficiency beyond the conventional absorption limits.  

---

## 3. Structure–Property Questions
**Purpose:** Evaluate ability to connect precursor structures (ligand families, rare earth types) with film properties (thermal stability, growth rates).  
**Typical Figures:** Precursor chemical families, periodic table coverage, box plots of source temperatures.  

**Examples:**
- Q: *Which ligand families are most commonly used for Eu and Ce precursors?*  
  A (list): Eu – diketones, amidinates; Ce – diketones, alkoxides.  

- Q: *Which precursor ligand class exhibits the lowest median source temperature?*  
  A (factoid): Amidinate ligands (R(amd)₃).  

- Q: *Which oxidant leads to the lowest growth per cycle for Y precursors?*  
  A (factoid): O₂ plasma.  

---

## 4. Application/Performance Questions
**Purpose:** Assess reasoning about device-relevant outcomes (luminescence spectra, CIE color coordinates, solar cell efficiencies).  
**Typical Figures:** Emission spectra, CIE chromaticity diagrams, device schematics with J–V curves.  

**Examples:**
- Q: *How does Tb₂O₃ doping ratio affect EL intensity in Al₂O₃:Tb₂O₃ devices?*  
  A (paragraph): Increasing the Tb₂O₃ doping ratio improves EL intensity up to an optimal concentration, typically around a 4:4 ratio. At lower ratios, the luminescence is weaker due to insufficient activator ions. At higher ratios, concentration quenching occurs, leading to reduced performance despite the higher dopant level.  

- Q: *How do the emission colors of ALD/MLD thin films compare to LED and incandescent lamps?*  
  A (paragraph): ALD/MLD films typically emit in the green region of the spectrum, similar to the output of LEDs and fluorescent lamps. This overlap suggests their potential use in solid-state lighting and display technologies. However, their emission is distinct from incandescent lamps, which have a warmer, broad-spectrum output, highlighting the unique advantages of thin-film phosphors.  

- Q: *What performance advantage is shown when emission intensity is enhanced by a plasmonic substrate?*  
  A (paragraph): The plasmonic substrate significantly amplifies the red emission from Eu-HQA films, making the signal brighter and more detectable. This enhancement arises from localized surface plasmon resonance, which boosts the excitation and emission processes. The result is a stronger photoluminescence output, which can be particularly advantageous for bio-detection applications where sensitivity is critical.  

---

## Figure–Question/Answer Mapping

| Figure No. | Main Content | Question Types | Suggested Answer Types | Example Question | Example Answer |
|------------|--------------|----------------|------------------------|-----------------|----------------|
| **[figure 1](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_1.jpg)** | Publication counts per year (ALD vs ALD/MLD) | Comparative/Trend | Paragraph | How has the number of ALD publications changed since 2000? | The number of ALD publications has grown steadily since 2000, showing the technology’s rising importance. Around 2010, growth accelerated, suggesting increased industrial and academic adoption. ALD/MLD publications began after 2015, marking the emergence of hybrid approaches as a significant subfield. |
| **[figure 2](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_2.jpg)** | ALD & ALD/MLD cycle schematic | Process-Oriented | List; Paragraph | What are the four main steps of the ALD/MLD cycle? | The ALD/MLD cycle consists of four steps: precursor pulse, purge, co-reactant pulse, and purge. Each step is self-limiting and ensures atomic-scale control of film thickness. Purging in particular is critical, as it removes unwanted gases and prevents uncontrolled reactions. |
| **[figure 3](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_3.jpg)** | GPC vs T, pulse length, cycles | Comparative/Trend | Factoid; Paragraph | How does GPC change with temperature? | Growth per cycle decreases as the temperature increases from 210 °C to 240 °C. This reduction is due to lower surface reactivity at elevated temperatures. It highlights the importance of optimizing process windows to achieve desired film growth. |
| **[figure 4](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_4.jpg)** | Precursor families + periodic table | Structure–Property | List | Which ligand families are most used for Eu and Ce? | Eu: diketones, amidinates; Ce: diketones, alkoxides. |
| **[figure 5](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_5.jpg)** | Precursor source temperatures | Structure–Property | Factoid | Which ligand class shows the lowest median source T? | Amidinates. |
| **[figure 6](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_6.jpg)** | GPC of Y precursors | Comparative/Trend; Structure–Property | Factoid; List | Which oxidant gives lowest GPC? | O₂ plasma. |
| **[figure 12](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_12.jpg)** | EL spectra + device schematic | Application/Performance | Paragraph | How does Tb₂O₃ doping affect EL intensity? | The EL spectra show that increasing Tb₂O₃ doping enhances green emission up to an optimal concentration. At lower doping, emission is weaker, while at higher doping, concentration quenching reduces intensity. This trend indicates a balance between dopant activation and quenching is required for device optimization. |
| **[figure 13](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_13.jpg)** | CIE diagram vs lamps | Application/Performance | List; Paragraph | How do film colors compare to LEDs? | The ALD/MLD films emit in the green region, closely aligning with LED and fluorescent sources. This makes them promising for applications in displays and energy-efficient lighting. Their emission differs from incandescent lamps, which cover a broader, warmer spectrum. |
| **[figure 14](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_14.jpg)** | Solar spectrum + upconversion device | Comparative/Trend; Application/Performance | Paragraph | What effect does upconversion layer have on J–V? | The solar cells with an upconversion layer demonstrate higher current density compared to the reference cell. This improvement results from the conversion of sub-bandgap infrared photons into usable visible photons. The outcome confirms the potential of integrating rare-earth upconversion materials into photovoltaic devices for efficiency enhancement. |
| **[figure 15](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_15.jpg)** | FRET schematic + spectra | Process-Oriented; Application/Performance | Paragraph | How does Eu³⁺ → AF 647 transfer enable FRET emission? | Eu³⁺ absorbs light in the UV-visible range and transfers energy non-radiatively to AF 647 molecules. This process enables AF 647 to emit at ~660 nm, effectively shifting the emission to the red. Such FRET interactions demonstrate how ALD/MLD films can be engineered for sensitive bio-detection applications. |

---

## Summary
By covering **Process-Oriented, Comparative/Trend, Structure–Property, and Application/Performance** questions with clear **answer types and examples**, this guide supports consistent, high-quality annotation of ALD/MLD images.  
All **paragraph answers must contain at least 3 sentences** to ensure sufficient reasoning and explanatory detail.
