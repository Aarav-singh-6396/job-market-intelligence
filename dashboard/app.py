import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from io import BytesIO
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Job Market Intelligence",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# PREMIUM DESIGN SYSTEM
# =========================================================

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f5f7fb;
    color: #172033;
}

#MainMenu,
footer,
header {
    visibility: hidden;
}

.block-container {
    max-width: 1500px;
    padding: 28px 32px 45px 32px;
}

/* =========================================================
   SIDEBAR
   ========================================================= */

section[data-testid="stSidebar"] {
    background:
        radial-gradient(circle at top left, rgba(110,70,240,.25), transparent 35%),
        linear-gradient(180deg, #07132f 0%, #0b1d46 100%);
    border-right: 1px solid rgba(255,255,255,.08);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

.brand {
    padding: 8px 4px 26px 4px;
}

.brand-icon {
    display: inline-flex;
    width: 46px;
    height: 46px;
    align-items: center;
    justify-content: center;
    border-radius: 14px;
    background: linear-gradient(135deg,#6937e8,#4167ee);
    font-size: 22px;
    box-shadow: 0 8px 25px rgba(82,55,220,.35);
    vertical-align: middle;
}

.brand-text {
    display: inline-block;
    margin-left: 10px;
    vertical-align: middle;
    font-size: 15px;
    line-height: 1.3;
    font-weight: 800;
}

.sidebar-label {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: rgba(255,255,255,.55) !important;
    margin: 12px 4px 8px 4px;
    font-weight: 700;
}

.stButton > button {
    border-radius: 10px !important;
    border: 1px solid transparent !important;
    background: transparent !important;
    color: white !important;
    font-weight: 600 !important;
    text-align: left !important;
    transition: all .2s ease !important;
}

.stButton > button:hover {
    background: rgba(255,255,255,.10) !important;
    border-color: rgba(255,255,255,.10) !important;
}

.filter-box {
    margin-top: 20px;
    padding: 15px;
    border-radius: 14px;
    background: rgba(255,255,255,.07);
    border: 1px solid rgba(255,255,255,.10);
}

section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stSlider label {
    font-size: 12px !important;
    font-weight: 600 !important;
}

section[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background: rgba(255,255,255,.08);
    border: 1px solid rgba(255,255,255,.12);
    border-radius: 9px;
}

/* =========================================================
   PAGE HEADER
   ========================================================= */

.page-header {
    margin-bottom: 25px;
}

.page-kicker {
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1.4px;
    color: #6d768b;
    font-weight: 700;
    margin-bottom: 7px;
}

.page-title {
    font-size: 34px;
    font-weight: 800;
    color: #11182e;
    line-height: 1.1;
}

.page-title span {
    color: #6937e8;
}

.page-subtitle {
    font-size: 14px;
    color: #6e778c;
    margin-top: 7px;
}

/* =========================================================
   KPI CARDS
   ========================================================= */

.kpi-card {
    background: #ffffff;
    border: 1px solid #e8ebf2;
    border-radius: 18px;
    padding: 19px;
    min-height: 142px;
    box-shadow: 0 8px 28px rgba(20,30,70,.055);
    transition: transform .2s ease, box-shadow .2s ease;
}

.kpi-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 14px 35px rgba(20,30,70,.09);
}

.kpi-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.kpi-icon {
    width: 43px;
    height: 43px;
    border-radius: 12px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    font-size: 20px;
}

.kpi-label {
    font-size: 12px;
    color: #747d91;
    margin-top: 13px;
    font-weight: 600;
}

.kpi-value {
    font-size: 26px;
    font-weight: 800;
    color: #121a31;
    margin-top: 3px;
}

.kpi-description {
    color: #20a968;
    font-size: 11px;
    margin-top: 6px;
    font-weight: 600;
}

/* =========================================================
   SECTION CARDS
   ========================================================= */

.section-card {
    background: #ffffff;
    border: 1px solid #e8ebf2;
    border-radius: 17px;
    padding: 18px;
    box-shadow: 0 7px 25px rgba(20,30,70,.045);
    margin-bottom: 14px;
}

.section-header {
    margin-bottom: 12px;
}

.section-title {
    font-size: 17px;
    font-weight: 800;
    color: #171e34;
}

.section-subtitle {
    color: #7a8397;
    font-size: 11px;
    margin-top: 3px;
}

/* =========================================================
   PAGE HERO
   ========================================================= */

.hero-card {
    background:
        radial-gradient(circle at 85% 20%, rgba(108,61,235,.25), transparent 28%),
        linear-gradient(135deg,#111d40,#1b2d61);
    border-radius: 20px;
    padding: 25px;
    color: white;
    margin-bottom: 22px;
    box-shadow: 0 14px 35px rgba(21,35,80,.13);
}

.hero-title {
    font-size: 24px;
    font-weight: 800;
}

.hero-text {
    color: rgba(255,255,255,.72);
    font-size: 13px;
    margin-top: 6px;
}

/* =========================================================
   TABLE
   ========================================================= */

div[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #e6e9f0;
}

/* =========================================================
   BUTTONS
   ========================================================= */

.stDownloadButton > button {
    border-radius: 10px !important;
    background: linear-gradient(135deg,#6937e8,#4b67e9) !important;
    color: white !important;
    border: none !important;
    font-weight: 700 !important;
}

.stDownloadButton > button:hover {
    box-shadow: 0 7px 18px rgba(89,61,220,.25);
}

/* =========================================================
   METRIC
   ========================================================= */

[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e7eaf1;
    border-radius: 15px;
    padding: 17px;
    box-shadow: 0 6px 20px rgba(20,30,70,.045);
}

[data-testid="stMetricLabel"] {
    color: #717b91 !important;
}

[data-testid="stMetricValue"] {
    color: #121a31 !important;
    font-weight: 800 !important;
}

/* =========================================================
   TABS / INPUTS
   ========================================================= */

.stTextInput input,
.stNumberInput input {
    border-radius: 10px !important;
}

.stCheckbox label {
    font-weight: 600 !important;
}

/* =========================================================
   DIVIDER
   ========================================================= */

hr {
    border: none;
    border-top: 1px solid #e6e9f0;
    margin: 18px 0;
}

</style>
""")

# =========================================================
# LOAD DATA
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = (
    BASE_DIR.parent
    / "data"
    / "processed"
    / "jobs_cleaned.csv"
)


@st.cache_data
def load_data():

    df = pd.read_csv(DATA_PATH)

    for col in [
        "averageSalary",
        "averageExperience"
    ]:

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    return df


df = load_data()

# =========================================================
# DATA VALIDATION
# =========================================================

required_columns = [
    "title",
    "companyName",
    "location",
    "averageSalary",
    "averageExperience"
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:

    st.error(
        "Missing columns: "
        + ", ".join(missing_columns)
    )

    st.stop()

# =========================================================
# CLEAN DATA
# =========================================================

df["title"] = (
    df["title"]
    .fillna("Unknown")
    .astype(str)
    .str.strip()
)

df["companyName"] = (
    df["companyName"]
    .fillna("Unknown")
    .astype(str)
    .str.strip()
)

df["location"] = (
    df["location"]
    .fillna("Unknown")
    .astype(str)
    .str.strip()
)

df["averageSalary"] = df["averageSalary"].fillna(0)

df["averageExperience"] = df["averageExperience"].fillna(0)

# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "saved_jobs" not in st.session_state:
    st.session_state.saved_jobs = []

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.html("""
    <div class="brand">

        <span class="brand-icon">💼</span>

        <span class="brand-text">
            Job Market<br>
            Intelligence
        </span>

    </div>
    """)

    st.html("""
    <div class="sidebar-label">
        MAIN MENU
    </div>
    """)

    navigation = [
        ("⌂", "Dashboard"),
        ("⌁", "Job Insights"),
        ("🔎", "Job Search"),
        ("▥", "Companies"),
        ("₹", "Salaries"),
        ("⚡", "Skills in Demand"),
        ("⌖", "Locations"),
        ("◈", "Advanced Analytics"),
        ("▤", "Reports"),
        ("♡", "Saved Jobs"),
        ("♧", "Alerts"),
        ("⚙", "Settings")
    ]

    for icon, name in navigation:

        if st.button(
            f"{icon}   {name}",
            key=f"nav_{name}",
            use_container_width=True
        ):
            st.session_state.page = name

    st.html("""
    <div class="sidebar-label">
        QUICK FILTERS
    </div>
    """)

    locations = sorted(
        df["location"]
        .dropna()
        .unique()
        .tolist()
    )

    job_titles = sorted(
        df["title"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_location = st.selectbox(
        "📍 Location",
        ["All India"] + locations
    )

    selected_job = st.selectbox(
        "💼 Job Title",
        ["All Job Titles"] + job_titles
    )

    min_exp = int(df["averageExperience"].min())
    max_exp = int(df["averageExperience"].max())

    if min_exp == max_exp:

        experience = (min_exp, max_exp)

    else:

        experience = st.slider(
            "👨‍💻 Experience",
            min_value=min_exp,
            max_value=max_exp,
            value=(min_exp, max_exp)
        )

    min_salary = int(df["averageSalary"].min())
    max_salary = int(df["averageSalary"].max())

    salary = st.slider(
        "💰 Minimum Salary",
        min_value=min_salary,
        max_value=max_salary,
        value=min_salary,
        step=1000
    )

# =========================================================
# APPLY FILTERS
# =========================================================

filtered_df = df.copy()

if selected_location != "All India":

    filtered_df = filtered_df[
        filtered_df["location"] == selected_location
    ]

if selected_job != "All Job Titles":

    filtered_df = filtered_df[
        filtered_df["title"] == selected_job
    ]

filtered_df = filtered_df[
    filtered_df["averageExperience"].between(
        experience[0],
        experience[1]
    )
]

filtered_df = filtered_df[
    filtered_df["averageSalary"] >= salary
]

if filtered_df.empty:

    st.warning(
        "⚠️ No jobs found for the selected filters."
    )

    st.stop()

# =========================================================
# COMMON HEADER FUNCTION
# =========================================================

def page_header(kicker, title, subtitle):

    st.html(f"""
    <div class="page-header">

        <div class="page-kicker">
            {kicker}
        </div>

        <div class="page-title">
            {title}
        </div>

        <div class="page-subtitle">
            {subtitle}
        </div>

    </div>
    """)


# =========================================================
# PROFESSIONAL PDF REPORT GENERATOR
# =========================================================

def build_pdf_report(report_df, selected_location, selected_job, experience_range, salary_min):
    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        fontSize=22,
        leading=26,
        alignment=TA_CENTER,
        spaceAfter=10
    )

    subtitle_style = ParagraphStyle(
        "ReportSubtitle",
        parent=styles["Normal"],
        fontSize=9,
        textColor=colors.grey,
        alignment=TA_CENTER,
        spaceAfter=18
    )

    heading_style = ParagraphStyle(
        "ReportHeading",
        parent=styles["Heading2"],
        fontSize=14,
        leading=18,
        spaceBefore=12,
        spaceAfter=8
    )

    body_style = ParagraphStyle(
        "ReportBody",
        parent=styles["Normal"],
        fontSize=9,
        leading=13
    )

    story = []

    story.append(Paragraph("Job Market Intelligence", title_style))
    story.append(Paragraph(
        "Professional Job Market Analytics Report",
        subtitle_style
    ))

    story.append(Paragraph("Report Overview", heading_style))

    overview = [
        ["Generated", datetime.now().strftime("%d %b %Y, %I:%M %p")],
        ["Jobs", f"{len(report_df):,}"],
        ["Companies", f"{report_df['companyName'].nunique():,}"],
        ["Locations", f"{report_df['location'].nunique():,}"],
        ["Average Salary", f"₹{report_df['averageSalary'].mean():,.0f}"],
        ["Average Experience", f"{report_df['averageExperience'].mean():.1f} years"],
        ["Location Filter", selected_location],
        ["Job Title Filter", selected_job],
        ["Experience Range", f"{experience_range[0]} - {experience_range[1]} years"],
        ["Minimum Salary", f"₹{salary_min:,}"],
    ]

    overview_table = Table(overview, colWidths=[150, 330])
    overview_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#eef1f7")),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#172033")),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d9deea")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (1, 0), (-1, -1), [colors.white, colors.HexColor("#fafbfe")]),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(overview_table)

    story.append(Paragraph("Top Hiring Companies", heading_style))
    companies = (
        report_df["companyName"]
        .value_counts()
        .head(10)
        .reset_index()
    )
    companies.columns = ["Company", "Job Openings"]
    company_rows = [["Company", "Job Openings"]] + companies.values.tolist()
    company_table = Table(company_rows, colWidths=[350, 130])
    company_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#6937e8")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d9deea")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f7f8fc")]),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(company_table)

    story.append(Paragraph("Top Job Titles", heading_style))
    titles = (
        report_df["title"]
        .value_counts()
        .head(10)
        .reset_index()
    )
    titles.columns = ["Job Title", "Job Openings"]
    title_rows = [["Job Title", "Job Openings"]] + titles.values.tolist()
    title_table = Table(title_rows, colWidths=[350, 130])
    title_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#3280ed")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d9deea")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f7f8fc")]),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(title_table)

    story.append(PageBreak())

    story.append(Paragraph("Top Job Locations", heading_style))
    locations_data = (
        report_df["location"]
        .value_counts()
        .head(10)
        .reset_index()
    )
    locations_data.columns = ["Location", "Job Openings"]
    location_rows = [["Location", "Job Openings"]] + locations_data.values.tolist()
    location_table = Table(location_rows, colWidths=[350, 130])
    location_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#20b974")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d9deea")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f7f8fc")]),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(location_table)

    story.append(Paragraph("Highest Paying Opportunities", heading_style))
    salary_data = (
        report_df[
            ["title", "companyName", "location", "averageSalary", "averageExperience"]
        ]
        .sort_values("averageSalary", ascending=False)
        .head(10)
    )

    salary_rows = [["Job Title", "Company", "Location", "Salary", "Exp."]]
    for _, row in salary_data.iterrows():
        salary_rows.append([
            str(row["title"])[:35],
            str(row["companyName"])[:25],
            str(row["location"])[:22],
            f"₹{float(row['averageSalary']):,.0f}",
            f"{float(row['averageExperience']):.1f}"
        ])

    salary_table = Table(
        salary_rows,
        colWidths=[145, 115, 100, 75, 55]
    )
    salary_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#ff8d12")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 7),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d9deea")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f7f8fc")]),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(salary_table)

    story.append(Paragraph("Key Market Insights", heading_style))

    top_company = companies.iloc[0]["Company"] if not companies.empty else "N/A"
    top_title = titles.iloc[0]["Job Title"] if not titles.empty else "N/A"
    top_location = locations_data.iloc[0]["Location"] if not locations_data.empty else "N/A"

    insights = [
        f"• The dataset contains {len(report_df):,} matching job opportunities.",
        f"• {top_company} is the leading hiring company in the selected data.",
        f"• {top_title} is the most frequently appearing job title.",
        f"• {top_location} has the highest number of listed opportunities.",
        f"• The average salary in the selected dataset is ₹{report_df['averageSalary'].mean():,.0f}.",
        f"• The average experience requirement is {report_df['averageExperience'].mean():.1f} years.",
    ]

    for insight in insights:
        story.append(Paragraph(insight, body_style))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "Generated automatically by Job Market Intelligence.",
        subtitle_style
    ))

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()


# =========================================================
# DASHBOARD
# =========================================================

if st.session_state.page == "Dashboard":

    page_header(
        "JOB MARKET INTELLIGENCE",
        'Job Market <span>Overview</span>',
        "Real-time analysis of jobs, companies, salaries and market demand."
    )

    total_jobs = len(filtered_df)

    companies = filtered_df["companyName"].nunique()

    average_salary = filtered_df["averageSalary"].mean()

    average_experience = filtered_df["averageExperience"].mean()

    c1, c2, c3, c4 = st.columns(4)

    cards = [

        (
            "#6937e8",
            "💼",
            "Total Jobs",
            f"{total_jobs:,}",
            "Current filtered jobs"
        ),

        (
            "#20b974",
            "🏢",
            "Companies",
            f"{companies:,}",
            "Companies hiring"
        ),

        (
            "#ff8d12",
            "₹",
            "Average Salary",
            f"₹{average_salary:,.0f}",
            "Market average"
        ),

        (
            "#3c7fed",
            "★",
            "Avg Experience",
            f"{average_experience:.1f} yrs",
            "Requirement"
        )
    ]

    for col, card in zip(
        [c1, c2, c3, c4],
        cards
    ):

        bg, icon, label, value, description = card

        with col:

            st.html(f"""
            <div class="kpi-card">

                <div class="kpi-top">

                    <div class="kpi-icon"
                         style="background:{bg};">
                        {icon}
                    </div>

                </div>

                <div class="kpi-label">
                    {label}
                </div>

                <div class="kpi-value">
                    {value}
                </div>

                <div class="kpi-description">
                    ● {description}
                </div>

            </div>
            """)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # TOP JOBS

    with col1:

        st.html("""
        <div class="section-card">

            <div class="section-header">

                <div class="section-title">
                    💼 Top Job Titles
                </div>

                <div class="section-subtitle">
                    Most in-demand roles
                </div>

            </div>

        </div>
        """)

        top_jobs = (
            filtered_df["title"]
            .value_counts()
            .head(10)
            .reset_index()
        )

        top_jobs.columns = [
            "Job Title",
            "Job Openings"
        ]

        fig = px.bar(
            top_jobs,
            x="Job Openings",
            y="Job Title",
            orientation="h",
            text="Job Openings"
        )

        fig.update_traces(
            marker_color="#6937e8",
            textposition="outside"
        )

        fig.update_layout(
            height=400,
            paper_bgcolor="white",
            plot_bgcolor="white",
            margin=dict(l=10, r=30, t=10, b=10),
            yaxis=dict(categoryorder="total ascending"),
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False}
        )

    # TOP LOCATIONS

    with col2:

        st.html("""
        <div class="section-card">

            <div class="section-header">

                <div class="section-title">
                    📍 Top Job Locations
                </div>

                <div class="section-subtitle">
                    Cities with highest opportunities
                </div>

            </div>

        </div>
        """)

        top_locations = (
            filtered_df["location"]
            .value_counts()
            .head(10)
            .reset_index()
        )

        top_locations.columns = [
            "Location",
            "Job Openings"
        ]

        fig = px.bar(
            top_locations,
            x="Job Openings",
            y="Location",
            orientation="h",
            text="Job Openings"
        )

        fig.update_traces(
            marker_color="#3280ed",
            textposition="outside"
        )

        fig.update_layout(
            height=400,
            paper_bgcolor="white",
            plot_bgcolor="white",
            margin=dict(l=10, r=30, t=10, b=10),
            yaxis=dict(categoryorder="total ascending"),
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False}
        )

    # DATASET

    st.html("""
    <div class="section-card">

        <div class="section-header">

            <div class="section-title">
                📊 Filtered Job Dataset
            </div>

            <div class="section-subtitle">
                Jobs matching your selected filters
            </div>

        </div>

    </div>
    """)

    st.dataframe(
        filtered_df.head(100),
        use_container_width=True,
        hide_index=True,
        height=380
    )

    st.download_button(
        "⬇ Download Filtered Jobs",
        data=filtered_df.to_csv(index=False).encode("utf-8"),
        file_name="filtered_job_market_data.csv",
        mime="text/csv"
    )


# =========================================================
# JOB INSIGHTS
# =========================================================

elif st.session_state.page == "Job Insights":

    page_header(
        "MARKET ANALYTICS",
        "Job <span>Insights</span>",
        "Understand job demand, role distribution and opportunity trends."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.html("""
        <div class="section-card">

            <div class="section-title">
                📈 Most In-Demand Jobs
            </div>

            <div class="section-subtitle">
                Roles with the highest number of openings
            </div>

        </div>
        """)

        demand = (
            filtered_df["title"]
            .value_counts()
            .head(20)
            .sort_values()
        )

        fig = px.bar(
            demand,
            orientation="h",
            text_auto=True
        )

        fig.update_traces(marker_color="#6937e8")

        fig.update_layout(
            height=550,
            paper_bgcolor="white",
            plot_bgcolor="white",
            margin=dict(l=10, r=20, t=10, b=10),
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        st.html("""
        <div class="section-card">

            <div class="section-title">
                📍 Job Distribution
            </div>

            <div class="section-subtitle">
                Opportunity distribution across locations
            </div>

        </div>
        """)

        location_data = (
            filtered_df["location"]
            .value_counts()
            .head(15)
            .sort_values()
        )

        fig = px.bar(
            location_data,
            orientation="h",
            text_auto=True
        )

        fig.update_traces(marker_color="#3280ed")

        fig.update_layout(
            height=550,
            paper_bgcolor="white",
            plot_bgcolor="white",
            margin=dict(l=10, r=20, t=10, b=10),
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# =========================================================
# COMPANIES
# =========================================================

elif st.session_state.page == "Companies":

    page_header(
        "EMPLOYER ANALYTICS",
        "Top <span>Hiring Companies</span>",
        "Explore organizations with the highest number of job openings."
    )

    company_data = (
        filtered_df["companyName"]
        .value_counts()
        .head(25)
        .reset_index()
    )

    company_data.columns = [
        "Company",
        "Job Openings"
    ]

    m1, m2, m3 = st.columns(3)

    m1.metric(
        "Hiring Companies",
        f"{filtered_df['companyName'].nunique():,}"
    )

    m2.metric(
        "Top Employer",
        company_data.iloc[0]["Company"]
    )

    m3.metric(
        "Top Employer Jobs",
        f"{company_data.iloc[0]['Job Openings']:,}"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.4])

    with col1:

        st.html("""
        <div class="section-card">

            <div class="section-title">
                🏢 Company Rankings
            </div>

            <div class="section-subtitle">
                Top employers by job openings
            </div>

        </div>
        """)

        st.dataframe(
            company_data,
            use_container_width=True,
            hide_index=True,
            height=540
        )

    with col2:

        fig = px.bar(
            company_data.head(15).sort_values("Job Openings"),
            x="Job Openings",
            y="Company",
            orientation="h",
            text="Job Openings"
        )

        fig.update_traces(
            marker_color="#6937e8",
            textposition="outside"
        )

        fig.update_layout(
            height=550,
            paper_bgcolor="white",
            plot_bgcolor="white",
            margin=dict(l=10, r=30, t=20, b=10),
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# =========================================================
# SALARIES
# =========================================================

elif st.session_state.page == "Salaries":

    page_header(
        "COMPENSATION ANALYTICS",
        "Salary <span>Analysis</span>",
        "Explore salary levels and identify the highest-paying job roles."
    )

    avg_salary = filtered_df["averageSalary"].mean()
    max_salary_value = filtered_df["averageSalary"].max()
    median_salary = filtered_df["averageSalary"].median()

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Average Salary",
        f"₹{avg_salary:,.0f}"
    )

    c2.metric(
        "Highest Salary",
        f"₹{max_salary_value:,.0f}"
    )

    c3.metric(
        "Median Salary",
        f"₹{median_salary:,.0f}"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    salary_by_job = (
        filtered_df
        .groupby("title")["averageSalary"]
        .mean()
        .sort_values(ascending=False)
        .head(15)
        .sort_values()
    )

    fig = px.bar(
        salary_by_job,
        orientation="h",
        text_auto=".0f"
    )

    fig.update_traces(marker_color="#ff8d12")

    fig.update_layout(
        height=550,
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(l=10, r=30, t=20, b=10),
        xaxis_title="Average Salary (₹)",
        yaxis_title="",
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.html("""
    <div class="section-card">

        <div class="section-title">
            💰 Highest Paying Opportunities
        </div>

        <div class="section-subtitle">
            Job roles ranked by average salary
        </div>

    </div>
    """)

    salary_data = (
        filtered_df[
            [
                "title",
                "averageSalary",
                "averageExperience",
                "location"
            ]
        ]
        .sort_values(
            "averageSalary",
            ascending=False
        )
        .head(30)
    )

    st.dataframe(
        salary_data,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# SKILLS
# =========================================================

elif st.session_state.page == "Skills in Demand":

    page_header(
        "SKILL ANALYTICS",
        "Skills in <span>Demand</span>",
        "Discover frequently appearing technologies and skills in job titles."
    )

    words = (
        filtered_df["title"]
        .str.lower()
        .str.replace(
            r"[^a-zA-Z0-9+#. ]",
            " ",
            regex=True
        )
        .str.split()
        .explode()
    )

    stop_words = {
        "senior",
        "junior",
        "lead",
        "manager",
        "developer",
        "engineer",
        "analyst",
        "specialist",
        "consultant",
        "associate",
        "intern",
        "executive",
        "architect"
    }

    words = words[~words.isin(stop_words)]

    words = words[words.str.len() >= 3]

    skills = (
        words.value_counts()
        .head(30)
        .reset_index()
    )

    skills.columns = [
        "Skill",
        "Frequency"
    ]

    c1, c2 = st.columns([1, 1.5])

    with c1:

        st.html("""
        <div class="section-card">

            <div class="section-title">
                ⚡ Skill Rankings
            </div>

            <div class="section-subtitle">
                Most frequently appearing terms
            </div>

        </div>
        """)

        st.dataframe(
            skills,
            use_container_width=True,
            hide_index=True,
            height=550
        )

    with c2:

        fig = px.bar(
            skills.head(15).sort_values("Frequency"),
            x="Frequency",
            y="Skill",
            orientation="h",
            text="Frequency"
        )

        fig.update_traces(
            marker_color="#6937e8",
            textposition="outside"
        )

        fig.update_layout(
            height=550,
            paper_bgcolor="white",
            plot_bgcolor="white",
            margin=dict(l=10, r=30, t=20, b=10),
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# =========================================================
# LOCATIONS
# =========================================================

elif st.session_state.page == "Locations":

    page_header(
        "GEOGRAPHIC ANALYTICS",
        "Job <span>Locations</span>",
        "Explore where the highest number of job opportunities are available."
    )

    location_data = (
        filtered_df["location"]
        .value_counts()
        .reset_index()
    )

    location_data.columns = [
        "Location",
        "Job Openings"
    ]

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Cities",
        f"{location_data.shape[0]:,}"
    )

    c2.metric(
        "Top Location",
        location_data.iloc[0]["Location"]
    )

    c3.metric(
        "Top Location Jobs",
        f"{location_data.iloc[0]['Job Openings']:,}"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.4])

    with col1:

        st.html("""
        <div class="section-card">

            <div class="section-title">
                📍 Location Rankings
            </div>

            <div class="section-subtitle">
                Cities ranked by job openings
            </div>

        </div>
        """)

        st.dataframe(
            location_data,
            use_container_width=True,
            hide_index=True,
            height=560
        )

    with col2:

        fig = px.bar(
            location_data.head(20).sort_values("Job Openings"),
            x="Job Openings",
            y="Location",
            orientation="h",
            text="Job Openings"
        )

        fig.update_traces(
            marker_color="#3280ed",
            textposition="outside"
        )

        fig.update_layout(
            height=600,
            paper_bgcolor="white",
            plot_bgcolor="white",
            margin=dict(l=10, r=30, t=20, b=10),
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# =========================================================
# REPORTS
# =========================================================

elif st.session_state.page == "Reports":

    page_header(
        "DATA EXPORT",
        "Market <span>Reports</span>",
        "Generate professional reports from your filtered job market dataset."
    )

    st.html("""
    <div class="hero-card">

        <div class="hero-title">
            📊 Professional Job Market Report
        </div>

        <div class="hero-text">
            Generate a structured PDF report containing market KPIs,
            hiring companies, job titles, locations, salary analysis
            and key insights based on your selected filters.
        </div>

    </div>
    """)

    report = filtered_df.copy()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Jobs", f"{len(report):,}")
    c2.metric("Companies", f"{report['companyName'].nunique():,}")
    c3.metric("Locations", f"{report['location'].nunique():,}")
    c4.metric("Avg Salary", f"₹{report['averageSalary'].mean():,.0f}")

    st.markdown("<br>", unsafe_allow_html=True)

    pdf_bytes = build_pdf_report(
        report,
        selected_location,
        selected_job,
        experience,
        salary
    )

    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            "📄 Download Professional PDF Report",
            data=pdf_bytes,
            file_name="job_market_intelligence_report.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    with col2:
        st.download_button(
            "⬇ Download Complete CSV Report",
            data=report.to_csv(index=False).encode("utf-8"),
            file_name="job_market_report.csv",
            mime="text/csv",
            use_container_width=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.html("""
    <div class="section-card">

        <div class="section-title">
            📋 Report Preview
        </div>

        <div class="section-subtitle">
            First 100 records from the generated report
        </div>

    </div>
    """)

    st.dataframe(
        report.head(100),
        use_container_width=True,
        hide_index=True,
        height=450
    )

# =========================================================
# SAVED JOBS
# =========================================================

elif st.session_state.page == "Saved Jobs":

    page_header(
        "PERSONAL WORKSPACE",
        "Saved <span>Jobs</span>",
        "Keep track of opportunities you want to explore later."
    )

    jobs = filtered_df.head(50)

    st.html("""
    <div class="hero-card">

        <div class="hero-title">
            ♡ Your Job Shortlist
        </div>

        <div class="hero-text">
            Select jobs below to add them to your personal shortlist.
        </div>

    </div>
    """)

    for index, row in jobs.iterrows():

        job_name = (
            f"{row['title']}  |  "
            f"{row['companyName']}  |  "
            f"{row['location']}"
        )

        if st.checkbox(
            job_name,
            key=f"save_{index}"
        ):

            if index not in st.session_state.saved_jobs:

                st.session_state.saved_jobs.append(index)

    st.markdown("<br>", unsafe_allow_html=True)

    st.html("""
    <div class="section-card">

        <div class="section-title">
            ❤️ Your Saved Jobs
        </div>

    </div>
    """)

    if st.session_state.saved_jobs:

        saved = df.loc[
            df.index.isin(
                st.session_state.saved_jobs
            )
        ]

        st.dataframe(
            saved,
            use_container_width=True,
            hide_index=True
        )

        if st.button("🗑 Clear All Saved Jobs", use_container_width=True):
            st.session_state.saved_jobs = []
            st.rerun()

    else:

        st.info(
            "No jobs saved yet. Select a job above to add it here."
        )


# =========================================================
# ALERTS
# =========================================================

elif st.session_state.page == "Alerts":

    page_header(
        "AUTOMATION",
        "Job <span>Alerts</span>",
        "Create personalized alerts for opportunities matching your criteria."
    )

    st.html("""
    <div class="hero-card">

        <div class="hero-title">
            🔔 Never Miss an Opportunity
        </div>

        <div class="hero-text">
            Define your preferred location, role and minimum salary
            to create a personalized job alert.
        </div>

    </div>
    """)

    col1, col2 = st.columns(2)

    with col1:

        st.html("""
        <div class="section-card">

            <div class="section-title">
                🎯 Alert Preferences
            </div>

            <div class="section-subtitle">
                Define your ideal job criteria
            </div>

        </div>
        """)

        alert_location = st.selectbox(
            "Alert Location",
            ["Any Location"] + locations,
            key="alert_location"
        )

        alert_job = st.selectbox(
            "Alert Job Title",
            ["Any Job Title"] + job_titles,
            key="alert_job"
        )

        alert_salary = st.number_input(
            "Minimum Salary",
            min_value=0,
            value=0,
            step=1000
        )

        if st.button(
            "🔔 Create Job Alert",
            use_container_width=True
        ):

            st.session_state.alert = {
                "location": alert_location,
                "job": alert_job,
                "salary": alert_salary
            }

            st.success(
                "Job alert created successfully!"
            )

    with col2:

        st.html("""
        <div class="section-card">

            <div class="section-title">
                🔔 Active Alert
            </div>

            <div class="section-subtitle">
                Your current notification criteria
            </div>

        </div>
        """)

        if "alert" in st.session_state:

            alert = st.session_state.alert

            st.metric(
                "Minimum Salary",
                f"₹{alert['salary']:,}"
            )

            st.write(
                f"📍 **Location:** {alert['location']}"
            )

            st.write(
                f"💼 **Job:** {alert['job']}"
            )

            alert_df = df.copy()

            if alert["location"] != "Any Location":
                alert_df = alert_df[
                    alert_df["location"] == alert["location"]
                ]

            if alert["job"] != "Any Job Title":
                alert_df = alert_df[
                    alert_df["title"] == alert["job"]
                ]

            alert_df = alert_df[
                alert_df["averageSalary"] >= alert["salary"]
            ]

            st.metric(
                "Matching Opportunities",
                f"{len(alert_df):,}"
            )

            if not alert_df.empty:
                st.dataframe(
                    alert_df[
                        [
                            "title",
                            "companyName",
                            "location",
                            "averageSalary",
                            "averageExperience"
                        ]
                    ].head(20),
                    use_container_width=True,
                    hide_index=True
                )

        else:

            st.info(
                "No active job alert."
            )

# =========================================================
# ADVANCED ANALYTICS
# =========================================================

elif st.session_state.page == "Advanced Analytics":

    page_header(
        "ADVANCED DATA ANALYTICS",
        "Advanced <span>Market Analytics</span>",
        "Explore deeper relationships between salary, experience, demand and location."
    )

    # SUMMARY
    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Jobs",
        f"{len(filtered_df):,}"
    )

    c2.metric(
        "Average Salary",
        f"₹{filtered_df['averageSalary'].mean():,.0f}"
    )

    c3.metric(
        "Average Experience",
        f"{filtered_df['averageExperience'].mean():.1f} yrs"
    )

    c4.metric(
        "Companies",
        f"{filtered_df['companyName'].nunique():,}"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # SALARY VS EXPERIENCE

    st.html("""
    <div class="section-card">

        <div class="section-title">
            💰 Salary vs Experience
        </div>

        <div class="section-subtitle">
            Relationship between experience and average salary
        </div>

    </div>
    """)

    salary_exp = (
        filtered_df[
            [
                "averageExperience",
                "averageSalary",
                "title"
            ]
        ]
        .dropna()
    )

    fig = px.scatter(
        salary_exp,
        x="averageExperience",
        y="averageSalary",
        hover_name="title",
        size="averageSalary",
        opacity=0.65
    )

    fig.update_layout(
        height=500,
        paper_bgcolor="white",
        plot_bgcolor="white",
        xaxis_title="Experience (Years)",
        yaxis_title="Average Salary (₹)",
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # COMPANY VS SALARY

    col1, col2 = st.columns(2)

    with col1:

        st.html("""
        <div class="section-card">

            <div class="section-title">
                🏢 Company-wise Salary
            </div>

            <div class="section-subtitle">
                Companies offering higher average salaries
            </div>

        </div>
        """)

        company_salary = (
            filtered_df
            .groupby("companyName")["averageSalary"]
            .mean()
            .sort_values(ascending=False)
            .head(15)
            .sort_values()
        )

        fig = px.bar(
            company_salary,
            orientation="h",
            text_auto=".0f"
        )

        fig.update_traces(
            marker_color="#6937e8"
        )

        fig.update_layout(
            height=500,
            paper_bgcolor="white",
            plot_bgcolor="white",
            xaxis_title="Average Salary (₹)",
            yaxis_title="",
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # LOCATION VS SALARY

    with col2:

        st.html("""
        <div class="section-card">

            <div class="section-title">
                📍 Location-wise Salary
            </div>

            <div class="section-subtitle">
                Average salary across major locations
            </div>

        </div>
        """)

        location_salary = (
            filtered_df
            .groupby("location")["averageSalary"]
            .mean()
            .sort_values(ascending=False)
            .head(15)
            .sort_values()
        )

        fig = px.bar(
            location_salary,
            orientation="h",
            text_auto=".0f"
        )

        fig.update_traces(
            marker_color="#3280ed"
        )

        fig.update_layout(
            height=500,
            paper_bgcolor="white",
            plot_bgcolor="white",
            xaxis_title="Average Salary (₹)",
            yaxis_title="",
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # JOB DEMAND VS SALARY

    st.html("""
    <div class="section-card">

        <div class="section-title">
            💼 Job Demand vs Salary
        </div>

        <div class="section-subtitle">
            Compare job openings with average compensation
        </div>

    </div>
    """)

    demand_salary = (
        filtered_df
        .groupby("title")
        .agg(
            Job_Openings=("title", "count"),
            Average_Salary=("averageSalary", "mean")
        )
        .reset_index()
        .sort_values(
            "Job_Openings",
            ascending=False
        )
        .head(30)
    )

    fig = px.scatter(
        demand_salary,
        x="Job_Openings",
        y="Average_Salary",
        size="Job_Openings",
        hover_name="title"
    )

    fig.update_layout(
        height=500,
        paper_bgcolor="white",
        plot_bgcolor="white",
        xaxis_title="Job Openings",
        yaxis_title="Average Salary (₹)",
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # EXPERIENCE DISTRIBUTION

    st.html("""
    <div class="section-card">

        <div class="section-title">
            📈 Experience-wise Job Distribution
        </div>

        <div class="section-subtitle">
            Number of jobs by required experience
        </div>

    </div>
    """)

    experience_data = (
        filtered_df["averageExperience"]
        .round()
        .value_counts()
        .sort_index()
    )

    fig = px.bar(
        x=experience_data.index,
        y=experience_data.values,
        text=experience_data.values
    )

    fig.update_traces(
        marker_color="#20b974",
        textposition="outside"
    )

    fig.update_layout(
        height=450,
        paper_bgcolor="white",
        plot_bgcolor="white",
        xaxis_title="Experience (Years)",
        yaxis_title="Number of Jobs",
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    # =========================================================
# JOB SEARCH
# =========================================================

elif st.session_state.page == "Job Search":

    page_header(
        "JOB DISCOVERY",
        "Find Your <span>Next Opportunity</span>",
        "Search and explore jobs using title, company, skills, location and salary."
    )



    # -----------------------------------------------------
    # SEARCH BAR
    # -----------------------------------------------------

    st.html("""
    <div class="section-card">

        <div class="section-title">
            🔎 Search Jobs
        </div>

        <div class="section-subtitle">
            Search across job titles, companies and required skills
        </div>

    </div>
    """)

    search_query = st.text_input(
        "Search",
        placeholder="e.g. Data Analyst, Python, TCS...",
        key="job_search_query"
    )

    # -----------------------------------------------------
    # SEARCH FILTERS
    # -----------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        search_location = st.selectbox(
            "📍 Location",
            ["All Locations"] + locations,
            key="search_location"
        )

    with col2:

        search_company = st.selectbox(
            "🏢 Company",
            ["All Companies"] +
            sorted(
                df["companyName"]
                .dropna()
                .unique()
                .tolist()
            ),
            key="search_company"
        )

    with col3:

        search_experience = st.slider(
            "👨‍💻 Maximum Experience",
            min_value=int(df["averageExperience"].min()),
            max_value=int(df["averageExperience"].max()),
            value=int(df["averageExperience"].max()),
            key="search_experience"
        )

    with col4:

        search_salary = st.number_input(
            "💰 Minimum Salary",
            min_value=0,
            value=0,
            step=5000,
            key="search_salary"
        )

    # -----------------------------------------------------
    # APPLY SEARCH
    # -----------------------------------------------------

    search_df = df.copy()

    # Text search

    if search_query:

        query = search_query.lower().strip()

        title_match = (
            search_df["title"]
            .str.lower()
            .str.contains(query, na=False, regex=False)
        )

        company_match = (
            search_df["companyName"]
            .str.lower()
            .str.contains(query, na=False, regex=False)
        )

        if "tagsAndSkills" in search_df.columns:
            skills_match = (
                search_df["tagsAndSkills"]
                .fillna("")
                .astype(str)
                .str.lower()
                .str.contains(query, na=False, regex=False)
            )
        else:
            skills_match = False

        search_df = search_df[title_match | company_match | skills_match]

    # Location

    if search_location != "All Locations":

        search_df = search_df[
            search_df["location"] == search_location
        ]

    # Company

    if search_company != "All Companies":

        search_df = search_df[
            search_df["companyName"] == search_company
        ]

    # Experience

    search_df = search_df[
        search_df["averageExperience"] <= search_experience
    ]

    # Salary

    search_df = search_df[
        search_df["averageSalary"] >= search_salary
    ]

    # -----------------------------------------------------
    # RESULTS SUMMARY
    # -----------------------------------------------------

    st.markdown("<br>", unsafe_allow_html=True)

    r1, r2, r3 = st.columns(3)

    r1.metric(
        "Matching Jobs",
        f"{len(search_df):,}"
    )

    r2.metric(
        "Companies",
        f"{search_df['companyName'].nunique():,}"
    )

    if len(search_df) > 0:

        r3.metric(
            "Average Salary",
            f"₹{search_df['averageSalary'].mean():,.0f}"
        )

    else:

        r3.metric(
            "Average Salary",
            "₹0"
        )

    # -----------------------------------------------------
    # RESULTS
    # -----------------------------------------------------

    st.markdown("<br>", unsafe_allow_html=True)

    st.html("""
    <div class="section-card">

        <div class="section-title">
            📋 Job Search Results
        </div>

        <div class="section-subtitle">
            Opportunities matching your search criteria
        </div>

    </div>
    """)

    if search_df.empty:

        st.warning(
            "⚠️ No jobs found. Try changing your search or filters."
        )

    else:

        display_columns = [
            "title",
            "companyName",
            "location",
            "averageSalary",
            "averageExperience",
            "tagsAndSkills",
            "AggregateRating",
            "jobid"
        ]

        available_columns = [
            col
            for col in display_columns
            if col in search_df.columns
        ]

        results = search_df[
            available_columns
        ].copy()

        results = results.rename(
            columns={
                "title": "Job Title",
                "companyName": "Company",
                "location": "Location",
                "averageSalary": "Average Salary",
                "averageExperience": "Experience",
                "tagsAndSkills": "Skills",
                "AggregateRating": "Rating",
                "jobid": "Job ID"
            }
        )

        st.dataframe(
            results.head(100),
            use_container_width=True,
            hide_index=True,
            height=500
        )

        # -------------------------------------------------
        # DOWNLOAD RESULTS
        # -------------------------------------------------

        st.download_button(
            "⬇ Download Search Results",
            data=search_df.to_csv(
                index=False
            ).encode("utf-8"),
            file_name="job_search_results.csv",
            mime="text/csv"
        )

# =========================================================
# SETTINGS
# =========================================================

elif st.session_state.page == "Settings":

    page_header(
        "SYSTEM PREFERENCES",
        "Dashboard <span>Settings</span>",
        "Customize your Job Market Intelligence experience."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.html("""
        <div class="section-card">

            <div class="section-title">
                🎨 Appearance
            </div>

            <div class="section-subtitle">
                Customize how your dashboard behaves
            </div>

        </div>
        """)

        if "dark_mode" not in st.session_state:
            st.session_state.dark_mode = False

        if "compact_tables" not in st.session_state:
            st.session_state.compact_tables = False

        if "notifications" not in st.session_state:
            st.session_state.notifications = True

        dark_mode = st.toggle(
            "Dark Mode",
            key="dark_mode"
        )

        compact = st.toggle(
            "Compact Tables",
            key="compact_tables"
        )

    with col2:

        st.html("""
        <div class="section-card">

            <div class="section-title">
                🔔 Notifications
            </div>

            <div class="section-subtitle">
                Manage your job notification preferences
            </div>

        </div>
        """)

        notifications = st.toggle(
            "Job Notifications",
            key="notifications"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "💾 Save Settings",
        use_container_width=True
    ):

        st.success(
            "Dashboard settings saved successfully!"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.html("""
    <div class="section-card">

        <div class="section-title">
            ⚙ Current Preferences
        </div>

    </div>
    """)

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Dark Mode",
        "Enabled" if dark_mode else "Disabled"
    )

    c2.metric(
        "Compact Tables",
        "Enabled" if compact else "Disabled"
    )

    c3.metric(
        "Notifications",
        "Enabled" if notifications else "Disabled"
    )