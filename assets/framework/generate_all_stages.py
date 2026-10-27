import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def base_canvas(title_stage, title_main, title_sub, badge_color='#38bdf8'):
    fig, ax = plt.subplots(figsize=(20, 11.25), dpi=150)
    fig.patch.set_facecolor('#0b1120')
    ax.set_facecolor('#0b1120')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Top Pill Badge
    pill = patches.FancyBboxPatch((4, 91.5), 26, 4.2, boxstyle="round,pad=0.5", 
                                  facecolor='#1e293b', edgecolor=badge_color, linewidth=1.5)
    ax.add_patch(pill)
    ax.text(17, 93.6, title_stage, color=badge_color, fontsize=11.5, fontweight='bold', ha='center', va='center')

    # Main Header
    ax.text(4, 86.5, title_main, color='#ffffff', fontsize=25, fontweight='bold', ha='left', va='center')
    ax.text(4, 82.5, title_sub, color='#94a3b8', fontsize=12.5, ha='left', va='center')

    # Divider
    ax.plot([4, 96], [79.5, 79.5], color='#334155', linewidth=1.2)
    return fig, ax

def save_and_close(fig, output_path):
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight', pad_inches=0.15)
    plt.close(fig)
    print("Saved:", output_path)

# ==================== STAGE 1: EMPATHIZE ====================
def generate_stage_1(output_path):
    fig, ax = base_canvas("DESIGN THINKING • STAGE 01",
                          "Stage 1: Empathize — Stakeholder 5W1H, Empathy Map & Dataset Exploration",
                          "Pre-Dashboard Discovery: Understanding the Marketing Manager's ROI challenges, decision cadence, and data silos",
                          badge_color='#0284c7')

    # Left: 5W1H Analysis
    b1 = patches.FancyBboxPatch((4, 23), 44, 53, boxstyle="round,pad=0.6", facecolor='#131e36', edgecolor='#1e293b', linewidth=1.5)
    ax.add_patch(b1)
    h1 = patches.FancyBboxPatch((4.5, 68.5), 43, 6.8, boxstyle="round,pad=0.3", facecolor='#0284c7', edgecolor='#38bdf8', linewidth=1.2)
    ax.add_patch(h1)
    ax.text(26.0, 71.9, "5W1H STAKEHOLDER DISCOVERY (MARKETING & SALES)", color='#ffffff', fontsize=13.0, fontweight='bold', ha='center', va='center')

    items_5w1h = [
        ("WHO (Key Stakeholders)", "Senior Marketing Manager & Sales Director — Responsible for digital ad expenditure,\ncampaign revenue contribution, acquisition channels, and retail merchandise sell-through."),
        ("WHAT (The Business Challenge)", "Ad spend is fragmented across 100+ ad sets without clear sales attribution;\nmarketing cost and retail revenue live in disconnected silos, masking true campaign ROI."),
        ("WHEN & WHERE", "Consulted daily for campaign spend pacing, weekly in Marketing ROI Reviews, and\nmonthly in Executive Board budget allocation and merchandising planning meetings."),
        ("WHY (Analytical Purpose)", "Eliminate wasted ad spend, identify high-converting fashion SKUs and campaigns,\noptimize Return on Ad Spend (ROAS), and safeguard profitable retail gross margins."),
        ("HOW (Dashboard Mandate)", "Build an integrated Marketing & Sales Intelligence Control Tower establishing full-funnel\nvisibility from Impression -> Click -> Inbox/Message -> Paid Conversion.")
    ]
    curr_y = 65.0
    for title, desc in items_5w1h:
        card = patches.FancyBboxPatch((5.5, curr_y - 7.4), 41, 7.0, boxstyle="round,pad=0.3", facecolor='#1e293b', edgecolor='#334155', linewidth=1.0)
        ax.add_patch(card)
        p = patches.FancyBboxPatch((6.5, curr_y - 3.2), 0.5, 1.8, boxstyle="round,pad=0.1", facecolor='#38bdf8', edgecolor='none')
        ax.add_patch(p)
        ax.text(7.6, curr_y - 2.2, title, color='#38bdf8', fontsize=10.5, fontweight='bold', ha='left')
        ax.text(7.6, curr_y - 5.0, desc, color='#cbd5e1', fontsize=8.8, ha='left', va='center')
        curr_y -= 8.3

    # Right: Empathy Map
    b2 = patches.FancyBboxPatch((52, 23), 44, 53, boxstyle="round,pad=0.6", facecolor='#131e36', edgecolor='#1e293b', linewidth=1.5)
    ax.add_patch(b2)
    h2 = patches.FancyBboxPatch((52.5, 68.5), 43, 6.8, boxstyle="round,pad=0.3", facecolor='#0369a1', edgecolor='#38bdf8', linewidth=1.2)
    ax.add_patch(h2)
    ax.text(74.0, 71.9, "EXECUTIVE EMPATHY MAP (STAKEHOLDER MINDSET)", color='#ffffff', fontsize=13.0, fontweight='bold', ha='center', va='center')

    quads = [
        ("THINKING & FEELING (Questions Stakeholders Ask)", [
            "• 'Is marketing spend being wasted on low-converting ads?'",
            "• 'If I double the budget for this campaign, will revenue scale?'",
            "• 'Which apparel category deserves the largest marketing push?'",
            "• Under heavy pressure to defend marketing ROI before the CEO."
        ], 53.5, 47.0),
        ("SEEING & DOING (Current Operating Reality)", [
            "• Massive ad spend outflow without automated revenue tracking.",
            "• Manually combining Facebook/Tiktok ad reports with POS data.",
            "• Budget adjustments made on intuition rather than concrete ROAS.",
            "• Overwhelmed by 300+ apparel SKUs with varied performance."
        ], 74.5, 47.0),
        ("PAINS (Key Frustrations to Resolve)", [
            "• Ad cost and transaction revenue trapped in separate databases.",
            "• Cannot identify which campaigns drive actual cash vs vanity clicks.",
            "• Low-ROAS campaigns drain budget while star SKUs are capped.",
            "• Lack of week-over-week (WoW) trajectory to monitor ad fatigue."
        ], 53.5, 25.0),
        ("GAINS (Expected Discovery Outcomes)", [
            "• Precise, granular ROAS calculated per campaign and per SKU.",
            "• Instant identification of hero products vs budget drainers.",
            "• Clear budget reallocation roadmap to maximize gross revenue.",
            "• Rapid executive reporting for C-suite decision-making."
        ], 74.5, 25.0)
    ]
    for q_title, bullets, qx, qy in quads:
        border_col = '#f43f5e' if 'PAINS' in q_title else ('#10b981' if 'GAINS' in q_title else '#334155')
        title_col = '#fb7185' if 'PAINS' in q_title else ('#34d399' if 'GAINS' in q_title else '#38bdf8')
        q_box = patches.FancyBboxPatch((qx - 0.5, qy), 20, 19.5, boxstyle="round,pad=0.4", facecolor='#1e293b', edgecolor=border_col, linewidth=1.1)
        ax.add_patch(q_box)
        ax.text(qx + 0.5, qy + 17.5, q_title, color=title_col, fontsize=9.8, fontweight='bold', ha='left')
        by = qy + 14.0
        for b in bullets:
            ax.text(qx + 0.5, by, b, color='#cbd5e1', fontsize=8.2, ha='left', va='top')
            by -= 3.8

    # Bottom Strip
    f = patches.FancyBboxPatch((4, 4), 92, 14.5, boxstyle="round,pad=0.5", facecolor='#1e293b', edgecolor='#0284c7', linewidth=1.2)
    ax.add_patch(f)
    ax.text(6, 15.2, "DATASET SCOPE & STAKEHOLDER NEED INVENTORIED AT STAGE 1:", color='#38bdf8', fontsize=11.5, fontweight='bold', ha='left')
    ax.text(6, 11.0, "• Data Architecture: 5 Tables identified (2 Fact Tables: fact_order, fact_mkt_camp_by_sku_cost | 3 Dim Tables: dim_danh_sach_san_pham, dim_mkt_camp_cost, Dim_Date).\n• Key Stakeholder Questions Defined: (1) How is marketing spend distributed over time? (2) Does marketing deliver revenue commensurate with ad spend (ROAS)?\n  (3) Which specific campaigns and fashion SKUs are genuine growth drivers? (4) How should marketing budget be reallocated to maximize profit while mitigating hero-SKU risk?", 
            color='#f1f5f9', fontsize=9.8, ha='left', va='center')

    save_and_close(fig, output_path)

