# QA types for Scientific Diagrams in Materials Science papers

This guide defines eight question families for annotating MatSci diagrams and maps each to **Bloom’s revised taxonomy** to elicit deeper reasoning in models (overview: [Krathwohl, 2002](https://www.tandfonline.com/doi/abs/10.1207/s15430421tip4104_2)).

## Question families (w/ Bloom levels & answer formats)
- **Process sequencing & control** — order steps/controls (e.g., ALD/MLD, supercycles). *Bloom:* Remember→Understand→Apply. *Answers:* **ordered list** (preferred), factoid, short paragraph.  
- **Mechanistic / causal interaction** — surface reactions, ligand exchange, FRET/energy transfer. *Bloom:* Understand→Analyze. *Answers:* **paragraph** (≥3 sentences), factoid, yes/no (presence/absence).  
- **Structure–Composition–Property (SCP) mapping** — link stacking/doping/composition to properties/spectra. *Bloom:* Apply→Analyze. *Answers:* **paragraph**, factoid, list.  
- **Design / synthesis planning** — propose a feasible recipe (cycles, order, co-reactant). *Bloom:* Create. *Answers:* **ordered list** (steps/spec), paragraph (rationale).  
- **Comparative route / trade-off analysis** — contrast routes (doping vs mixing vs nanolaminates) under constraints. *Bloom:* Analyze→Evaluate. *Answers:* **paragraph** (argument), list (pros/cons), yes/no (choice + rationale).  
- **Taxonomy & chemical-space coverage** — classify precursors; read periodic-table coverage. *Bloom:* Remember→Understand. *Answers:* **list** (classes/elements), factoid, yes/no.  
- **Parameter sensitivity / what-if** — predict effects of T/pulse time/co-reactant on growth/impurities/emission. *Bloom:* Apply→Analyze. *Answers:* **paragraph**, yes/no (direction), factoid (trend).  
- **Application & performance inference** — infer device implications from spectra/architecture. *Bloom:* Analyze→Evaluate. *Answers:* **paragraph** (evidence-based), factoid, list.

**Answer types used across all:** yes/no, factoid (entity/term), **list**, **ordered list**, and **paragraph** (≥3 sentences; **at least one paragraph per figure** for reasoning).

---

## Examples

### Figure 2 — ALD vs ALD/MLD cycle  
Link: example_data/1/images/figures/figure_2.jpg

- **Process sequencing & control — Q:** List the correct step order for the ALD sub-cycle (oxidant = O₃).  
  **A (ordered list):** 1) Metal precursor pulse → 2) Purge → 3) O₃ pulse → 4) Purge.

- **Comparative route / trade-off — Q:** What’s the key difference between the ALD (left) and ALD/MLD (right) cycles?  
  **A (factoid/list):** ALD uses an **oxidant (O₃)** in step 3 to form an inorganic layer; ALD/MLD uses an **organic precursor** in step 3 to build an inorganic–organic network. Both retain purge steps.

- **Mechanistic / causal — Q:** Why are purge steps necessary after each exposure?  
  **A (paragraph):** Purging removes excess precursor and by-products, preventing gas-phase reactions that would cause CVD-like, non-self-limiting growth. It restores a clean carrier gas so the next half-reaction proceeds surface-limited and conformal. Insufficient purging raises impurity levels, roughness, and undermines thickness control.

- **Design / synthesis planning — Q:** Specify one complete hybrid cycle that switches from ALD to ALD/MLD as depicted.
  **A (ordered list):** 1) Metal precursor pulse → 2) Purge → 3) Organic precursor pulse → 4) Purge (repeat to build an inorganic–organic hybrid stack).

- **Parameter sensitivity / what-if — Q:** If the purge after the metal pulse is shortened, what outcome is most likely during the next exposure?
  **A (factoid/paragraph):** Parasitic gas-phase reaction (CVD) and loss of self-limitation, yielding non-uniform growth and increased impurities.

- **Structure–composition–property (SCP) mapping (local to process) — Q:** In the ALD/MLD path, what change in film structure is expected when replacing the O₃ step with an organic pulse?
  **A (paragraph):** The film transitions from purely inorganic (e.g., oxide) to an inorganic–organic hybrid, where the organic linker inserts between metal-terminated surfaces, altering density, mechanical response, and potentially optical properties relative to the ALD-only path.

- **Taxonomy & chemical-space coverage (lightweight here) — Q:** Classify the figure type and name the two process classes illustrated.
  **A (factoid):** Process flow diagram showing ALD and ALD/MLD cycles.

