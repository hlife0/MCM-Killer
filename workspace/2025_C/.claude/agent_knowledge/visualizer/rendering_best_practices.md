# Rendering Best Practices for Publication-Quality Diagrams

> **"A well-designed diagram rendered at 800px width is worse than a mediocre diagram rendered at 3000px. Resolution matters as much as design."**

This guide covers optimal rendering configurations, CLI commands, and quality assurance for publication-ready Mermaid diagrams.

---

## Mermaid CLI (mmdc) Configuration

### Installation

```bash
# Global installation (recommended)
npm install -g @mermaid-js/mermaid-cli

# Verify installation
mmdc --version
```

### Basic Rendering Command

```bash
mmdc -i input.mmd -o output.png -w 3000 -H 2000 -b white
```

### Command Parameters

| Parameter | Description | Recommended Value |
|-----------|-------------|-------------------|
| `-i` | Input file | `diagram.mmd` |
| `-o` | Output file | `output.png` or `output.svg` |
| `-w` | Width in pixels | **3000** (minimum for complex diagrams) |
| `-H` | Height in pixels | **2000** (auto-scales if omitted) |
| `-b` | Background color | `white` or `transparent` |
| `-c` | Config file (JSON) | `mermaid-config.json` |
| `-C` | CSS file | `custom.css` |
| `-t` | Theme | `default`, `forest`, `dark`, `neutral` |

---

## Resolution Guidelines

### By Diagram Complexity

| Complexity | Nodes | Width | Height | File Size |
|------------|-------|-------|--------|-----------|
| Simple | 5-10 | 2000px | 1500px | ~100KB |
| Medium | 10-20 | 2500px | 2000px | ~200KB |
| Complex | 20-40 | 3000px | 2500px | ~400KB |
| Very Complex | 40+ | 4000px | 3000px | ~600KB |

### For Paper Submission

```bash
# Standard figure (single column)
mmdc -i diagram.mmd -o figure.png -w 2400 -H 1800 -b white

# Large figure (full page width)
mmdc -i diagram.mmd -o figure.png -w 3600 -H 2400 -b white

# Architecture overview (poster-quality)
mmdc -i diagram.mmd -o figure.png -w 4800 -H 3200 -b white
```

### DPI Conversion

LaTeX and many publications require 300 DPI. To convert:

```bash
# Using ImageMagick
convert -units PixelsPerInch -density 300 input.png output.png

# Verification
identify -verbose output.png | grep -i resolution
```

**Width to DPI relationship:**
- 2400px at 300 DPI = 8 inches (standard column width)
- 3600px at 300 DPI = 12 inches (full page width)
- 4800px at 300 DPI = 16 inches (poster/presentation)

---

## Production Rendering Commands

### Command for Model Architecture Diagrams

```bash
mmdc -i model_1_diagram_architecture.mmd \
     -o model_1_diagram_architecture.png \
     -w 3000 \
     -H 2000 \
     -b white \
     -c mermaid-config.json
```

### Command for Data Pipeline Diagrams

```bash
mmdc -i model_0_diagram_pipeline.mmd \
     -o model_0_diagram_pipeline.png \
     -w 3500 \
     -H 1800 \
     -b white
```

### Command for State/Transition Diagrams

```bash
mmdc -i model_0_diagram_states.mmd \
     -o model_0_diagram_states.png \
     -w 2800 \
     -H 2400 \
     -b white
```

### Batch Rendering Script

```bash
#!/bin/bash
# render_all_diagrams.sh

OUTPUT_DIR="output/figures"
WIDTH=3000
HEIGHT=2000

for mmd_file in *.mmd; do
    base_name="${mmd_file%.mmd}"
    echo "Rendering: $mmd_file"
    mmdc -i "$mmd_file" \
         -o "${OUTPUT_DIR}/${base_name}.png" \
         -w $WIDTH \
         -H $HEIGHT \
         -b white
done

echo "All diagrams rendered to $OUTPUT_DIR"
```

---