# ==================== STAGE 2: DEFINE POV ====================
def generate_stage_2(output_path):
    fig, ax = base_canvas("DESIGN THINKING • STAGE 02",
                          "Stage 2: Define Point of View (POV) — Dual Northstars & Analytical Perspectives",
                          "Pre-Dashboard Discovery: Formulating the core metric hypotheses, growth equations, and 4 operational lenses",
                          badge_color='#059669')

    # Left: Dual Northstars
    b1 = patches.FancyBboxPatch((4, 23), 29, 53, boxstyle="round,pad=0.6", facecolor='#131e36', edgecolor='#1e293b', linewidth=1.5)
    ax.add_patch(b1)
    h1 = patches.FancyBboxPatch((4.5, 68.5), 28, 6.8, boxstyle="round,pad=0.3", facecolor='#059669', edgecolor='#34d399', linewidth=1.2)
    ax.add_patch(h1)
    ax.text(18.5, 71.9, "DUAL NORTHSTAR HYPOTHESIS", color='#ffffff', fontsize=12.5, fontweight='bold', ha='center', va='center')

    # Card 1: Northstar 1
    c1 = patches.FancyBboxPatch((5.5, 47.0), 26, 19.5, boxstyle="round,pad=0.3", facecolor='#1e293b', edgecolor='#334155', linewidth=1.0)
    ax.add_patch(c1)
    ax.text(7.0, 63.5, "NORTHSTAR 1: Scale & Value", color='#34d399', fontsize=11, fontweight='bold', ha='left')
    ax.text(7.0, 59.5, "• Target Measure: Marketing Revenue", color='#f8fafc', fontsize=10, fontweight='bold', ha='left')
    ax.text(7.0, 56.0, "• Supporting Metrics: MKT Revenue Contrib %,", color='#cbd5e1', fontsize=9.2, ha='left')
    ax.text(7.0, 53.0, "  Total Revenue, Attributed Order Volume.", color='#cbd5e1', fontsize=9.2, ha='left')
    ax.text(7.0, 49.5, "Why: Directly quantifies marketing's commercial", color='#94a3b8', fontsize=8.6, ha='left')
    ax.text(7.0, 47.0, "contribution to overall company turnover.", color='#94a3b8', fontsize=8.6, ha='left')

    # Card 2: Northstar 2
    c2 = patches.FancyBboxPatch((5.5, 25.0), 26, 19.5, boxstyle="round,pad=0.3", facecolor='#1e293b', edgecolor='#334155', linewidth=1.0)
    ax.add_patch(c2)
    ax.text(7.0, 41.5, "NORTHSTAR 2: Capital Efficiency", color='#f59e0b', fontsize=11, fontweight='bold', ha='left')
    ax.text(7.0, 37.5, "• Target Measure: Blended ROAS", color='#f8fafc', fontsize=10, fontweight='bold', ha='left')
    ax.text(7.0, 34.0, "• Supporting Metrics: % Budget Utilization,", color='#cbd5e1', fontsize=9.2, ha='left')
    ax.text(7.0, 31.0, "  CPC, CPM, Cost Per Result (CPA).", color='#cbd5e1', fontsize=9.2, ha='left')
    ax.text(7.0, 27.5, "Why: Ensures top-line growth is achieved with high", color='#94a3b8', fontsize=8.6, ha='left')
    ax.text(7.0, 25.0, "capital productivity without burning ad cash.", color='#94a3b8', fontsize=8.6, ha='left')

    # Center: Growth Formula & Metric Logic
    b2 = patches.FancyBboxPatch((35, 23), 30, 53, boxstyle="round,pad=0.6", facecolor='#131e36', edgecolor='#1e293b', linewidth=1.5)
    ax.add_patch(b2)
    h2 = patches.FancyBboxPatch((35.5, 68.5), 29, 6.8, boxstyle="round,pad=0.3", facecolor='#0d9488', edgecolor='#2dd4bf', linewidth=1.2)
    ax.add_patch(h2)
    ax.text(50.0, 71.9, "GROWTH FORMULA & METRIC LOGIC", color='#ffffff', fontsize=12.0, fontweight='bold', ha='center', va='center')

    eqs = [
        ("Gross Revenue Decomposition", "Total Revenue = Marketing Revenue + Direct Revenue\n• Hypothesized need: Evaluate the balance between\n  paid acquisition and organic/direct brand retention\n  to assess dependency risks."),
        ("Full-Funnel Ad Conversion Logic", "MKT Revenue = Spend x ROAS\n  = (Impr x CTR x CPC) x Conv Rate x AOV\n• Objective: Trace conversion leakages from ad\n  engagement down to completed retail orders."),
        ("Capital Allocation Efficiency", "Budget Utilization % = Actual Spend / Budget Cap\n• ROAS Efficiency Ratio = Attributed Revenue / Spend\n• Objective: Identify over-budget underperformers vs\n  star campaigns starved of ad capital.")
    ]
    ey = 65.0
    for eq_title, eq_desc in eqs:
        ec = patches.FancyBboxPatch((36.5, ey - 12.5), 27, 12.0, boxstyle="round,pad=0.3", facecolor='#1e293b', edgecolor='#334155', linewidth=1.0)
        ax.add_patch(ec)
        ax.text(38.0, ey - 3.0, eq_title, color='#2dd4bf', fontsize=10.5, fontweight='bold', ha='left')
        ax.text(38.0, ey - 7.5, eq_desc, color='#cbd5e1', fontsize=8.8, ha='left', va='center')
        ey -= 13.5

    # Right: 4 Analytical Perspectives (Lenses)
    b3 = patches.FancyBboxPatch((67, 23), 29, 53, boxstyle="round,pad=0.6", facecolor='#131e36', edgecolor='#1e293b', linewidth=1.5)
    ax.add_patch(b3)
    h3 = patches.FancyBboxPatch((67.5, 68.5), 28, 6.8, boxstyle="round,pad=0.3", facecolor='#0284c7', edgecolor='#38bdf8', linewidth=1.2)
    ax.add_patch(h3)
    ax.text(81.5, 71.9, "4 ANALYTICAL PERSPECTIVES (POV LENSES)", color='#ffffff', fontsize=12.0, fontweight='bold', ha='center', va='center')

    lenses = [
        ("POV 1: Executive Overview", "Question: How is marketing driving overall business health?\nTarget Metrics: Total Revenue, MKT Revenue %, Spend,\nBudget Utilization %, Blended ROAS, Total Orders."),
        ("POV 2: Campaign Performance", "Question: Are marketing campaigns operating efficiently?\nTarget Metrics: Campaign ROAS, Spend vs. Budget,\nFunnel conversion: Impressions, Clicks, Inboxes, Orders."),
        ("POV 3: Product Merchandising", "Question: Which fashion products drive profitable returns?\nTarget Metrics: Category revenue, Hero SKU leaderboard,\nMarketing vs. Direct revenue contribution per product."),
        ("POV 4: Strategic Recommendations", "Question: How should ad spend be reallocated?\nTarget Output: Actionable P1-P4 matrix linking budget\nreallocation to expected revenue and margin expansion.")
    ]
    ly = 65.0
    for l_title, l_desc in lenses:
        lc = patches.FancyBboxPatch((68.5, ly - 9.0), 26, 8.5, boxstyle="round,pad=0.3", facecolor='#1e293b', edgecolor='#334155', linewidth=1.0)
        ax.add_patch(lc)
        ax.text(70.0, ly - 2.5, l_title, color='#38bdf8', fontsize=10.0, fontweight='bold', ha='left')
        ax.text(70.0, ly - 6.0, l_desc, color='#cbd5e1', fontsize=8.4, ha='left', va='center')
        ly -= 10.0

    # Bottom Callout Strip
    f = patches.FancyBboxPatch((4, 4), 92, 14.5, boxstyle="round,pad=0.5", facecolor='#1e293b', edgecolor='#059669', linewidth=1.2)
    ax.add_patch(f)
    ax.text(6, 15.0, "CORE POINT OF VIEW (POV) STATEMENT DEFINED IN DISCOVERY BLUEPRINT:", color='#34d399', fontsize=11.5, fontweight='bold', ha='left')
    ax.text(6, 10.5, "The Senior Marketing Manager needs an omnichannel ROI dashboard because evaluating ad costs without granular sales attribution results in misallocated budgets.\nBy organizing analysis across 4 progressive analytical layers (Executive Health -> Campaign Efficiency -> Merchandising Drivers -> Strategic Action),\nthe BI solution establishes an objective framework to redirect ad dollars toward high-margin hero SKUs while curbing wasted ad spend.", 
            color='#f1f5f9', fontsize=9.8, ha='left', va='center')

    save_and_close(fig, output_path)

