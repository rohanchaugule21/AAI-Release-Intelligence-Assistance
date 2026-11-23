from src.llm.qwen_client import (
    ask_qwen
)


# ==========================================================
# SEARCH
# ==========================================================

def generate_search_answer(
    question,
    evidence
):

    prompt = f"""
You are an IRS Release Intelligence Analyst.

Question:
{question}

Evidence:
{evidence}

Using ONLY the supplied evidence:

Provide a concise answer.

If information exists, include:

- Related Releases
- Related Stories
- Related Components
- Related Dependencies
- Technologies Involved
- Business Purpose

CRITICAL INSTRUCTIONS

1. NEVER output section headings that have no data.
2. NEVER output:
   - None
   - Not Available
   - Not Applicable
   - No Data Found
3. NEVER output:
   - Rules
   - Instructions
   - Critical Rules
4. NEVER explain what instructions you followed.
5. NEVER mention missing sections.
6. Mention release numbers whenever available.
7. Mention story IDs whenever available.
8. Mention component names exactly as provided.
9. Mention dependency names exactly as provided.
10. Use only supplied evidence.
11. Do not hallucinate.

Return only the final answer.
"""

    return ask_qwen(prompt)

# ==========================================================
# COMPARE
# ==========================================================

def generate_compare_answer(
    question,
    evidence
):

    prompt = f"""
You are comparing IRS releases.

Question:
{question}

Evidence:
{evidence}

Response Structure

WHAT CHANGED

NEW STORIES

COMPONENT DIFFERENCES

DEPENDENCY DIFFERENCES

KEY TAKEAWAYS

Instructions

- Focus on actual differences.
- Mention releases.
- Mention story IDs.
- Mention component names.
- Mention dependency names.
- Use bullet points.
- Do not hallucinate.
- Omit empty sections.
"""

    return ask_qwen(prompt)

# ==========================================================
# TREND
# ==========================================================

def generate_trend_answer(
    question,
    evidence
):

    prompt = f"""
You are an IRS Release Intelligence Analyst.

Question:
{question}

Evidence:
{evidence}

Analyze the supplied release evidence.

Focus on:

- Actual work delivered
- Stories implemented
- Monitoring changes
- Reporting changes
- Cloud migrations
- Database changes
- Components updated

Avoid generic themes.

Examples of good themes:

- Azure Blob Storage Migration
- Central Application Availability Reporting
- Dynatrace Integration
- TouchPoint Monitoring
- Async Processing Improvements

CRITICAL INSTRUCTIONS

1. USE only supplied evidence.
2. NEVER mention instructions.
3. NEVER output:
   - Rules
   - Instructions
   - Critical Rules
4. NEVER hallucinate.
5. NEVER mention empty sections.
6. If no data exists for a section, skip it entirely.
7. Prefer business and technical changes over release metadata.
8. Mention release numbers and story IDs whenever available.

Return only the final answer.
"""

    return ask_qwen(prompt)
    
# ==========================================================
# RAG
# ==========================================================

def generate_rag_answer(
    question,
    evidence
):

    prompt = f"""
You are an IRS Release Intelligence Assistant.

Question:
{question}

Evidence:
{evidence}

If the question is asking about:

history
timeline
evolution
journey
progression
started
first introduced

Then create a release-by-release timeline.

Response Structure

TIMELINE
(if applicable)

ANSWER

KEY CHANGES

SUPPORTING EVIDENCE

RELATED RELEASES

RELATED STORIES

Instructions

- Use only supplied evidence.
- Never hallucinate.
- Never invent releases.
- Never invent stories.
- Mention release numbers whenever possible.
- Mention story IDs whenever possible.
- For timeline questions:
  list releases chronologically.
- Be concise.
- Omit empty sections.
"""

    return ask_qwen(prompt)