## Configuration File (mermaid-config.json)

Create this file in your working directory for consistent rendering:

```json
{
  "theme": "base",
  "themeVariables": {
    "primaryColor": "#4a90d9",
    "primaryTextColor": "#ffffff",
    "primaryBorderColor": "#2c5282",
    "lineColor": "#4a5568",
    "secondaryColor": "#90cdf4",
    "tertiaryColor": "#f7fafc",
    "fontSize": "16px",
    "fontFamily": "Arial, Helvetica, sans-serif"
  },
  "flowchart": {
    "htmlLabels": true,
    "curve": "basis",
    "nodeSpacing": 50,
    "rankSpacing": 50,
    "padding": 15
  },
  "sequence": {
    "diagramMarginX": 50,
    "diagramMarginY": 10,
    "actorMargin": 50,
    "width": 150,
    "height": 65,
    "boxMargin": 10,
    "boxTextMargin": 5,
    "noteMargin": 10,
    "messageMargin": 35
  }
}
```

### Using the Config File

```bash
mmdc -i diagram.mmd -o output.png -w 3000 -c mermaid-config.json
```

---

## Custom CSS for Advanced Styling

Create `mermaid-custom.css` for fine-grained control:

```css
/* Node text styling */
.node rect,
.node circle,
.node ellipse,
.node polygon,
.node path {
    stroke-width: 2px;
}

/* Subgraph styling */
.cluster rect {
    stroke-width: 2px !important;
    rx: 8px;
    ry: 8px;
}

/* Subgraph label */
.cluster-label {
    font-weight: bold;
    font-size: 16px;
}

/* Edge/Arrow styling */
.edgePath .path {
    stroke-width: 2px;
}

/* Arrow markers */
.marker {
    fill: #4a5568;
}

/* Edge labels */
.edgeLabel {
    background-color: white;
    padding: 2px 4px;
    font-size: 12px;
}
```

### Using Custom CSS

```bash
mmdc -i diagram.mmd -o output.png -w 3000 -C mermaid-custom.css
```

---

## SVG vs PNG Trade-offs

### When to Use PNG

- **Paper submission** - Most journals accept/prefer PNG
- **Consistent rendering** - Looks the same everywhere
- **Complex diagrams** - Better performance in documents
- **Backgrounds needed** - Solid white background for print

```bash
# PNG rendering
mmdc -i diagram.mmd -o output.png -w 3000 -b white
```

### When to Use SVG

- **Web presentations** - Infinite scaling
- **Editing required** - Can modify in Inkscape/Illustrator
- **Small file size** - Text-based, compresses well
- **High DPI displays** - No pixelation

```bash
# SVG rendering
mmdc -i diagram.mmd -o output.svg -b white
```

### SVG to High-Quality PNG Conversion

```bash
# Using Inkscape (recommended)
inkscape --export-type=png --export-dpi=300 input.svg -o output.png

# Using ImageMagick
convert -density 300 input.svg -background white -flatten output.png

# Using rsvg-convert (fast)
rsvg-convert -d 300 -p 300 input.svg > output.png
```

---

## Background Options

### Solid White (Recommended for Papers)

```bash
mmdc -i diagram.mmd -o output.png -w 3000 -b white
```

### Transparent (for Overlays)

```bash
mmdc -i diagram.mmd -o output.png -w 3000 -b transparent
```

Note: Transparent backgrounds work only with PNG, not JPEG.

### Custom Background Color

```bash
mmdc -i diagram.mmd -o output.png -w 3000 -b "#f7fafc"
```

---

## Quality Verification Checklist

After rendering, verify each diagram:

### Visual Inspection

- [ ] Text is crisp and readable (zoom to 100%)
- [ ] No aliasing artifacts on edges
- [ ] Colors match specification
- [ ] Subgraph backgrounds are visible

### Technical Checks