- **Application / performance inference (near-term implication) — Q:** Given the right-hand ALD/MLD cycle, name one plausible reason to choose it over pure ALD for a device stack.
  **A (list/paragraph):** To introduce organic linkers for flexibility/tunability (e.g., lower modulus, modified refractive index, tailored barrier properties) while retaining layer-by-layer thickness control.


---

### Figure 4 — Precursor families & element coverage  
Link: example_data/1/images/figures/figure_4.jpg

- **Taxonomy & coverage — Q:** Name two N-donor ligand families shown and two O-donor families.  
  **A (list):** N-donors: *silylamides, acetamidinates, formamidinates, guanidinates* (any two). O-donors: *diketonates, alkoxides*.

- **Taxonomy & coverage — Q:** Which ligand families display the broadest element coverage across the lanthanides in the panel?

  **A (factoid):** Diketonates and alkoxides (long coverage bars), whereas guanidinates and formamidinates appear sparse.

- **Comparative route / trade-off — Q:** If you must start screening precursors for Ce and Eu, which ligand classes would you try first based on the figure? 
  **A (factoid/list):** Diketonates and alkoxides, as they show broad reported coverage for multiple lanthanides; silylamides may be considered next if available.

- **SCP mapping — Q:** What practical implication follows from choosing an N-donor family (e.g., silylamides/acamid(in)ates) instead of an O-donor family (diketonates/alkoxides) for ALD?  
  **A (paragraph):** In ALD practice, many N-donor complexes tend to offer higher volatility and more reactive surface chemistry (often eliminating amines as cleaner by-products), which can lower growth temperature or improve saturation, whereas O-donor complexes are widely available and stable but can show stronger ligand binding and higher deposition temperatures; the choice trades reactivity and by-product cleanliness against availability and thermal stability.


---

### Figure 7 — Supercycle doping  
Link: example_data/1/images/figures/figure_7.jpg

**Applicable families:** process sequencing & control; structure–composition–property (SCP) mapping; design/synthesis planning; parameter sensitivity/what-if.

- **Process sequencing & control — Q:** List the steps that make one doped supercycle.  
  **A (ordered list):** Metal-A pulse → O₃ pulse → Dopant pulse → O₃ pulse → repeat X times.

- **Structure–composition–property (SCP) mapping — Q:** How does dopant fraction change with X in an X:1 supercycle?  
  **A (factoid):** Approximately \( f_{\text{dopant}} \approx \frac{1}{X+1} \) assuming saturated half-reactions and similar GPC; e.g., X=1 → ~50%, X=3 → ~25%, X=5 → ~17%.

- **Design / planning — Q:** You target ~20% dopant. Which supercycle would you start with?  
  **A (paragraph):** Start with **X ≈ 4:1** (between the 3:1 and 5:1 examples), which nominally yields ~20% under saturated growth. Verify with metrology and fine-tune by adjusting X or inserting/removing dopant sub-cycles if incorporation is off target.

- **Parameter sensitivity / what-if — Q:** If pulses are saturated but you increase X from 1 to 5, what happens to composition and likely properties?
  **A (paragraph):** The **dopant fraction decreases** from ~½ to ~1/6 per supercycle, so properties tied to dopant content (e.g., carrier concentration, refractive index, bandgap, catalytic activity) shift toward the host’s values. Film uniformity remains controlled because the half-reactions stay surface-limited.

---

### Figure 8 — Doping vs homogeneous mixing vs nanolaminates  
Link: example_data/1/images/figures/figure_8.jpg

- **Comparative route / trade-off — Q:** What distinguishes doping, homogeneous mixing, and nanolaminates in terms of stacking and interfaces?  
  **A (paragraph):** **Doping** inserts a small number of dopant exposures within a host growth, producing a mostly single-phase film with **few interfaces** and dilute composition. **Homogeneous mixing** interleaves A/B exposures at short periods so that reactions intermix during growth, yielding a **uniform solid solution** (purple block) with **no periodic interfaces**. **Nanolaminates** alternate thicker A and B sublayers, intentionally creating a **high density of sharp interfaces** (red/blue stack) and preserving layer identity over the period.

- **Structure–composition–property (SCP) mapping — Q:** Which route maximizes **interface density** and is therefore best to exploit interface-driven properties (e.g., barrier performance, superlattice effects)?  
  **A (factoid):** **Nanolaminates** — they intentionally create many A|B interfaces per thickness.