# ==================== STAGE 3: IDEATE ====================
def generate_stage_3(output_path):
    fig, ax = base_canvas("DESIGN THINKING • STAGE 03",
                          "Stage 3: Ideate — Information Hierarchy & 4-Page Architecture",
                          "Pre-Dashboard Discovery: Brainstorming metric breakdown layers and structuring page layouts to prevent cognitive fatigue",
                          badge_color='#d97706')

    # Left: 3-Layer Information Hierarchy
    b1 = patches.FancyBboxPatch((4, 23), 44, 53, boxstyle="round,pad=0.6", facecolor='#131e36', edgecolor='#1e293b', linewidth=1.5)
    ax.add_patch(b1)
    h1 = patches.FancyBboxPatch((4.5, 68.5), 43, 6.8, boxstyle="round,pad=0.3", facecolor='#d97706', edgecolor='#fbbf24', linewidth=1.2)
    ax.add_patch(h1)
    ax.text(26.0, 71.9, "3-LAYER METRIC BREAKDOWN (TEMPLATE DESIGN)", color='#ffffff', fontsize=13.0, fontweight='bold', ha='center', va='center')

    layers = [
        ("LAYER 0: SCORECARD METRICS (Macro Signals)", 
         "• Definition: Top-of-page KPI cards delivering instant situational awareness.\n• Features: Value + Week-over-Week (WoW) variance dynamic color-coded labels.\n• Target Measures: Total Revenue, Marketing Revenue, Marketing Spend,\n  Blended ROAS, % Budget Utilization, Total Orders.",
         '#fbbf24'),
        ("LAYER 1: 1-DIMENSIONAL BREAKDOWN (Directional Trends)",
         "• Definition: Core KPIs sliced across a single key business dimension.\n• Planned Visuals: Dual-axis combo trend charts, horizontal bar charts, donut curves.\n• Target Views: Spend vs Revenue Trend by Week, Prospecting vs Retargeting split,\n  Budget Utilization Distribution, Category Revenue shares.",
         '#38bdf8'),
        ("LAYER 2: 2-DIMENSIONAL BREAKDOWN (Cross-Diagnostic Interactions)",
         "• Definition: Deep-dive interactions cross-analyzing two business dimensions.\n• Planned Visuals: Scatter bubble matrix, ranked product tables, stacked contributions.\n• Target Interactions: Campaign Efficiency (Spend vs. ROAS Bubble Matrix),\n  Product Category Summary by Channel, Marketing vs. Direct Revenue per SKU.",
         '#34d399')
    ]
    ly = 65.0
    for title, desc, col in layers:
        card = patches.FancyBboxPatch((5.5, ly - 12.5), 41, 12.0, boxstyle="round,pad=0.3", facecolor='#1e293b', edgecolor='#334155', linewidth=1.0)
        ax.add_patch(card)
        p = patches.FancyBboxPatch((6.5, ly - 3.2), 0.5, 1.8, boxstyle="round,pad=0.1", facecolor=col, edgecolor='none')
        ax.add_patch(p)
        ax.text(7.6, ly - 2.2, title, color=col, fontsize=10.5, fontweight='bold', ha='left')
        ax.text(7.6, ly - 7.5, desc, color='#cbd5e1', fontsize=8.8, ha='left', va='center')
        ly -= 13.5

    # Right: 4-Page Dashboard Layout Structure
    b2 = patches.FancyBboxPatch((52, 23), 44, 53, boxstyle="round,pad=0.6", facecolor='#131e36', edgecolor='#1e293b', linewidth=1.5)
    ax.add_patch(b2)
    h2 = patches.FancyBboxPatch((52.5, 68.5), 43, 6.8, boxstyle="round,pad=0.3", facecolor='#b45309', edgecolor='#f59e0b', linewidth=1.2)
    ax.add_patch(h2)
    ax.text(74.0, 71.9, "4-PAGE DASHBOARD STRUCTURE & MANDATES", color='#ffffff', fontsize=13.0, fontweight='bold', ha='center', va='center')

    pages = [
        ("PAGE 1: Executive Overview", "Role: Corporate Pulse & Growth Health\n• Displays top scorecards with WoW variance, weekly Spend vs Revenue trend,\n  Prospecting vs Retargeting split, and Budget Utilization pacing distribution."),
        ("PAGE 2: Campaign Performance Analysis", "Role: Ad Set Optimization & Efficiency Evaluation\n• Houses the Spend vs ROAS Scatter Bubble Matrix, compares Allocated Budget vs\n  Actual Spend, and delivers a granular funnel table (Impr, Clicks, CTR, CPC, Orders)."),
        ("PAGE 3: Product & Merchandising Analysis", "Role: Catalog Contribution & Inventory Alignment\n• Dissects revenue contribution across apparel categories, ranks Hero SKUs,\n  and contrasts Marketing vs Direct organic sales contribution per product."),
        ("PAGE 4: Strategic Insights & Recommendations", "Role: Executive Synthesis & Action Roadmap\n• Synthesizes findings using the Finding -> Evidence -> Business Impact -> Action\n  framework, delivering a concrete P1-P4 budget reallocation roadmap.")
    ]
    py = 65.0
    for p_title, p_desc in pages:
        p_card = patches.FancyBboxPatch((53.5, py - 9.2), 41, 8.8, boxstyle="round,pad=0.3", facecolor='#1e293b', edgecolor='#334155', linewidth=1.0)
        ax.add_patch(p_card)
        ax.text(55.0, py - 2.5, p_title, color='#fbbf24', fontsize=10.5, fontweight='bold', ha='left')
        ax.text(55.0, py - 6.0, p_desc, color='#cbd5e1', fontsize=8.6, ha='left', va='center')
        py -= 10.2

    # Bottom Strip
    f = patches.FancyBboxPatch((4, 4), 92, 14.5, boxstyle="round,pad=0.5", facecolor='#1e293b', edgecolor='#d97706', linewidth=1.2)
    ax.add_patch(f)
    ax.text(6, 15.0, "IDEATION PRINCIPLE: PURPOSE-DRIVEN PAGINATION OVER CROWDED CANVASES", color='#fbbf24', fontsize=11.5, fontweight='bold', ha='left')
    ax.text(6, 10.5, "As defined in Design Thinking Ver 4: 'Each page must have 1 specific role and serve 1 dedicated purpose.'\nBy structuring metrics into Layer 0 (Scorecard), Layer 1 (1D Trend), and Layer 2 (2D Interaction), executive leaders can scan business health\nin 10 seconds while performance marketers can drill down into granular ad sets and SKU unit economics on specialized pages.", 
            color='#f1f5f9', fontsize=9.8, ha='left', va='center')

    save_and_close(fig, output_path)

