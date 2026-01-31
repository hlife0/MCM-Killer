# Advanced Mermaid Templates for MCM Diagrams

> **"Mermaid diagrams bridge the gap between text explanations and formal diagrams. Master these templates for rapid conceptual figure generation."**

This guide extends the basic Mermaid templates in the visualizer agent with advanced patterns for MCM papers.

---

## Rendering Instructions

### Option 1: Mermaid CLI (Recommended)
```bash
# Install
npm install -g @mermaid-js/mermaid-cli

# Render to PNG
mmdc -i diagram.mmd -o output.png -w 2000 -H 1500 -b white

# Render to SVG (for vector quality)
mmdc -i diagram.mmd -o output.svg -b white
```

### Option 2: Online Editors
- [Mermaid Live Editor](https://mermaid.live/) - Real-time preview
- [Draw.io](https://draw.io) - Import Mermaid, export PNG

### Option 3: VS Code Extension
- Install "Markdown Preview Mermaid Support"
- Preview in markdown files
- Export via screenshot (lower quality)

### Quality Settings
- **Width**: 2000px minimum for paper figures
- **Background**: White (`-b white`)
- **Format**: PNG for raster, SVG for vector
- **Final DPI**: Convert to 300 DPI if needed

---

## Template 1: Complex Flowchart with Subgraphs

**Use Case**: Multi-stage model pipelines, data processing workflows

```mermaid
flowchart TB
    subgraph Input["📥 Data Collection"]
        direction TB
        R1[("Olympic Results<br/>1896-2024<br/>N=28 Games")]
        R2[("Country Stats<br/>GDP, Population<br/>N=235 Countries")]
        R3[("Sports Investment<br/>Training Facilities<br/>N=180 Countries")]
    end

    subgraph Preprocessing["🔧 Preprocessing"]
        direction TB
        P1["Missing Value<br/>Imputation<br/>(MICE Algorithm)"]
        P2["Outlier Detection<br/>(IQR Method)"]
        P3["Feature Scaling<br/>(Robust Scaler)"]
    end

    subgraph Features["📊 Feature Engineering"]
        direction TB
        F1["Lag Features<br/>(t-1, t-2, t-3)"]
        F2["Rolling Stats<br/>(4-game window)"]
        F3["Derived Ratios<br/>(medals/GDP)"]
        F4["Interaction Terms<br/>(GDP × Host)"]
    end

    subgraph Models["🧮 Modeling"]
        direction TB
        M1["Model 1<br/>Hurdle"]
        M2["Model 2<br/>Hierarchical"]
        M3["Model 3<br/>Ensemble"]
    end

    subgraph Output["📈 Predictions"]
        direction TB
        O1["Point Estimates<br/>2028 LA"]
        O2["95% Intervals"]
        O3["Sensitivity<br/>Analysis"]
    end

    Input --> Preprocessing
    Preprocessing --> Features
    Features --> Models
    Models --> Output

    R1 --> P1
    R2 --> P1
    R3 --> P2
    P1 --> P3
    P2 --> P3
    P3 --> F1
    P3 --> F2
    P3 --> F3
    F1 --> F4
    F2 --> F4
    F3 --> F4
    F4 --> M1
    F4 --> M2
    F4 --> M3
    M1 --> O1
    M2 --> O1
    M3 --> O1
    O1 --> O2
    O2 --> O3
```

**Styling Notes**:
- Use subgraphs to group related steps
- Direction TB (top-bottom) for vertical flow
- Direction LR (left-right) for horizontal stages
- Add quantities in node labels (N=, %)

---

## Template 2: State Diagram for Model Transitions

**Use Case**: Markov models, state-based dynamics, transition systems

```mermaid
stateDiagram-v2
    [*] --> NonMedalist: Initial State (N=79)

    NonMedalist --> Emerging: Breakthrough\n(p=0.023/yr)
    Emerging --> Established: Consolidation\n(p=0.15/yr)
    Established --> Superpower: Dominance\n(p=0.05/yr)

    NonMedalist --> NonMedalist: Persist\n(p=0.977/yr)
    Emerging --> NonMedalist: Regression\n(p=0.08/yr)
    Established --> Emerging: Decline\n(p=0.12/yr)
    Superpower --> Established: Reduction\n(p=0.10/yr)

    Superpower --> [*]: Sustained (N=8)

    note right of NonMedalist
        79 countries (34%)
        Expected medals: 0
    end note

    note right of Emerging
        45 countries (19%)
        Expected medals: 1-5
    end note

    note right of Established
        103 countries (44%)
        Expected medals: 6-30
    end note

    note right of Superpower
        8 countries (3%)
        Expected medals: 31+
    end note
```

**Caption Format**: "Figure X: Countries transition between four medal-winning states with asymmetric probabilities. The 'breakthrough' transition (NonMedalist → Emerging) has probability 0.023/year, meaning the average non-medalist waits 43 years for their first medal. Regression is 3.5× more likely than breakthrough, explaining the persistence of medal inequality."

---

## Template 3: Sequence Diagram for Model Workflow

**Use Case**: Training procedures, iterative algorithms, agent interactions

```mermaid
sequenceDiagram
    autonumber
    participant Data as Data Source
    participant Pre as Preprocessor
    participant FE as Feature Engineer
    participant Model as Bayesian Model
    participant Val as Validator
    participant Out as Output

    Data->>Pre: Raw data (N=8,225)
    Pre->>Pre: Handle missing (3.2%)
    Pre->>FE: Clean data (N=7,962)

    FE->>FE: Create lag features
    FE->>FE: Compute rolling stats
    FE->>FE: Generate interactions
    FE->>Model: Feature matrix (47 features)

    loop MCMC Sampling (10,000 iterations)
        Model->>Model: Propose θ'
        Model->>Model: Compute likelihood
        Model->>Model: Accept/Reject
    end

    Model->>Val: Posterior samples
    Val->>Val: Check R-hat < 1.1
    Val->>Val: Verify ESS > 1,000

    alt Convergence OK
        Val->>Out: Generate predictions
    else Convergence Failed
        Val->>Model: Increase samples
    end

    Out->>Out: Compute 95% CI
    Out-->>Data: Save results.csv
```

**Caption Format**: "Figure X: The training pipeline processes 8,225 country-year observations through 6 stages. MCMC sampling (steps 7-10) runs for 10,000 iterations with convergence verification (R-hat < 1.1). The feedback loop (steps 11-12) doubles sample size if convergence fails, ensuring reliable posterior estimates."

---

## Template 4: Entity Relationship Diagram

**Use Case**: Data structure, database schema, variable relationships

```mermaid
erDiagram
    COUNTRY ||--o{ PARTICIPATION : "participates in"
    COUNTRY {
        string country_code PK "ISO 3166-1"
        string name
        float gdp_per_capita
        int population
        string region
    }

    OLYMPICS ||--o{ PARTICIPATION : "hosts"
    OLYMPICS {
        int year PK
        string host_city
        string host_country FK
        int total_events
        int participating_countries
    }

    PARTICIPATION ||--o{ MEDAL : "earns"
    PARTICIPATION {
        string country_code FK
        int year FK
        int athletes_sent
        float sports_investment
        bool is_host
    }

    MEDAL {
        int medal_id PK
        string country_code FK
        int year FK
        string sport
        string event
        string medal_type "Gold/Silver/Bronze"
    }

    FEATURES ||--|| PARTICIPATION : "derived from"
    FEATURES {
        string country_code FK
        int year FK
        float lag1_medals
        float lag2_medals
        float rolling_avg_4
        float medals_per_gdp
        float host_advantage
    }
```

**Caption Format**: "Figure X: The relational data model links 235 countries across 28 Olympic Games through 6,580 participation records. The FEATURES table derives 47 predictors from the base tables, with key transformations including lag features (1-3 games), rolling averages (4-game window), and normalized ratios (medals per GDP)."

---

## Template 5: Gantt Chart for Timeline

**Use Case**: Project phases, historical periods, prediction horizons

```mermaid
gantt
    title Olympic Medal Prediction: Data and Forecast Timeline
    dateFormat YYYY
    axisFormat %Y

    section Historical Data
    Cold War Era (Bipolar)        :done, cold, 1956, 1991
    Post-Soviet Transition        :done, post, 1992, 2000
    Modern Era (Multipolar)       :done, modern, 2001, 2024

    section Training Period
    Feature Engineering           :active, fe, 2024-01, 2024-06
    Model Development             :active, model, 2024-03, 2024-09
    Validation                    :active, val, 2024-06, 2024-12

    section Forecast Horizon
    LA 2028 Prediction            :la2028, 2025-01, 2028-07
    Brisbane 2032 Projection      :bris, 2028-08, 2032-07
    Future Olympics               :future, 2032-08, 2040-12

    section Key Events
    Paris 2024 (Last Training)    :milestone, paris, 2024-07, 0d
    LA 2028 (Target)              :milestone, la, 2028-07, 0d
    Brisbane 2032                 :milestone, bris2, 2032-07, 0d
```

---

## Template 6: Pie Chart Alternative (Subgraph Distribution)

**Use Case**: Showing proportions without actual pie charts (which Mermaid doesn't support well)

```mermaid
flowchart LR
    subgraph Distribution["Medal Count Distribution (N=235 Countries)"]
        direction TB

        subgraph Zero["Zero Medals"]
            Z1["79 countries<br/>(33.6%)"]
        end

        subgraph Low["1-5 Medals"]
            L1["67 countries<br/>(28.5%)"]
        end

        subgraph Medium["6-30 Medals"]
            M1["61 countries<br/>(26.0%)"]
        end

        subgraph High["31+ Medals"]
            H1["28 countries<br/>(11.9%)"]
        end
    end

    Zero ~~~ Low ~~~ Medium ~~~ High

    style Zero fill:#ffcccc
    style Low fill:#ffffcc
    style Medium fill:#ccffcc
    style High fill:#ccccff
```

**Better Alternative**: Use matplotlib for actual pie/donut charts.

---

## Template 7: Class Diagram for Model Components

**Use Case**: Object-oriented model design, component relationships

```mermaid
classDiagram
    class BaseModel {
        <<abstract>>
        +features: DataFrame
        +params: Dict
        +fit(X, y) void
        +predict(X) array
        +get_uncertainty() array
    }

    class HurdleModel {
        +hurdle_prob: LogisticRegression
        +count_model: TruncatedPoisson
        +fit(X, y) void
        +predict(X) array
        +predict_proba(X) array
    }

    class HierarchicalModel {
        +global_params: Dict
        +region_params: Dict
        +country_params: Dict
        +fit_mcmc(X, y, n_samples) void
        +predict_posterior(X) array
    }

    class EnsembleModel {
        +models: List~BaseModel~
        +weights: array
        +combine_predictions() array
        +optimize_weights() void
    }

    BaseModel <|-- HurdleModel
    BaseModel <|-- HierarchicalModel
    BaseModel <|-- EnsembleModel
    EnsembleModel o-- BaseModel : contains
```

---

## Template 8: Mind Map for Problem Decomposition

**Use Case**: Research questions, problem structure, solution components

```mermaid
mindmap
    root((Olympic Medal<br/>Prediction))
        Data Sources
            Historical Results
                1896-2024
                28 Games
            Country Statistics
                GDP
                Population
                Sports Investment
            External Factors
                Host Advantage
                Political Events
        Modeling Approaches
            Hurdle Model
                Zero-inflation
                Count process
            Hierarchical Bayes
                Partial pooling
                Regional effects
            Ensemble
                Model averaging
                Uncertainty propagation
        Predictions
            LA 2028
                Point estimates
                95% intervals
            Sensitivity
                GDP scenarios
                Host effects
        Validation
            Holdout Testing
                2024 Paris
            Cross-validation
                Leave-one-out
            Metrics
                RMSE
                Coverage
```

---

## Template 9: Comparison Flowchart (Before/After)

**Use Case**: Showing improvement, model evolution, design changes

```mermaid
flowchart LR
    subgraph Before["❌ Baseline Approach"]
        direction TB
        B1["All Countries<br/>Same Model"]
        B2["Single Poisson<br/>Distribution"]
        B3["Point Estimates<br/>Only"]
        B4["RMSE: 12.3<br/>Coverage: 72%"]

        B1 --> B2 --> B3 --> B4
    end

    subgraph After["✅ Our Approach"]
        direction TB
        A1["Stratified by<br/>Medal History"]
        A2["Hurdle + <br/>Hierarchical"]
        A3["Full Posterior<br/>Distributions"]
        A4["RMSE: 4.7<br/>Coverage: 94%"]

        A1 --> A2 --> A3 --> A4
    end

    Before -.->|"62% RMSE<br/>Reduction"| After
```

---

## Template 10: Decision Matrix Flowchart

**Use Case**: Model selection criteria, feature selection, methodology choices

```mermaid
flowchart TD
    Start["Select Modeling Approach"] --> Q1{"Zero-inflation<br/>> 20%?"}

    Q1 -->|"Yes<br/>(51% zeros)"| Q2{"Need<br/>Interpretability?"}
    Q1 -->|"No"| Standard["Standard<br/>GLM"]

    Q2 -->|"Yes"| Q3{"Data<br/>Hierarchical?"}
    Q2 -->|"No"| Neural["Neural<br/>Network"]

    Q3 -->|"Yes<br/>(Countries in Regions)"| Hierarchical["Hierarchical<br/>Bayesian<br/>✓ SELECTED"]
    Q3 -->|"No"| Hurdle["Simple<br/>Hurdle"]

    Standard --> Validate["Validate on<br/>Holdout"]
    Neural --> Validate
    Hierarchical --> Validate
    Hurdle --> Validate

    style Hierarchical fill:#90EE90,stroke:#006400,stroke-width:3px
```

---

## Advanced Styling

### Custom Colors
```mermaid
flowchart TD
    A["Input"] --> B["Process"] --> C["Output"]

    style A fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style B fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style C fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px
```

### Link Labels with Values
```mermaid
flowchart LR
    A["Raw Data"] -->|"N=8,225"| B["Clean Data"]
    B -->|"47 features"| C["Model"]
    C -->|"R²=0.89"| D["Predictions"]
```

### Subgraph Nesting
```mermaid
flowchart TB
    subgraph Outer["Complete Pipeline"]
        subgraph Inner1["Stage 1"]
            A --> B
        end
        subgraph Inner2["Stage 2"]
            C --> D
        end
        Inner1 --> Inner2
    end
```

---

## Conversion to Image

### Recommended Workflow

1. **Write Mermaid code** in `.mmd` file
2. **Preview** in Mermaid Live Editor
3. **Render** with CLI:
   ```bash
   mmdc -i diagram.mmd -o model_1_diagram_architecture.png -w 2400 -H 1800 -b white
   ```
4. **Verify** resolution: should be ≥2000px wide
5. **Convert if needed**: ensure 300 DPI for paper

### Troubleshooting

| Issue | Solution |
|-------|----------|
| Text too small | Increase width (`-w 3000`) |
| Diagram cut off | Increase height (`-H 2500`) |
| Low resolution | Export as SVG, convert to PNG at 300 DPI |
| Colors wrong | Check `style` syntax, use hex codes |

---

## Naming Convention for Mermaid-Generated Figures

Following standardized naming:
```
{model_number}_diagram_{description}.png
```

**Examples**:
- `model_0_diagram_data_pipeline.png`
- `model_1_diagram_hurdle_architecture.png`
- `model_2_diagram_hierarchy.png`
- `model_3_diagram_ensemble_flow.png`
- `model_0_diagram_state_transitions.png`