```bash
# Check dimensions
identify output.png
# Expected: output.png PNG 3000x2000 ...

# Check file size (should be substantial for complex diagrams)
ls -lh output.png
# Expected: 200KB-600KB for complex diagrams

# Check for corruption
file output.png
# Expected: PNG image data, 3000 x 2000, 8-bit/color RGBA, non-interlaced
```

### Resolution Verification

```bash
# Using ImageMagick
identify -verbose output.png | grep -E "Resolution|Geometry"
```

---

## Troubleshooting Common Issues

### Issue: Text Too Small

**Cause**: Low resolution or small font size in config

**Solution**:
```bash
# Increase width
mmdc -i diagram.mmd -o output.png -w 4000

# Or update config
{
  "themeVariables": {
    "fontSize": "18px"
  }
}
```

### Issue: Diagram Cut Off

**Cause**: Height insufficient for content

**Solution**:
```bash
# Let height auto-calculate (omit -H)
mmdc -i diagram.mmd -o output.png -w 3000

# Or increase height explicitly
mmdc -i diagram.mmd -o output.png -w 3000 -H 3000
```

### Issue: Colors Not Applied

**Cause**: Syntax error in classDef or style

**Solution**:
1. Validate Mermaid syntax at https://mermaid.live/
2. Check hex color format (use `#4a90d9` not `4a90d9`)
3. Ensure classDef comes before node definitions

### Issue: Fuzzy/Blurry Edges

**Cause**: Low resolution or JPEG compression

**Solution**:
```bash
# Use PNG (not JPEG)
mmdc -i diagram.mmd -o output.png -w 3000

# Increase resolution
mmdc -i diagram.mmd -o output.png -w 4000
```

### Issue: Fonts Don't Match

**Cause**: Font not available on rendering system

**Solution**:
```json
{
  "themeVariables": {
    "fontFamily": "Arial, Helvetica, sans-serif"
  }
}
```

Use web-safe fonts: Arial, Helvetica, Georgia, Times New Roman

---

## Workflow: From Design to Publication

### Step 1: Create Mermaid File

```bash
# Create diagram file
cat > model_1_diagram_architecture.mmd << 'EOF'
%%{init: {'theme': 'base', 'themeVariables': {...}}}%%
flowchart TB
    ...
EOF
```

### Step 2: Preview (Optional)

- Open https://mermaid.live/
- Paste code and verify layout
- Adjust as needed

### Step 3: Render High Resolution

```bash
mmdc -i model_1_diagram_architecture.mmd \
     -o output/figures/model_1_diagram_architecture.png \
     -w 3000 \
     -b white \
     -c mermaid-config.json
```

### Step 4: Verify Quality

```bash
# Check output
identify output/figures/model_1_diagram_architecture.png
file output/figures/model_1_diagram_architecture.png
```

### Step 5: Convert DPI if Needed

```bash
# For journals requiring 300 DPI
convert -units PixelsPerInch -density 300 \
        output/figures/model_1_diagram_architecture.png \
        output/figures/model_1_diagram_architecture_300dpi.png
```

---

## Quick Reference: Production Commands

```bash
# Standard diagram (recommended)
mmdc -i diagram.mmd -o output.png -w 3000 -H 2000 -b white

# Large architecture
mmdc -i diagram.mmd -o output.png -w 4000 -b white

# With config file
mmdc -i diagram.mmd -o output.png -w 3000 -c mermaid-config.json

# SVG output
mmdc -i diagram.mmd -o output.svg -b white

# Batch all .mmd files
for f in *.mmd; do mmdc -i "$f" -o "${f%.mmd}.png" -w 3000 -b white; done
```

---

## File Naming Convention

```
{model_number}_diagram_{description}.{ext}
```

**Examples:**
- `model_0_diagram_data_pipeline.png`
- `model_1_diagram_hurdle_architecture.png`
- `model_2_diagram_hierarchy.png`
- `model_3_diagram_ensemble_flow.png`
- `model_0_diagram_state_transitions.png`

**Source files:**
- `model_0_diagram_data_pipeline.mmd`
- `model_1_diagram_hurdle_architecture.mmd`