# ==================== STAGE 4: PROTOTYPE ====================
def generate_stage_4(output_path):
    fig, ax = base_canvas("DESIGN THINKING • STAGE 04",
                          "Stage 4: Prototype — Visual Selection Matrix & Wireframing Standards",
                          "Pre-Dashboard Discovery: Selecting optimal chart types, visual layout hierarchy, and semantic color schemes",
                          badge_color='#7c3aed')

    visuals = [
        ("SCATTER BUBBLE EFFICIENCY MATRIX", "Target: Page 2 (Campaign Analysis)",
         "• Objective: Diagnose ad efficiency by cross-plotting Spend vs. ROAS.\n• Visual Mechanism: 4-quadrant bubble chart where bubble size represents\n  attributed revenue; reference lines mark average ROAS & median spend.\n• Design Decision: Instantly exposes over-funded underperformers (Money Pits)\n  and high-converting ad sets ripe for budget scaling (Hidden Gems).",
         '#c084fc', 4, 47),
        ("DUAL-AXIS SPEND VS REVENUE TREND", "Target: Page 1 (Executive Overview)",
         "• Objective: Contrast weekly marketing expenditure against attributed revenue.\n• Visual Mechanism: Clustered column bars for spend paired with a line\n  curve for marketing revenue progression across weeks.\n• Design Decision: Reveals ad spend pacing and lag effects in sales conversion\n  without forcing the user to toggle between separate reports.",
         '#38bdf8', 52, 47),
        ("100% STACKED REVENUE CONTRIBUTION", "Target: Page 3 (Product Analysis)",
         "• Objective: Evaluate organic brand strength vs paid ad dependence per category.\n• Visual Mechanism: 100% stacked horizontal bar chart contrasting Marketing\n  Attributed Revenue vs Direct/Organic Revenue per merchandise category.\n• Design Decision: Makes paid dependency immediately obvious across categories\n  (e.g., Dresses vs Accessories) to guide merchandising strategy.",
         '#34d399', 4, 18),
        ("REPORT-PAGE TOOLTIPS (MICRO-UX)", "Target: Cross-Page UX Feature",
         "• Objective: Deliver contextual diagnostic granularity on hover without clutter.\n• Visual Mechanism: 3 dedicated tooltip canvases:\n  - Tooltip_Campaign_type: CTR, CPM, New Customer conversion rates\n  - Tooltip_product_detail: SKU image, unit economics, ROAS & ROI\n  - Tooltip_Campaign_detail: Daily trajectory of impressions, clicks & chats.",
         '#f59e0b', 52, 18)
    ]

    for title, page, desc, color, vx, vy in visuals:
        card = patches.FancyBboxPatch((vx, vy), 44, 27, boxstyle="round,pad=0.5", facecolor='#131e36', edgecolor='#1e293b', linewidth=1.5)
        ax.add_patch(card)
        hdr = patches.FancyBboxPatch((vx + 0.5, vy + 21.0), 43, 5.2, boxstyle="round,pad=0.3", facecolor='#1e293b', edgecolor=color, linewidth=1.2)
        ax.add_patch(hdr)
        ax.text(vx + 2.0, vy + 23.6, title, color=color, fontsize=11.5, fontweight='bold', ha='left', va='center')
        ax.text(vx + 41.5, vy + 23.6, page, color='#94a3b8', fontsize=9.0, fontstyle='italic', ha='right', va='center')
        ax.text(vx + 2.0, vy + 10.5, desc, color='#cbd5e1', fontsize=9.0, ha='left', va='center')

    # Bottom Strip
    f = patches.FancyBboxPatch((4, 3.5), 92, 11.5, boxstyle="round,pad=0.5", facecolor='#1e293b', edgecolor='#7c3aed', linewidth=1.2)
    ax.add_patch(f)
    ax.text(6, 11.8, "PROTOTYPING CRITERIA FROM TEMPLATE WORKSHOP:", color='#c084fc', fontsize=11.5, fontweight='bold', ha='left')
    ax.text(6, 7.5, "1. Information Hierarchy: Follow strict Z-pattern layout (Scorecards top -> 1D Trend center -> 2D Breakdown bottom).\n2. Color Palette: Adopt 'Accessible Orchid' theme — high contrast, professional purple/teal accents, avoiding harsh primary saturations.\n3. Micro-Interactions: Employ Report-Page Tooltips and Field Parameters to enable seamless dimension switching without cluttering the canvas.", 
            color='#f1f5f9', fontsize=9.6, ha='left', va='center')

    save_and_close(fig, output_path)

