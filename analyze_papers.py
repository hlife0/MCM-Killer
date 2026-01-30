# Complete analysis with all 8 papers

papers_analysis = []

# Paper 1: 2021A-2100454
papers_analysis.append({
    'label': '2021A-2100454',
    'year_problem': '2021-A',
    'total_pages': 24,
    'intro': 4,  # Introduction + background
    'model': 7,  # Model formulation
    'results': 6,  # Results and analysis
    'sensitivity': 2,  # Sensitivity analysis
    'conclusion': 1,  # Strengths/weaknesses/conclusion
    'references': 1,
    'appendix': 2
})

# Paper 2: 2020B-2007698
papers_analysis.append({
    'label': '2020B-2007698',
    'year_problem': '2020-B',
    'total_pages': 29,
    'intro': 2,
    'model': 13,  # Multiple models
    'results': 10,  # Results distributed through sections
    'sensitivity': 1,
    'conclusion': 2,  # S&W and conclusion
    'references': 1,
    'appendix': 0
})

# Paper 3: 2021B-2102199
papers_analysis.append({
    'label': '2021B-2102199',
    'year_problem': '2021-B',
    'total_pages': 24,
    'intro': 3,
    'model': 9,  # Model sections (pages 6-15)
    'results': 3,  # Verification and results (pages 15-18)
    'sensitivity': 2,  # Pages 19-20
    'conclusion': 1,  # S&W page 21
    'references': 1,
    'appendix': 5
})

# Paper 4: 2021C-2101166
papers_analysis.append({
    'label': '2021C-2101166',
    'year_problem': '2021-C',
    'total_pages': 24,
    'intro': 3,
    'model': 11,  # Pages 6-16 (multiple models)
    'results': 3,  # Results sections (pages 17-19)
    'sensitivity': 2,  # Pages 20-21
    'conclusion': 1,  # Page 21
    'references': 1,
    'appendix': 3
})

# Paper 5: 2022A-2200289
papers_analysis.append({
    'label': '2022A-2200289',
    'year_problem': '2022-A',
    'total_pages': 24,
    'intro': 3,
    'model': 10,  # Pages 6-15
    'results': 0,  # Integrated in models
    'sensitivity': 4,  # Pages 16-19
    'conclusion': 2,  # Pages 20-21 (Extension + S&W)
    'references': 1,
    'appendix': 4
})

# Paper 6: 2020C-2002116 (39 pages total)
papers_analysis.append({
    'label': '2020C-2002116',
    'year_problem': '2020-C',
    'total_pages': 38,  # 39-1 summary
    'intro': 1,
    'model': 12,  # Multiple complex models
    'results': 15,  # Results integrated throughout
    'sensitivity': 4,  # Distributed sensitivity analysis
    'conclusion': 2,
    'references': 1,
    'appendix': 3
})

# Paper 7: 2020D-2002526 (24 pages)
papers_analysis.append({
    'label': '2020D-2002526',
    'year_problem': '2020-D',
    'total_pages': 23,  # 24-1
    'intro': 3,  # Introduction and background
    'model': 10,  # Pages 4-13
    'results': 5,  # Results and analysis
    'sensitivity': 2,
    'conclusion': 1,
    'references': 1,
    'appendix': 1
})

# Paper 8: 2020A-2001334 (31 pages)
papers_analysis.append({
    'label': '2020A-2001334',
    'year_problem': '2020-A',
    'total_pages': 30,  # 31-1
    'intro': 2,
    'model': 12,  # Model I and Model II (pages 4-15)
    'results': 10,  # Results sections for both models
    'sensitivity': 2,
    'conclusion': 2,
    'references': 1,
    'appendix': 1
})

# Calculate statistics
import statistics

print('='*100)
print('SAMPLE PAPER SECTION BREAKDOWN')
print('='*100)
print()
print('Paper|Year|Total|Intro|Model|Results|Sensitivity|Conclusion|Refs|Appendix')
print('---|---|---|---|---|---|---|---|---|---')

for p in papers_analysis:
    print(f'{p["label"]}|{p["year_problem"]}|{p["total_pages"]}|{p["intro"]}|{p["model"]}|{p["results"]}|{p["sensitivity"]}|{p["conclusion"]}|{p["references"]}|{p["appendix"]}')

# Calculate averages
totals = [p['total_pages'] for p in papers_analysis]
intros = [p['intro'] for p in papers_analysis]
models = [p['model'] for p in papers_analysis]
results = [p['results'] for p in papers_analysis]
sensitivity = [p['sensitivity'] for p in papers_analysis]
conclusions = [p['conclusion'] for p in papers_analysis]
refs = [p['references'] for p in papers_analysis]
appendices = [p['appendix'] for p in papers_analysis]

print()
print('='*100)
print('STATISTICAL SUMMARY')
print('='*100)
print()
print(f'Average Total Pages (excluding summary): {statistics.mean(totals):.1f}')
print(f'Average Introduction: {statistics.mean(intros):.1f} pages ({statistics.mean(intros)/statistics.mean(totals)*100:.1f}%)')
print(f'Average Model Section: {statistics.mean(models):.1f} pages ({statistics.mean(models)/statistics.mean(totals)*100:.1f}%)')
print(f'Average Results Section: {statistics.mean(results):.1f} pages ({statistics.mean(results)/statistics.mean(totals)*100:.1f}%)')
print(f'Average Sensitivity: {statistics.mean(sensitivity):.1f} pages ({statistics.mean(sensitivity)/statistics.mean(totals)*100:.1f}%)')
print(f'Average Conclusion/S&W: {statistics.mean(conclusions):.1f} pages ({statistics.mean(conclusions)/statistics.mean(totals)*100:.1f}%)')
print(f'Average References: {statistics.mean(refs):.1f} pages ({statistics.mean(refs)/statistics.mean(totals)*100:.1f}%)')
print(f'Average Appendix: {statistics.mean(appendices):.1f} pages ({statistics.mean(appendices)/statistics.mean(totals)*100:.1f}%)')

