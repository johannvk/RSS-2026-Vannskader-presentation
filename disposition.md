# RSS 2026 presentation disposition

## Presentation brief

- **Working title:** Future damage costs from pluvial flooding in Norway
- **Format:** 20-minute conference presentation
- **Main deck:** 18 slides, approximately 17 minutes of planned speech
- **Language:** British English
- **Audience:** RSS attendees with statistical expertise, but no assumed knowledge of Norwegian insurance classifications or geography
- **Technical level:** One conceptual model diagram in the main deck; detailed equations in the appendix
- **Core message:** Short-duration precipitation must be interpreted both absolutely and relative to the local climate. A building-level frequency-severity model suggests that expected pluvial damage costs rise under all three climate scenarios, reaching a national median increase of 33% under high emissions late in the century.

## Scope and terminology

Use **pluvial flooding** for damage caused when rainwater or snowmelt overwhelms drainage, causes sewer backflow, or enters a building through the envelope. The analysis excludes damage caused by rivers or lakes overtopping their banks; these claims are classified separately as natural-hazard flooding in Norway.

Use **damage cost** for the modelled sum of deductibles and insurer payouts. Do not describe the projections as total socioeconomic costs or absolute nationwide losses. The results are relative changes for a fixed building portfolio.

The Hans-specific claim of more than NOK 1 billion in pluvial property damage is a candidate opening statistic, but it must not be used until its category, time period, geographic scope, and market coverage have been verified against an authoritative source.

## Narrative structure

1. Make the problem concrete through Storm Hans.
2. Define precisely which water damage is being modelled.
3. Introduce the two motivations: climate-adaptation costs and insurance risk drivers.
4. Establish the insurance, weather, terrain, and building data.
5. Separate inherited model structure from the new precipitation work.
6. Show the two selected precipitation indices and their interpretation.
7. Be candid about annual cross-validated performance.
8. Explain the fixed-portfolio climate experiment.
9. Present national results before regional variation and uncertainty.
10. End with three claims the evidence supports.

## Timing overview

| Section | Slides | Planned time |
|---|---:|---:|
| Context and questions | 1-4 | 2:55 |
| Data and model | 5-10 | 6:15 |
| Cross-validation | 11-12 | 1:55 |
| Climate projections | 13-17 | 5:15 |
| Conclusions | 18 | 0:40 |
| **Total planned speech** | **18** | **17:00** |
| **Buffer for transitions and overrun** | | **3:00** |

---

## Slide-by-slide plan

### Slide 1 - Future damage costs from pluvial flooding in Norway

**Time:** 0:20

**Purpose:** Introduce the question and the empirical approach.

**On the slide:**

- Johannes Voll Kolsto, Silius Mortensonn Vandeskog and Ola Haug
- Norwegian Computing Center
- RSS 2026

**Visual:** Use the NR title background. Keep the slide free of results and explanatory paragraphs.

**Speaker note:** We connect building-level insurance records to local weather and exposure, then use climate projections to estimate relative changes in damage costs.

**Sources:** [Conference abstract](../Vann-Ekspertutvalg-GJ-rapport-1/rss_abstract.tex)

### Slide 2 - Hans made the risk visible

**Time:** 1:00

**Purpose:** Make the hazard concrete before introducing the statistical abstraction.

**On the slide:**

- Southern and Eastern Norway, August 2023
- 45% more precipitation than normal across Norway that month
- More than 100 local precipitation records

**Visual:** Use [Hans_METNo_reduced.png](../Vann-Ekspertutvalg-GJ-rapport-1/fig/data/Hans_METNo_reduced.png), or a licensed MET image or map with a short source line.

**Speaker note:** A wet July was followed by extreme August rainfall. Hans is motivation, not a single-event attribution argument: MET states that global warming increases the probability of more frequent and intense precipitation events, but individual events cannot simply be attributed to climate change.

**Sources:**