# ==================== STAGE 5: REVIEW & ITERATE ====================
def generate_stage_5(output_path):
    fig, ax = base_canvas("DESIGN THINKING • STAGE 05",
                          "Stage 5: Review & Iteration — Human-Centric Feedback & Pre-Build Validation",
                          "Pre-Dashboard Discovery: Evaluating wireframes against stakeholder needs and planning iterative metric refinements",
                          badge_color='#e11d48')

    # Left: Evaluation Criteria
    b1 = patches.FancyBboxPatch((4, 23), 44, 53, boxstyle="round,pad=0.6", facecolor='#131e36', edgecolor='#1e293b', linewidth=1.5)
    ax.add_patch(b1)
    h1 = patches.FancyBboxPatch((4.5, 68.5), 43, 6.8, boxstyle="round,pad=0.3", facecolor='#be123c', edgecolor='#fb7185', linewidth=1.2)
    ax.add_patch(h1)
    ax.text(26.0, 71.9, "PROTOTYPE EVALUATION WORKSHOP", color='#ffffff', fontsize=13.0, fontweight='bold', ha='center', va='center')

    criteria = [
        ("Information Quality Audit", "• Does the dashboard clearly answer: 'Is ad spend driving profitable sales?'\n• Check for metric completeness across both ad cost and POS transaction tables.\n• Ensure no critical dimensions (SKU, Category, Campaign Type, Week) were omitted."),
        ("Visual & Cognitive Clarity", "• Can the Marketing Manager grasp weekly performance trajectory within 10 seconds?\n• Are chart types appropriate (e.g., scatter matrix for spend efficiency vs tables)?\n• Does visual hierarchy naturally guide the viewer from macro KPIs down to root causes?"),
        ("Interaction & UX Ergonomics", "• Are slicers synchronized across pages (Week, Campaign Type, Category)?\n• Do custom report-page tooltips provide instant SKU/Campaign details without clutter?\n• Does dynamic Top N filtering prevent overwhelming table views?"),
        ("Actionability & Business Alignment", "• Does the dashboard directly support weekly budget re-allocation decisions?\n• Can leadership readily identify specific ad sets to scale, pause, or optimize?\n• Does Page 4 clearly translate analytical findings into strategic actions?")
    ]
    cy = 65.0
    for c_title, c_desc in criteria:
        card = patches.FancyBboxPatch((5.5, cy - 9.0), 41, 8.5, boxstyle="round,pad=0.3", facecolor='#1e293b', edgecolor='#334155', linewidth=1.0)
        ax.add_patch(card)
        ax.text(7.0, cy - 2.5, c_title, color='#fb7185', fontsize=10.5, fontweight='bold', ha='left')
        ax.text(7.0, cy - 6.0, c_desc, color='#cbd5e1', fontsize=8.6, ha='left', va='center')
        cy -= 10.0

    # Right: Pre-Build Iterations Log
    b2 = patches.FancyBboxPatch((52, 23), 44, 53, boxstyle="round,pad=0.6", facecolor='#131e36', edgecolor='#1e293b', linewidth=1.5)
    ax.add_patch(b2)
    h2 = patches.FancyBboxPatch((52.5, 68.5), 43, 6.8, boxstyle="round,pad=0.3", facecolor='#9f1239', edgecolor='#f43f5e', linewidth=1.2)
    ax.add_patch(h2)
    ax.text(74.0, 71.9, "PRE-BUILD ITERATION LOG (FROM DRAFT TO FINAL)", color='#ffffff', fontsize=13.0, fontweight='bold', ha='center', va='center')

    iterations = [
        ("ITERATION 1: Initial Data Pipeline & Schema Validation", 
         "• Feedback: Raw dataset had disparate campaign cost records and POS order lines.\n• Action: Engineered Kimball Star Schema linking fact_order and fact_mkt_camp\n  via Dim_Date and dim_danh_sach_san_pham to resolve many-to-many pitfalls.",
         '#38bdf8'),
        ("ITERATION 2: Scorecard Dynamics & Time Intelligence", 
         "• Feedback: Static scorecards lacked context — impossible to tell if ROAS was improving.\n• Action: Implemented DAX Time Intelligence with dynamic WoW % labels (e.g., ▲ +12.5%\n  vs LW) and sparklines to visualize weekly momentum instantly.",
         '#34d399'),
        ("ITERATION 3: Advanced UX & Report-Page Tooltips", 
         "• Feedback: Merchandisers wanted SKU images and daily cost breakdown without extra tabs.\n• Action: Designed 3 dedicated micro-interaction tooltip pages (Campaign Type,\n  Product Detail with SKU photo, and Campaign Daily Drilldown).",
         '#fbbf24'),
        ("ITERATION 4: Strategic Synthesis Page Integration", 
         "• Feedback: Executive Board required direct translation of data into business actions.\n• Action: Added dedicated Page 4 structured around Finding -> Evidence -> Business\n  Impact -> Prioritized Recommendations (P1-P4 Action Matrix).",
         '#c084fc')
    ]
    iy = 65.0
    for i_title, i_desc, icol in iterations:
        icard = patches.FancyBboxPatch((53.5, iy - 9.0), 41, 8.5, boxstyle="round,pad=0.3", facecolor='#1e293b', edgecolor='#334155', linewidth=1.0)
        ax.add_patch(icard)
        ax.text(55.0, iy - 2.5, i_title, color=icol, fontsize=10.5, fontweight='bold', ha='left')
        ax.text(55.0, iy - 6.0, i_desc, color='#cbd5e1', fontsize=8.6, ha='left', va='center')
        iy -= 10.0

    # Bottom Strip
    f = patches.FancyBboxPatch((4, 4), 92, 14.5, boxstyle="round,pad=0.5", facecolor='#1e293b', edgecolor='#e11d48', linewidth=1.2)
    ax.add_patch(f)
    ax.text(6, 15.0, "CORE DESIGN THINKING PRINCIPLE: CONTINUOUS ITERATION & HUMAN-CENTRICITY", color='#fb7185', fontsize=11.5, fontweight='bold', ha='left')
    ax.text(6, 10.5, "As stated in the Design Thinking guide: 'Always keep humans at the center. Return to the Empathize stage whenever an output falls short.'\nBy systematically evaluating wireframe prototypes against stakeholder needs across information quality, visual clarity, UX ergonomics,\nand commercial actionability, the dashboard evolved from basic descriptive charts into an enterprise-grade Decision Support System.", 
            color='#f1f5f9', fontsize=9.8, ha='left', va='center')

    save_and_close(fig, output_path)

if __name__ == '__main__':
    base_dir = r'C:\Users\admin\Desktop\Xuân Thu\Da_Portfolio\02_PowerBI\Project 3\assets\framework'
    generate_stage_1(os.path.join(base_dir, 'stage_1_empathize.png'))
    generate_stage_2(os.path.join(base_dir, 'stage_2_define_pov.png'))
    generate_stage_3(os.path.join(base_dir, 'stage_3_ideate.png'))
    generate_stage_4(os.path.join(base_dir, 'stage_4_prototype.png'))
    generate_stage_5(os.path.join(base_dir, 'stage_5_review_iterate.png'))
    print("All 5 Design Thinking stage infographics generated successfully!")
