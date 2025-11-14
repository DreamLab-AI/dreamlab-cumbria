---
name: perplexity-prompt-generator
description: Generate optimised prompts for Perplexity AI research assistant. Use when the user wants to create a Perplexity prompt, needs help structuring a query for Perplexity, asks for a prompt to use in Perplexity, or mentions using Perplexity for research. Helps craft prompts with proper structure, context, and formatting to maximise Perplexity's real-time web search capabilities with UK-centric focus.
---

# Perplexity Prompt Generator

Generate effective prompts that leverage Perplexity's strength as a real-time research assistant with live web access and source citations, optimised for UK context.

## Core methodology

Every strong Perplexity prompt should incorporate these five elements in the appropriate order:

1. **Instruction** - What you want Perplexity to do
2. **Context** - Background that frames the task
3. **Input** - Specific data, constraints, or materials
4. **Keywords** - Focused terms guiding relevance
5. **Output format** - How to structure the response

Not every prompt needs all five elements explicitly—simple factual queries may only need instruction and keywords. Complex research tasks benefit from all five.

## Prompt types and when to use them

### Informational prompts
**Use for:** Quick facts, definitions, current events, straightforward data

**Structure:** Direct question with specifics
```
What are the current mortgage rates from major UK banks?
```

### Instructional prompts
**Use for:** How-to guidance, procedures, troubleshooting

**Structure:** Scenario + specifics + constraints
```
How can I remove red wine stains from a white cotton shirt using household items available in the UK?
```

### Research prompts
**Use for:** Analysis, comparisons, comprehensive investigation, synthesising multiple sources

**Structure:** Full five-element approach with clear deliverable
```
Context: I'm a product manager at a B2B SaaS company in London
Task: Research current best practices for user onboarding flows
Focus: Reduce time-to-value, increase activation rates, UK and European industry benchmarks
Deliverable: Summary report with 3-5 actionable recommendations backed by recent sources
```

### Interactive prompts
**Use for:** Role-play scenarios, conversational guidance, coaching

**Structure:** Role definition + scenario + parameters
```
Act as a hiring manager at a Series B startup in the UK. I'm interviewing for a Senior Engineer role. Ask me behavioural questions focused on system design and team collaboration.
```

## Construction guidelines

**Maximise Perplexity's strengths:**
- Always request real-time/current data when relevance matters
- Ask for source citations explicitly for verification needs
- Leverage live web access for trends, news, pricing, and rapidly-changing info
- Specify UK or European context when regional differences matter

**Be specific:**
- Narrow scope with precise constraints (timeframe, geography, industry)
- Include relevant context that shapes the answer (experience level, use case, goal)
- Specify output length/format when it matters (brief vs. detailed, table vs. prose)
- Use UK spelling and terminology (organisation, colour, programme, etc.)

**Avoid:**
- Vague language ("good companies" → "top 10 UK companies by revenue")
- Assuming context Perplexity doesn't have ("our industry" → specify the industry)
- Multiple unrelated questions in one prompt (break them up)
- US-centric assumptions (specify UK laws, regulations, market conditions)

## Quality checklist

Before finalising a Perplexity prompt, verify:

- Clear instruction that states the goal
- Sufficient context for understanding
- Relevant keywords and specifics included
- Output format specified if non-standard
- Request for current/real-time data if needed
- Scope neither too broad nor too narrow
- UK/European context specified where relevant

## Professional templates

For common professional use cases, see [templates.md](references/templates.md) which includes ready-to-customise templates for:
- Education & academic research
- Product management & market research
- Financial analysis & sector reports
- Marketing & competitive analysis
- Legal compliance & regulatory research
- Business planning & strategy
- Technical documentation

## Workflow

When generating a Perplexity prompt:

1. **Understand the goal** - What specific question needs answering?
2. **Assess complexity** - Simple fact lookup or multi-source research?
3. **Choose structure** - Match prompt type to task
4. **Add specifics** - Include context, constraints, keywords
5. **Format output** - Specify how results should be structured
6. **Emphasise real-time needs** - Explicitly request current data when relevant
7. **Specify UK context** - Add geographic or regulatory specifics for UK

## Example transformations

**Weak prompt:**
"Tell me about AI trends"

**Strong prompt:**
"Research the top 5 AI trends in UK enterprise software for 2025. Focus on: adoption rates, business impact, and implementation challenges. Deliverable: Executive summary with sources published in the last 90 days, prioritising UK and European sources."

---

**Weak prompt:**
"How do I invest in renewable energy?"

**Strong prompt:**
"I'm a UK retail investor with £10K to allocate. Research current investment options in renewable energy including: UK-listed ETFs, individual stocks on the LSE, and REITs. Compare: expense ratios, YTD performance, and volatility. Format: Comparison table with 3-5 options and brief pros/cons for each."

---

**Weak prompt:**
"Regulations for my business"

**Strong prompt:**
"I run an e-commerce company selling supplements in the UK. Research: UK Food Standards Agency regulations for dietary supplements, Consumer Rights Act 2015 requirements, and online sales compliance under UK law. Deliverable: Checklist of required compliance actions with source citations from .gov.uk and regulatory bodies."