- [MET: August 2023 and Storm Hans](https://www.met.no/nyhetsarkiv/august-2023-vil-bli-husket-for-ekstremvaeret-som-rammet-sor-norge)
- Bibliography key `met_Hans_event` in [ref.bib](../Vann-Ekspertutvalg-GJ-rapport-1/ref.bib)

**Open item:** `SOURCE NEEDED` for any Hans-specific monetary loss. The draft abstract's “more than NOK 1 billion” must not appear in the deck until verified.

### Slide 3 - The hazard we model is not river flooding

**Time:** 0:45

**Purpose:** Prevent a category error that would undermine the rest of the talk.

**On the slide:**

| Included | Excluded |
|---|---|
| Rain or snowmelt entering from outside | Rivers overtopping their banks |
| Sewer backflow from overloaded drainage | Lakes overtopping their banks |
| Water entering through the building envelope | Natural-hazard flood claims |

**Visual:** A simple two-column inclusion/exclusion diagram. Use familiar building, drain, river, and lake icons rather than photographs.

**Speaker note:** These categories are separated in Norwegian insurance data. Over 1995-2024, the report states that external-water damage costs were around four times river-flood costs, but the exact wording must be checked in the cited Finans Norge report before use on the slide.

**Sources:**

- [Data section](../Vann-Ekspertutvalg-GJ-rapport-1/sections/data.tex), subsection `Forsikring`
- Bibliography key `finansnorge_klimarapport2025` in [ref.bib](../Vann-Ekspertutvalg-GJ-rapport-1/ref.bib)

### Slide 4 - Two motivations, one modelling framework

**Time:** 0:50

**Purpose:** State what the project is intended to answer.

**On the slide:**

1. **Climate adaptation:** How might expected building-damage costs change by mid-century and late century?
2. **Insurance insight:** Which local factors drive claim frequency and claim size, especially short-duration precipitation?

**Visual:** Two questions feeding into one model, with outputs labelled `relative cost change` and `risk drivers`.

**Speaker note:** The first motivation supports knowledge about socioeconomic consequences, but this project does not estimate total socioeconomic cost. The second uses unusually detailed insurance records to investigate building vulnerability and local exposure.

**Sources:**

- [Introduction](../Vann-Ekspertutvalg-GJ-rapport-1/sections/introduksjon.tex)
- [Summary](../Vann-Ekspertutvalg-GJ-rapport-1/sections/oppsummering.tex)

### Slide 5 - Sixteen years of building-level insurance data

**Time:** 1:00

**Purpose:** Establish why the data can identify both incidence and cost.

**On the slide:**

- Gjensidige building portfolio, 2010-2025
- Daily claim timing and building-level exposure
- Homes, holiday homes, agriculture, commercial property, housing cooperatives and condominiums
- Claims, payouts, deductibles, building attributes, and claim-free exposure

**Visual:** Translate and relabel [skadefrekvens_og_utbetalinger_normalisert.png](../Vann-Ekspertutvalg-GJ-rapport-1/fig/data/skadefrekvens_og_utbetalinger_normalisert.png). Highlight 2023 without covering the time series.

**Speaker note:** Access to the insured portfolio tells us not only where claims occurred, but also when and where insured buildings did not claim. Monetary values and insured values are indexed to 2026 NOK. Claims below the deductible are absent.

**Sources:** [Data section](../Vann-Ekspertutvalg-GJ-rapport-1/sections/data.tex), subsection `Forsikring`

### Slide 6 - Weather, terrain and the built environment

**Time:** 0:55

**Purpose:** Show how the external pressure and local vulnerability are joined.

**On the slide:**

- **Weather:** seNorge daily precipitation and temperature, 1 km grid
- **Terrain:** topographic wetness index (TWI) and height above nearest drainage (HAND), 20 m grid
- **Surface:** built-up versus non-built-up AR50 class
- **Building:** type, age, insured value, basement, standard and use
- **Region:** municipality and county effects

**Visual:** A compact data-fusion diagram centred on a building-season observation. Do not use all three detailed topographic maps in the main deck.

**Speaker note:** The modelling unit is a building in a year-season. Some predictors vary by building, some by location, and the precipitation indices vary by location and season.

**Sources:**

- [Data section](../Vann-Ekspertutvalg-GJ-rapport-1/sections/data.tex)
- [Method section](../Vann-Ekspertutvalg-GJ-rapport-1/sections/metode.tex)

### Slide 7 - We build on an existing risk model

**Time:** 0:45

**Purpose:** Distinguish prior structure from this project's contribution.

**On the slide:**

| Retained | Revised or new |
|---|---|
| Generalised additive models | Year-season precipitation indices |
| Separate frequency and severity models | Explicit focus on short-duration rainfall |
| Building and topographic predictors | Updated 2024 regional structure |
| Regional effects | Municipality-specific urban/rural effects |

**Visual:** A restrained `retained / revised / new` comparison.

**Speaker note:** The earlier model represented climate mainly using seasonal quantities averaged over 30-year periods. The central development here is to distinguish unusually wet seasons from dry seasons at the same location while retaining local climatological context.

**Sources:**

- [Introduction](../Vann-Ekspertutvalg-GJ-rapport-1/sections/introduksjon.tex)
- [Model development](../Vann-Ekspertutvalg-GJ-rapport-1/sections/modellering-B.tex)
- Heinrich and Mertsching (2023), bibliography key `HeinrichMertsching2023`

### Slide 8 - Total cost = how often x how costly

**Time:** 1:10

**Purpose:** Explain the statistical architecture without displaying full formulae.

**On the slide:**

```text
Building + terrain + region + precipitation
                 |
          +------+------+
          |             |
  Claim frequency   Cost per claim
   NegBin GAM         Gamma GAM
          |             |
          +------+------+
                 |
       Aggregate simulated cost
```

**Visual:** Redraw the pipeline graphically. Give frequency and severity equal visual weight.

**Speaker note:** The frequency model predicts claims per insured exposure day. Conditional on a claim, the severity model predicts the insurer payout. Simulated counts and severities are combined, deductibles are added, and costs are summed over buildings and seasons.

**Sources:** [Method section](../Vann-Ekspertutvalg-GJ-rapport-1/sections/metode.tex), subsections `Skadefrekvens`, `Enkeltskadebelop` and `Totalt skadebelop`

### Slide 9 - Two precipitation indices survived validation

**Time:** 1:15

**Purpose:** Present the project's main modelling contribution.

**On the slide:**

1. **Absolute intensity:** mean precipitation across the three wettest days in a year-season
2. **Relative anomaly:** the extreme-season measure relative to the local climatological 95th percentile of daily precipitation

**Visual:** Two mini-graphics:

- Three highlighted bars in a seasonal daily-rainfall series for `amount`
- The same event shown against different local baselines for `unusual here`

**Speaker note:** A damage event requires enough water in absolute terms. But local construction, drainage and practice may have adapted to normal rainfall, so departure from the local norm can also matter. Candidate indices and representations were compared on unseen data before these two were selected.

**Sources:** [Model development](../Vann-Ekspertutvalg-GJ-rapport-1/sections/modellering-B.tex), subsection `Skadefrekvensmodellen`

**Terminology check:** Confirm the exact computational definition and English axis label for `snitt-topp-3d-nedborsmengde` before drawing the final graphic.

### Slide 10 - The same rainfall can mean different risk

**Time:** 1:10

**Purpose:** Interpret the two precipitation terms jointly.

**On the slide:**

- Dry-climate locations respond more steeply than wet-climate locations
- At 40 mm, expected frequency is approximately 9 times the dry-season reference in the driest context, versus approximately 3 times in wetter contexts
- The corresponding payout response is smaller: almost 2 times versus less than 1.5 times

**Visual:** Translate or redraw both:

- [Frequency precipitation effect](../Vann-Ekspertutvalg-GJ-rapport-1/fig/model/claim_incidence_kombinert_nedborseffekt_99_9pct.png)
- [Severity precipitation effect](../Vann-Ekspertutvalg-GJ-rapport-1/fig/model/claim_size_kombinert_nedborseffekt_99_9pct.png)

If both panels are too dense, reveal frequency first and severity second on the same slide.

**Speaker note:** These are marginal effects relative to the driest year-seasons with observed claims, not unconditional risk ratios. The curves illustrate why both absolute intensity and local abnormality are needed.

**Sources:** [Model development](../Vann-Ekspertutvalg-GJ-rapport-1/sections/modellering-B.tex), subsection `Fortolkning av nedborstermer i skademodellene`

### Slide 11 - Annual performance is tested out of sample

**Time:** 0:45

**Purpose:** Explain the validation design before showing its result.

**On the slide:**

- Hold out four consecutive years
- Fit frequency and severity models on the remaining years
- Predict aggregate payout for the held-out years
- Roll the held-out block through 2010-2025

**Visual:** A 16-year timeline with a moving four-year holdout block. Use one example split rather than several dense panels.

**Speaker note:** The test evaluates the two models together on years not used for fitting. The final climate projections differ in one important respect: their damage models are fitted using all 16 historical years.

**Sources:** [Model development](../Vann-Ekspertutvalg-GJ-rapport-1/sections/modellering-B.tex), cross-validation discussion following the severity-model specification

### Slide 12 - The model tracks the trend, not every extreme year

**Time:** 1:10

**Purpose:** Give an honest account of predictive performance and connect back to Hans.

**On the slide:**

- Broad rises and falls are captured
- Some individual years have substantial level errors
- In 2023, the prediction is almost one period mean below the observation
- Intended use: long-period aggregate change, not individual-year prediction

**Visual:** Translate and relabel [cross-validated observed versus simulated payout](../Vann-Ekspertutvalg-GJ-rapport-1/fig/model/normalized_claim_payments_actual_vs_simulated_no_errorbars_n_sims_100.png). Annotate 2023 directly.

**Speaker note:** When 2023 is held out, no comparable Hans year remains for training. Seasonal indices also omit rainfall sequencing and antecedent soil saturation. Alternating annual under- and overprediction can still permit useful estimates over 30-year periods, but this is an argument about aggregation, not a claim that annual errors disappear by definition.

**Sources:** [Model development](../Vann-Ekspertutvalg-GJ-rapport-1/sections/modellering-B.tex), cross-validation discussion

### Slide 13 - Change the climate, hold buildings fixed

**Time:** 0:55

**Purpose:** Define exactly what the projection ratios measure.

**On the slide:**

- Reference: 1991-2020
- Horizons: 2041-2070 and 2071-2100
- Scenarios: low `RCP2.6`, intermediate `RCP4.5`, high `SSP3-7.0`
- 10 climate simulations x 2 bias adjustments x 10 damage-model simulations = 200 ratios

**Visual:** A baseline portfolio copied into three climate windows. Keep the building stock visually identical while the rainfall pattern changes.

**Speaker note:** Today's portfolio, deductibles and 2026 price level are fixed. This isolates the effect of precipitation change. It does not forecast future construction, demolition, adaptation or absolute nationwide cost.

**Sources:**

- [Method section](../Vann-Ekspertutvalg-GJ-rapport-1/sections/metode.tex), subsection `Framskriving av endringer i skadebelop`
- [Data section](../Vann-Ekspertutvalg-GJ-rapport-1/sections/data.tex), subsection `Meteorologi`
- KSS report, bibliography key `Dyrrdal2025`

### Slide 14 - National costs rise in every scenario

**Time:** 1:20

**Purpose:** Deliver the principal national result clearly.

**On the slide:**

| Scenario | 2041-2070 median | 2071-2100 median |
|---|---:|---:|
| Low - RCP2.6 | +9.5% | +9.9% |
| Intermediate - RCP4.5 | +14.9% | +23.4% |
| High - SSP3-7.0 | +18.3% | **+33.2%** |

**Visual:** Rebuild this as a presentation-native 3 x 2 matrix or compact dot plot. Do not paste the report table. Make `+33.2%` the focal number without hiding the other scenarios.

**Speaker note:** These are medians across the simulation ensemble. The increase is positive in every scenario and horizon at national level. Under high emissions late in the century, expected damage cost is about one third higher than in the reference climate for the same portfolio.

**Sources:** [Climate projections](../Vann-Ekspertutvalg-GJ-rapport-1/sections/skadeframskriving.tex), table `nasjonale_endringer`

### Slide 15 - Emissions matter most late in the century

**Time:** 0:55

**Purpose:** Show both scenario divergence and ensemble spread.

**On the slide:**

- Scenario medians are closer at mid-century
- They diverge substantially by 2071-2100
- High emissions, 2071-2100: IQR `+17.0% to +41.6%`
- National 10th-90th percentile: `+10.1% to +46.8%`

**Visual:** A two-panel point-and-range chart, one panel per horizon and one colour per scenario. Prioritise medians and interquartile ranges; show 10th-90th only for the high late-century result if space permits.

**Speaker note:** Ensemble spread is not a calibrated probability distribution. Do not say that a percentile gives the probability of a particular future. Differences between climate simulations dominate much of the spread.

**Sources:**

- [Climate projections](../Vann-Ekspertutvalg-GJ-rapport-1/sections/skadeframskriving.tex)
- [Caveats](../Vann-Ekspertutvalg-GJ-rapport-1/sections/forbehold.tex), subsection `Valg av kvantilnivaer`

### Slide 16 - The increase is geographically uneven

**Time:** 1:10

**Purpose:** Move from the national headline to decision-relevant spatial variation.

**On the slide:**

- High-emissions county medians, 2041-2070: approximately `+8% to +25%`
- High-emissions county medians, 2071-2100: approximately `+17% to +61%`
- Largest increases: Finnmark and parts of Southern Norway's mountain regions
- Lower increases: much of Western Norway

**Visual:** Use page 6 of [county damage changes](../Vann-Ekspertutvalg-GJ-rapport-1/fig/data/fylkesendringer_totalt_skadebelop.pdf) if the filename is available without Norwegian characters in the production environment; otherwise copy the current report asset and give the presentation copy an ASCII filename. Translate all labels. Prefer county results in the main deck and move municipality maps to the appendix.

**Speaker note:** Aggregating more buildings reduces variability, so county medians are more robust than municipality tails. Finnmark's result is consistent with KSS projections of a large increase in very heavy precipitation.

**Sources:**

- [Climate projections](../Vann-Ekspertutvalg-GJ-rapport-1/sections/skadeframskriving.tex)
- [Summary](../Vann-Ekspertutvalg-GJ-rapport-1/sections/oppsummering.tex)

### Slide 17 - What the ratios do and do not say

**Time:** 0:55

**Purpose:** Bound the interpretation before the conclusion.

**On the slide:**

- **Relative, not absolute:** Gjensidige's portfolio does not cover all Norwegian buildings
- **Fixed portfolio:** no future construction, demolition or adaptation
- **Conservative extrapolation:** precipitation effects are capped at the historical training range
- **Uneven robustness:** national and county medians are stronger than municipality tail estimates

**Visual:** Four compact statements with distinct icons. Optionally include a small crop from [county variability](../Vann-Ekspertutvalg-GJ-rapport-1/fig/data/fylkesvariabilitet_totalt_skadebelop.pdf) only if it remains readable.

**Speaker note:** The 200 ratios do not behave like 200 independent climate futures. Ten damage simulations based on the same climate projection cluster closely, so the effective information in the tails is much smaller.

**Sources:** [Caveats](../Vann-Ekspertutvalg-GJ-rapport-1/sections/forbehold.tex)

### Slide 18 - Three takeaways

**Time:** 0:40

**Purpose:** End with claims that are memorable and fully supported by the analysis.

**On the slide:**

1. Extreme rainfall matters both absolutely and relative to local climate.
2. The model is designed for long-period aggregate change, not single-year prediction.
3. Expected costs rise under every scenario; the high-emissions late-century median is **+33%**.

**Visual:** Use `+33%` as the only large number. Keep the three statements visible simultaneously.

**Speaker note:** The two practical uses are evidence for climate-adaptation planning and better insurance understanding of the drivers of building water damage.

**Sources:**

- [Model development](../Vann-Ekspertutvalg-GJ-rapport-1/sections/modellering-B.tex)
- [Climate projections](../Vann-Ekspertutvalg-GJ-rapport-1/sections/skadeframskriving.tex)
- [Summary](../Vann-Ekspertutvalg-GJ-rapport-1/sections/oppsummering.tex)

---

## Appendix candidates

These slides do not count towards the 18-slide main deck.

1. Full frequency and severity model specifications
2. TWI, HAND and AR50 examples
3. Municipality map and county/municipality scatter
4. Climate-projection clustering and effective ensemble size
5. Results by building type
6. Full national quantile table
7. Data exclusions, censoring and model extrapolation limits

## Asset register

### Ready as source material

| Asset | Intended use | Work required |
|---|---|---|
| [Hans_METNo_reduced.png](../Vann-Ekspertutvalg-GJ-rapport-1/fig/data/Hans_METNo_reduced.png) | Slide 2 | Check licence/source line and projection resolution |
| [Historical normalised series](../Vann-Ekspertutvalg-GJ-rapport-1/fig/data/skadefrekvens_og_utbetalinger_normalisert.png) | Slide 5 | Translate axes and legend; annotate 2023 |
| [Frequency precipitation effect](../Vann-Ekspertutvalg-GJ-rapport-1/fig/model/claim_incidence_kombinert_nedborseffekt_99_9pct.png) | Slide 10 | Translate or redraw; simplify legend |
| [Severity precipitation effect](../Vann-Ekspertutvalg-GJ-rapport-1/fig/model/claim_size_kombinert_nedborseffekt_99_9pct.png) | Slide 10 | Translate or redraw; simplify legend |
| [Cross-validation result](../Vann-Ekspertutvalg-GJ-rapport-1/fig/model/normalized_claim_payments_actual_vs_simulated_no_errorbars_n_sims_100.png) | Slide 12 | Translate labels; annotate 2023 |
| County projection PDF in `fig/data` | Slide 16 | Extract page 6; translate labels; consider an ASCII presentation filename |

### Build natively for the presentation

- Scope inclusion/exclusion diagram, slide 3
- Two-motivation diagram, slide 4
- Data-fusion diagram, slide 6
- Retained/revised model comparison, slide 7
- Frequency-severity pipeline, slide 8
- Two precipitation-index mini-graphics, slide 9
- Rolling cross-validation timeline, slide 11
- Fixed-portfolio projection experiment, slide 13
- National scenario matrix, slide 14
- Scenario and uncertainty range chart, slide 15
- Interpretation caveats, slide 17

### Claims requiring verification

| Claim | Status | Required evidence |
|---|---|---|
| Hans caused more than NOK 1 billion in pluvial property damage | `SOURCE NEEDED` | Authoritative Gjensidige or Finans Norge source specifying category, dates, geography and market scope |
| External-water costs were about four times river-flood costs over 1995-2024 | Verify exact wording | Finans Norge Climate Report 2025, with categories matched to slide 3 |
| Storm Hans image reuse | Verify licence | MET image credit and reuse conditions |

## Source register

### Report sections

- [Introduction](../Vann-Ekspertutvalg-GJ-rapport-1/sections/introduksjon.tex): mandate, motivations and earlier work
- [Data](../Vann-Ekspertutvalg-GJ-rapport-1/sections/data.tex): insurance scope, hazard definition, meteorology and topography
- [Method](../Vann-Ekspertutvalg-GJ-rapport-1/sections/metode.tex): GAM framework, frequency-severity simulation and projection design
- [Model development](../Vann-Ekspertutvalg-GJ-rapport-1/sections/modellering-B.tex): precipitation indices, final models, effects and cross-validation
- [Climate projections](../Vann-Ekspertutvalg-GJ-rapport-1/sections/skadeframskriving.tex): national, county, municipality and building-type results
- [Summary](../Vann-Ekspertutvalg-GJ-rapport-1/sections/oppsummering.tex): principal findings and interpretation
- [Caveats](../Vann-Ekspertutvalg-GJ-rapport-1/sections/forbehold.tex): representativeness, fixed portfolio and quantile robustness
- [Conference abstract](../Vann-Ekspertutvalg-GJ-rapport-1/rss_abstract.tex): submitted presentation framing
- [Bibliography](../Vann-Ekspertutvalg-GJ-rapport-1/ref.bib): complete citation details

### External sources already identified

- [MET: August 2023 and Storm Hans](https://www.met.no/nyhetsarkiv/august-2023-vil-bli-husket-for-ekstremvaeret-som-rammet-sor-norge)
- [Finans Norge Climate Report 2025](https://www.finansnorge.no/siteassets/dokumenter/publikasjoner/finans-norge-klimarapport-2025.pdf)
- Norwegian Climate Service Centre report: bibliography key `Dyrrdal2025`
- seNorge description: bibliography key `Lussana2019`
- Earlier statistical risk model: bibliography key `HeinrichMertsching2023`

## Production checklist

### Content

- [ ] Verify or remove the Hans-specific NOK amount.
- [ ] Verify the exact Finans Norge comparison between pluvial/external-water and river-flood losses.
- [ ] Confirm the precise English definition of both precipitation indices.
- [ ] Keep `damage cost`, `payout`, and `socioeconomic cost` distinct.
- [ ] Keep pluvial flooding distinct from river and lake flooding.
- [ ] Describe ensemble spread without assigning calibrated probabilities.

### Visuals

- [ ] Recreate Norwegian-labelled plots in English where source data or plotting code are available.
- [ ] Use at least 14 pt body text in the Beamer deck and test at projected size.
- [ ] Use a colour-blind-safe palette and do not rely on colour alone.
- [ ] Preserve aspect ratios and source credits for all external images.
- [ ] Keep report tables out of the deck; redraw the required values.

### Rehearsal

- [ ] Rehearse the 18-slide deck against a stopwatch.
- [ ] Aim for 17 minutes of planned speech, preserving three minutes for transitions and overrun.
- [ ] If the talk runs long, first shorten slide 15 and remove the optional uncertainty mini-panel on slide 17.
- [ ] Do not cut the annual validation result or the two precipitation indices; they support the central methodological claim.

### LaTeX implementation

- [ ] Preserve British English via `\usepackage[british]{babel}`.
- [ ] Implement the approved disposition in [nr-presentation.tex](nr-presentation.tex).
- [ ] Copy selected report figures into the presentation's `images` directory with descriptive ASCII filenames.
- [ ] Compile with `latexmk -pdf -outdir=build nr-presentation.tex`.
- [ ] Inspect every slide in 16:9 format for overflow, label size and source visibility.