print()
print('='*100)
print('RECOMMENDED PAGE BUDGETS FOR 28-PAGE SYSTEM')
print('='*100)
print()

# For a 28-page target (excluding summary sheet)
target_total = 28

# Calculate proportions and apply to 28 pages
intro_budget = round(statistics.mean(intros) / statistics.mean(totals) * target_total)
model_budget = round(statistics.mean(models) / statistics.mean(totals) * target_total)
results_budget = round(statistics.mean(results) / statistics.mean(totals) * target_total)
sensitivity_budget = round(statistics.mean(sensitivity) / statistics.mean(totals) * target_total)
conclusion_budget = round(statistics.mean(conclusions) / statistics.mean(totals) * target_total)
refs_budget = 1  # Always 1 page
appendix_budget = round(statistics.mean(appendices) / statistics.mean(totals) * target_total)

# Adjust to ensure total is exactly 28
budget_sum = intro_budget + model_budget + results_budget + sensitivity_budget + conclusion_budget + refs_budget + appendix_budget
diff = target_total - budget_sum

# Adjust the largest section if needed
if diff != 0:
    model_budget += diff

print('Section Type|Average Pages|28-Page Budget|Percentage')
print('---|---|---|---')
print(f'Introduction + Background|{statistics.mean(intros):.1f}|{intro_budget}|{intro_budget/target_total*100:.1f}%')
print(f'Model Formulation|{statistics.mean(models):.1f}|{model_budget}|{model_budget/target_total*100:.1f}%')
print(f'Results + Analysis|{statistics.mean(results):.1f}|{results_budget}|{results_budget/target_total*100:.1f}%')
print(f'Sensitivity Analysis|{statistics.mean(sensitivity):.1f}|{sensitivity_budget}|{sensitivity_budget/target_total*100:.1f}%')
print(f'Conclusion + Strengths/Weaknesses|{statistics.mean(conclusions):.1f}|{conclusion_budget}|{conclusion_budget/target_total*100:.1f}%')
print(f'References|{statistics.mean(refs):.1f}|{refs_budget}|{refs_budget/target_total*100:.1f}%')
print(f'Appendix (Code/Tables)|{statistics.mean(appendices):.1f}|{appendix_budget}|{appendix_budget/target_total*100:.1f}%')
print(f'**TOTAL**|**{statistics.mean(totals):.1f}**|**{target_total}**|**100%**')

print()
print('='*100)
print('PHASE 7 SUB-PHASE RECOMMENDATIONS')
print('='*100)
print()

# Map to Phase 7 structure
phase_7a = intro_budget  # Abstract + Intro + Notation
phase_7b = model_budget   # Model sections
phase_7c = results_budget  # Results + figures
phase_7d = sensitivity_budget + conclusion_budget  # Sensitivity + S/W
phase_7e = 0  # Discussion integrated into 7D
refs_app = refs_budget + appendix_budget

print('Phase|Description|Target Pages|Percentage')
print('---|---|---|---')
print(f'Phase 7A|Abstract + Introduction + Notation|{phase_7a}|{phase_7a/target_total*100:.1f}%')
print(f'Phase 7B|Model Development (all models)|{phase_7b}|{phase_7b/target_total*100:.1f}%')
print(f'Phase 7C|Results + Validation + Figures|{phase_7c}|{phase_7c/target_total*100:.1f}%')
print(f'Phase 7D|Sensitivity + Strengths/Weaknesses|{phase_7d}|{phase_7d/target_total*100:.1f}%')
print(f'Phase 7E|Conclusion (integrated into 7D)|included in 7D|included')
print(f'References + Appendix|Citations + Code/Supplementary|{refs_app}|{refs_app/target_total*100:.1f}%')
print(f'**TOTAL CONTENT**|**(excluding summary sheet)**|**{target_total}**|**100%**')

print()
print('='*100)
print('KEY INSIGHTS FROM O-PRIZE PAPER ANALYSIS')
print('='*100)
print()
print('1. Model Section Dominance:')
print(f'   - Model formulation takes up {statistics.mean(models)/statistics.mean(totals)*100:.0f}% of paper')
print('   - O-Prize papers prioritize detailed mathematical development')
print()
print('2. Results Integration:')
print(f'   - Results section varies widely ({min(results)}-{max(results)} pages)')
print('   - Many papers integrate results within model sections')
print('   - Focus on validation and visualization over extensive discussion')
print()
print('3. Compact Introduction:')
print(f'   - Introduction averages only {statistics.mean(intros):.1f} pages ({statistics.mean(intros)/statistics.mean(totals)*100:.0f}%)')
print('   - Papers get to the models quickly')
print('   - Background is concise and problem-focused')
print()
print('4. Sensitivity + Strengths/Weaknesses:')
print(f'   - Combined averages {statistics.mean(sensitivity) + statistics.mean(conclusions):.1f} pages')
print('   - Critical for demonstrating robustness')
print('   - Often includes model limitations')
print()
print('5. Page Count Range:')
print(f'   - Total pages range: {min(totals)}-{max(totals)} (excluding summary)')
print(f'   - Most papers: 24-30 pages')
print(f'   - Appendix varies significantly (0-5 pages)')
