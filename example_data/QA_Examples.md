# ALD/MLD Image Annotation – Question Types, Answer Types, and Examples

This document defines the four question types for **Materials Science (ALD/E images)**, adapted from prior QA designs in other domains.  
Each type is illustrated with examples tailored to the figures in this project.  
Questions can be answered in **yes/no, factoid, list, or paragraph** format. At least one **paragraph-style answer** should be provided per figure.

---

## 1. Process-Oriented Questions
**Purpose:** Test understanding of ALD/MLD cycles, precursor chemistry, and reaction mechanisms.  
**Typical Figures:** Process schematics, reaction diagrams, FRET energy transfer schemes.  

**Examples:**
- Q: *What are the four main steps of the ALD/MLD cycle shown in this schematic, and why is purging essential?*  
  A (list/paragraph): Steps: (1) Precursor pulse, (2) Purge, (3) Co-reactant pulse, (4) Purge. Purging removes residual gases and ensures self-limiting growth.  
- Q: *How does energy transfer between Eu³⁺ and AF 647 enable FRET emission?*  
  A (paragraph): Eu³⁺ absorbs at ~400 nm and transfers energy non-radiatively to AF 647, which emits at ~660 nm, enabling FRET-based detection.

---

## 2. Comparative/Trend Questions
**Purpose:** Probe reasoning about experimental variables (e.g., temperature, pulse length, cycles) and their impact on outcomes (growth rate, thickness, emission intensity).  
**Typical Figures:** Growth-per-cycle plots, thickness vs cycles, publication trends, efficiency curves.  

**Examples:**
- Q: *How has the number of ALD publications changed since 2000, and when did ALD/MLD publications first appear?*  
  A (paragraph): ALD publications rose steadily after 2000, with strong growth around 2010. ALD/MLD papers appeared post-2015 and are steadily increasing.  
- Q: *How does growth per cycle vary with deposition temperature?*  
  A (factoid): GPC decreases from 7.3 Å at 210 °C to 5.4 Å at 240 °C.  
- Q: *What effect does adding an upconversion layer have on solar cell current density compared to the reference cell?*  
  A (paragraph): Devices with upconversion layers show higher current density, suggesting improved infrared-to-visible conversion efficiency.

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
  A (paragraph): Increasing Tb₂O₃ ratio improves EL intensity up to an optimal 4:4 ratio; beyond that, emission may saturate.  
- Q: *How do the emission colors of ALD/MLD thin films compare to LED and incandescent lamps?*  
  A (list/paragraph): Films emit in the green region, close to LEDs and fluorescents, but distinct from incandescent sources.  
- Q: *What performance advantage is shown when emission intensity is enhanced by a plasmonic substrate?*  
  A (paragraph): The plasmonic substrate amplifies Eu-HQA red emission, improving bio-detection sensitivity.

---

## Figure–Question/Answer Mapping

| Figure No. | Main Content | Question Types | Suggested Answer Types | Example Question | Example Answer |
|------------|--------------|----------------|------------------------|-----------------|----------------|
| **[figure 1](.../figure_1.jpg)** | Publication counts per year (ALD vs ALD/MLD) | Comparative/Trend | Paragraph | How has the number of ALD publications changed since 2000? | Publications increased steadily, peaking ~2010; ALD/MLD appears post-2015. |
| **[figure 2](.../figure_2.jpg)** | ALD & ALD/MLD cycle schematic | Process-Oriented | List; Paragraph | What are the four main steps of the ALD/MLD cycle? | Precursor pulse → Purge → Co-reactant pulse → Purge. |
| **[figure 3](.../figure_3.jpg)** | GPC vs T, pulse length, cycles | Comparative/Trend | Factoid; Paragraph | How does GPC change with temperature? | GPC decreases as temperature increases from 210 °C to 240 °C. |
| **[figure 4](.../figure_4.jpg)** | Precursor families + periodic table | Structure–Property | List | Which ligand families are most used for Eu and Ce? | Eu: diketones, amidinates; Ce: diketones, alkoxides. |
| **[figure 5](.../figure_5.jpg)** | Precursor source temperatures | Structure–Property | Factoid | Which ligand class shows the lowest median source T? | Amidinates. |
| **[figure 6](.../figure_6.jpg)** | GPC of Y precursors | Comparative/Trend; Structure–Property | Factoid; List | Which oxidant gives lowest GPC? | O₂ plasma. |
| **[figure 12](.../figure_12.jpg)** | EL spectra + device schematic | Application/Performance | Paragraph | How does Tb₂O₃ doping affect EL intensity? | Optimal ratios (4:2, 4:4) maximize green emission intensity. |
| **[figure 13](.../figure_13.jpg)** | CIE diagram vs lamps | Application/Performance | List; Paragraph | How do film colors compare to LEDs? | Green region close to LEDs, distinct from incandescent lamps. |
| **[figure 14](.../figure_14.jpg)** | Solar spectrum + upconversion device | Comparative/Trend; Application/Performance | Paragraph | What effect does upconversion layer have on J–V? | Higher current density vs reference, due to IR→visible conversion. |
| **[figure 15](.../figure_15.jpg)** | FRET schematic + spectra | Process-Oriented; Application/Performance | Paragraph | How does Eu³⁺ → AF 647 transfer enable FRET emission? | Eu³⁺ absorbs UV and transfers energy to AF 647, which emits red light. |

---

## Summary
By covering **Process-Oriented, Comparative/Trend, Structure–Property, and Application/Performance** questions with clear **answer types and examples**, this guide supports consistent, high-quality annotation of ALD/MLD images.


## Figure–Question Type Mapping

| Figure No. | Main Content                                               | Applicable Question Types                     |
|------------|------------------------------------------------------------|-----------------------------------------------|
| **[figure 1](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_1.jpg)**      | Publication counts per year (ALD vs ALD/MLD)               | Comparative/Trend                             |
| **[figure 2](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_2.jpg)**      | ALD & ALD/MLD cycle schematic (metal/organic pulses)       | Process-Oriented                              |
| **[figure 3](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_3.jpg)**      | Plots: GPC vs T, GPC vs pulse length, thickness vs cycles  | Comparative/Trend                             |
| **[figure 4](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_4.jpg)**      | Precursor ligand families + periodic table coverage        | Structure–Property                            |
| **[figure 5](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_5.jpg)**      | Box plots of precursor source temperatures by ligand type  | Structure–Property                            |
| **[figure 6](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_6.jpg)**      | GPC of Y precursors vs ligands/oxidants                    | Comparative/Trend; Structure–Property         |
| **[figure 12](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_12.jpg)**     | EL spectra + device schematic + emission images            | Application/Performance                       |
| **[figure 13](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_13.jpg)**     | CIE chromaticity diagram vs lamp standards                 | Application/Performance                       |
| **[figure 14](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_14.jpg)**     | Solar spectrum overlap + upconversion device schematic     | Comparative/Trend; Application/Performance    |
| **[figure 15](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/example_data/1/images/figures/figure_15.jpg)**     | FRET schematic + spectra + emission enhancement            | Process-Oriented; Application/Performance     |

---

## Summary
By covering these four categories—**Process-Oriented, Comparative/Trend, Structure–Property, and Application/Performance**—the question set challenges contextual inference, reasoning, and scientific understanding specific to ALD/E images.