- **Design / synthesis planning — Q:** *You want **continuous band‑gap tuning** without periodic interfaces. Which route and cycle strategy should you choose?*  
  **A (paragraph):** Choose **homogeneous mixing**. Use short alternating A/B sub‑cycles (e.g., A–purge–co‑reactant–purge // B–purge–co‑reactant–purge) with a chosen A:B cycle ratio (e.g., 1:1 or 3:2) until the target thickness is reached. This keeps the film as a **single mixed phase** rather than a layered stack.

- **Process sequencing & control — Q:** Provide a minimal ALD pulse plan to make a nanolaminate period **[A/B]** with ~1 nm per sublayer assuming ~1 Å growth per cycle for both A and B.  
  **A (ordered list):**  
  1. Repeat **10 cycles of A**: (A precursor → purge → co‑reactant → purge) × 10  
  2. Repeat **10 cycles of B**: (B precursor → purge → co‑reactant → purge) × 10  
  3. Repeat steps 1–2 for the required number of periods.

- **Parameter sensitivity / what‑if — Q:** *After high‑temperature annealing, which route is most likely to **lose its layered character** through interdiffusion, and what happens to the other two?*  
  **A (paragraph):** **Nanolaminates** are **most susceptible**—interfaces may blur and the stack can relax toward a mixed alloy. **Homogeneous mixing** is already intermixed, so its phase remains largely unchanged (apart from possible phase segregation if unstable). **Doped** films stay mostly single‑phase with dilute dopant distribution, though dopant diffusion profiles may broaden.


---

### Figure 15 — Eu(thd)₃–HQA emission & FRET  
Link: example_data/1/images/figures/figure_15.jpg

**Applicable families:** mechanistic/causal interaction; structure–composition–property (SCP) mapping; comparative route / trade-off analysis; application/performance inference; design / synthesis planning.

- **Mechanistic / causal interaction — Q:** How does visible-light excitation lead to Eu³⁺ and AF647 emission?  
  **A (paragraph):** Under ~400 nm illumination, the **HQA organic linker** absorbs and transfers energy non‑radiatively to nearby **Eu³⁺ centers**, populating the ⁵D₀ manifold. Radiative decay from ⁵D₀→⁷F₂ produces the **~615 nm Eu³⁺ emission**. When **AF647** is positioned within the Förster distance and there is spectral overlap, energy can be transferred from the excited Eu³⁺ to AF647 via **FRET**, leading to **~660 nm AF647 emission**; the efficiency depends on donor–acceptor separation and orientation.

- **Structure–composition–property (SCP) mapping — Q:** Why is the Eu‑HQA emission stronger on the nanoplasmonic surface than on flat Si?  
  **A (paragraph):** The nanostructured **plasmonic substrate** concentrates the local electromagnetic field near the film, increasing the **excitation rate** of HQA/Eu³⁺ and enhancing **radiative outcoupling**. This yields a higher peak intensity in the spectrum. If the emitters are placed too close to metal, **quenching** can occur, so spacing and resonance tuning are critical to maintain enhancement.

- **Comparative route / trade-off analysis — Q:** What practical trade‑offs distinguish deposition on flat Si versus a plasmonic surface for this emitter?
  **A (list):**  
  - **Si (flat):** lower background, simpler processing, baseline emission (lower intensity).  
  - **Plasmonic:** higher emission via field enhancement but requires **precise spacing** to avoid quenching; adds fabrication complexity and potential spectral reshaping.

- **Application / performance inference — Q:** How can this scheme be used for bio‑detection with AF647? What would be the signal?  
  **A (paragraph):** The Eu‑HQA film acts as an **energy donor**. When **AF647‑tagged analytes** are brought into proximity, **FRET** transfers energy from Eu³⁺ to AF647, producing an **increase at ~660 nm** (and often a corresponding decrease at 615 nm). The presence and magnitude of the 660 nm band thus report **binding/proximity**, enabling surface‑based bio‑detection.

- **Design / synthesis planning — Q:** Outline a minimal ALD/MLD recipe to form the Eu‑HQA hybrid layer suitable for the optical tests.  
  **A (ordered list):**  
  1. **ALD/MLD cycle:** Eu(thd)₃ pulse → N₂ purge → HQA pulse → N₂ purge (repeat to target thickness).  
  2. **Substrate option:** deposit on **plasmonic nanostructure** (for enhancement) or **flat Si** (for baseline).  
  3. **Assay prep:** introduce **AF647** (acceptor) to the film under conditions that control donor–acceptor spacing for measurable FRET.

